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
        msg = bottle.request.forms.get('msg')
        dataEnvio = bottle.request.forms.get('dataEnvio')
        quedas.append(Queda(msg, dataEnvio))
        return msg + " " + dataEnvio
    except:
        bottle.redirect('/queda')
