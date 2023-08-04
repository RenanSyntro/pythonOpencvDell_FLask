from db import mysql

class GetAreasName():
    def Select():
        with mysql.cursor() as cur:
            cur.execute("SELECT id,name FROM areasofoperationinthefilter")
            name_areas = cur.fetchall()
        return  name_areas
  

  