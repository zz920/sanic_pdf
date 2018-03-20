# Sanic-pdf-server


This is a pdf generation server based on Sanic framework. The pdf generation lib is wkhtmltopdf.

  - Async to make things fast.
  - Accept html file to generate pdf
  - Auto upload to your S3 and return link
  - Make full use of your server

# Install
  - ``git clone https://github.com/zz920/sanic_pdf.git``
  - ``virtualenv --python=python3.6 env``
  - ``source env/bin/active``
  - ``pip install -r requirement.txt``
  - Set your S3 key in the configure file ``common/configure/default.py``.
  - ``python wsgi.py``
  - Send a html file to ``127.0.0.1:5000`` with post method, and check your pdf file from return pdf link.
  - Check the ``test/sample.py`` for detail usage.

You can also:
  - Use the wkhtmltopdfwrapper to get yourself a different pdf generator. 
  - Rewrite the application to get a better one.

This sever is a very simple html-to-pdf application based on wkhtmltopdf and sanic. The reason for establishing this async server is "FAST". I mean, it's not that fast, but it's fast enough to generate 100 pdf files within 5 seconds (one page html, 2 core cpu, local test). Meanwhile it's asynchronous, so it could handle a lot of requests with only one process.  

This project is an experiment more than a production. So take care, before you decide to use it.
