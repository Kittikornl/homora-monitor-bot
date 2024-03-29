import time

from utils import *


def main():
    print("monitoring positions...")
    counter = 0
    while True:
        # fetch all my positions
        positions = fetch_position(my_positions)
        reports = ["Report ~~~\n"]
        for position in positions:
            # create reports every 24 hr
            if counter == 0:
                msg = (
                    f'pos: {position["id"]}\n'
                    + f'trading fee: {(position["apy"])}\n'
                    + f'debt: {position["debtRatio"]}\n'
                    + "x" * 30
                    + "\n"
                )
                reports.append(msg)
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
        # send reports
        if counter == 0:
            send_alert("".join(reports))

        time.sleep(300)
        # update counter for daily report
        counter = (counter + 1) % 288


if __name__ == "__main__":
    main()
