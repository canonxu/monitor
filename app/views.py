#!flask/bin/python
#-*-coding:utf-8-*-

from app import app

@app.route('/')
#def main():
#	return 'Welcome!'

@app.route('/index')
def index():
	return '<h1>index</h1>'


