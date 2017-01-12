# coding = utf-8
# __author__ = 'wang wei'

import urllib.request


class HtmlDownloader:
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
