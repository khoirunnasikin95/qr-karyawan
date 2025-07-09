from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', views.dashboard, name='dashboard'),

    path('scan/informasi/', views.informasi_page, name='informasi'),
    path('api/informasi/<str:no_id>/', views.api_informasi, name='api_informasi'), 
    path('karyawan/', views.karyawan_list, name='karyawan_list'),
    path('karyawan/upload/', views.upload_karyawan_excel, name='upload_karyawan_excel'),
    path('karyawan/tambah/', views.karyawan_tambah, name='karyawan_tambah'),

    path('scan/benefit/', views.benefit_page, name='benefit'),
    path('api/benefit/<str:no_id>/', views.api_benefit, name='api_benefit'),
    path('api/benefit/take/', views.take_benefit, name='take_benefit'),

    path('scan/kedisiplinan/', views.kedisiplinan_page, name='kedisiplinan'),
    path('api/kedisiplinan/<str:no_id>/', views.api_kedisiplinan, name='api_kedisiplinan'),
    path('sp/', views.sp_list, name='sp_list'),
    path('sp/upload/', views.upload_sp_excel, name='upload_sp_excel'),
    path('kedisiplinan/upload/', views.upload_kedisiplinan_excel, name='upload_kedisiplinan_excel'),

    path('pengguna/', views.kelola_pengguna, name='kelola_pengguna'),
    path('pengguna/update/<int:user_id>/', views.update_grup_pengguna, name='update_grup_pengguna'),
    path('pengguna/toggle-status/<int:user_id>/', views.toggle_status_user, name='toggle_status_user'),

    path('rekap/benefit/', views.rekap_benefit, name='rekap_benefit'),
    path('rekap/benefit/export/', views.export_benefit_excel, name='export_benefit_excel'),

]   