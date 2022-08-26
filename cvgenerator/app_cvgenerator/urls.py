from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.cv_index, name='cv.index'),
    path('app/create/', views.cv_create, name='cv.create'),
    path('app/update/', views.cv_update, name='cv.update'),
    path('app/show/<int:id>/', views.cv_show, name='cv.show'),
    path('app/edit/<int:id>/', views.cv_edit, name='cv.edit'),
    path('app/delete/<int:id>/', views.cv_delete, name='cv.delete'),
]
