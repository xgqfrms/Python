# coding:utf-8
import json
from url.parse import parse_qs
from wsgiref.simple_server import make_server

# 此处定义一个字典
dic_t = {"test1":'Hello', "test2":'Hi'}
# ​dic_t = {
#   "test1":'Hello',
#   "test2":'Hi',
# }

# 用于返回网址中的参数对应值​
def application(environ, start_response):
  start_response('200 OK', [('Content-Type','text/html')])
  params = parse_qs(environ['QUERY_STRING'])
  # 得到网址中的参数
  name = params['name'][0]
  try:
    # 字典查值并返回为字典
    dic = {name: dic_t[name]}
  except:
    # 如果字典中没有，则返回‘KeyError’
    KeyError:dic = {name:"KeyError"}
  # 网页返回值​
  return[json.dumps(dic)]
# main
if __name__ == "__main__":
  # 自定义开启的端口
  port = 5088
  httpd = make_server("0.0.0.0", port, application)
  print("serving http on port {0}...").format(str(port))
  httpd.serve_forever()
