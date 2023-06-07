from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape



class Calendar():
    def __init__(self, filename, info_dict, **kwargs):
        self.indexes = ["month_name", "month_greg_start", "full_moon_day"]
        self.info_dict = info_dict
        can = canvas.Canvas(filename, pagesize=landscape(letter))
        for i in info_dict:
            can.setFont("Helvetica", 45)
            can.drawString(20, 550, info_dict[i][0])
            can.setFont("Helvetica", 25)
            can.drawString(600, 550, info_dict[i][1].split(" ")[0])

            # Make the calendar grid
            can.line(100, 500, 700, 500)
            can.line(100, 425, 700, 425)
            can.line(100, 350, 700, 350)
            can.line(100, 275, 700, 275)
            can.line(100, 200, 700, 200)
            can.line(100, 125, 400, 125)

            can.line(100, 500, 100, 125)
            can.line(200, 500, 200, 125)
            can.line(300, 500, 300, 125)
            can.line(400, 500, 400, 125)
            can.line(500, 500, 500, 200)
            can.line(600, 500, 600, 200)
            can.line(700, 500, 700, 200)

            # Add the days (good lord there must be a better way)
            can.setFontSize(13)
            for day in range(6):
                can.drawString(105+(day*100), 485, str(day+1))
            for day in range(6):
                can.drawString(105+(day*100), 410, str(day+7))
            for day in range(6):
                can.drawString(105+(day*100), 335, str(day+13))
            for day in range(6):
                can.drawString(105+(day*100), 260, str(day+20))
            for day in range(3):
                can.drawString(105+(day*100), 185, str(day+27))

            # Add the full moon
            # x = 105+(day*100) y = 335
            fullmoon_info = info_dict[i][2]
            fullmoon_d = int(fullmoon_info.split(" ")[0]) - 13
            can.setFont("Helvetica",15)
            can.drawString(105+(fullmoon_d*100), 320, "Full Moon")
            fullmoon_hms = fullmoon_info.split(" ")[1]
            can.drawString(105+(fullmoon_d*100), 300, fullmoon_hms)


            # Skip to next page
            can.showPage()
        can.save()
