"""
URL configuration for mydjangobackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog, set_language
from django.urls import path, include
from django.views.generic.base import TemplateView
from base.views import redirect_view
handler404 = 'base.views.custom_page_not_found_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('set_language/', set_language, name='set_language'),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(template_name="sitemap.xml", content_type="text/plain"),
    ),
    path('', redirect_view)
]
urlpatterns += i18n_patterns(
    # Put translatable views here
    path('', include('base.urls')),

    # Needed for translations in Javascript
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
)
