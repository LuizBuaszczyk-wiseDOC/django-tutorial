from django.urls import path, reverse_lazy
from django.views.generic import TemplateView

from . import views

app_name="pics"
urlpatterns = [
    path('', views.PicListView.as_view(), name='all'),
    path('pic/<int:pk>', views.PicDetailView.as_view(), name='pic_detail'),
    path('pic/create', views.PicCreateView.as_view(), name='pic_create'),
    path('pic/<int:pk>/update', views.PicUpdateView.as_view(), name='pic_update'),
    path('pic/<int:pk>/delete', views.PicDeleteView.as_view(), name='pic_delete'),
    #path('pic_picture/<int:pk>', views.stre.as_view(), name='pic_picture'),
]
