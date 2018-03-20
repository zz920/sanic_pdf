import builtins
from sanic import Sanic

from application.view.taskview import TaskView
from common.configure import Default_Config 


def append_url(app):
    app.add_route(TaskView.as_view(), '/') 
   

def registry(app):
    builtins._app = app


def create_app(app_name="pdf_generation"):
    app = Sanic(app_name, load_env=False, log_config=Default_Config.LOG_SETTING)
    app.config.from_object(Default_Config)
    append_url(app) 
    registry(app)
    return app
