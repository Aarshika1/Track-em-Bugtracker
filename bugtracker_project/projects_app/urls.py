from django.urls import path
from projects_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home,name='home'),
    path('project',views.project,name='project'),
    path('register/',views.RegisterPage,name='register'),
    path('login',views.LoginPage,name='login'),
    path('logout',views.Logout,name='logout'),
    path('createproject/',views.add_project,name='addproject'),
    path('delete/<int:project_id>',views.project_delete,name = 'project_delete'),
    path('updateproject/<int:project_id>',views.update_project,name='updateproject'),
    path('viewproject/<int:project_id>',views.view_project,name='viewproject')
]

urlpatterns += staticfiles_urlpatterns()