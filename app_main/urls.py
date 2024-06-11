from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('add_cost/',views.add_cost,name='add_cost'),
    path('chiqim_get_costs_within_7_days/',views.chiqim_get_costs_within_7_days,name='chiqim_get_costs_within_7_days'),
    path('chiqim_get_costs_within_30_days/',views.chiqim_get_costs_within_30_days,name='chiqim_get_costs_within_30_days'),
    path('kirim_get_costs_within_7_days/',views.kirim_get_costs_within_7_days,name='kirim_get_costs_within_7_days'),
    path('kirim_get_costs_within_30_days/',views.kirim_get_costs_within_30_days,name='kirim_get_costs_within_30_days'),
    path('update_cost/<int:cost_id>/', views.update_cost, name='update_cost'),
    path('delete_cost/<int:cost_id>/', views.delete_cost, name='delete_cost'),
    path('get_cost_info/<int:cost_id>/', views.get_cost_info, name='get_cost_info'),
]