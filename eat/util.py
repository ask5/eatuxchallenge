from eat.models import Application
import datetime


class App(object):

    @classmethod
    def get(self, id):
        return Application.applications.get(pk=id)

    @classmethod
    def get_by_user(self, user):
        return Application.applications.filter(user=user.id)
