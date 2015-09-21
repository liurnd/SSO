import tornado.ioloop
import tornado.web
import redis

class AuthHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,world")

application = tornado.web.Application([
    (r"/", AuthHandler),
])

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
