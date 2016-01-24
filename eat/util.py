from eat.models import Application
from django.core.urlresolvers import resolve


class AppUtil(object):

    @classmethod
    def get(self, id):
        return Application.applications.get(pk=id)

    @classmethod
    def get_by_user(self, user):
        app = Application.applications.filter(user=user.id)
        return app

    @classmethod
    def set_last_page(cls, app, path):
        app.last_page = resolve(path).url_name
        app.save()