from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, re_path

from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('articles.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # in settings we joined BASE_DIR and build. By calling TemplateView and specifying template_name as index.html we are referencing test/build/index.html, which is taking care of js and css from test/build/static

    # нужно для того, чтобы можно было иметь доступ к фронтэнду без запуска веб-сервера через npm run start => localhost:3000.
    # Можно просто запустить python src/backend/manage.py runserver => localhost:8000
    # 'DIRS': [
    #     os.path.join(
    #         os.path.dirname(
    #             os.path.dirname(BASE_DIR)
    #         ), 'build'
    #     )
    # ],
    re_path('.*', TemplateView.as_view(template_name='index.html')),
]
