from db import mysql
import controllers.varGlobal.global_areas_props as global_variable


class db_Delete():
    def Delete():
        with mysql.cursor() as cur:
            if(global_variable.var_parametersArea_id is None or global_variable.var_parametersArea_id <= 0):
                return None
            cur.execute("DELETE FROM areasofoperationinthefilter WHERE id=%s", global_variable.var_parametersArea_id)
           
            global_variable.var_parametersArea_id = 0
            global_variable.var_parametersArea_name = 0
            global_variable.var_parametersArea_Area01_X1 = 0
            global_variable.var_parametersArea_Area01_Y1 = 0
            global_variable.var_parametersArea_Area01_X2 = 0
            global_variable.var_parametersArea_Area01_Y2 = 0
            global_variable.var_parametersArea_Area02_X1 = 0
            global_variable.var_parametersArea_Area02_Y1 = 0
            global_variable.var_parametersArea_Area02_X2 = 0
            global_variable.var_parametersArea_Area02_Y2 = 0
            global_variable.var_parametersArea_Area03_X1 = 0
            global_variable.var_parametersArea_Area03_Y1 = 0
            global_variable.var_parametersArea_Area03_X2 = 0
            global_variable.var_parametersArea_Area03_Y2 = 0
            global_variable.var_parametersArea_Area04_X1 = 0
            global_variable.var_parametersArea_Area04_Y1 = 0
            global_variable.var_parametersArea_Area04_X2 = 0
            global_variable.var_parametersArea_Area04_Y2 = 0