'''
爬取电影天堂
'''
import re
import requests
import time


class Spider_video():
    print('需要爬取哪一页的资源？')
    print('page = ', end='')
    page = input()
    http = 'http://www.dytt8.net/html/gndy/dyzz/list_23_' + page + '.html'
    screen_one = r'<a href="([\s\S]*?)" class="ulink">'
    screen_two = r'bgcolor="#fdfddf"><a href="([\s\S]*?)">'
    screen_add = r'(/html/gndy/dyzz/[\S\s]*?.html)'
    http_add = r'http://www.dytt8.net'

    def __get_html(self):
        html = requests.get(Spider_video.http)
        html.encoding = 'gb2312'
        return html.text

    def __screen(self, html_str):
        result1 = re.findall(Spider_video.screen_one, html_str)
        result1[0] = re.findall(Spider_video.screen_add, result1[0])
        result1[0] = (result1[0][-1])
        return result1

    def __http_add(self, http_list):
        http = []
        for http_str in http_list:
            http_str = Spider_video.http_add + http_str
            http.append(http_str)
        return http

    def __download(self, http):
        for http in http:
            Spider_video.http = http
            html = self.__get_html()
            self.__screen_one(html)
        # print(html)

    def __screen_one(self, html):
        download = re.findall(Spider_video.screen_two, html)
        download = download[0]
        if '阳光电影' in download:
            self.__write(download)

    def __write(self, download_http):
        print('成功获取资源：'+download_http)
        txt = open(r'C:\Users\Administrator\Desktop\spider_电影天堂.txt', 'a+')
        txt.write('\n'+download_http+'\n')
        txt.close()

    def go(self):
        print('爬取资源中，请稍等……')
        html_str = self.__get_html()
        http_list = self.__screen(html_str)
        http_add = self.__http_add(http_list)
        self.__download(http_add)


result = Spider_video()
result.go()
print('恭喜你！资源已爬取完成！')
time.sleep(5)
