import controllers.varGlobal.adjustmentPanel

from flask import redirect
from db import mysql

def CheckIfRecipeNameAlreadyExists(name):
    with mysql.cursor() as cur:
        cur.execute(
        "SELECT id FROM parametersAdjustFilterImg WHERE name = %s", name)
        data = cur.fetchone()
        return data
           
class Insert_parametersAdjustFilterImg():
    def salvar():
        #
        #Name
        #
        name                    = controllers.varGlobal.adjustmentPanel.var_name

        #
        #Color
        #
        FilterColor_Red_Min     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min
        FilterColor_Red_Max     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max

        FilterColor_Green_Min   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min
        FilterColor_Green_Max   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max

        FilterColor_Blue_Min    = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min
        FilterColor_Blue_Max    = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max

        #
        #Area
        #
        DefinedAreaForFilter_init_X             = controllers.varGlobal.adjustmentPanel.var_parametersFilter_DefinedAreaForFilter_init_X
        DefinedAreaForFilter_init_Y             = controllers.varGlobal.adjustmentPanel.var_parametersFilter_DefinedAreaForFilter_init_Y

        #
        #Iterations
        #
        FilterInterations_Erode                 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_erode
        FilterInterations_Dilate                = controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_dilate

        #
        #Seam according to color
        #
        #Vertically     - White
        SpliceLineJumpWhiteVer_JumpSize_Min     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min
        SpliceLineJumpWhiteVer_JumpSize_Max     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max
        #Area
        SpliceLineJumpWhiteVer_JumpSize_Field   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_IdAreasOfOperationInTheFilter

        #Horizontally   - White
        SpliceLineJumpWhiteHor_JumpSize_Min     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min
        SpliceLineJumpWhiteHor_JumpSize_Max     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max
        #Area
        SpliceLineJumpWhiteHor_JumpSize_Field   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteHor_IdAreasOfOperationInTheFilter

        #Vertically     - Black
        SpliceLineJumpBlackVer_JumpSize_Min     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Min
        SpliceLineJumpBlackVer_JumpSize_Max     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Max
        #Area
        SpliceLineJumpBlackVer_JumpSize_Field   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpBlackVer_IdAreasOfOperationInTheFilter

        #Horizontally   - Black
        SpliceLineJumpBlackHor_JumpSize_Min     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min
        SpliceLineJumpBlackHor_JumpSize_Max     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max
        #Area
        SpliceLineJumpBlackHor_JumpSize_Field   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpBlackHor_IdAreasOfOperationInTheFilter

        #
        #Filter Object Size 
        #
        FoundObjectSizeFilter_Min                   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min
        FoundObjectSizeFilter_Max                   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max

        VerticalLineSizeFilterOfFoundObject_Min     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min
        VerticalLineSizeFilterOfFoundObject_Max     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max

        HorizontalLineSizeFilterOfFoundObject_Min   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min
        HorizontalLineSizeFilterOfFoundObject_Max   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max

        #
        #Reserve Integer
        #
        parameter01                                 = 0 
        parameter02                                 = 0
        parameter03                                 = 0 
        parameter04                                 = 0
        parameter05                                 = 0 
        parameter06                                 = 0
        parameter07                                 = 0 
        parameter08                                 = 0
        parameter09                                 = 0 
        parameter10                                 = 0

        #
        #Conversion Pixel in Unit
        #
        ConstResolutionPixelMm_X                    = controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X
        ConstResolutionPixelMm_Y                    = controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y

        #
        #Reserve Real
        #
        parameterReal01                             = 0.0
        parameterReal02                             = 0.0
        parameterReal03                             = 0.0
        parameterReal04                             = 0.0
        parameterReal05                             = 0.0
        parameterReal06                             = 0.0
        parameterReal07                             = 0.0
        parameterReal08                             = 0.0

        with mysql.cursor() as cur:
            res = CheckIfRecipeNameAlreadyExists(name) 
        
            if (res is None):
                
                # print(f"INSERT INTO parametersAdjustFilterImg VALUE"
                #             f"(0,  {name}, "
                #             f"{FilterColor_Red_Min}, {FilterColor_Red_Max}, "
                #             f"{FilterColor_Green_Min}, {FilterColor_Green_Max}, "
                #             f"{FilterColor_Blue_Min}, {FilterColor_Blue_Max}, "
                #             f"{DefinedAreaForFilter_init_X}, {DefinedAreaForFilter_init_Y}, "
                #             f"{FilterInterations_Erode}, {FilterInterations_Dilate}, "
                #             f"{SpliceLineJumpWhiteVer_JumpSize_Min}, {SpliceLineJumpWhiteVer_JumpSize_Max}, "
                #             f"{SpliceLineJumpWhiteVer_JumpSize_Field},"
                #             f"{SpliceLineJumpWhiteHor_JumpSize_Min}, {SpliceLineJumpWhiteHor_JumpSize_Max}, "
                #             f"{SpliceLineJumpWhiteHor_JumpSize_Field},"
                #             f"{SpliceLineJumpBlackVer_JumpSize_Min}, {SpliceLineJumpBlackVer_JumpSize_Max}, "
                #             f"{SpliceLineJumpBlackVer_JumpSize_Field},"
                #             f"{SpliceLineJumpBlackHor_JumpSize_Min}, {SpliceLineJumpBlackHor_JumpSize_Max}, "
                #             f"{SpliceLineJumpBlackHor_JumpSize_Field},"
                #             f"{FoundObjectSizeFilter_Min}, {FoundObjectSizeFilter_Max}, "
                #             f"{VerticalLineSizeFilterOfFoundObject_Min}, {VerticalLineSizeFilterOfFoundObject_Max}, "
                #             f"{HorizontalLineSizeFilterOfFoundObject_Min}, {HorizontalLineSizeFilterOfFoundObject_Max}, "
                #             f"{parameter01}, {parameter02}, {parameter03},  {parameter04}, {parameter05}, "
                #             f"{parameter06}, {parameter07}, {parameter08},  {parameter09}, {parameter10}, "
                #             f"{ConstResolutionPixelMm_X},  {ConstResolutionPixelMm_Y}, "
                #             f"{parameterReal01}, {parameterReal02}, {parameterReal03}, {parameterReal04}, "
                #             f"{parameterReal05}, {parameterReal06}, {parameterReal07}, {parameterReal08}"
                #             ")"
                #             )  

                cur.execute("INSERT INTO parametersAdjustFilterImg VALUE"
                            "(0, %s, "
                            "%s, %s, "
                            "%s, %s, "
                            "%s, %s, "
                            "%s, %s, "
                            "%s, %s, "
                            "%s, %s, "
                            "%s, "
                            "%s, %s, "
                            "%s, "
                            "%s, %s, "
                            "%s, "
                            "%s, %s, "
                            "%s, "
                            "%s, %s, "
                            "%s, %s, "
                            "%s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, "
                            "%s, %s, %s, %s,"
                            "%s, %s, %s, %s"
                            ")",
                            (name,
                            FilterColor_Red_Min                         , FilterColor_Red_Max                       , 
                            FilterColor_Green_Min                       , FilterColor_Green_Max                     , 
                            FilterColor_Blue_Min                        , FilterColor_Blue_Max                      ,
                            DefinedAreaForFilter_init_X                 , DefinedAreaForFilter_init_Y               ,
                            FilterInterations_Erode                     , FilterInterations_Dilate                  ,
                            SpliceLineJumpWhiteVer_JumpSize_Min         , SpliceLineJumpWhiteVer_JumpSize_Max       ,
                            SpliceLineJumpWhiteVer_JumpSize_Field       ,
                            SpliceLineJumpWhiteHor_JumpSize_Min         , SpliceLineJumpWhiteHor_JumpSize_Max       , 
                            SpliceLineJumpWhiteHor_JumpSize_Field       ,
                            SpliceLineJumpBlackVer_JumpSize_Min         , SpliceLineJumpBlackVer_JumpSize_Max       ,
                            SpliceLineJumpBlackVer_JumpSize_Field       ,
                            SpliceLineJumpBlackHor_JumpSize_Min         , SpliceLineJumpBlackHor_JumpSize_Max       ,
                            SpliceLineJumpBlackHor_JumpSize_Field       ,
                            FoundObjectSizeFilter_Min                   , FoundObjectSizeFilter_Max                 ,
                            VerticalLineSizeFilterOfFoundObject_Min     , VerticalLineSizeFilterOfFoundObject_Max   ,
                            HorizontalLineSizeFilterOfFoundObject_Min   , HorizontalLineSizeFilterOfFoundObject_Max ,
                            parameter01 , parameter02   , parameter03   , parameter04   , parameter05               ,                                 
                            parameter06 , parameter07   , parameter08   , parameter09   , parameter10               ,
                            ConstResolutionPixelMm_X                    , ConstResolutionPixelMm_Y                  ,
                            parameterReal01 , parameterReal02   , parameterReal03   , parameterReal04               ,
                            parameterReal05 , parameterReal06   , parameterReal07   , parameterReal08   
                            ))
                cur.connection.commit()
            else:
                id = res[0]

                cur.execute("UPDATE parametersAdjustFilterImg SET "
                            "name                                       = %s , "
                            "FilterColor_Red_Min                        = %s , FilterColor_Red_Max                          = %s ,  "
                            "FilterColor_Green_Min                      = %s , FilterColor_Green_Max                        = %s ,  "
                            "FilterColor_Blue_Min                       = %s , FilterColor_Blue_Max                         = %s ,  "
                            "DefinedAreaForFilter_init_X                = %s , DefinedAreaForFilter_init_Y                  = %s ,  "
                            "FilterInterations_Erode                    = %s , FilterInterations_Dilate                     = %s ,  "
                            "SpliceLineJumpWhiteVer_JumpSize_Min        = %s , SpliceLineJumpWhiteVer_JumpSize_Max          = %s ,  "
                            "SpliceLineJumpWhiteVer_JumpSize_Field      = %s ,"
                            "SpliceLineJumpWhiteHor_JumpSize_Min        = %s , SpliceLineJumpWhiteHor_JumpSize_Max          = %s ,  "
                            "SpliceLineJumpWhiteHor_JumpSize_Field      = %s ,"
                            "SpliceLineJumpBlackVer_JumpSize_Min        = %s , SpliceLineJumpBlackVer_JumpSize_Max          = %s ,  "
                            "SpliceLineJumpBlackVer_JumpSize_Field      = %s ,"
                            "SpliceLineJumpBlackHor_JumpSize_Min        = %s , SpliceLineJumpBlackHor_JumpSize_Max          = %s ,  "
                            "SpliceLineJumpBlackHor_JumpSize_Field      = %s ,"
                            "FoundObjectSizeFilter_Min                  = %s , FoundObjectSizeFilter_Max                    = %s ,  "
                            "VerticalLineSizeFilterOfFoundObject_Min    = %s , VerticalLineSizeFilterOfFoundObject_Max      = %s ,  "
                            "HorizontalLineSizeFilterOfFoundObject_Min  = %s , HorizontalLineSizeFilterOfFoundObject_Max    = %s ,  "
                            "parameter01 = %s, parameter02 = %s, parameter03 = %s, parameter04 = %s, parameter05 =  %s,             "
                            "parameter06 = %s, parameter07 = %s, parameter08 = %s, parameter09 = %s, parameter10 =  %s,             "
                            "ConstResolutionPixelMm_X                   = %s , ConstResolutionPixelMm_Y                     = %s ,  "
                            "parameterReal01 = %s, parameterReal02 = %s, parameterReal03 = %s, parameterReal04 = %s,                 "
                            "parameterReal05 = %s, parameterReal06 = %s, parameterReal07 = %s, parameterReal08 = %s                 "
                            " WHERE id = %s",
                            (name,
                            FilterColor_Red_Min                         , FilterColor_Red_Max                       , 
                            FilterColor_Green_Min                       , FilterColor_Green_Max                     , 
                            FilterColor_Blue_Min                        , FilterColor_Blue_Max                      ,
                            DefinedAreaForFilter_init_X                 , DefinedAreaForFilter_init_Y               ,
                            FilterInterations_Erode                     , FilterInterations_Dilate                  ,
                            SpliceLineJumpWhiteVer_JumpSize_Min         , SpliceLineJumpWhiteVer_JumpSize_Max       ,
                            SpliceLineJumpWhiteVer_JumpSize_Field       ,
                            SpliceLineJumpWhiteHor_JumpSize_Min         , SpliceLineJumpWhiteHor_JumpSize_Max       , 
                            SpliceLineJumpWhiteHor_JumpSize_Field       ,
                            SpliceLineJumpBlackVer_JumpSize_Min         , SpliceLineJumpBlackVer_JumpSize_Max       ,
                            SpliceLineJumpBlackVer_JumpSize_Field       ,
                            SpliceLineJumpBlackHor_JumpSize_Min         , SpliceLineJumpBlackHor_JumpSize_Max       ,
                            SpliceLineJumpBlackHor_JumpSize_Field       ,
                            FoundObjectSizeFilter_Min                   , FoundObjectSizeFilter_Max                 ,
                            VerticalLineSizeFilterOfFoundObject_Min     , VerticalLineSizeFilterOfFoundObject_Max   ,
                            HorizontalLineSizeFilterOfFoundObject_Min   , HorizontalLineSizeFilterOfFoundObject_Max ,
                            parameter01 , parameter02   , parameter03   , parameter04   , parameter05               ,                                 
                            parameter06 , parameter07   , parameter08   , parameter09   , parameter10               ,
                            ConstResolutionPixelMm_X                    , ConstResolutionPixelMm_Y                  ,
                            parameterReal01 , parameterReal02   , parameterReal03   , parameterReal04               ,
                            parameterReal05 , parameterReal06   , parameterReal07   , parameterReal08               ,
                            id
                            ))
                cur.connection.commit()

        return redirect('base.html')