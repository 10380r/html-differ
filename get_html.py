import urllib.request
from bs4 import BeautifulSoup
import datetime
import codecs

def get_html(url):
    # URLからHTTPレスポンスを取得
    html = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
    return html

def save_as_file(html):
    #今日の日付の取得
    today = datetime.date.today()
    #ファイル名の指定
    file_name = 'src/{}.html'.format(str(today))
    #ファイルをつくる
    file = codecs.open(file_name,"ab",'cp932', 'ignore')
    file.write(html)
    file.close()

def main():
    #指定するURL
   # url = "https://www.cinemanavi.com/ranking_list/type/favorite/%E6%98%A0%E7%94%BB%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0.html"
    url = 'https://docs.python.jp/3/library/difflib.html'
    save_as_file(get_html(url))

if __name__ == '__main__':
    main()
