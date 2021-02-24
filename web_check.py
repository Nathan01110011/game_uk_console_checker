import datetime
from bs4 import BeautifulSoup
from playsound import playsound
from requests_html import HTMLSession


def console_checker(args):
    print(args[0] + " check started at " + datetime.datetime.now())
    session = HTMLSession()
    resp = session.get('http://www.game.co.uk/' + args[0])
    resp.html.render()
    soup = BeautifulSoup(resp.html.html, "lxml")

    console_section = soup.find_all("section", {"id": args[1]})
    purchase_buttons = []

    for ul in console_section:
        purchase_buttons.extend(ul.findAll('a'))

    try:
        if purchase_buttons[0].text != "Out of stock":
            print(args[2] + " in stock")
            playsound("ring.mp3")
        else:
            print(args[2] + " OOS")

        if purchase_buttons[1].text != "Out of stock":
            print(args[3] + " in stock")
            playsound("ring.mp3")
        else:
            print(args[3] + " OOS")
    except:
        print("Something is broken :(")
        raise
