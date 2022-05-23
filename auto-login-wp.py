import mechanicalsoup
import time
import logging

def main():
    ##########
    #mainの処理
    ##########
    browser = mechanicalsoup.StatefulBrowser()
    logging.info("Let's Go...")

    username = "hogehoge" #あなたのユーザー名を入れてください
    password = "passpass" #あなたのパスワードを入れてください

    #ログインページを開く
    browser.open("https://c-sushiringblog.com/wp-admin/")
    time.sleep(1)

    browser.select_form()

    browser["log"] = username
    browser["pwd"] = password

    logging.info("Signing in...")
    browser.submit_selected()
    time.sleep(1)

    top = browser.get_current_page().select('h1')
    print(top) #[ダッシュボード, リンクの挿入/編集]
    #print(top.text)はエラーになります。
    for wp in browser.get_current_page().select('.welcome-panel-content h2'):
        print(wp.text)

    #################
    #mainの処理おわり
    #################

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  main()