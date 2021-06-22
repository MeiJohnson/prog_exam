import tornado.ioloop
import tornado.web
import asyncio
import tornado.websocket
import json

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class MessageBuffer():
    def __init__(self, messages):
        self.__messages = []
        for m in messages:
            self.__messages.append(m)

    def add_message(self, message):
        self.__messages.append(message)
    def get_messages(self):
        return self.__messages

test_messages = [{"message":"Hello, world"}, {"message":"This is me!"}]
globalmessagebuffer = MessageBuffer(test_messages)
print(globalmessagebuffer.get_messages())


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class IndexHandler(tornado.web.RequestHandler):
    # отображать индекс страницу
    def get(self):
        self.render("index.html", messages = globalmessagebuffer.get_messages())

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    messages = {}

    def open(self):
        print('websocket is open')
    
    def on_message(self, message):
        #import time
        #key = time.strftime("%Y%m%d%H%M%S")
        
        data = json.loads(message)
        new_message = {'message':f"{data['nickname']}: {data['textmsg']}"}
        print(new_message)
        globalmessagebuffer.add_message(new_message)
        self.write_message(f"{new_message['message']}\n")
        print(globalmessagebuffer.get_messages())
    
    def on_close(self):
        print('websocket was close')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/index", IndexHandler),
        (r"/websocket", EchoWebSocket)  
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()