import tornado.ioloop
import tornado.web
import redis
import json
import time

class AuthHandler(tornado.web.RequestHandler):
    def initialize(self, roDB, rwDB):
        self.roConn = redis.StrictRedis(host=roDB, port=6379, db=0)
        self.rwConn = redis.StrictRedis(host=rwDB, port=6379, db=0)
    def delete(self, tokenID):
        self.rwConn.delete(tokenID)
        self.write({'status':True})
    def get(self, tokenID):
        res = self.roConn.get(tokenID)
        if (res == None):
            self.set_status(404)
            self.write({'status': False})
        else:
            try:
                t = json.loads(res)
                if (t['expire_time'] < int(time.time())):
                    self.rwConn.delete(tokenID)
                    self.set_status(404)
                    self.write({'status':False})
                else:
                    self.write({'status':True, 'user_data': t})
            except Exception, e:
                self.rwConn.delete(tokenID)
                self.set_status(500)
                self.write({'status':False})
            
    def post(self, tokenID):
        try:
            requestObj = {k:self.get_argument(k) for k in self.request.arguments}
            requestObj['expire_time'] = int(requestObj['expire_time'])
            requestJSON = json.dumps(requestObj)
            self.rwConn.set(tokenID, requestJSON)
            self.write({"status": True})
        except Exception, e:
            self.set_status(500)
            self.write({'status': False})

import os
ro_redis = os.getenv('REIDS_RO', 'redis')
rw_redis = os.getenv('REDIS_RW', 'redis')

application = tornado.web.Application([
    (r"/token/([0-9a-fA-F]{32})", AuthHandler, dict(roDB=ro_redis, rwDB=rw_redis)),
])

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
