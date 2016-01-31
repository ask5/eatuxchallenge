from eat.models import EarningsPage
from django.core.urlresolvers import resolve
from eat.forms import *
from . import *

class AppUtil(object):

    @classmethod
    def get(cls, id):
        return Application.applications.get(pk=id)

    @classmethod
    def get_by_user(cls, user):
        app = Application.applications.filter(user=user.id)
        return app

    @classmethod
    def set_last_page(cls, app, path):
        app.last_page = path
        app.save()


    @classmethod
    def get_adult_earning_categories(self):
        earnings_categories = list()
        for k, v in adult_earnings_meta_data.items():
            if v['type'] == 'earnings':
                earnings_categories.append(v)
        return sorted(earnings_categories, key=lambda category: (category['order']))

