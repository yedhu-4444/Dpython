
from django.urls import path
from . import views
app_name='tokoapp'

urlpatterns = [
    path('',views.home,name='home'),
    # path('details/',views.details,name='details'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),

]
