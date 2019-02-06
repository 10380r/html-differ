import urllib.request
from bs4 import BeautifulSoup
import datetime
import codecs

#指定するURL
url = "https://www.cinemanavi.com/ranking_list/type/favorite/%E6%98%A0%E7%94%BB%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0.html"

#今日の日付の取得
today = datetime.date.today()

# URLからHTTPレスポンスを取得

html= BeautifulSoup(urllib.request.urlopen(url), "html.parser")

#ファイル名の指定
file_name = 'src/{}.html'.format(str(today))

#ファイルをつくる
file = codecs.open(file_name,"ab",'cp932', 'ignore')
file.write(html)
file.close()
