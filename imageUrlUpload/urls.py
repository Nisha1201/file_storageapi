from django.urls import path
from .import views


urlpatterns = [
    # path('display/', views.index, name='index'),
    path('', views.fileStorageImage, name= 'upload_image')
    # path("/",views. model_form_upload, name="model")
]
