# coding = utf-8
# __author__ = 'wang wei'

from MLDemo.PythonSpider import url_manager
from MLDemo.PythonSpider import html_downloader
from MLDemo.PythonSpider import html_parser
from MLDemo.PythonSpider import html_outputer


class SpiderMain:
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.download = html_downloader.HtmlDownloader()
        self.parse = html_parser.HtmlParser()
        self.output = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():

            new_url = self.urls.get_new_url()
            print(count, new_url)
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.coolect_data(new_data)

            if count == 1000:
                break

            count += 1

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
