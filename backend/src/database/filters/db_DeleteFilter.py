from db import mysql
import controllers.varGlobal.adjustmentPanel as global_variable


class db_DeleteFilter():
    def Delete():
        name = global_variable.var_name
        if( name is None or name == ""):
            return "name is required"
        
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM parametersAdjustFilterImg WHERE name=%s", name)