from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="challanges-index-page"),
    # for those values which can be parsed into integer
    path("<int:month>", views.month_challange_by_num, name="month-num-challange"),
    # for those which can be parsed into string
    path("<str:month>", views.month_challange, name="month-challange"),
]
