import datetime
import ephem
from typing import List, Tuple

from calendar_creation import Calendar


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


def get_lua_day(start, end):
    """Calculates the current Lua month for a given day, and all months previous.

    :param today: Defaults to the current time. Can be any datetime object after 2016/11
    :return: None
    """
    lua_months = ["Wyrm", "Dance", "Milk", "Mead", "Wrath", "Dim", "Moth",
                   "Blood", "Veil", "Blooming", "Memory", "Bane", "Wake"]
    calendar_info = {}
    start_day = datetime.datetime(2016, 10, 13)
    index = 7
    new_moons_since = get_moons_in_timeframe(start=start_day, end=end, moon_type="new")

    years_since = 0
    ly_list = [2, 5, 7, 10, 13, 16, 18]
    if len(new_moons_since) <= 0:
        print("Error! It's been 0 or fewer new moons since 2016??")
        return
    counter = 0
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
        new_moon = new_moons_since[i].replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
        date_str = "{}/{}/{} {}:{}:{}".format(new_moon.month, new_moon.day, new_moon.year,
                                              new_moon.hour, new_moon.minute, new_moon.second)
        if new_moons_since[i] > start_date:
            print("New moon date:", date_str, "New month name:", this_month)
        counter += 1
        # Not doing the last month:
        if i < len(new_moons_since) - 1:
            full_moon_greg = ephem.next_full_moon(new_moons_since[i]).datetime()
            full_moon_lua = new_moons_since[i+1] - full_moon_greg
            full_moon_greg = full_moon_greg.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
            full_moon_lua_ref = "{} {}:{}:{}".format(full_moon_lua.days + 1, full_moon_greg.hour, full_moon_greg.minute,
                                                     full_moon_greg.second)
            if new_moons_since[i] > start_date:
                print("Lua full moon:", full_moon_lua_ref)
                calendar_info[counter] = [this_month, date_str, full_moon_lua_ref, full_moon_greg]
    this_calendar = Calendar("calendar.pdf", calendar_info)
    print("====================\n\n")
    days_since_start = end - new_moons_since[i]
    print("Lua date: {} of {}".format(days_since_start.days + 1, this_month))
    next_moon = ephem.next_new_moon(datetime.datetime.now()).datetime()
    next_moon = next_moon.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
    print("Next new moon: {}/{}/{} {}:{}:{}".format(next_moon.month, next_moon.day, next_moon.year,
                                                    next_moon.hour, next_moon.minute, next_moon.second))
    index += 1
    if index == 12 and years_since not in ly_list:
        index = 0
    if index == 13:
        index = 0
    next_month = lua_months[index]
    print("Next month: ", next_month)

future_date = datetime.datetime(2026, 1, 30)
start_date = datetime.datetime(2022, 12, 20)
get_lua_day(start_date, future_date)

"""info needed for calendar
New moon date/time
Full moon date/time (of Lua month)
Month name
"""