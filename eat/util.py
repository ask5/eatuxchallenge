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
    def reset_assistance_program(cls, app):
        app.assistance_program = False
        app.case_number = None
        app.save()

    @classmethod
    def all_adults_entered(cls, app):
        app.all_adults_entered = True
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

    @classmethod
    def get_app_progress(self, app):
        completed_steps = 0
        if app.assistance_program or app.app_for_foster_child:
            total_steps = 2
            children = Child.children.filter(application=app)
            if children.count() >= app.total_children:
                completed_steps += 1
            if app.street_address:
                completed_steps += 0.5
            if app.signature:
                completed_steps += 0.5
        else:
            total_steps = 3
            children = Child.children.filter(application=app)
            adults = Adult.adults.filter(application=app)
            if children.count() >= app.total_children:
                completed_steps += 1
            if adults.count() >= app.total_adults:
                completed_steps += 0.5

            total_adults_earnings = 0
            for adult in adults:
                total_adults_earnings += adult.get_total_earning()
            if total_adults_earnings > 0:
                completed_steps += 0.5
            if app.street_address:
                completed_steps += 0.5
            if app.signature:
                completed_steps += 0.5

        percent = (completed_steps / total_steps) * 100
        return  percent

    @classmethod
    def get_nav(cls, nav, url):
        t = []
        for k, v in nav.items():
            v['current'] = True if v['url'] == url else False
            t.append(v)
        s = sorted(t, key=lambda k:k['position'])
        return s
