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
            for i in range(6):
                can.drawString(105+(i*100), 485, str(i+1))
            for i in range(6):
                can.drawString(105+(i*100), 410, str(i+7))
            for i in range(6):
                can.drawString(105+(i*100), 335, str(i+13))
            for i in range(6):
                can.drawString(105+(i*100), 260, str(i+20))
            for i in range(3):
                can.drawString(105+(i*100), 185, str(i+27))


            # Skip to next page
            can.showPage()
        can.save()
