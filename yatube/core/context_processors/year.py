import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        'current_year_footer': datetime.date.today().year
    }
