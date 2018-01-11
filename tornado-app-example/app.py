import os.path
import tornado.ioloop
import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        storm_chasers = ["TIV 1", "TIV 2"]
        self.render("home.html", 
                    storm_chasers=storm_chasers)                   

class CarsHandler(tornado.web.RequestHandler):
    def get(self):
        cars = ["Toyota", "Mazda"]
        self.render("cars.html", 
                    cars=cars)                   


if __name__ == "__main__":
    handlers = [
        (r"/", HomeHandler),
        (r"/cars", CarsHandler),
    ]
    settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
    )               
    application = tornado.web.Application(handlers, **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

