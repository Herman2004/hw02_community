import datetime

my_age = (datetime.date.today() - datetime.date(
    2004, 9, 13
    )) / datetime.timedelta(days=365.45)
my_age = int(my_age)
def year(request):
    """Оперирует с годами/датами"""
    return {
        'current_year_footer': datetime.date.today().year,
        "author_age": my_age
    }
