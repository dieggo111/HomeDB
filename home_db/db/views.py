from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from db.models import User
from django.forms.models import model_to_dict
import django_tables2 as tables

class UserTable(tables.Table):
    user = tables.Column()
    email = tables.Column()

def index(request):
    return HttpResponse("<h1>db view<h1>")

class DbUserView(ListView):
    template_name = "db_user_view.html"
    model = User
    context_object_name = 'table'
    table_class = UserTable
    # filterset_class = Part_Filter

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset





# def db_content_view(request):
#     template_name = 'db_content_view.html'
#     context = User.objects.all()
#     return render(request, template_name, context)

    # def get_query_set(self):
    #     return User.objects.all()
    # for item in User.objects.all():
    #     print(item.name, item.email)
    # return HttpResponse("<h1>db view<h1>")
