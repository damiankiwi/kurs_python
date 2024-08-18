import calendar
import locale

def display_locale_calendar(year, month, locale_name):
    locale.setlocale(locale.LC_TIME, locale_name)

    locale_cal = calendar.LocaleTextCalendar(firstweekday=0, locale=locale_name)

    print(locale_cal.formatmonth(year, month))

year = 2024
month = 8
locale_name = 'fr_FR.UTF-8'

display_locale_calendar(year, month, locale_name)