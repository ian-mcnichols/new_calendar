import datetime
import ephem
from typing import List, Tuple

def get_moons_in_timeframe(start=datetime.datetime.now(), end=None, years=1, moon_type="full") -> List[Tuple[ephem.Date, str]]:
    """Returns a list of the full moons in a year."""
    moons=[]
    this_year = start.year
    this_month = start.month
    this_day = start.day
    date=ephem.Date(datetime.date(this_year,this_month,this_day))
    if end is None:
        end = this_year + years
    while date.datetime() <= end:
        if moon_type == "full":
          date=ephem.next_full_moon(date)
        elif moon_type == "new":
          date=ephem.next_new_moon(date)
        if date.datetime() < end:
            moons.append(date.datetime())

    return moons


def get_lua_day():
    lua_months = ["1", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "11", "12", "0"]
    lua_months = ["wyrm", "dance", "milk", "mead", "wrath", "dim", "moth",
                   "blood", "veil", "blooming", "memory", "bane", "wake"]

    start_day = datetime.datetime(2016, 11, 14)
    index = 7
    today = datetime.datetime.now()
    new_moons_since = get_moons_in_timeframe(start=start_day, end=today, moon_type="new")

    print(new_moons_since)
    years_since = 0
    ly_list = [2, 5, 7, 10, 13, 16, 18]
    for i in range(len(new_moons_since)):
        index += 1
        if index == 12 and years_since not in ly_list:
            index = 0
            years_since += 1
        if index == 13:
            index = 0
            years_since += 1
        this_month = lua_months[index]
        new_moon_datetime = new_moons_since[i]
        date_str = "{}/{}/{}".format(new_moon_datetime.month, new_moon_datetime.day, new_moon_datetime.year)
        print("New moon date:", date_str, "new month name:", this_month)
    print("Current month:", this_month)

get_lua_day()
