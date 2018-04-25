import random
import asyncio
from asyncio import create_subprocess_exec, subprocess, Lock

from common.constant import CPU_CORE, WKHTMLTOPDF_PATH


lock = Lock()


class WKHtmlToPdf(object):
   
    def __init__(self):
        self.process = None
        self.working = False

    async def create_subprocess(self):
        await lock.acquire()
        self.process = await create_subprocess_exec(
            WKHTMLTOPDF_PATH,
            '--read-args-from-stdin', 
            stdin=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        lock.release()
   
    @property
    def isvalid(self):
        return self.process and not self.process.returncode 
    
    @property
    def isbusy(self):
        return self.working

    async def render(self, url, output_file, options_str=''):
        self.working = True
        if not self.isvalid:
            await self.create_subprocess()
        to_bytes = "{} {} {}\n".format(options_str, url, output_file).encode()
        try:
            self.process.stdin.write(to_bytes)
            await self.process.stdin.drain()
            while True:
                data = await self.process.stderr.readline()
                if "Done" in data.decode("utf-8"):
                    self.working = False
                    return True
        except Exception as e:
            if not self.isvalid:
                self.close()
                self.working = False
                raise RuntimeError("WKHtmlToPdf Crashed.")
        self.working = False
        return False

    def close(self):
        self.process.stdin.close()
        self.process.terminate()
        self.process = None


class WKHtmlToPdfManager(object):

    def __init__(self, max_process=6):
        self.worker_list = [WKHtmlToPdf() for _ in range(max_process)]

    async def assign(self):
        while True:
            for worker in self.worker_list:
                if not worker.isbusy:
                    return worker
            await asyncio.sleep(0)


WKManager = WKHtmlToPdfManager(CPU_CORE)
