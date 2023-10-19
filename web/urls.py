from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('',views.home,name='home'),
    path('CheckAuthentication/', views.CheckAuthenticationView.as_view(), name='CheckAuthentication'),
    path('ApprovalView/', views.ApprovalViewSet.as_view({'get': 'list'}), name='Approval-view'),
    path('Approval/<int:pk>/', views.ApprovalUpdateView.as_view(), name='update-approval'),


    
]
    