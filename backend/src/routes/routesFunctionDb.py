import controllers.varGlobal.adjustmentPanel

from flask                                              import Response
from flask                                              import render_template, request

from database.db_DeleteFilter                           import db_DeleteFilter
from database.db_InsertRow_parametersAdjustFilterImg    import Insert_parametersAdjustFilterImg
from database.db_SelectFilterByName                     import db_SelectFilterByName
from database.db_SelectFiltersName                      import db_SelectFiltersName
from database.db_SelectRow_nameParameters               import SelectRow_NameParametersAdjustFilterImg
from database.db_SelectRow_SeachForID                   import selectRow_SearchForID

def init_app(app):
    @app.route("/save-filter", methods=["POST"])
    def saveFilter():
        request_data = request.get_json()
        fileName = request_data['fileName']
        controllers.adjustmentPanel.varname = fileName
        Insert_parametersAdjustFilterImg.salvar()
        return 'ok'
    
    @app.route("/form-salvar", methods=["get"])
    def formsalvar():
        print("Chamada de evento ok")
        Insert_parametersAdjustFilterImg.salvar()
        return render_template('base.html')
    

    @app.route("/filter", methods=["POST"])
    def filter():
        request_data = request.get_json()
        fileName = request_data['fileName']
        if len(fileName) <= 0:
            return ''
       
        data = db_SelectFilterByName.Select(fileName)
        if data == None:
            return ''

        return {
            'id': data[0],
            'name': data[1],
            'lvermelho': data[2],
            'lverde': data[3],
            'lazul': data[4],
            'hvermelho': data[5],
            'hverde': data[6],
            'hazul': data[7],
            'erode': data[8],
            'dilate': data[9],
            'tamMinLv': data[10],
            'tamMaxLv': data[11],
            'tamMinLh': data[12],
            'tamMaxLh': data[13],
            'tamMin': data[14],
            'tamMax': data[15],
            'lineHorizontal': data[16],
            'lineVertical': data[17],
            'lineRange': data[18],
        }

    @app.route("/current_filter", methods=["GET"])
    def current_filter():
        current_file_name = controllers.adjustmentPanel.varname
        data = db_SelectFilterByName.Select(current_file_name)
        if data == None:
            return ''

        return {
            'id': data[0],
            'name': data[1],
            'lvermelho': data[2],
            'lverde': data[3],
            'lazul': data[4],
            'hvermelho': data[5],
            'hverde': data[6],
            'hazul': data[7],
            'erode': data[8],
            'dilate': data[9],
            'tamMinLv': data[10],
            'tamMaxLv': data[11],
            'tamMinLh': data[12],
            'tamMaxLh': data[13],
            'tamMin': data[14],
            'tamMax': data[15],
            'lineHorizontal': data[16],
            'lineVertical': data[17],
            'lineRange': data[18],
        }

    @app.route("/filters", methods=["GET"])
    def filtersName():
        filters = db_SelectFiltersName.Select()
        if len(filters) > 0:
            arrayFilters = []
            for i in list(filters):
                arrayFilters.append(i[0])
            return arrayFilters
        return []
    
    @app.route("/delete-filter", methods=["POST"])
    def deletefilter():
        request_data = request.get_json()
        name = request_data["name"]
        try:
            db_DeleteFilter.Delete(name)
        except:
            return 'Erro ao excluir filtro'
        return 'ok'





