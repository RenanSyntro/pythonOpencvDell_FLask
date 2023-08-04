import controllers.varGlobal.adjustmentPanel

from flask                                              import Response
from flask                                              import render_template, request

def init_app(app):
    
    #@app.route("/loeheight", methods=["POST"])
    @app.route("/parametersFilter_selectFilterColor", methods=["POST"])
    def selectFilterColor():
        request_data = request.get_json()
        color   = request_data["color"]
        low     = request_data["low"]
        hight   = request_data["hight"]

        if (low != None and hight != None):
            match color:
                case "vermelho":
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min      != int(low)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min      = int(low)
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max      != int(hight)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max      = int(hight)
                case "verde":
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min    != int(low)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min    = int(low)
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max    != int(hight)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max    = int(hight)
                case "azul":
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min     != int(low)): 
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min     = int(low)
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max     != int(hight)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max     = int(hight)
        return 'ok'
    
    #Iterações desgastam
    @app.route("/parametersFilter_Iterations_erode", methods=["POST"])
    def Iterations_erode():
        request_data = request.get_json()
        value = request_data["value"]

        if (value != None):
           if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_erode            != int(value)):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_erode       = int(value)
        return 'ok'
    
    #Iterações dilatam
    @app.route("/parametersFilter_Iterations_dilate", methods=["POST"])
    def Iterations_dilate():
        request_data = request.get_json()
        value = request_data["value"]

        if (value != None):
           if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_dilate           != int(value)):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_Iterations_dilate      = int(value)
        return 'ok'

    #@app.route("/tamminmaxlvlh", methods=["POST"])
    #Emenda linha pulando cor branca - Tamanho do salto
    @app.route("/parametersFilter_SpliceLineJumpingWhiteColor_JumpSize", methods=["POST"])
    def SpliceLineJumpingWhiteColor_JumpSize():
        request_data = request.get_json()
        lvlh    = request_data["attr"]
        min     = request_data["min"]
        max     = request_data["max"]

        if (min != None and max != None):
            match lvlh:
                case "lv":
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min   != int(min)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min   = int(min)
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max   != int(max)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max   = int(max)    
                case "lh":
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min   != int(min)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min   = int(min)
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max   != int(max)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max   = int(max)
        return 'ok'
 
    #Emenda linha pulando cor preta - Tamanho do salto
    @app.route("/parametersFilter_SpliceLineJumpingBlackColor_JumpSize", methods=["POST"])
    def SpliceLineJumpingBlackColor_JumpSize():
        request_data = request.get_json()
        lvlh    = request_data["attr"]
        min     = request_data["min"]
        max     = request_data["max"]

        if (min != None and max != None):
            match lvlh:
                case "lv":
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min   != int(min)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min   = int(min)
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max   != int(max)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max   = int(max)    
                case "lh":
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min   != int(min)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min   = int(min)
                    if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max   != int(max)):
                        controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max   = int(max)
        return 'ok'
   
    #@app.route("/tamminmax", methods=["POST"])
    #Filtro tamanho do objeto encontrado
    @app.route("/parametersFilter_FoundObjectSizeFilter", methods=["POST"])
    def FoundObjectSizeFilter():
        request_data = request.get_json()
        min = request_data["min"]
        max = request_data["max"]

        if (min != None and max != None):
           if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min != int(min)):
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min = int(min)
           if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max != int(max)):
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max = int(max)
        return 'ok'
    
    #@app.route("/trackbar_LineVertical", methods=["POST"])
    #Filtro tamanho da linha vertical do objeto encontrado
    @app.route("/parametersFilter_VerticalLineSizeFilterOfFoundObject", methods=["POST"])
    def VerticalLineSizeFilterOfFoundObject():
        request_data = request.get_json()
        min     = request_data["min"]
        max     = request_data["max"]

        if (min != None):
            if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min != int(min)):
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min = int(min)
        if  (max != None):
            if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max != int(max)):
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max = int(max)

        return 'ok'
    
    #@app.route("/trackbar_LineHorizontal", methods=["POST"])
    @app.route("/parametersFilter_HorizontalLineSizeFilterOfFoundObject", methods=["POST"])
    def HorizontalLineSizeFilterOfFoundObject():
        request_data = request.get_json()
        min     = request_data["min"]
        max     = request_data["max"]

        if (min != None):
            if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min != int(min)):
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min = int(min)
        if  (max != None):
            if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max != int(max)):
                controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max = int(max)

        return 'ok'
    





