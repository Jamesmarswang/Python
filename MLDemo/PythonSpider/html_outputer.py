# coding = utf-8
# __author__ = 'wang wei'


class HtmlOutputer:
    def __init__(self):
        self.data_s = []

    def collect_data(self, data):
        if data is None:
            return
        self.data_s.append(data)

    def output_html(self):
        file_out = open('output.html', 'w')
        file_out.write("<html>")
        file_out.write("<body>")
        file_out.write("<table>")

        for data in self.data_s:
            file_out.write("<tr>")
            file_out.write("<td>%s</td>" % data['url'])
            file_out.write("<td>%s</td>" % data['title'].encode('utf-8'))
            file_out.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            file_out.write("</tr>")
            file_out.write("</table>")
        file_out.write("</body>")
        file_out.write("</html>")
        file_out.close()
