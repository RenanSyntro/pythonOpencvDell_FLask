import controllers.varGlobal.global_areas_props as global_variable

from flask import redirect
from db import mysql

class Save_areas():
    def save(name):
        if name is None or name == "":
            return "name is required"
        
        with mysql.cursor() as cur:   
            cur.execute("INSERT INTO areasofoperationinthefilter VALUE (0, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (name,
                         global_variable.var_parametersArea_Area01_X1,
                         global_variable.var_parametersArea_Area01_Y1,
                         global_variable.var_parametersArea_Area01_X2,
                         global_variable.var_parametersArea_Area01_Y2,
                         global_variable.var_parametersArea_Area02_X1,
                         global_variable.var_parametersArea_Area02_Y1,
                         global_variable.var_parametersArea_Area02_X2,
                         global_variable.var_parametersArea_Area02_Y2,
                         global_variable.var_parametersArea_Area03_X1,
                         global_variable.var_parametersArea_Area03_Y1,
                         global_variable.var_parametersArea_Area03_X2,
                         global_variable.var_parametersArea_Area03_Y2,
                         global_variable.var_parametersArea_Area04_X1,
                         global_variable.var_parametersArea_Area04_Y1,
                         global_variable.var_parametersArea_Area04_X2,
                         global_variable.var_parametersArea_Area04_Y2
                        ))
            cur.connection.commit()
            global_variable.var_parametersArea_name = name
        return redirect('base.html')