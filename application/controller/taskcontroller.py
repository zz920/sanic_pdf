import os
import time
import random
import asyncio
import hashlib

from uuid import uuid4 

from application.wrapper.wkhtmlpdfwrapper import WKManager 
from application.wrapper.botowrapper import BotoS3Client 
from application.wrapper.logwrapper import InfoLog, ErrorLog
from common.constant import TMP_FOLDER, PDF_OPTION, RETRY_TIME 


class TaskController():
    """
    Task controller
    """

    def __init__(self, request_obj):
        self._json = request_obj.json
        self._html = self._json.get("html_page", "")
        self._md5 = self._json.get("md5", "")
        self._type = self._json.get("type", "standard")

    def is_valid(self):
        return True
        return hashlib.md5(self._html.encode("utf-8")).hexdigest() == self._md5
    
    def file_prefix(self, tid):
        return os.path.join(TMP_FOLDER, tid)

    def remove_tmp_file(self, tid):
        prefix = self.file_prefix(tid)
        try:
            os.remove(prefix + ".html")
            os.remove(prefix + ".pdf")
        except:
            pass
    
    def generate_file_path(self, tid):
        prefix = self.file_prefix(tid)
        html_file = prefix + ".html"
        pdf_file = prefix + ".pdf"
        
        with open(html_file, "w") as html:
            html.write(self._html)
        return html_file, pdf_file

    def get_option(self):
        return PDF_OPTION.get(self._type)
    
    async def execute_task(self):
        tid = uuid4().hex[:10]
        start_time = time.time()
        InfoLog.dump("Received a valid task, tid is {}.".format(tid))
        html_file, pdf_file = self.generate_file_path(tid) 
        options_str = self.get_option()
        
        for _ in range(RETRY_TIME):
            worker = await WKManager.assign()
            result = await worker.render(html_file, pdf_file, options_str)
            if result:
                break
            # too much job coming
            InfoLog.dump("Too busy for wk lib, why not buy a more powerful server?")
            await asyncio.sleep(random.random())
        else:
            self.remove_tmp_file(tid)
            ErrorLog.dump("Failed with task, tid is {}.".format(tid))
            return None 
        
        try:
            url = BotoS3Client(_app.config.AWS_CONFIG).upload_to_s3(pdf_file)
        except Exception as e:
            ErrorLog.dump("Failed when uploading the file, tid is {}".format(tid)) 

        self.remove_tmp_file(tid)
        end_time = time.time() - start_time
        InfoLog.dump("Finished task in {0:.0f}ms, tid is {}".format(end_time * 100, tid))
        return url


