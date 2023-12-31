from django.urls import path

from .views import (
    ProductListView,
    ProductDetail,
)
urlpatterns = [
    path('list-view/', ProductListView.as_view()),
    path('<uuid:id>/detail-view/<str:slug>/', ProductDetail.as_view()),
]