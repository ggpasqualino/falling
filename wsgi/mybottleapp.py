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
        self.dataRecebido = datetime.utcnow().strftime("%Y/%m/%d %H:%M")

quedas = []
    
@route('/queda')
def getQueda():
    return bottle.template('visual', quedas=quedas, get_url=application.get_url)

@route('/queda', method='POST')
def postQueda():
    try:        
        msg = bottle.request.forms.get('msg')
        dataEnvio = bottle.request.forms.get('dataEnvio')
        quedas.append(Queda(msg, dataEnvio))
        return msg + " " + dataEnvio
    except:
        bottle.redirect('/queda')

@route('/static/<filename>', name='static')
def server_static(filename):
    root_dir = os.path.join(os.getcwd(), 'static')
    return static_file(filename, root=root_dir)
