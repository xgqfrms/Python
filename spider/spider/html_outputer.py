# coding:utf-8

class HtmlOutputer(object):
  # HTML 输出器
  def __init__(self):
    self.datas = []
  #
  def collect_data(self,data):
    if data is None:
      return
    self.datas.append(data)
  #
  def output_html(self):
    # w, 开启写
    fout = open('output.html', 'w')
    # 输出 HTML 表格
    fout.write("<html><body><table>")
    # fout.write("<html>")
    # fout.write("<body>")
    # fout.write("<table>")

    # UTF-8, python2 default encoding ascii
    for data in self.datas:
      fout.write("<tr>")
      fout.write("<td>%s</td>"%data['url'])
      fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
      fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
      fout.write("</tr>")

    # fout.write("</table>")
    # fout.write("</body>")
    # fout.write("</html>")
    fout.write("</table></body></html>")
    # 关闭写
    fout.close()
