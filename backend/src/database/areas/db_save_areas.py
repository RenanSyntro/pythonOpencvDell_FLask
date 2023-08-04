from controllers.varGlobal.global_areas_props import *

from flask import redirect
from db import mysql

class Save_areas():
    def save():
        with mysql.cursor() as cur:   
            cur.execute("INSERT INTO areasofoperationinthefilter VALUE (0, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (var_parametersArea_name,
                         var_parametersArea_Area01_X1,
                         var_parametersArea_Area01_Y1,
                         var_parametersArea_Area01_X2,
                         var_parametersArea_Area01_Y2,
                         var_parametersArea_Area02_X1,
                         var_parametersArea_Area02_Y1,
                         var_parametersArea_Area02_X2,
                         var_parametersArea_Area02_Y2,
                         var_parametersArea_Area03_X1,
                         var_parametersArea_Area03_Y1,
                         var_parametersArea_Area03_X2,
                         var_parametersArea_Area03_Y2,
                         var_parametersArea_Area04_X1,
                         var_parametersArea_Area04_Y1,
                         var_parametersArea_Area04_X2,
                         var_parametersArea_Area04_Y2
                        ))
            cur.connection.commit()
    

        return redirect('base.html')