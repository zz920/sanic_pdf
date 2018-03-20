import os
from os import path
import multiprocessing


# ROOT FOLDER
BASE_DIR = path.dirname(path.dirname(path.realpath(__file__))) 

# TMP FILE
TMP_FOLDER = path.join(BASE_DIR, "tmp")
os.makedirs(TMP_FOLDER, exist_ok=True)

# SYSTEM PARAMS
CPU_CORE = 10 or multiprocessing.cpu_count()

# PDF SETTINGS
PDF_PAGE_MARGIN = '-T 0 -R 0 -B 0 -L 0'
PDF_OPTION = {
    'default': '',
    'standard': '--no-outline --page-height 297mm --page-width 210mm  ' + PDF_PAGE_MARGIN +
                ' --encoding UTF-8 --page-size A4 --dpi 300 --javascript-delay 0',
    'mini': '--no-outline --page-height 148mm --page-width 210mm  ' + PDF_PAGE_MARGIN +
            ' --encoding UTF-8 --page-size A5 --dpi 300 --javascript-delay 0',
    'label': '--no-outline --page-height 100mm --page-width 100mm  ' + PDF_PAGE_MARGIN +
             ' --encoding UTF-8 --page-size A4 --dpi 300 --javascript-delay 0',
    'label6x4': '--no-outline --page-height 150mm --page-width 100mm  ' + PDF_PAGE_MARGIN +
                ' --encoding UTF-8 --page-size A4 --dpi 300 --javascript-delay 0',
    'label8x4': '--no-outline --page-height 200mm --page-width 100mm  ' + PDF_PAGE_MARGIN +
                ' --encoding UTF-8 --page-size A4 --dpi 320 --javascript-delay 0',
    'manifest': '--no-outline --page-height 297mm --page-width 210mm  ' + PDF_PAGE_MARGIN +
                ' --encoding UTF-8 --page-size A4 --dpi 300 --javascript-delay 0',
    'report': '--no-outline --page-height 420mm --page-width 297mm  ' + PDF_PAGE_MARGIN +
              ' --encoding UTF-8 --page-size A3 --dpi 300 --javascript-delay 0',
    'pod': '--no-outline --page-height 297mm --page-width 210mm  ' + PDF_PAGE_MARGIN +
           ' --encoding UTF-8 --page-size A4 --dpi 300 --javascript-delay 0',
    'invoice': '--no-outline --page-height 297mm --page-width 210mm  ' + PDF_PAGE_MARGIN +
               ' --encoding UTF-8 --page-size A4 --dpi 300 --javascript-delay 0',
    'cod': '--no-outline --page-height 297mm --page-width 210mm  ' + PDF_PAGE_MARGIN +
           ' --encoding UTF-8 --page-size A4 --dpi 300 --javascript-delay 0',
    'commercial': '--no-outline --page-height 297mm --page-width 210mm  ' + PDF_PAGE_MARGIN +
                  ' --encoding UTF-8 --page-size A4 --dpi 300 --javascript-delay 0',
    'reverse_declaration': '--no-outline --page-height 297mm --page-width 210mm  ' + PDF_PAGE_MARGIN +
                           ' --encoding UTF-8 --page-size A4 --dpi 300 --javascript-delay 0',
}
WKHTMLTOPDF_PATH = path.join(BASE_DIR, "/static/wkhtmltopdf")
RETRY_TIME = 3
