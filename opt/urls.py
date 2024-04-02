from django.urls import path
from . import views

urlpatterns = [
    path('showAll/',views.showAll,name='showAll'),
    path('html/',views.gadhaDolly,name='html'),
    path('add/',views.postData,name='add'),
    path('delete/<int:id>',views.deleteData,name='delete'),
    path('update/<int:id>',views.updateData,name='update'),
    path('updateRecord/<int:id>',views.updateRecord,name='updateRecord')
]