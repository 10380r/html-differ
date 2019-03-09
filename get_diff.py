import urllib.request
from bs4 import BeautifulSoup
import datetime
import codecs
import difflib


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
    with codecs.open(file_name,"wb",'cp932', 'ignore') as f:
        f.write(str(html))

def print_diff(yesterday_html, today_html):
    #HTMLファイルの差分の解析
    result = difflib.ndiff(yesterday_html, today_html)
    #HTMLファイルの差分のみを出力
    for i in list(result):
        if ' ' == i[0]:
            continue
        elif "+" or "-" == i[0]:
            print(i)

def main():
    #今日の日付を取得
    today = datetime.date.today()
    #昨日の日付を取得
    yesterday = today - datetime.timedelta(days=1)

    url = 'https://docs.python.jp/3/library/difflib.html'
    save_as_file(get_html(url))

    #今日のHTMLファイルの読み込み
    today_file = 'src/{}.html'.format(str(today))
    with open(today_file, 'r', encoding='cp932') as today_f:
        today_html = today_f.readlines()
    
    #昨日のHTMLファイルの読み込み
    yesterday_file = 'src/{}.html'.format(str(yesterday))
    with open (yesterday_file,'r', encoding='utf-8') as yesterday_f:
        yesterday_html = yesterday_f.readlines()

    print_diff(yesterday_html, today_html)


if __name__ == '__main__':
    main()
