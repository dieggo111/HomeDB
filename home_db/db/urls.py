from django.urls import path
from db.views import DbUserView, index

urlpatterns = [
    path('', DbUserView.as_view(), name='db_user_view'),
    path('upload/', index, name='upload'),
]
