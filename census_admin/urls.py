# My django imports
from django.urls import path

# My app imports
from census_admin.views import (
    AdminDashboardView,
    
    AdminUserListView,
    AdminUserDetailView,
    AdminUserEditView,
    AdminUserDeleteView,
    
    AdminLGAListView,
    AdminLGADeleteView,
    
    AdminCreateStaffView,
    AdminStaffListView,
    AdminStaffDetailView,
    AdminStaffDeleteView,
    AdminStaffEditView,
    AdminSupportMessageView,
)
app_name = 'staff'

urlpatterns = [
    path('admin_dashboard', AdminDashboardView.as_view(), name='admin_dashboard'),
    
    path('admin_user_list', AdminUserListView.as_view(), name='admin_user_list'),
    path('admin_user_edit/<int:user_id>/', AdminUserEditView.as_view(), name='admin_user_edit'),
    path('admin_user_details/<int:user_id>/', AdminUserDetailView.as_view(), name='admin_user_details'),
    path('admin_user_delete/<int:user_id>/', AdminUserDeleteView.as_view(), name='admin_user_delete'),
    
    path('admin_lga_list', AdminLGAListView.as_view(), name='admin_lga_list'),
    path('admin_lga_delete/<int:user_id>/', AdminLGADeleteView.as_view(), name='admin_lga_delete'),
    
    path('admin_create_staffs', AdminCreateStaffView.as_view(), name='admin_create_staffs'),
    path('admin_staff_list', AdminStaffListView.as_view(), name='admin_staff_list'),
    path('admin_staff_details/<int:user_id>/', AdminStaffDetailView.as_view(), name='admin_staff_details'),
    path('admin_staff_delete/<int:user_id>/', AdminStaffDeleteView.as_view(), name='admin_staff_delete'),
    path('admin_staff_edit/<int:user_id>/', AdminStaffEditView.as_view(), name='admin_staff_edit'),
    
    path('admin_support_message', AdminSupportMessageView.as_view(), name='admin_support_message'),
    
]