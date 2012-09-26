# -*- coding: utf-8 -*-
from bottle import route, default_app, TEMPLATE_PATH, template
import os
import bottle
import pymongo
from datetime import datetime

bottle.debug(True)

bottle.TEMPLATE_PATH.append(
  os.path.join(
    os.environ['OPENSHIFT_GEAR_DIR'],'runtime/repo/wsgi/views/'))

mongo_con = pymongo.Connection(
  os.environ['OPENSHIFT_NOSQL_DB_HOST'],
  int(os.environ['OPENSHIFT_NOSQL_DB_PORT']))

mongo_db = mongo_con[os.environ['OPENSHIFT_APP_NAME']]
mongo_db.authenticate(
    os.environ['OPENSHIFT_NOSQL_DB_USERNAME'],
    os.environ['OPENSHIFT_NOSQL_DB_PASSWORD'])

@route('/queda')
def getQueda():
    quedas = list(mongo_db.quedas.find().sort('dataRecebido', pymongo.DESCENDING))
    return bottle.template('visual', quedas=quedas, get_url=application.get_url)

@route('/queda', method='POST')
def postQueda():
    try:                
        dataEnvio = bottle.request.forms.get('dataEnvio')
        pessoa = bottle.request.forms.get('pessoa')
        msg = bottle.request.forms.get('msg')
        local = bottle.request.forms.get('local')
        nova_queda = {'dataEnvio':dataEnvio, 
                                'dataRecebido':datetime.utcnow().strftime("%Y/%m/%d %H:%M"),
                                'pessoa':pessoa, 
                                'msg':msg, 
                                'local':local,}
        mongo_db.quedas.insert(nova_queda)
        return msg + " " + dataEnvio
    except:
        bottle.redirect('/queda')

@route('/static/<filename>', name='static')
def server_static(filename):
    root_dir = os.path.join(os.getcwd(), 'static')
    return static_file(filename, root=root_dir)


application = default_app()
