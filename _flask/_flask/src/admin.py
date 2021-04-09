from flask import request, redirect, url_for
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

from models import Post, Tag, User, Role


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super().on_model_change(form, model, is_created)


class AuthMixin:

    def is_accessible(self):
        return True
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class PostModelView(BaseModelView, AuthMixin, ModelView):
    form_columns = [
        'title',
        'body',
    ]


class TagModelView(AuthMixin, ModelView):
    form_columns = [
        'name',
        'posts',
    ]


class UserModelView(AuthMixin, ModelView):
    pass


class HomeAdminView(AuthMixin, AdminIndexView):
    pass

