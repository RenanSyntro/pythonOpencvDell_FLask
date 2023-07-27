from flask.views import MethodView
from flask import request, render_template, redirect, flash
from db import mysql
from controllers.varGlobal.adjustmentPanel import *

class SelectRow_NameParametersAdjustFilterImg():
    def Select():
        with mysql.cursor() as cur:
                cur.execute("SELECT * FROM parametersAdjustFilterImg")
                nameParameters = cur.fetchall()

        return  nameParameters
  

  