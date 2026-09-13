"""
URL configuration for owner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('insertuserregistration',views.insertuserregistration,name='insertuserregistration'),
    path('showuserregistration',views.showuserregistration,name='showuserregistration'),
    path('deluserregistration/<int:pk>/',views.deluserregistration,name='deluserregistration'),


    path('insertuserlogin',views.insertuserlogin,name='insertuserlogin'),
    path('showuserlogin',views.showuserlogin,name='showuserlogin'),
    path('deluserlogin/<int:pk>/',views.deluserlogin,name='deluserlogin'),


    path('insertkitchen',views.insertkitchen,name='insertkitchen'),
    path('showkitchen',views.showkitchen,name='showkitchen'),
    path('delkitchen/<int:pk>/',views.delkitchen,name='delkitchen'),


    path('insertmenucategory',views.insertmenucategory,name='insertmenucategory'),
    path('showmenucategory',views.showmenucategory,name='showmenucategory'),
    path('delmenucategory/<int:pk>/',views.delmenucategory,name='delmenucategory'),


    path('insertmenuitem',views.insertmenuitem,name='insertmenuitem'),
    path('showmenuitem',views.showmenuitem,name='showmenuitem'),
    path('delmenuitem/<int:pk>/',views.delmenuitem,name='delmenuitem'),


    path('insertorder',views.insertorder,name='insertorder'),
    path('showorder',views.showorder,name='showorder'),
    path('delorder/<int:pk>/',views.delorder,name='delorder'),


    path('insertorderitem',views.insertorderitem,name='insertorderitem'),
    path('showorderitem',views.showorderitem,name='showorderitem'),
    path('delorderitem/<int:pk>/',views.delorderitem,name='delorderitem'),


    path('insertdelivery',views.insertdelivery,name='insertdelivery'),
    path('showdelivery',views.showdelivery,name='showdelivery'),
    path('deldelivery/<int:pk>/',views.deldelivery,name='deldelivery'),


    path('insertpayment',views.insertpayment,name='insertpayment'),
    path('showpayment',views.showpayment,name='showpayment'),
    path('delpayment/<int:pk>/',views.delpayment,name='delpayment'),
    path('payment_qrcode',views.payment_qrcode,name='payment_qrcode'),


    path('insertcoupon',views.insertcoupon,name='insertcoupon'),
    path('showcoupon',views.showcoupon,name='showcoupon'),
    path('delcoupon/<int:pk>/',views.delcoupon,name='delcoupon'),


    path('insertingredient',views.insertingredient,name='insertingredient'),
    path('showingredient',views.showingredient,name='showingredient'),
    path('delingredient/<int:pk>/',views.delingredient,name='delingredient'),


    path('insertreview',views.insertreview,name='insertreview'),
    path('showreview',views.showreview,name='showreview'),
    path('delreview/<int:pk>/',views.delreview,name='delreview'),

    path('insertnotification',views.insertnotification,name='insertnotification'),
    path('shownotification',views.shownotification,name='shownotification'),
    path('delnotification/<int:pk>/',views.delnotification,name='delnotification'),

    path('', views.showindex, name='showindex'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('owner_home', views.owner_home, name='owner_home'),
    path('customer_home', views.customer_home, name='customer_home'),
    path('logcheck', views.logcheck, name='logcheck'),
    path('logout', views.logout, name='logout'),

    path('owner_showmenucategory', views.owner_showmenucategory, name='owner_showmenucategory'),
    path('owner_delmenucategory/<int:pk>/', views.owner_delmenucategory, name='owner_delmenucategory'),
    path('owner_updatemenucategory/<int:pk>/', views.owner_updatemenucategory, name='owner_updatemenucategory'),

    path('owner_showmenuitem', views.owner_showmenuitem, name='owner_showmenuitem'),
    path('owner_delmenuitem/<int:pk>/', views.owner_delmenuitem, name='owner_delmenuitem'),
    path('owner_updatemenuitem/<int:pk>/', views.owner_updatemenuitem, name='owner_updatemenuitem'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

