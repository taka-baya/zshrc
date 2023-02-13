import requests
import urllib.request
from bs4 import BeautifulSoup

def getw(): #今日の天気スクレイピング
    #対象のサイトURL
    url = "https://tenki.jp/forecast/3/16/4410/13112/"
    #インスタンス作成
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    #対象の要素
    location = soup.find_all("h3", class_="bottom-style date-set")
    weather = soup.find_all("p", class_="weather-telop")
    temp = soup.find_all("dd", class_="high-temp temp")
    low_temp = soup.find_all("dd", class_="low-temp temp")
    tds = soup.select("tr.rain-probability td")
    hini = soup.find_all("h3", class_="left-style")

    tenki = "\n" + hini[0].getText()
    location = "の" + location[0].getText().replace("10日間","") + "は「"
    weather = weather[0].getText() + "」。\n\n"
    kion = "最高気温は" + temp[0].getText() + "\n"
    low_kion = "最低気温は" + low_temp[0].getText()
    rain1 = "\n\n時間ごとの降水確率は\n00-06時  " + tds[0].getText()
    rain2 = "\n06-12時  " + tds[1].getText()
    rain3 = "\n12-18時  " + tds[2].getText()
    rain4 = "\n18-24時  " + tds[3].getText() + "\nです。"

    return_text = tenki + location + weather + kion + low_kion + rain1 + rain2 + rain3 + rain4
    return return_text

def alert_message():
    line_notify_token = 'pr3GHec1zhbDdny8tcN6mA8B1njHAVxD6nq4DYaYWDD'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = getw()

    text1 = "\n\n本日の曜日・天気・イベントから予測される売上金は\n ¥143,231 \nです。\n\n各パンの本日の販売予測個数は以下の通りになります。\nバケット : 23個\nカスクルート : 12個\nレトロバケット : 17個\nクロワッサン : 18個\nブリオッシュ : 7個\nクリームパン : 8個\nバターロール : 15個"

    message = message + text1

    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)


alert_message()