#返回具体的数据,根据路径
#你给个路径,我给你一个数据
def application(url_path):
    if url_path == "/index.py":
        return "index data is show"
    elif url_path == "/center.py":
        return  "center.py data is show"
    else:
        return "not page is find!"

