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
    def get_earnings_pages(self, entity):
        p = EarningsPage.objects.get(name=entity)
        e = []
        while p.next.name != entity:
            if p.next.page_type == 'form':
                e.append(p.next)
            p = p.next
        return e
