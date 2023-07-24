import controllers.adjustmentPanel

from flask import redirect
from db import mysql

class db_insert_historyProductionParametersAdjustFilterImg():
    def salvar(imageName):
        id          = imageName
        name        = controllers.adjustmentPanel.varname
        parameter01 = controllers.adjustmentPanel.varTrackbar1
        parameter02 = controllers.adjustmentPanel.varTrackbar2
        parameter03 = controllers.adjustmentPanel.varTrackbar3
        parameter04 = controllers.adjustmentPanel.varTrackbar4
        parameter05 = controllers.adjustmentPanel.varTrackbar5
        parameter06 = controllers.adjustmentPanel.varTrackbar6
        parameter07 = controllers.adjustmentPanel.varTrackbar_iterations_erode
        parameter08 = controllers.adjustmentPanel.varTrackbar_iterations_dilate
        parameter09 = controllers.adjustmentPanel.varTrackbar_TamMinLv
        parameter10 = controllers.adjustmentPanel.varTrackbar_TamMaxLv
        parameter11 = controllers.adjustmentPanel.varTrackbar_TamMinLh
        parameter12 = controllers.adjustmentPanel.varTrackbar_TamMaxLh
        parameter13 = controllers.adjustmentPanel.varTrackbar_TamMin
        parameter14 = controllers.adjustmentPanel.varTrackbar_TamMax
        parameter15 = controllers.adjustmentPanel.varTrackbar_LineHorizontal
        parameter16 = controllers.adjustmentPanel.varTrackbar_LineVertical
        parameter17 = controllers.adjustmentPanel.varTrackbar_LineRange
        parameter18 = 0
        parameter19 = 0
        parameter20 = 0
        parameterReal01 = controllers.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X
        parameterReal02 = controllers.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y
        parameterReal03 = 0.0
        parameterReal04 = 0.0

        with mysql.cursor() as cur:
            #try:
                cur.execute("INSERT INTO historyProductionParametersAdjustFilterImg VALUE"
                            "(%s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s, "
                            "%s, %s, %s, %s, %s,"
                            "%s, %s, %s, %s"
                            ")",
                            (id, name,
                            parameter01     , parameter02       , parameter03       , parameter04       , parameter05,
                            parameter06     , parameter07       , parameter08       , parameter09       , parameter10,
                            parameter11     , parameter12       , parameter13       , parameter14       , parameter15,
                            parameter16     , parameter17       , parameter18       , parameter19       , parameter20,
                            parameterReal01 , parameterReal02   , parameterReal03   , parameterReal04
                            ))
                cur.connection.commit()
        return redirect('base.html')