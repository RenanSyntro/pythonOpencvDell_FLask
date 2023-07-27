import threading

from enum                               import Enum

from pycomm3                            import LogixDriver

from database.db_SelectRow_SeachForID   import selectRow_SearchForID

from rich.console				        import Console
from rich.table					        import Table

listCoordinateAll = []

class enum_Fault(Enum):
    Fault_Empty                 = 0
    Fault_VisionImageFailure    = 1
    Fault_NoObjectFound         = 2

class enum_Status(Enum):
    Status_Empty                = 0
    Status_RecipeLoaded         = 1

#
#Console Teminal Rich
#
console = Console()
console.print("Terminal OpenCV", "Root", style="bold white on blue")

table = Table(show_header=True, header_style="bold magenta")

table.add_column("R Xmm", justify="right")
table.add_column("R Ymm", justify="right")

table.add_column("C Xmm", justify="right")
table.add_column("C Ymm", justify="right")

table.add_column("C Xp", justify="right")
table.add_column("C Yp", justify="right")

table.add_column("ID Trig", justify="right")
table.add_column("ID Det", justify="right")

#
#
#
Id_trigger  =   0
Id_Det      =   0

#
#Flag
#
Flag_Write_Coordenate_x                             = 0.0
Flag_Write_Coordenate_y                             = 0.0

Flag_subSequence_ImageAnalysis_Step                 = 0

Flag_Recipe_Pallet_HiveMatrix_CounterPosition       = 0

Flag_NW_I_Recipe_Number                             = 0

#
#Read general variable do PLC.
#
NW_I_IA01_Calc_ConvDistanceToHeight      = 0
NW_I_IA01_Calc_Value_Unit                = 0
Recipe_Pallet_HiveMatrix_CounterPosition = 0
HMI_O_AR_AxisCommandPos_01               = 0.0
HMI_O_AR_AxisCommandPos_02               = 0.0
HMI_O_AR_AxisCommandPos_03               = 0.0

HMI_I_ImgAna_DistToolCamera_X            = 0.0
HMI_I_ImgAna_DistToolCamera_Y            = 0.0

HMI_I_CamRepositioningToStartBoxScan_X  = 0.0
HMI_I_CamRepositioningToStartBoxScan_Y  = 0.0

subSequence_ImageAnalysis_Step          = 0

NW_I_RC_DT_PRD_SpaceBetweenGab_X        = 0
NW_I_RC_DT_PRD_SpaceBetweenGab_Y        = 0

NW_I_RC_DT_Product_Box_HiveAmountAxisX  = 0
NW_I_RC_DT_Product_Box_HiveAmountAxisY  = 0



#NW_I_RC_DT_Product_Box_height           = 0
#NW_I_RC_DT_Product_Box_lenght           = 0
#NW_I_RC_DT_Product_Box_Width            = 0






NW_I_Recipe_Number                      = 0

CP_I_ST_Fault                           = 0
CP_I_ST_GeneralState                    = 0

CP_I_DistanceBetweenCameraAndObject     = 0

CP_IO_PingComunication                  = 0

#
#Read comunication with system vision computer - CP
#
CP_O_ListCoordinateClear                = False
CP_O_ListCoordinateClearOK_Received     = False

CP_O_TriggerCamera                      = False
CP_O_ReturnOK_Received                  = False

#
#Write comunication with system vision computer - CP
#
CP_I_ListCoodinateClear_Return_OK       = False

CP_I_TriggerCamera_Return_OK            = False

#
#Analysis system asking to write information
#
#comunication Trigger
mWrite_TriggerReturn                    = False

#Matrix
Matrix_Colum_Position                   = 0
Matrix_Row_Position                     = 0

#
#
#
mWrite_Fault                             = False
mWrite_Fault_Value                       = 0

def sortSecond(val):
    return val[1]

def ListCoordenate(listCoordinate):
    #listCoordinateAll.append(listCoordinate.copy())
    global listCoordinateAll
    aux = listCoordinateAll.copy()
    if (len(listCoordinateAll) <= 0):
        listCoordinateAll = listCoordinate.copy()
    else:
        listCoordinateAll = aux + listCoordinate.copy()

    listCoordinateAll.sort(key=sortSecond)
    #print('(List Coordinate All)')
    #print(listCoordinateAll)

    for row in listCoordinateAll:
          console.print((
                " / R Xmm: {:0>7} "
                " / R Ymm: {:0>7} "
                " / C Xmm: {:0>7} "
                " / C Ymm: {:0>7} "
                " / C Xp: {:0>7} "
                " / C Yp: {:0>7} "
                " / ID Trig: {:0>7} "
                " / ID Det: {:0>7} ").format(
                round(row[0], 2),
                round(row[1], 2),
                round(row[2], 2),
                round(row[3], 2),
                round(row[4], 2),
                round(row[5], 2),
                round(row[6], 2),
                round(row[7], 2),
                ),style="bold on black")

def Write_TriggerReturnOK():
    global mWrite_TriggerReturn
    mWrite_TriggerReturn 				= True

def Write_Fault(value):
    global mWrite_Fault
    global mWrite_Fault_Value
    mWrite_Fault                        = True
    mWrite_Fault_Value                  = value

def findHiveRowAndColumnPosition():
    global Recipe_Pallet_HiveMatrix_CounterPosition
    if (not Recipe_Pallet_HiveMatrix_CounterPosition is None):
        Aux_Recipe_Pallet_HiveMatrix_CounterPosition = Recipe_Pallet_HiveMatrix_CounterPosition + 1

    if (    NW_I_RC_DT_Product_Box_HiveAmountAxisX > 0
        and NW_I_RC_DT_Product_Box_HiveAmountAxisY > 0):
        linha       = (Aux_Recipe_Pallet_HiveMatrix_CounterPosition - 1) %  NW_I_RC_DT_Product_Box_HiveAmountAxisX  + 1 
        coluna      = (Aux_Recipe_Pallet_HiveMatrix_CounterPosition - 1) // NW_I_RC_DT_Product_Box_HiveAmountAxisX  + 1
    else:
        linha       = 0
        coluna      = 0
    #linha       = (Aux_Recipe_Pallet_HiveMatrix_CounterPosition - 1) % 5   + 1 
    #coluna      = (Aux_Recipe_Pallet_HiveMatrix_CounterPosition - 1) // 5  + 1
    return coluna,  linha

def thr_comunicationPlc():
    with LogixDriver('192.168.11.5') as micro850:

        def Write_CP_O_ST_GeneralState(value):
            if(micro850.connected):
                micro850.write('CP_O_ST_GeneralState', value)

        def Write_CP_O_ST_Fault(value):
            if(micro850.connected):
                micro850.write('CP_O_ST_Fault', value)

        def Write_CP_IO_PingComunication(Value):
            if(micro850.connected):
                micro850.write('CP_IO_PingComunication', Value)

        def Write_CP_I_TriggerCamera_Return_OK(Value):
            if(micro850.connected):
                micro850.write('CP_I_TriggerCamera_Return_OK', Value)

        def Write_CP_I_HiveCoordinateAmount(Value):
            if(micro850.connected):
                micro850.write('CP_I_HiveCoordinateAmount', Value)

        while(True):
            #
            #Read information comunication PLC
            #
            #
            #Read mananger information
            #
            global NW_I_IA01_Calc_ConvDistanceToHeight 
            global NW_I_IA01_Calc_Value_Unit

            NW_I_IA01_Calc_ConvDistanceToHeight     = micro850.read('NW_I_IA01_Calc_ConvDistanceToHeight').value
            NW_I_IA01_Calc_Value_Unit               = micro850.read('NW_I_IA01_Calc_Value_Unit').value

            if(NW_I_IA01_Calc_ConvDistanceToHeight   is None):
                NW_I_IA01_Calc_ConvDistanceToHeight = 0

            if (NW_I_IA01_Calc_Value_Unit               is None):
                NW_I_IA01_Calc_Value_Unit           = 0

            global HMI_O_AR_AxisCommandPos_01
            global HMI_O_AR_AxisCommandPos_02
            global HMI_O_AR_AxisCommandPos_03

            micro850.read

            HMI_O_AR_AxisCommandPos_01              = micro850.read('HMI_O_AR_AxisCommandPos_01').value
            HMI_O_AR_AxisCommandPos_02              = micro850.read('HMI_O_AR_AxisCommandPos_02').value          
            HMI_O_AR_AxisCommandPos_03              = micro850.read('HMI_O_AR_AxisCommandPos_03').value

            if (HMI_O_AR_AxisCommandPos_01               is None):
                HMI_O_AR_AxisCommandPos_01           = 0

            if (HMI_O_AR_AxisCommandPos_02               is None):
                HMI_O_AR_AxisCommandPos_02           = 0

            if (HMI_O_AR_AxisCommandPos_03               is None):
                HMI_O_AR_AxisCommandPos_03           = 0

            global HMI_I_ImgAna_DistToolCamera_X    
            global HMI_I_ImgAna_DistToolCamera_Y

            HMI_I_ImgAna_DistToolCamera_X           = micro850.read('HMI_I_ImgAna_DistToolCamera_X').value
            HMI_I_ImgAna_DistToolCamera_Y           = micro850.read('HMI_I_ImgAna_DistToolCamera_Y').value

            if (HMI_I_ImgAna_DistToolCamera_X               is None):
                HMI_I_ImgAna_DistToolCamera_X           = 0

            if (HMI_I_ImgAna_DistToolCamera_Y               is None):
                HMI_I_ImgAna_DistToolCamera_Y           = 0

            global  Recipe_Pallet_HiveMatrix_CounterPosition
            Recipe_Pallet_HiveMatrix_CounterPosition = micro850.read('Recipe_Pallet_HiveMatrix_CounterPosition').value

            if (Recipe_Pallet_HiveMatrix_CounterPosition    is None):
                Recipe_Pallet_HiveMatrix_CounterPosition           = 0

            global HMI_I_CamRepositioningToStartBoxScan_X
            global HMI_I_CamRepositioningToStartBoxScan_Y
            HMI_I_CamRepositioningToStartBoxScan_X  = micro850.read('HMI_I_CamRepositioningToStartBoxScan_X').value
            HMI_I_CamRepositioningToStartBoxScan_Y  = micro850.read('HMI_I_CamRepositioningToStartBoxScan_Y').value

            if( HMI_I_CamRepositioningToStartBoxScan_X      is None):
                HMI_I_CamRepositioningToStartBoxScan_X = 0
            
            if( HMI_I_CamRepositioningToStartBoxScan_Y      is None):
                HMI_I_CamRepositioningToStartBoxScan_Y = 0

            global NW_I_RC_DT_PRD_SpaceBetweenGab_X
            global NW_I_RC_DT_PRD_SpaceBetweenGab_Y
            NW_I_RC_DT_PRD_SpaceBetweenGab_X        = micro850.read('NW_I_RC_DT_PRD_SpaceBetweenGab_X').value
            NW_I_RC_DT_PRD_SpaceBetweenGab_Y        = micro850.read('NW_I_RC_DT_PRD_SpaceBetweenGab_Y').value

            if( NW_I_RC_DT_PRD_SpaceBetweenGab_X            is None):
                NW_I_RC_DT_PRD_SpaceBetweenGab_X = 0
            
            if( NW_I_RC_DT_PRD_SpaceBetweenGab_Y            is None):
                NW_I_RC_DT_PRD_SpaceBetweenGab_Y = 0

            global NW_I_RC_DT_Product_Box_HiveAmountAxisX
            global NW_I_RC_DT_Product_Box_HiveAmountAxisY
            NW_I_RC_DT_Product_Box_HiveAmountAxisX  = micro850.read('NW_I_RC_DT_Product_Box_HiveAmountAxisX').value
            NW_I_RC_DT_Product_Box_HiveAmountAxisY  = micro850.read('NW_I_RC_DT_Product_Box_HiveAmountAxisY').value

            if( NW_I_RC_DT_Product_Box_HiveAmountAxisX      is None):
                NW_I_RC_DT_Product_Box_HiveAmountAxisX = 0

            if(NW_I_RC_DT_Product_Box_HiveAmountAxisY       is None):
                NW_I_RC_DT_Product_Box_HiveAmountAxisY = 0

            global CP_I_DistanceBetweenCameraAndObject
            CP_I_DistanceBetweenCameraAndObject     = micro850.read('CP_I_DistanceBetweenCameraAndObject').value

            if( CP_I_DistanceBetweenCameraAndObject         is None):
                CP_I_DistanceBetweenCameraAndObject = 0

            #Read Ping Communication
            global CP_IO_PingComunication
            CP_IO_PingComunication                  = micro850.read('CP_IO_PingComunication').value

            if( CP_IO_PingComunication                      is None):
                CP_IO_PingComunication = 0

            if (CP_IO_PingComunication == 1):
                Write_CP_IO_PingComunication(0)

            #Read Recipe Number
            global NW_I_Recipe_Number
            global Flag_NW_I_Recipe_Number
            NW_I_Recipe_Number                      = micro850.read('NW_I_Recipe_Number').value

            if( NW_I_Recipe_Number                         is None):
                NW_I_Recipe_Number = 0

            if (Flag_NW_I_Recipe_Number != NW_I_Recipe_Number):
                Flag_NW_I_Recipe_Number = NW_I_Recipe_Number
                match NW_I_Recipe_Number:
                    case 0:
                        selectRow_SearchForID.Select(59)
                        Write_CP_O_ST_GeneralState(enum_Status.Status_RecipeLoaded)
                        #controllers.adjustmentPanel.labelWeb_RecipeName = "MICRO"
                    case 1:
                        selectRow_SearchForID.Select(60)
                        Write_CP_O_ST_GeneralState(enum_Status.Status_RecipeLoaded)
                        #controllers.adjustmentPanel.labelWeb_RecipeName = "SFF"

            #Read seq image analysis step
            global subSequence_ImageAnalysis_Step
            global Flag_subSequence_ImageAnalysis_Step
            global CP_I_TriggerCamera_Return_OK
            subSequence_ImageAnalysis_Step          = micro850.read('subSequence_ImageAnalysis_Step').value

            if( subSequence_ImageAnalysis_Step is None):
                subSequence_ImageAnalysis_Step = 0

            if (subSequence_ImageAnalysis_Step != Flag_subSequence_ImageAnalysis_Step):
                Flag_subSequence_ImageAnalysis_Step = subSequence_ImageAnalysis_Step

                match subSequence_ImageAnalysis_Step:
                    case 0:
                        console.print(("CLPSEQ: #00  Start Condition"),                             style="green on black")
                        CP_I_TriggerCamera_Return_OK    = False
                    case 1:
                        console.print(("CLPSEQ: #01 - Clear list coordinate Step01"),               style="green on black")
                    case 2:
                        console.print(("CLPSEQ: #02 - Clear list coordinate Step02"),               style="green on black")
                    case 5:
                        console.print(("CLPSEQ: #05 - Go to photo starting position for review 01"),style="green on black")
                    case 6:
                        console.print(("CLPSEQ: #06 - Liberando eixo"),                             style="green on black")
                    case 7:
                        console.print(("CLPSEQ: #05 - Go to photo starting position for review 02"),style="green on black")
                    case 10:
                        console.print(("CLPSEQ: #10 - Free next motion axis"),                      style="green on black")
                    case 15:
                        console.print(("CLPSEQ: #15 - Trigger camera"),                             style="green on black")
                    case 20:
                        console.print(("CLPSEQ: #20 - Waiting to return CP received"),              style="green on black")
                    case 25:
                        console.print(("CLPSEQ: #25 - camera repositioning to start box scan"),     style="green on black")
                    case 30:
                        console.print(("CLPSEQ: #30 - Free next motion axis"),                      style="green on black")
                    case 31:
                        console.print(("CLPSEQ: #31 - Clear list coordinate Step01"),               style="green on black")
                    case 32:
                        console.print(("CLPSEQ: #32 - Clear list coordinate Step02"),               style="green on black")
                    case 35:
                        console.print(("CLPSEQ: #35 - Trigger camera"),                             style="green on black")
                    case 36:
                        console.print(("CLPSEQ: #36 - Waiting to return CP received"),              style="green on black")
                    case 45:
                        console.print(("CLPSEQ: #45 - Check position scanner"),                     style="green on black")
                    case 50:
                        console.print(("CLPSEQ: #50 - Go to position"),                             style="green on black")
                    case 55:
                        console.print(("CLPSEQ: #55 - END"),                                        style="green on black")  
                    #case _:

            #
            #Write information comunication PLC
            #
            #Write Fault
            global mWrite_Fault
            global mWrite_Fault_Value
            if (mWrite_Fault):
                Write_CP_O_ST_Fault(mWrite_Fault_Value)
                Write_CP_O_ST_GeneralState(0)
                mWrite_Fault = False

            #Write

            #Write_Coordenate
            global Flag_Write_Coordenate_x
            global Flag_Write_Coordenate_y

            global Matrix_Colum_Position
            global Matrix_Row_Position
            Matrix_Row_Position, Matrix_Colum_Position       = findHiveRowAndColumnPosition()

            global Flag_Recipe_Pallet_HiveMatrix_CounterPosition
            if (Recipe_Pallet_HiveMatrix_CounterPosition != Flag_Recipe_Pallet_HiveMatrix_CounterPosition):

                Flag_Recipe_Pallet_HiveMatrix_CounterPosition = Recipe_Pallet_HiveMatrix_CounterPosition

                console.print((
                "Debug:"
                " / LINHA   (Y): {:0>7} "
                " / COLUNA  (X): {:0>7} "
                ).format(
                round(Matrix_Row_Position,             2),
                round(Matrix_Colum_Position,           2),
                ),style="red on black")

            if (     len(listCoordinateAll)      >   0 
                #and Recipe_Pallet_HiveMatrix_CounterPosition   < len(listCoordinateAll)
                ):

                #
                #this process searches only for the coordinates present in the camera capture.
                #
                #Write_Coordenate_x                   = ((listCoordinateAll[Recipe_Pallet_HiveMatrix_CounterPosition][0]) 
                #                                            + HMI_I_ImgAna_DistToolCamera_X)
                #Write_Coordenate_y                   = ((listCoordinateAll[Recipe_Pallet_HiveMatrix_CounterPosition][1]) 
                #                                            + HMI_I_ImgAna_DistToolCamera_Y)

                #this process searches by merging matrix process according to count correcting the Y axis according to coordinates requested by the camera.
                #console.print((
                #"Current handle coordinates:"
                #" / COL: {:0>7} "
                #" / ROW: {:0>7} "
                #).format(
                #round(Column, 2),
                #round(row, 2),
                #),style="red on black")

                if (len(listCoordinateAll)      >   0    
                    and Matrix_Row_Position     >   0 
                    and Matrix_Row_Position     <=   len(listCoordinateAll)   # >=   len(listCoordinateAll) # >   0 
                    and Matrix_Colum_Position   >   0):
                    Write_Coordenate_x                  = (((listCoordinateAll[Matrix_Row_Position - 1][0]) 
                                                                + HMI_I_ImgAna_DistToolCamera_X)
                                                                + (NW_I_RC_DT_PRD_SpaceBetweenGab_X * (Matrix_Colum_Position - 1)))

                    Write_Coordenate_y                  = ((listCoordinateAll[Matrix_Row_Position - 1][1]) 
                                                                + HMI_I_ImgAna_DistToolCamera_Y)
                    #console.print((
                    #"Debug:"
                    #" / R Xmm: {:0>7} "
                    #" / R Ymm: {:0>7} "
                    #" / LINHA   (Y): {:0>7} "
                    #" / COLUNA  (X): {:0>7} "
                    #).format(
                    #round(Write_Coordenate_x,   2),
                    #round(Write_Coordenate_y,   2),
                    #round(row,                  2),
                    #round(Column,               2),
                    #),style="red on black")

            else:
                Write_Coordenate_x                  = 0.0
                Write_Coordenate_y                  = 0.0

            Write_CP_I_HiveCoordinateAmount(len(listCoordinateAll))
            micro850.write('CP_I_ImgAna_targetHiveCount_Xmm', Write_Coordenate_x)
            micro850.write('CP_I_ImgAna_targetHiveCount_Ymm', Write_Coordenate_y)

            if (    Flag_Write_Coordenate_x != Write_Coordenate_x
                or  Flag_Write_Coordenate_y != Write_Coordenate_y
                ):
                Flag_Write_Coordenate_x = Write_Coordenate_x
                Flag_Write_Coordenate_y = Write_Coordenate_y

                
                console.print((
                "Current handle coordinates:"
                " / R Xmm: {:0>7} "
                " / R Ymm: {:0>7} "
                " / LINHA   (Y): {:0>7} "
                " / COLUNA  (X): {:0>7} "
                ).format(
                round(Write_Coordenate_x,       2),
                round(Write_Coordenate_y,       2),
                round(Matrix_Row_Position,      2),
                round(Matrix_Colum_Position,    2),
                ),style="red on white")

            #Repositioning of the camera on the box, according to the reference of the first cabinet
            #
            #Write_Coordenate
            #
            if (    len(listCoordinateAll)      >   0 ):
                micro850.write('CP_I_ImgAna_TargetHiveRepos_Xmm', listCoordinateAll[0][0])
                micro850.write('CP_I_ImgAna_TargetHiveRepos_Ymm', listCoordinateAll[0][1])

            #
            #Cycle automatic - Read / Write
            #
            #
            #Sequence Clear List Coordinate
            #
            #Seq. 01 - Waiting to receive list coodinate clear and clear list
            global CP_O_ListCoordinateClear
            CP_O_ListCoordinateClear                = micro850.read('CP_O_ListCoordinateClear').value

            global CP_I_ListCoodinateClear_Return_OK
            if (CP_O_ListCoordinateClear):
                console.print("#Seq 01 - Clear list coordinate all", style="magenta")
                listCoordinateAll.clear()
                CP_I_ListCoordinateClear_Return_OK        = True
                micro850.write('CP_I_ListCoordinateClear_Return_OK', CP_I_ListCoordinateClear_Return_OK)

            #
            #Seq. 02 - Send return list coodinate clear
            #
            global CP_O_ListCoordinateClearOK_Received
            CP_O_ListCoordinateClearOK_Received     = micro850.read('CP_O_ListCoordinateClearOK_Received').value

            if (CP_O_ListCoordinateClearOK_Received):
                console.print("#Seq 02 - Clear list - ReturnOK", style="magenta")
                CP_I_ListCoordinateClear_Return_OK        = False
                micro850.write('CP_I_ListCoordinateClear_Return_OK', CP_I_ListCoordinateClear_Return_OK)

            #
            #Sequence Trigger
            #
            #
            #Seq. 01 - Waiting to receive trigger camera - Read trigger camera
            #
            global CP_O_TriggerCamera
            CP_O_TriggerCamera                      = micro850.read('CP_O_TriggerCamera').value

            #
            #Seq. 02 - Send return trigger - Write Trigger Return
            #
            global mWrite_TriggerReturn
            if (mWrite_TriggerReturn):
                print('PLC - #02 Write Trigger Return')
                Write_CP_I_TriggerCamera_Return_OK(CP_I_TriggerCamera_Return_OK)
                mWrite_TriggerReturn                 = False

            #
            #Seq. 03 - Waiting to receive data signal received from PLC. - Read Return OK Received
            #
            global CP_O_ReturnOK_Received
            CP_O_ReturnOK_Received                  = micro850.read('CP_O_ReturnOK_Received').value
            if (CP_O_ReturnOK_Received):
                print('PLC - #03 Received return OK')
                CP_I_TriggerCamera_Return_OK        = False
                Write_CP_I_TriggerCamera_Return_OK(CP_I_TriggerCamera_Return_OK)

#def thr_pingComunicationPlc():
    #with LogixDriver('192.168.11.5') as micro850:
#   while(True):


def comunicationPlc():
    t1 = threading.Thread(target=thr_comunicationPlc)
    t1.daemon = True
    t1.start()

    #t2 = threading.Thread(target=thr_pingComunicationPlc)
    #t2.daemon = True
    #t2.start()



