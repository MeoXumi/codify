"""instant_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from instant_work.views import api

urlpatterns = [
	url(r'^api/get_employee/$', api.get_employee),
	url(r'^api/get_employees/$', api.get_employees),
	url(r'^api/get_owner_jobs/$', api.get_onwer_jobs),
	url(r'^api/get_jobs/$', api.get_jobs),
	url(r'^api/apply_job/$', api.apply_job),
	url(r'^api/submit_job/$', api.submit_job),
]
