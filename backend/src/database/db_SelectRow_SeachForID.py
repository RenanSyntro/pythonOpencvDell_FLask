import controllers.varGlobal.adjustmentPanel

from flask import redirect
from db import mysql

class selectRow_SearchForID():

    def Select(id):
        with mysql.cursor() as cur:
                cur.execute("SELECT * FROM parametersAdjustFilterImg WHERE id = %s", (id,))
                data = cur.fetchone()

                #
                #Name
                #
                controllers.varGlobal.adjustmentPanel.var_name                                                                      = data[1]
                print(controllers.varGlobal.adjustmentPanel.var_name)

                #
                #Color
                #
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min                                = data[2]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max                                = data[3]

                controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min                              = data[4]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max                              = data[5]

                controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min                               = data[6]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max                               = data[7]

                #
                #Defined Area For Filter init
                #
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_DefinedAreaForFilter_init_X                              = data[8]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_DefinedAreaForFilter_init_Y                              = data[9]

                #
                #Iterations
                #
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_erode                                         = data[10]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_dilate                                        = data[11]

                #
                #Seam according to color
                #
                #Vertically     - White
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min       = data[12]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max       = data[13]
                #Area
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_IdAreasOfOperationInTheFilter     = data[14]

                #Horizontally   - White
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min     = data[15]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max     = data[16]
                #Area
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteHor_IdAreasOfOperationInTheFilter     = data[17]

                #Vertically     - Black
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Min       = data[18]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Max       = data[19]
                #Area
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpBlackVer_IdAreasOfOperationInTheFilter     = data[20]

                #Horizontally   - Black
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min     = data[21]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max     = data[22]
                #Area
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpBlackHor_IdAreasOfOperationInTheFilter     = data[23]

                #
                #Filter Object Size 
                #
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min                                = data[24]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max                                = data[25]

                controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min                  = data[26]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max                  = data[27]

                controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min                = data[28]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max                = data[29]

        return redirect('base.html')
  




