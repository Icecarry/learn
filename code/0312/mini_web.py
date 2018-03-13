
import re


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    # 显示具体数据
    url_path = environ["url_path"]

    if url_path == "/index.py":
        with open("./代码/sh_python_07_mini02/templates/index.html") as f:
            content = f.read()

        row_str = """
         <tr>
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
        </tr>
        """

        show_table = ''
        for i in range(10):
            show_table += row_str

        content =re.sub(r"\{%content%\}", show_table, content)
        return content

    # return 'Hello World!'