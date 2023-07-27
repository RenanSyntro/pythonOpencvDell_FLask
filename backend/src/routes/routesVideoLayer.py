import controllers.frames.generateFrame

from flask                                              import Response

#
#Video Layer
#
def init_app(app):
    @app.route("/videolayer01")
    def videolayer01():
        return Response(controllers.frames.generateFrame.generate_FrameLayer01("videolayer01"),
            mimetype = "multipart/x-mixed-replace; boundary=videolayer01")

    @app.route("/videolayer02")
    def videolayer02():
        return Response(controllers.frames.generateFrame.generate_FrameLayer02("videolayer02"),
            mimetype = "multipart/x-mixed-replace; boundary=videolayer02")

    @app.route("/videolayer03")
    def videolayer03():
        return Response(controllers.frames.generateFrame.generate_FrameLayer03("videolayer03"),
            mimetype = "multipart/x-mixed-replace; boundary=videolayer03")

    @app.route("/videolayer04")
    def videolayer04():
        return Response(controllers.frames.generateFrame.generate_FrameLayer04("videolayer04"),
            mimetype = "multipart/x-mixed-replace; boundary=videolayer04")

    @app.route("/videolayer05")
    def videolayer05():
        return Response(controllers.frames.generateFrame.generate_FrameLayer05("videolayer05"),
            mimetype = "multipart/x-mixed-replace; boundary=videolayer05")


