import time
import schedule
from web_check import console_checker


def timer(arg):
    playstation_content = ["Playstation", "playstation-5", "contentPanels3", "Playstation 5", "Playstation 5 DE"]
    xbox_content = ["Xbox", "xbox-series-x", "contentPanelsConsoles", "Series X", "Series S"]

    if arg == "ps":
        schedule.every(60).seconds.do(console_checker, playstation_content)
        while True:
            schedule.run_pending()
            time.sleep(1)

    elif arg == "xbox":
        schedule.every(60).seconds.do(console_checker, xbox_content)
        while True:
            schedule.run_pending()
            time.sleep(1)

    elif arg == "both":
        schedule.every(60).seconds.do(console_checker, playstation_content)
        schedule.every(60).seconds.do(console_checker, xbox_content)
        while True:
            schedule.run_pending()
            time.sleep(1)
