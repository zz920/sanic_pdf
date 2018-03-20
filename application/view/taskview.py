from sanic.views import HTTPMethodView
from sanic.response import json, text
from application.controller.taskcontroller import TaskController


class TaskView(HTTPMethodView):
    """
    Task view class
    """

    def get(self, request):
        return text('Pdf generation server.')

    async def post(self, request):
        task = TaskController(request)
        if not task.is_valid():
            return json({"status": "fail"})
        pdf_link = await task.execute_task()
        if pdf_link is None:
            return json({"status": "fail"})
        return json({"status": "sucess", "pdf_link": pdf_link})
