from db import mysql
import controllers.varGlobal.global_areas_props as global_variable

class GetAreasByID():
    def Select():
        id = global_variable.var_parametersArea_id
        with mysql.cursor() as cur:
            if(id is None or id <= 0):
                return "ok"
            
            cur.execute("SELECT * FROM areasofoperationinthefilter")
            areas = cur.fetchall()

            if(len(areas) >0 ):
                global_variable.var_parametersArea_id = areas[0][0]
                global_variable.var_parametersArea_name = areas[0][1]
                global_variable.var_parametersArea_Area01_X1 = areas[0][2]
                global_variable.var_parametersArea_Area01_Y1 = areas[0][3]
                global_variable.var_parametersArea_Area01_X2 = areas[0][4]
                global_variable.var_parametersArea_Area01_Y2 = areas[0][5]
                global_variable.var_parametersArea_Area02_X1 = areas[0][6]
                global_variable.var_parametersArea_Area02_Y1 = areas[0][7]
                global_variable.var_parametersArea_Area02_X2 = areas[0][8]
                global_variable.var_parametersArea_Area02_Y2 = areas[0][9]
                global_variable.var_parametersArea_Area03_X1 = areas[0][10]
                global_variable.var_parametersArea_Area03_Y1 = areas[0][11]
                global_variable.var_parametersArea_Area03_X2 = areas[0][12]
                global_variable.var_parametersArea_Area03_Y2 = areas[0][13]
                global_variable.var_parametersArea_Area04_X1 = areas[0][14]
                global_variable.var_parametersArea_Area04_Y1 = areas[0][15]
                global_variable.var_parametersArea_Area04_X2 = areas[0][16]
                global_variable.var_parametersArea_Area04_Y2 = areas[0][17]

        return "ok"