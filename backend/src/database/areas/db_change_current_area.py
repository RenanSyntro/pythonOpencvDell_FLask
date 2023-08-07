from db import mysql
import controllers.varGlobal.global_areas_props as global_variable

class ChangeCurrentArea():
    def Change(id):
        with mysql.cursor() as cur: 
            if(id is None or id < 1):
                return "id is required"
            
            cur.execute("SELECT * FROM areasofoperationinthefilter WHERE id = %s", id)
            areas = cur.fetchone()

            if(len(areas) >0 ):
                global_variable.var_parametersArea_id = areas[0]
                global_variable.var_parametersArea_name = areas[1]
                global_variable.var_parametersArea_Area01_X1 = areas[2]
                global_variable.var_parametersArea_Area01_Y1 = areas[3]
                global_variable.var_parametersArea_Area01_X2 = areas[4]
                global_variable.var_parametersArea_Area01_Y2 = areas[5]
                global_variable.var_parametersArea_Area02_X1 = areas[6]
                global_variable.var_parametersArea_Area02_Y1 = areas[7]
                global_variable.var_parametersArea_Area02_X2 = areas[8]
                global_variable.var_parametersArea_Area02_Y2 = areas[9]
                global_variable.var_parametersArea_Area03_X1 = areas[10]
                global_variable.var_parametersArea_Area03_Y1 = areas[11]
                global_variable.var_parametersArea_Area03_X2 = areas[12]
                global_variable.var_parametersArea_Area03_Y2 = areas[13]
                global_variable.var_parametersArea_Area04_X1 = areas[14]
                global_variable.var_parametersArea_Area04_Y1 = areas[15]
                global_variable.var_parametersArea_Area04_X2 = areas[16]
                global_variable.var_parametersArea_Area04_Y2 = areas[17]

            return "ok"