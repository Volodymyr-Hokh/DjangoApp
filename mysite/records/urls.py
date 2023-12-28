from django.urls import path

from . import views

app_name = "records"
urlpatterns = [
    path("", views.main, name="index"),
    path("page/<int:page>/", views.main, name="index_paginate"),
    path("add_record/", views.add_record, name="add_record"),
    path("tag/<str:tag_name>/", views.show_records, name="show_records"),
    path(
        "tag/<str:tag_name>/page/<int:page>/",
        views.show_records,
        name="show_records_paginate",
    ),
]
