#可以让我们写的mini_web运行在任何的支持wsgi协议的服务器上

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8'),("name","oldyang")])
    return 'python您好!!'

#return 就是返回数据
#start_response 用来返回响应头
#,*args,**kwargs,list () dict  [key value]
# environ 这里请传字典,服务 器传数据给mini_web