# -*- coding: utf-8 -*-
from bottle import route, default_app, TEMPLATE_PATH, template
import os
import bottle
from datetime import datetime

bottle.debug(True)

bottle.TEMPLATE_PATH.append(
  os.path.join(
    os.environ['OPENSHIFT_GEAR_DIR'],'runtime/repo/wsgi/views/'))

application = default_app()

class Queda:
    def __init__(self, msg, dataEnvio):
        self.msg= msg
        self.dataEnvio = dataEnvio
        self.dataRecebido = str(datetime.now())

quedas = [Queda("Teste", "24/09/2012 09:10")]
    
@route('/queda')
def getQueda():
    return bottle.template('visual', quedas=quedas)

@route('/queda', method='POST')
def postQueda():
    try:        
        msg = request.forms.get('msg')
        dataEnvio = request.forms.get('dataEnvio')
        quedas.append(Queda(msg, dataEnvio))
        return msg + " " + dataEnvio
    except:
        pass
    bottle.redirect('/queda')

@route('/login')
def login_form():
    return '''<form method="POST" action="/login">
                <input name="name"     type="text" />
                <input name="password" type="password" />
                <input type="submit" />
              </form>'''

@route('/login', method='POST')
def login_submit():
    name     = request.forms.get('name')
    password = request.forms.get('password')
    return "<p>Your login was correct</p>"
