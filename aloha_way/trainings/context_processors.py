from datetime import datetime


def get_date(request):
    return {'data': datetime.today().strftime('%Y-%m-%d %H:%M')}
