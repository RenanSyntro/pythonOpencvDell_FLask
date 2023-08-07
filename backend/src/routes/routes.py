
from flask                                          import render_template, request
from flask_cors                                     import CORS
from database.filters.db_InsertRow_parametersAdjustFilterImg import Insert_parametersAdjustFilterImg
from database.filters.db_SelectFiltersName import db_SelectFiltersName
from database.filters.db_SelectRow_nameParameters   import SelectRow_NameParametersAdjustFilterImg
from database.filters.db_SelectRow_SeachForID       import selectRow_SearchForID
from database.areas.db_get_areas_name               import GetAreasName
from database.areas.db_save_areas                   import Save_areas
from database.areas.db_change_current_area              import ChangeCurrentArea
from database.areas.db_delete_area                  import db_Delete
import controllers.frames.generateFrame
import controllers.frames.frames
import controllers.varGlobal.adjustmentPanel 
import controllers.varGlobal.adjustmentPanel         as global_variable 
import controllers.varGlobal.global_areas_props      as area_global_variable


def init_app(app):
    CORS(app, resources={"*": {"origins": "*"}})

    ############### API DOS FILTROS ###############
    ###############################################
    @app.route("/selectFilterColorRedMin", methods=["POST"])
    def selectFilterColorRedMin():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_selectFilterColor_Red_Min = value
        return 'ok'


    @app.route("/selectFilterColorRedMax", methods=["POST"])
    def selectFilterColorRedMax():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_selectFilterColor_Red_Max = value
        return 'ok'
    

    @app.route("/selectFilterColorGreenMin", methods=["POST"])
    def selectFilterColorGreenMin():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_selectFilterColor_Green_Min = value
        return 'ok'


    @app.route("/selectFilterColorGreenMax", methods=["POST"])
    def selectFilterColorGreenMax():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_selectFilterColor_Green_Max = value
        return 'ok'


    @app.route("/selectFilterColorBlueMin", methods=["POST"])
    def selectFilterColorBlueMin():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_selectFilterColor_Blue_Min = value
        return 'ok'
    

    @app.route("/selectFilterColorBlueMax", methods=["POST"])
    def selectFilterColorBlueMax():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_selectFilterColor_Blue_Max = value
        return 'ok'


    @app.route("/parametersFilter_Iterations_erode", methods=["POST"])
    def parametersFilter_Iterations_erode():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_Iterations_erode = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_iterations_dilate", methods=["POST"])
    def trackbar_parametersFilter_iterations_dilate():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_Iterations_dilate = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min", methods=["POST"])
    def trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min", methods=["POST"])
    def trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max", methods=["POST"])
    def trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_FoundObjectSizeFilter_Min", methods=["POST"])
    def trackbar_parametersFilter_FoundObjectSizeFilter_Min():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_FoundObjectSizeFilter_Min = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_FoundObjectSizeFilter_Max", methods=["POST"])
    def trackbar_parametersFilter_FoundObjectSizeFilter_Max():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_FoundObjectSizeFilter_Max = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min", methods=["POST"])
    def trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max", methods=["POST"])
    def trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Min", methods=["POST"])
    def trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Min():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min = int(value)
        return 'ok'
    

    @app.route("/trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Max", methods=["POST"])
    def trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Max():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max = int(value)
        return 'ok'
    

    @app.route("/trackbar_ResolutionPixMm_X", methods=["POST"])
    def trackbar_ResolutionPixMm_X():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.varTrackbar_ConstResolutionPixelMm_X = int(value)
        return 'ok'
    

    @app.route("/trackbar_ResolutionPixMm_Y", methods=["POST"])
    def trackbar_ResolutionPixMm_Y():
        request_data = request.get_json()
        value = request_data["value"]
        global_variable.varTrackbar_ConstResolutionPixelMm_Y = int(value)
        return 'ok'
    

    @app.route("/get_filters", methods=["GET"])
    def get_filters():
        filters_name = db_SelectFiltersName.Select()
        if len(filters_name) > 0:
            arrayFilters = []
            for i in list(filters_name):
                arrayFilters.append({"id":i[0], "name":i[1]})
            return arrayFilters
        return []
    

    @app.route("/save_filters", methods=["POST"])
    def save_filters():
        request_data = request.get_json()
        name = request_data['name']
        if name is None or name == "":
            return "name is required"
        
        Insert_parametersAdjustFilterImg.salvar(name)
        return "ok"
    
    
    @app.route("/delete_filters", methods=["POST"])
    def delete_filters():
        return "ok"
    

    @app.route("/change_current_filters", methods=["POST"])
    def change_current_filters():
        request_data = request.get_json()
        id = request_data['id']
        return "ok"
    






    ############### API DAS AREAS ###############
    ###############################################
    @app.route("/set_areas", methods=["POST"])
    def create_areas():
        request_data = request.get_json()
        area_eixo = request_data['area_eixo']
        value = request_data['value']

        match area_eixo:
            case 'area01_X':
                 area_global_variable.var_parametersArea_Area01_X1 = value[0]
                 area_global_variable.var_parametersArea_Area01_X2 = value[1]
            case 'area01_Y':
                 area_global_variable.var_parametersArea_Area01_Y1 = value[0]
                 area_global_variable.var_parametersArea_Area01_Y2 = value[1]
            case 'area02_X':
                 area_global_variable.var_parametersArea_Area02_X1 = value[0]
                 area_global_variable.var_parametersArea_Area02_X2 = value[1]
            case 'area02_Y':
                 area_global_variable.var_parametersArea_Area02_Y1 = value[0]
                 area_global_variable.var_parametersArea_Area02_Y2 = value[1]
            case 'area03_X':
                 area_global_variable.var_parametersArea_Area03_X1 = value[0]
                 area_global_variable.var_parametersArea_Area03_X2 = value[1]
            case 'area03_Y':
                 area_global_variable.var_parametersArea_Area03_Y1 = value[0]
                 area_global_variable.var_parametersArea_Area03_Y2 = value[1]
            case 'area04_X':
                 area_global_variable.var_parametersArea_Area04_X1 = value[0]
                 area_global_variable.var_parametersArea_Area04_X2 = value[1]
            case 'area04_Y':
                 area_global_variable.var_parametersArea_Area04_Y1 = value[0]
                 area_global_variable.var_parametersArea_Area04_Y2 = value[1]
        return 'ok'


    @app.route("/get_current_areas_params", methods=["GET"])
    def get_current_areas_params():
        return {"width":area_global_variable.var_size_max_img_width,
                "height":area_global_variable.var_size_max_img_height,
                "area01_X1":area_global_variable.var_parametersArea_Area01_X1,
                "area01_Y1":area_global_variable.var_parametersArea_Area01_Y1,
                "area01_X2":area_global_variable.var_parametersArea_Area01_X2,
                "area01_Y2":area_global_variable.var_parametersArea_Area01_Y2,
                "area02_X1":area_global_variable.var_parametersArea_Area02_X1,
                "area02_Y1":area_global_variable.var_parametersArea_Area02_Y1,
                "area02_X2":area_global_variable.var_parametersArea_Area02_X2,
                "area02_Y2":area_global_variable.var_parametersArea_Area02_Y2,
                "area03_X1":area_global_variable.var_parametersArea_Area03_X1,
                "area03_Y1":area_global_variable.var_parametersArea_Area03_Y1,
                "area03_X2":area_global_variable.var_parametersArea_Area03_X2,
                "area03_Y2":area_global_variable.var_parametersArea_Area03_Y2,
                "area04_X1":area_global_variable.var_parametersArea_Area04_X1,
                "area04_Y1":area_global_variable.var_parametersArea_Area04_Y1,
                "area04_X2":area_global_variable.var_parametersArea_Area04_X2,
                "area04_Y2":area_global_variable.var_parametersArea_Area04_Y2}
    

    @app.route("/get_areas", methods=["GET"])
    def get_areas():
        areas_name = GetAreasName.Select()
        if len(areas_name) > 0:
            arrayFilters = []
            for i in list(areas_name):
                arrayFilters.append({"id":i[0], "name":i[1]})
            return arrayFilters
        return []


    @app.route("/change_current_areas", methods=["POST"])
    def change_current_areas():
        request_data = request.get_json()
        id = request_data['id']
        if id < 1:
            return "id is required"
        
        ChangeCurrentArea.Change(id)
        return "ok"


    @app.route("/save_areas", methods=["POST"])
    def save_areas():
        request_data = request.get_json()
        Save_areas.save(request_data['name'])
        return "ok"
    

    @app.route("/delete_areas", methods=["POST"])
    def delete_areas():
        db_Delete.Delete()
        return "ok"
        







    ############### API FLASK ###############
    ###############################################
    @app.route("/", methods=["GET", "POST"])
    def index():
        nameParameters = SelectRow_NameParametersAdjustFilterImg.Select()

        if request.method == "POST":

            if  (request.form.get("parametrosSelect") != None):
                selectRow_SearchForID.Select(int(request.form.get("parametrosSelect")))

            #
            #Color
            #
            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Red_Min") != None):
                if (global_variable.var_parametersFilter_selectFilterColor_Red_Min                      !=  int(request.form.get("trackbar_parametersFilter_selectFilterColor_Red_Min"))):
                    global_variable.var_parametersFilter_selectFilterColor_Red_Min                      =	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Red_Min"))
                elif (global_variable.var_parametersFilter_selectFilterColor_Red_Min                    !=  int(request.form.get("number_parametersFilter_selectFilterColor_Red_Min"))):
                    global_variable.var_parametersFilter_selectFilterColor_Red_Min                      =	int(request.form.get("number_parametersFilter_selectFilterColor_Red_Min"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Red_Max") != None):
                if (global_variable.var_parametersFilter_selectFilterColor_Red_Max                      !=	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Red_Max"))):
                    global_variable.var_parametersFilter_selectFilterColor_Red_Max                      =	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Red_Max"))
                elif (global_variable.var_parametersFilter_selectFilterColor_Red_Max                    !=  int(request.form.get("number_parametersFilter_selectFilterColor_Red_Max"))):
                    global_variable.var_parametersFilter_selectFilterColor_Red_Max                      =	int(request.form.get("number_parametersFilter_selectFilterColor_Red_Max"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Green_Min") != None):
                if (global_variable.var_parametersFilter_selectFilterColor_Green_Min                    !=	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Green_Min"))):
                    global_variable.var_parametersFilter_selectFilterColor_Green_Min                    =	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Green_Min"))
                elif (global_variable.var_parametersFilter_selectFilterColor_Green_Min                  !=  int(request.form.get("number_parametersFilter_selectFilterColor_Green_Min"))):
                    global_variable.var_parametersFilter_selectFilterColor_Green_Min                    =	int(request.form.get("number_parametersFilter_selectFilterColor_Green_Min"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Green_Max") != None):
                if (global_variable.var_parametersFilter_selectFilterColor_Green_Max                    !=	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Green_Max"))):
                    global_variable.var_parametersFilter_selectFilterColor_Green_Max                    =	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Green_Max"))
                elif (global_variable.var_parametersFilter_selectFilterColor_Green_Max                  !=  int(request.form.get("number_parametersFilter_selectFilterColor_Green_Max"))):
                    global_variable.var_parametersFilter_selectFilterColor_Green_Max                    =	int(request.form.get("number_parametersFilter_selectFilterColor_Green_Max"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Blue_Min") != None):
                if (global_variable.var_parametersFilter_selectFilterColor_Blue_Min                    !=	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Blue_Min"))):
                    global_variable.var_parametersFilter_selectFilterColor_Blue_Min                    =	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Blue_Min"))
                elif (global_variable.var_parametersFilter_selectFilterColor_Blue_Min                  !=   int(request.form.get("number_parametersFilter_selectFilterColor_Blue_Min"))):
                    global_variable.var_parametersFilter_selectFilterColor_Blue_Min                    =	int(request.form.get("number_parametersFilter_selectFilterColor_Blue_Min"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Blue_Max") != None):
                if (global_variable.var_parametersFilter_selectFilterColor_Blue_Max                    !=	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Blue_Max"))):
                    global_variable.var_parametersFilter_selectFilterColor_Blue_Max                    =	int(request.form.get("trackbar_parametersFilter_selectFilterColor_Blue_Max"))
                elif (global_variable.var_parametersFilter_selectFilterColor_Blue_Max                  != int(request.form.get("number_parametersFilter_selectFilterColor_Blue_Max"))):
                    global_variable.var_parametersFilter_selectFilterColor_Blue_Max                    =	int(request.form.get("number_parametersFilter_selectFilterColor_Blue_Max"))

            #
            #Iterations
            #
            if (request.form.get("trackbar_parametersFilter_iterations_erode") != None):
                if (global_variable.var_parametersFilter_Iterations_erode                             
                    !=	int(request.form.get("trackbar_parametersFilter_iterations_erode"))):
                    global_variable.var_parametersFilter_Iterations_erode = int(request.form.get("trackbar_parametersFilter_iterations_erode"))
                elif (global_variable.var_parametersFilter_Iterations_erode                           !=  int(request.form.get("number_parametersFilter_iterations_erode"))):
                    global_variable.var_parametersFilter_Iterations_erode 	                        =	int(request.form.get("number_parametersFilter_iterations_erode"))

            if (request.form.get("trackbar_parametersFilter_iterations_dilate") != None):
                if (global_variable.var_parametersFilter_Iterations_dilate                            !=	int(request.form.get("trackbar_parametersFilter_iterations_dilate"))):
                    global_variable.var_parametersFilter_Iterations_dilate 	                        =	int(request.form.get("trackbar_parametersFilter_iterations_dilate"))
                elif (global_variable.var_parametersFilter_Iterations_dilate                          !=  int(request.form.get("number_parametersFilter_iterations_dilate"))):
                    global_variable.var_parametersFilter_Iterations_dilate 	                        =	int(request.form.get("number_parametersFilter_iterations_dilate"))

            #
            #Seam according to color
            #
            if (request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min") != None):
                if (global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min               !=	int(request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min"))):
                    global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min               =	int(request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min"))
                elif (global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min             !=  int(request.form.get("number_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min"))):
                    global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min               =	int(request.form.get("number_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min"))

            if (request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max") != None):
                if (global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max               !=	int(request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max"))):
                    global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max               = 	int(request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max"))
                elif (global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max             !=  int(request.form.get("number_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max"))):
                    global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max               =	int(request.form.get("number_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max"))

            if (request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min") != None):
                if (global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min            !=   int(request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min"))):
                    global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min            =    int(request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min"))
                elif (global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min          !=   int(request.form.get("number_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min"))):
                    global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min            =    int(request.form.get("number_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min"))

            if (request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max") != None):
                if (global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max            !=	int(request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max"))):
                    global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max            =	int(request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max"))
                elif (global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max          !=   int(request.form.get("number_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max"))):
                    global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max            =	int(request.form.get("number_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max"))

            #s
            #Filter Object Size 
            #
            if (request.form.get("trackbar_parametersFilter_FoundObjectSizeFilter_Min") != None):
                if (global_variable.var_parametersFilter_FoundObjectSizeFilter_Min                           !=  int(request.form.get("trackbar_parametersFilter_FoundObjectSizeFilter_Min"))):
                    global_variable.var_parametersFilter_FoundObjectSizeFilter_Min                           =   int(request.form.get("trackbar_parametersFilter_FoundObjectSizeFilter_Min"))
                elif (global_variable.var_parametersFilter_FoundObjectSizeFilter_Min                         !=  int(request.form.get("number_parametersFilter_FoundObjectSizeFilter_Min"))):
                    global_variable.var_parametersFilter_FoundObjectSizeFilter_Min                           =   int(request.form.get("number_parametersFilter_FoundObjectSizeFilter_Min"))

            if (request.form.get("trackbar_parametersFilter_FoundObjectSizeFilter_Max") != None):
                if (global_variable.var_parametersFilter_FoundObjectSizeFilter_Max                           !=   int(request.form.get("trackbar_parametersFilter_FoundObjectSizeFilter_Max"))):
                    global_variable.var_parametersFilter_FoundObjectSizeFilter_Max                           =    int(request.form.get("trackbar_parametersFilter_FoundObjectSizeFilter_Max"))
                elif (global_variable.var_parametersFilter_FoundObjectSizeFilter_Max                         !=   int(request.form.get("number_parametersFilter_FoundObjectSizeFilter_Max"))):
                    global_variable.var_parametersFilter_FoundObjectSizeFilter_Max                           =	int(request.form.get("number_parametersFilter_FoundObjectSizeFilter_Max"))

            if (request.form.get("trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min") != None):
                if (global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min             !=   int(request.form.get("trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min"))):
                    global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min             =	int(request.form.get("trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min"))
                elif (global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min           !=   int(request.form.get("number_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min"))):
                    global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min             =	int(request.form.get("number_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min"))

            if (request.form.get("trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max") != None):
                if (global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max             !=   int(request.form.get("trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max"))):
                    global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max             =    int(request.form.get("trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max"))
                elif (global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max           !=   int(request.form.get("number_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max"))):
                    global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max             =    int(request.form.get("number_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max"))

            if (request.form.get("trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Min") != None):
                if (global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min            !=  int(request.form.get("trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Min"))):
                    global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min            =	int(request.form.get("trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Min"))
                elif (global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min          !=  int(request.form.get("number_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Min"))):
                    global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min            =	int(request.form.get("number_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Min"))

            if (request.form.get("trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Max") != None):
                if (global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max             !=  int(request.form.get("trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Max"))):
                    global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max             =   int(request.form.get("trackbar_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Max"))
                elif (global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max           !=  int(request.form.get("number_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Max"))):
                    global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max             =   int(request.form.get("number_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Max"))

            #
            #Resolution Pix to Mm
            #
            if (request.form.get("trackbar_ResolutionPixMm_X") != None):
                if (global_variable.varTrackbar_ConstResolutionPixelMm_X                                      !=	float(request.form.get("trackbar_ResolutionPixMm_X"))):
                    global_variable.varTrackbar_ConstResolutionPixelMm_X 	                                    =	float(request.form.get("trackbar_ResolutionPixMm_X"))
                elif (global_variable.varTrackbar_ConstResolutionPixelMm_X                                    !=  float(request.form.get("number_ResolutionPixMm_X"))):
                    global_variable.varTrackbar_ConstResolutionPixelMm_X 	                                    =	float(request.form.get("number_ResolutionPixMm_X"))

            if (request.form.get("trackbar_ResolutionPixMm_Y") != None):
                if (global_variable.varTrackbar_ConstResolutionPixelMm_Y                                      !=	float(request.form.get("trackbar_ResolutionPixMm_Y"))):
                    global_variable.varTrackbar_ConstResolutionPixelMm_Y 	                                    =	float(request.form.get("trackbar_ResolutionPixMm_Y"))
                elif (global_variable.varTrackbar_ConstResolutionPixelMm_Y                                    !=  float(request.form.get("number_ResolutionPixMm_Y"))):
                    global_variable.varTrackbar_ConstResolutionPixelMm_Y 	                                    =	float(request.form.get("number_ResolutionPixMm_Y"))

            #
            #Name Recipe
            #
            if (request.form.get("parameters_name") != None):
                global_variable.var_name = request.form.get("parameters_name")
        return render_template("base.html", 
                                    #
                                    #Name
                                    #
                                    nameParameters                                          = nameParameters,
                                    varhtml_name                                            = global_variable.var_name,
                                    
                                    #
                                    #Color
                                    #
                                    varhtml_parametersFilter_selectFilterColor_Red_Min	    = global_variable.var_parametersFilter_selectFilterColor_Red_Min, 
                                    varhtml_parametersFilter_selectFilterColor_Red_Max	    = global_variable.var_parametersFilter_selectFilterColor_Red_Max,
                                    
                                    varhtml_parametersFilter_selectFilterColor_Green_Min	= global_variable.var_parametersFilter_selectFilterColor_Green_Min,
                                    varhtml_parametersFilter_selectFilterColor_Green_Max	= global_variable.var_parametersFilter_selectFilterColor_Green_Max,
                                    
                                    varhtml_parametersFilter_selectFilterColor_Blue_Min	    = global_variable.var_parametersFilter_selectFilterColor_Blue_Min,
                                    varhtml_parametersFilter_selectFilterColor_Blue_Max	    = global_variable.var_parametersFilter_selectFilterColor_Blue_Max,

                                    #
                                    #Iterations
                                    #
                                    varhtml_parametersFilter_iterations_erode	= global_variable.var_parametersFilter_Iterations_erode,
                                    varhtml_parametersFilter_Iterations_dilate	= global_variable.var_parametersFilter_Iterations_dilate,

                                    #
                                    #Seam according to color
                                    #
                                    #Vertically     - White
                                    varhtml_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min     = global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min,
                                    varhtml_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max     = global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max,
                                    #Horizontally   - White
                                    varhtml_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min   = global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min,
                                    varhtml_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max    = global_variable.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max,
                                    #Vertically     - Black
                                    varhtml_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Min     = global_variable.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Min,
                                    varhtml_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Max     = global_variable.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Max,
                                    #Horizontally   - Black
                                    varhtml_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min   = global_variable.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min,
                                    varhtml_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max    = global_variable.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max,

                                    #
                                    #Filter Object Size 
                                    #
                                    varhtml_parametersFilter_FoundObjectSizeFilter_Min 	                                = global_variable.var_parametersFilter_FoundObjectSizeFilter_Min,
                                    varhtml_parametersFilter_FoundObjectSizeFilter_Max 	                                = global_variable.var_parametersFilter_FoundObjectSizeFilter_Max,
                                    
                                    varhtml_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min                    = global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min,
                                    varhtml_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max                    = global_variable.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max,

                                    varhtml_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Min                  = global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min,
                                    varhtml_parametersFilter_HorizontallyLineSizeFilterOfFoundObject_Max                  = global_variable.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max,

                                    #
                                    #Const Resolution Pixel Mm
                                    #
                                    varhtml_ConstResolutionPixelMm_X                               = global_variable.varTrackbar_ConstResolutionPixelMm_X,
                                    varhtml_ConstResolutionPixelMm_Y                               = global_variable.varTrackbar_ConstResolutionPixelMm_Y,
                                    
                                    #
                                    #Label Video Layer
                                    #
                                    get_video_nameLayer01           = "Camada 01",
                                    get_video_nameLayer02           = "Camada 02",
                                    get_video_nameLayer03           = "Camada 03",
                                    get_video_nameLayer04           = "Camada 04",
                                    get_video_nameLayer05           = "Camada 05",
                                    get_video_nameLayer06           = "Camada 06",

                                    #
                                    #Label Recipe Name
                                    #
                                    labelWeb_RecipeName             = global_variable.labelWeb_RecipeName									
                                    )


    @app.route("/base2", methods=["GET"])
    def base2():
        return render_template("base2.html", 
                               get_video_nameLayer03            = "Camada 03",
                               labelWeb_RecipeName              = global_variable.labelWeb_RecipeName	
                               )


    @app.route("/printPointsCoordinates", methods=["GET", "POST"])
    def console(): 
        return render_template(
            "public/printPointsCoordinates.html",
            varOutputItemCoordinatesVector  = controllers.frames.outputItemCoordinatesVector)