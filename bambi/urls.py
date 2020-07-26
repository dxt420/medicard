from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'bambi'

urlpatterns = [
    path('index', views.index, name="index"),
    path('', views.index, name="index"),
    path('adminDashboard', views.adminDashboard, name="adminDashboard"),
    path('agents', views.agents, name="agents"),
    path('accountPage/<slug:id>', views.accountPage, name="accountPage"),
    path('memberFunds', views.memberFunds, name="memberFunds"),

    path('updateBalance/<slug:id>', views.updateBalance, name="updateBalance"),
    path('log', views.log, name="log"),
     path('logout', views.logout, name="logout"),
    path('logs', views.logs, name="logs"),
    path('agentDetail/<slug:id>', views.agentDetail, name="agentDetail"),
    path('memberDetail/<slug:id>', views.memberDetail, name="memberDetail"),
    path('editMember/<slug:id>', views.editMember, name="editMember"),
    path('editAgent/<slug:id>', views.editAgent, name="editAgent"),
    path('deleteMember/<slug:id>', views.deleteMember, name="deleteMember"),
    path('deleteAgent/<slug:id>', views.deleteAgent, name="deleteAgent"),
    path('members', views.members, name="members"),
    path('newMember', views.newMember, name="newMember"),
    path('newAgent', views.newAgent, name="newAgent"),
    path('saveAgent', views.saveAgent, name="saveAgent"),
    path('saveMember', views.saveMember, name="saveMember"),
    path('agentDashboard', views.agentDashboard, name="agentDashboard"),

    






    

]