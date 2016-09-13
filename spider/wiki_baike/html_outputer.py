__author__ = 'xray'
# coding: utf8


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file_out = open('output.html', 'w')  # 'w' write pattern
        file_out.write('<html>')
        file_out.write('<body>')
        file_out.write('<table>')
        for data in self.datas:
            file_out.write('<tr>')
            # assic
            file_out.write('<td>%</td>' % data['url'].encode('utf-8'))
            file_out.write('<td>%</td>' % data['title'].encode('utf-8'))
            file_out.write('<td>%</td>' % data['summary'].encode('utf-8'))
            file_out.write('</tr>')
        file_out.write('</table>')
        file_out.write('</body>')
        file_out.write('</html>')

        file_out.close()