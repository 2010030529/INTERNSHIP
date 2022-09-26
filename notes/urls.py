from django.urls import  path
from .import views
urlpatterns=[
    path('',views.listView.as_view(),name="notes.list"),
    path('<int:pk>',views.detailView.as_view(),name='notes.details')
]