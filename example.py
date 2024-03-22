import datetime


today = datetime.datetime.today()

tommorow = (today + datetime.timedelta(days=1)).strftime(f"%d/%m/%Y")

six_months_later_day = (today + datetime.timedelta(days=180)).strftime(f"%d/%m/%Y")
