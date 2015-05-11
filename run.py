#!flask/bin/python
#-*-coding:utf-8-*-

from app import app

app.debug = True
#app.run(host='0.0.0.0', port=227)
app.run()
