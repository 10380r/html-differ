import datetime
import difflib

def print_diff(today_html, yesterday_html):
    #HTMLファイルの差分の解析
    result = difflib.Differ().compare(today_html, yesterday_html)
    #HTMLファイルの差分のみを出力
    for i in list(result):
        if "+" or "-"in i:
            print(i)

def main():
    #今日の日付を取得
    today = datetime.date.today()
    #昨日の日付を取得
    yesterday = today - datetime.timedelta(days=1)

    #今日のHTMLファイルの読み込み
    today_file = 'src/{}.html'.format(str(today))
    with open(today_file, 'r', encoding='shift-jis') as today_f:
        today_html = today_f.readlines()
    
    #昨日のHTMLファイルの読み込み
    yesterday_file = 'src/{}.html'.format(str(yesterday))
    with open (yesterday_file,'r', encoding='shift-jis') as yesterday_f:
        yesterday_html = yesterday_f.readlines()

    print_diff(today_html, yesterday_html)

if __name__ == '__main__':
    main()
