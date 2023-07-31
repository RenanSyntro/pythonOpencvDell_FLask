import controllers.varGlobal.adjustmentPanel

from flask import redirect
from db import mysql


class db_SelectFilterByName():
    def Select(name):
        with mysql.cursor() as cur:
            cur.execute(
                "SELECT * FROM parametersAdjustFilterImg WHERE name = %s", name)
            data = cur.fetchone()
            if data != None:
                #
                #Name
                #
                controllers.varGlobal.adjustmentPanel.var_name                                                                      = data[1]

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
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_JumpSize_Field_X                  = data[14]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_JumpSize_Field_Y                  = data[15]

                #Horizontally   - White
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min     = data[16]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max     = data[17]
                #Area
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_JumpSize_Field_X                  = data[18]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_JumpSize_Field_Y                  = data[19]

                #Vertically     - Black
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Min       = data[20]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Max       = data[21]
                #Area
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_JumpSize_Field_X                  = data[22]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_JumpSize_Field_Y                  = data[23]

                #Horizontally   - Black
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min     = data[24]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max     = data[25]
                #Area
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_JumpSize_Field_X                  = data[26]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpWhiteVer_JumpSize_Field_Y                  = data[27]

                #
                #Filter Object Size 
                #
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min                                = data[28]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max                                = data[29]

                controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min                  = data[30]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max                  = data[31]

                controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min                = data[32]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max                = data[33]
                
            return data