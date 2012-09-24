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

quedas = []
    
@route('/queda')
def getQueda():
    return bottle.template('visual', quedas=quedas)

@post('/queda', method='POST')
def postQueda():
    msg = request.forms.get('msg')
    dataEnvio = request.forms.get('dataEnvio')
    quedas.append(Queda(msg, dataEnvio))
    bottle.redirect('/queda')

