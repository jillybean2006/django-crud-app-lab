from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('jellycats/', views.jellycat_index, name='jellycat-index'),
    path('jellycats/<int:jellycat_id>', views.jellycat_detail, name='jellycat-detail' ),
    path('jellycats/create/', views.JellycatCreate.as_view(), name='jellycat-create'),
    path('jellycats/<int:pk>/update/', views.JellycatUpdate.as_view(), name="jellycat-update"),
    path('jellycats/<int:pk>/delete/', views.JellycatDelete.as_view(), name="jellycat-delete"),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessory-create'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessory-detail'),
    path('accessories/', views.AccessoryList.as_view(), name='accessory-index'),
    path('accessories/<int:pk>/update', views.AccessoryUpdate.as_view(), name="accessory-update"),
    path('accessories/<int:pk>/delete', views.AccessoryDelete.as_view(), name="accessory-delete"),
    path('jellycats/<int:jellycat_id>/associate-accessory/<int:accessory_id>', views.associate_accessory, name='associate-accessory'),
    path('jellycats/<int:jellycat_id>/remove-accessory/<int:accessory_id>/', views.remove_accessory, name='remove-accessory '),
    path('accounts/signup/', views.signup, name='signup')
]