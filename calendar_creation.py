import datetime

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
import ephem



class Calendar():
    def __init__(self, filename, info_dict, **kwargs):
        self.indexes = ["month_name", "month_greg_start", "full_moon_day"]
        self.info_dict = info_dict
        can = canvas.Canvas(filename, pagesize=landscape(letter))
        for i in info_dict:
            # Get the last day of the month
            try:
                next_month = info_dict[i+1][1].split(" ")[0]
                last_day = datetime.datetime(int(next_month.split("/")[-1]), int(next_month.split("/")[0]),
                                             int(next_month.split("/")[1])) - datetime.timedelta(1)
            except KeyError:
                this_month = info_dict[i][1].split(" ")[0]
                skip_days = datetime.datetime(int(this_month.split("/")[-1]), int(this_month.split("/")[0]),
                                             int(this_month.split("/")[1])) + datetime.timedelta(2)
                last_day = ephem.next_new_moon(skip_days).datetime() - datetime.timedelta(1)
            # Get the first day of the month
            first_day = info_dict[i][1].split(" ")[0]
            first_day_dt = datetime.datetime(int(first_day.split("/")[-1]), int(first_day.split("/")[0]),
                                             int(first_day.split("/")[1]))
            # Total days
            total_days = (last_day - first_day_dt).days + 1

            can.setFontSize(25)
            can.drawString(600, 520, "- {}/{}/{}".format(last_day.month, last_day.day, last_day.year))
            can.setFont("Helvetica", 45)
            can.drawString(20, 550, info_dict[i][0])
            can.setFontSize(15)
            can.drawString(20, 535, info_dict[i][1])
            can.setFont("Helvetica", 25)
            first_day = info_dict[i][1].split(" ")[0]
            can.drawString(600, 550, first_day)

            # Make the calendar grid
            can.line(60, 500, 740, 500)
            can.line(60, 410, 740, 410)
            can.line(60, 320, 740, 320)
            can.line(60, 230, 740, 230)
            can.line(60, 140, 740, 140)
            if total_days == 29:
                can.line(60, 50, 400, 50)
            else:
                can.line(60, 50, 513.3, 50)

            can.line(60, 500, 60, 50)
            can.line(173.3, 500, 173.3, 50)
            can.line(289.6, 500, 289.6, 50)
            can.line(400, 500, 400, 50)
            if total_days == 29:
                can.line(513.3, 500, 513.3, 140)
            else:
                can.line(513.3, 500, 513.3, 50)
            can.line(626.6, 500, 626.6, 140)
            can.line(740, 500, 740, 140)

            # Add the days (good lord there must be a better way)
            can.setFontSize(13)
            for day in range(6):
                can.drawString(65+(day*113.3), 485, str(day+1))
            for day in range(6):
                can.drawString(65+(day*113.3), 395, str(day+7))
            for day in range(6):
                can.drawString(65+(day*113.3), 300, str(day+13))
            for day in range(6):
                can.drawString(65+(day*113.3), 210, str(day+20))
            for day in range(3):
                can.drawString(65+(day*113.3), 125, str(day+27))
            if total_days == 30:
                can.drawString(65+(3*113.3), 125, "30")

            # Add the full moon
            # x = 105+(day*100) y = 335
            fullmoon_info = info_dict[i][2]
            fullmoon_d = int(fullmoon_info.split(" ")[0]) - 13
            can.setFont("Helvetica",15)
            fullmoon_hms = fullmoon_info.split(" ")[1]
            can.drawString(65+(fullmoon_d*113.3), 233, fullmoon_hms)
            can.drawInlineImage("./imgs/full_moon_tiny.jpg", 145+(fullmoon_d*113.3), 293)

            # Pretty pictures!
            #can.drawInlineImage("./imgs/moon_phases.jpg", -100, 20)

            # Skip to next page
            can.showPage()
        can.save()
