import time

from utils import *


def main():
    print("monitoring positions...")
    counter = 0
    while True:
        # fetch all my positions
        positions = fetch_position(my_positions)
        for position in positions:
            # report every 24 hr
            if counter == 0:
                msg = (
                    "Report ~~~\n"
                    + f'pos: {position["id"]}\n'
                    + f'trading fee: {(position["apy"])}\n'
                    + f'debt: {position["debtRatio"]}'
                )
                send_alert(msg)
            # apy too small ?
            if position["apy"] - HARDCODED_BORROW_APY <= MIN_APY:
                msg = (
                    "APY ALERT!!!\n"
                    + f'pos: {position["id"]}\n'
                    + f'trading fee: {(position["apy"])}'
                )
                send_alert(msg)
            # over debt ?
            if float(position["debtRatio"]) >= ALERT_DEBT_RATIO:
                msg = (
                    "DEBT ALERT!!!\n"
                    + f'pos: {position["id"]}\n'
                    + f'debt: {position["debtRatio"]}'
                )
                send_alert(msg)
        time.sleep(300)
        # update counter for daily report
        counter = (counter + 1) % 288


if __name__ == "__main__":
    main()
