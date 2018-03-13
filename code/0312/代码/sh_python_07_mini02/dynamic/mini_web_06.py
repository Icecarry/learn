#可以让我们写的mini_web运行在任何的支持wsgi协议的服务器上
import re


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8'),("name","oldyang")])

    #显示具体的数据,
    url_path = environ["url_path"]

    if url_path == "/index.py":
        with open("./templates/index.html") as f:
            content = f.read()



        row_str = """ <tr>
        <td>1</td>
        <td>000007</td>
        <td>全新好</td>
        <td>10.01%</td>
        <td>4.40%</td>
        <td>16.05</td>
        <td>14.60</td>
        <td>2017-07-18</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
        </tr>  """

        table_show = ""
        #通过循环去添加数据
        for i in range(100):
            table_show += row_str

        #替换
        content = re.sub(r"\{%content%\}",table_show,content)

        return content
    elif url_path == "/center.py":
        return "centery.py"
    else:
        return "not page is find!"

#return 就是返回数据
#start_response 用来返回响应头
#,*args,**kwargs,list () dict  [key value]
# environ 这里请传字典,服务 器传数据给mini_web