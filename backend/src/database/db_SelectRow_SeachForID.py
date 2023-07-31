import controllers.varGlobal.adjustmentPanel

from flask import redirect
from db import mysql

class selectRow_SearchForID():

    def Select(id):
        with mysql.cursor() as cur:
                cur.execute("SELECT * FROM parametersAdjustFilterImg WHERE id = %s", (id,))
                data = cur.fetchone()

                print (data)

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
                #Iterations
                #
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_erode                                         = data[8]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_dilate                                        = data[9]

                #
                #Seam according to color
                #
                #Vertically     - White
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min       = data[10]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max       = data[11]
                #Horizontally   - White
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min     = data[12]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max     = data[13]
                #Vertically     - Black
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Min       = data[14]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Max       = data[15]
                #Horizontally   - Black
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min     = data[16]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max     = data[17]

                #
                #Filter Object Size 
                #
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min                                = data[14]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max                                = data[15]

                controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min                  = data[16]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max                  = data[17]

                controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min                = data[18]
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max                = data[19]

                controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X                                          = data[21]
                controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y                                          = data[22]

        return redirect('base.html')
  




