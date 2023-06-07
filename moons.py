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


def get_lua_day(today=datetime.datetime.now()):
    lua_months = ["1", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "11", "12", "0"]
    lua_months = ["Wyrm", "Dance", "Milk", "Mead", "Wrath", "Dim", "Moth",
                   "Blood", "Veil", "Blooming", "Memory", "Bane", "Wake"]

    start_day = datetime.datetime(2016, 11, 14)
    index = 7
    new_moons_since = get_moons_in_timeframe(start=start_day, end=today, moon_type="new")

    print(new_moons_since)
    years_since = 0
    ly_list = [2, 5, 7, 10, 13, 16, 18]
    if len(new_moons_since) <= 0:
        print("Error! It's been 0 or fewer new moons since 2016??")
        return
    for i in range(len(new_moons_since)):
        index += 1
        if index == 12 and years_since not in ly_list:
            index = 0
            years_since += 1
        if index == 13:
            index = 0
            years_since += 1
        if years_since == 19:
            years_since = 0
        this_month = lua_months[index]
        new_moon = new_moons_since[i]
        date_str = "{}/{}/{} {}:{}:{}".format(new_moon.month, new_moon.day, new_moon.year,
                                              new_moon.hour, new_moon.minute, new_moon.second)
        print("New moon date:", date_str, "new month name:", this_month)
    print("====================\n\n")
    print("Current month:", this_month)
    print("Next new moon: ", ephem.next_new_moon(datetime.datetime.now()))
    index += 1
    if index == 12 and years_since not in ly_list:
        index = 0
    if index == 13:
        index = 0
    next_month = lua_months[index]
    print("Next month: ", next_month)

random_future_day = datetime.datetime(2035,12,3)
get_lua_day(random_future_day)
