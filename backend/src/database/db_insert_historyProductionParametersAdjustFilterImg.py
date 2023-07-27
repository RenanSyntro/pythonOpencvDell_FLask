import controllers.varGlobal.adjustmentPanel

from flask import redirect
from db import mysql

class db_insert_historyProductionParametersAdjustFilterImg():
    def salvar(imageName):
        id          = imageName

        #
        #Name
        #
        name        = controllers.varGlobal.adjustmentPanel.var_name

        #
        #Color
        #
        parameter01 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min
        parameter02 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max

        parameter03 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min
        parameter04 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max

        parameter05 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min
        parameter06 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max

        #
        #Iterations
        #
        parameter07 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_erode
        parameter08 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_dilate

        #
        #Seam according to color
        #
        #Vertically     - White
        parameter09 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min
        parameter10 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max
        #Horizontally   - White
        parameter11 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min
        parameter12 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max
        #Vertically     - Black
        parameter13 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Min
        parameter14 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Max
        #Horizontally   - Black
        parameter15 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min
        parameter16 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max

        #
        #Filter Object Size 
        #
        parameter17 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min
        parameter18 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max

        parameter19 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min
        parameter20 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max

        parameter21 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min
        parameter22 = controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max

        #
        #Reserve Integer
        #
        parameter23 = 0 
        parameter24 = 0
        parameter25 = 0 
        parameter26 = 0
        parameter27 = 0 
        parameter28 = 0
        parameter29 = 0 
        parameter30 = 0

        #
        #Conversion Pixel in Unit
        #
        parameterReal01 = controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X
        parameterReal02 = controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y

        #
        #Reserve Real
        #
        parameterReal03 = 0.0
        parameterReal04 = 0.0

        with mysql.cursor() as cur:
            #try:
                cur.execute("INSERT INTO historyProductionParametersAdjustFilterImg VALUE"
                            "(%s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s"
                            ")",
                            (id, name,
                            parameter01     , parameter02       , parameter03       , parameter04       , parameter05,
                            parameter06     , parameter07       , parameter08       , parameter09       , parameter10,
                            parameter11     , parameter12       , parameter13       , parameter14       , parameter15,
                            parameter16     , parameter17       , parameter18       , parameter19       , parameter20,
                            parameter21     , parameter22       , parameter23       , parameter24       , parameter25,
                            parameter26     , parameter27       , parameter28       , parameter29       , parameter30,
                            parameterReal01 , parameterReal02   , parameterReal03   , parameterReal04
                            ))
                cur.connection.commit()
        return redirect('base.html')