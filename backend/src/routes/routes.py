import controllers.varGlobal.adjustmentPanel


from flask                                              import render_template, request
from database.db_SelectRow_nameParameters               import SelectRow_NameParametersAdjustFilterImg
from database.db_SelectRow_SeachForID                   import selectRow_SearchForID
import controllers.frames.generateFrame
import controllers.frames.frames
from flask_cors                                         import CORS

def init_app(app):
    CORS(app, resources={"*": {"origins": "*"}})

    @app.route("/", methods=["GET", "POST"])
    
    def index():
        nameParameters = SelectRow_NameParametersAdjustFilterImg.Select()

        if request.method == "POST":

            if  (request.form.get("parametrosSelect") != None):
                print("chamada de parametrosSelect")
                print(request.form.get("parametrosSelect"))
                selectRow_SearchForID.Select(int(request.form.get("parametrosSelect")))

            #
            #Color
            #
            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Red_Min") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min                      !=  int(request.form.get("trackbar_parametersFilter_selectFilterColor_Red_Min"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min                      =	int(request.form.get("trackbar1"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min                    !=  int(request.form.get("number1"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min                      =	int(request.form.get("number1"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Red_Max") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max                      !=	int(request.form.get("trackbar2"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max                      =	int(request.form.get("trackbar2"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max                    !=  int(request.form.get("number2"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max                      =	int(request.form.get("number2"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Green_Min") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min                    !=	int(request.form.get("trackbar3"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min                    =	int(request.form.get("trackbar3"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min                  !=  int(request.form.get("number3"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min                    =	int(request.form.get("number3"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Green_Max") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max                    !=	int(request.form.get("trackbar4"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max                    =	int(request.form.get("trackbar4"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max                  !=  int(request.form.get("number4"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max                    =	int(request.form.get("number4"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Blue_Min") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min                    !=	int(request.form.get("trackbar5"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min                    =	int(request.form.get("trackbar5"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min                  !=   int(request.form.get("number5"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min                    =	int(request.form.get("number5"))

            if (request.form.get("trackbar_parametersFilter_selectFilterColor_Blue_Max") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max                    !=	int(request.form.get("trackbar6"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max                    =	int(request.form.get("trackbar6"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max                  !=   int(request.form.get("number6"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max                    =	int(request.form.get("number6"))

            #
            #Iterations
            #
            if (request.form.get("trackbar_parametersFilter_selectFilterColor_iterations_erode") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_erode                   !=	int(request.form.get("trackbar_iterations_erode"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_erode 	                =	int(request.form.get("trackbar_iterations_erode"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_erode                 !=  int(request.form.get("number_iterations_erode"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_erode 	                =	int(request.form.get("number_iterations_erode"))

            if (request.form.get("trackbar_parametersFilter_varTrackbar_iterations_dilate") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_dilate                  !=	int(request.form.get("trackbar_iterations_dilate"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_dilate 	                =	int(request.form.get("trackbar_iterations_dilate"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_dilate                !=  int(request.form.get("number_iterations_dilate"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_dilate 	                =	int(request.form.get("number_iterations_dilate"))

            #
            #Seam according to color
            #
            if (request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min            !=	int(request.form.get("trackbar_TamMinLh"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min            =	int(request.form.get("trackbar_TamMinLh"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min          != int(request.form.get("number_TamMinLh"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min            =	int(request.form.get("number_TamMinLh"))

            if (request.form.get("trackbar_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max            !=	int(request.form.get("trackbar_TamMaxLh"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max            = 	int(request.form.get("trackbar_TamMaxLh"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max          != int(request.form.get("number_TamMaxLh"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max            =	int(request.form.get("number_TamMaxLh"))

            if (request.form.get("trackbar_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min            !=	int(request.form.get("trackbar_TamMinLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min            =	int(request.form.get("trackbar_TamMinLv"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min          != int(request.form.get("number_TamMinLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min            =	int(request.form.get("number_TamMinLv"))

            if (request.form.get("trackbar_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max            !=	int(request.form.get("trackbar_TamMaxLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max            =	int(request.form.get("trackbar_TamMaxLv"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max          != int(request.form.get("number_TamMaxLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max            =	int(request.form.get("number_TamMaxLv"))

            #
            #Filter Object Size 
            #
            if (request.form.get("trackbar_parametersFilter_FoundObjectSizeFilter_Min") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min                           !=  int(request.form.get("trackbar_TamMinLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min                           =   int(request.form.get("trackbar_TamMinLv"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min                         !=  int(request.form.get("number_TamMinLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Min                           =   int(request.form.get("number_TamMinLv"))

            if (request.form.get("trackbar_parametersFilter_FoundObjectSizeFilter_Max") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max                           !=   int(request.form.get("trackbar_TamMaxLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max                           =    int(request.form.get("trackbar_TamMaxLv"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max                         !=   int(request.form.get("number_TamMaxLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_FoundObjectSizeFilter_Max                           =	int(request.form.get("trackbar_TamMaxLv"))

            if (request.form.get("trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min             !=   int(request.form.get("trackbar_TamMaxLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min             =	int(request.form.get("trackbar_TamMaxLv"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min           !=   int(request.form.get("number_TamMaxLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min             =	int(request.form.get("trackbar_TamMaxLv"))

            if (request.form.get("trackbar_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max             !=   int(request.form.get("trackbar_TamMinLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max             =    int(request.form.get("trackbar_TamMinLv"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max           !=   int(request.form.get("number_TamMinLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max             =    int(request.form.get("number_TamMinLv"))

            if (request.form.get("trackbar_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min            !=  int(request.form.get("trackbar_TamMaxLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min            =	int(request.form.get("trackbar_TamMaxLv"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min          !=  int(request.form.get("number_TamMaxLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min            =	int(request.form.get("number_TamMinLv"))

            if (request.form.get("trackbar_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max") != None):
                if (controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max             !=  int(request.form.get("trackbar_TamMinLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max             =   int(request.form.get("trackbar_TamMinLv"))
                elif (controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max           !=  int(request.form.get("number_TamMinLv"))):
                    controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max             =   int(request.form.get("number_TamMinLv"))

            if (request.form.get("trackbar_ResolutionPixMm_X") != None):
                if (controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X                                      !=	float(request.form.get("trackbar_ResolutionPixMm_X"))):
                    controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X 	                                    =	float(request.form.get("trackbar_ResolutionPixMm_X"))
                elif (controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X                                    !=   float(request.form.get("number_ResolutionPixMm_X"))):
                    controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X 	                                    =	float(request.form.get("number_ResolutionPixMm_X"))

            if (request.form.get("trackbar_ResolutionPixMm_Y") != None):
                if (controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y                                      !=	float(request.form.get("trackbar_ResolutionPixMm_Y"))):
                    controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y 	                                    =	float(request.form.get("trackbar_ResolutionPixMm_Y"))
                elif (controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y                                    !=   float(request.form.get("number_ResolutionPixMm_Y"))):
                    controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y 	                                    =	float(request.form.get("number_ResolutionPixMm_Y"))

            if (request.form.get("parameters_name") != None):
                controllers.varGlobal.adjustmentPanel.var_name = request.form.get("parameters_name")
                print(controllers.varGlobal.adjustmentPanel.var_name)

        return render_template("base.html", 
                                    #
                                    #Name
                                    #
                                    nameParameters                                          = nameParameters,
                                    varhtml_name                                            = controllers.varGlobal.adjustmentPanel.var_name,
                                    
                                    #
                                    #Color
                                    #
                                    varhtml_parametersFilter_selectFilterColor_Red_Min	    = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Min, 
                                    varhtml_parametersFilter_selectFilterColor_Red_Max	    = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Red_Max,
                                    
                                    varhtml_parametersFilter_selectFilterColor_Green_Min	= controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Min,
                                    varhtml_parametersFilter_selectFilterColor_Green_Max	= controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Green_Max,
                                    
                                    varhtml_parametersFilter_selectFilterColor_Blue_Min	    = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Min,
                                    varhtml_parametersFilter_selectFilterColor_Blue_Max	    = controllers.varGlobal.adjustmentPanel.var_parametersFilter_selectFilterColor_Blue_Max,

                                    #
                                    #Iterations
                                    #
                                    varhtml_parametersFilter_varTrackbar_iterations_erode	= controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_erode,
                                    varhtml_parametersFilter_varTrackbar_iterations_dilate	= controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_dilate,

                                    #
                                    #Seam according to color
                                    #
                                    #Vertically     - White
                                    varhtml_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Min,
                                    varhtml_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorVertically_JumpSize_Max,
                                    #Horizontally   - White
                                    varhtml_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Min,
                                    varhtml_parametersFilter_SpliceLineJumpingWhiteolorHorizontally_JumpSize_Max    = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingWhiteColorHorizontally_JumpSize_Max,
                                    #Vertically     - Black
                                    varhtml_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Min     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Min,
                                    varhtml_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Max     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorVertically_JumpSize_Max,
                                    #Horizontally   - Black
                                    varhtml_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min   = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Min,
                                    varhtml_parametersFilter_SpliceLineJumpingBlackolorHorizontally_JumpSize_Max    = controllers.varGlobal.adjustmentPanel.var_parametersFilter_SpliceLineJumpingBlackColorHorizontally_JumpSize_Max,

                                    #
                                    #Filter Object Size 
                                    #
                                    var_parametersFilter_varTrackbar_iterations_erode 	               = controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_erode,
                                    var_parametersFilter_varTrackbar_iterations_dilate 	               = controllers.varGlobal.adjustmentPanel.var_parametersFilter_varTrackbar_iterations_dilate,

                                    var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min       = controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Min,
                                    var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max       = controllers.varGlobal.adjustmentPanel.var_parametersFilter_VerticalLineSizeFilterOfFoundObject_Max,

                                    var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Min,
                                    var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max     = controllers.varGlobal.adjustmentPanel.var_parametersFilter_HorizontalLineSizeFilterOfFoundObject_Max,

                                    varTrackbar_ConstResolutionPixelMm_X                               = controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X,
                                    varTrackbar_ConstResolutionPixelMm_Y                               = controllers.varGlobal.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y,
                                    
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
                                    labelWeb_RecipeName             = controllers.varGlobal.adjustmentPanel.labelWeb_RecipeName									
                                    )

    @app.route("/base2", methods=["GET"])
    def base2():
        return render_template("base2.html", 
                               get_video_nameLayer03            = "Camada 03",
                               labelWeb_RecipeName              = controllers.varGlobal.adjustmentPanel.labelWeb_RecipeName	
                               )

    @app.route("/printPointsCoordinates", methods=["GET", "POST"])
    def console(): 
        return render_template("public/printPointsCoordinates.html", 
                                    varOutputItemCoordinatesVector  = controllers.frames.outputItemCoordinatesVector
                                    )