from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'bambi'

urlpatterns = [
    path('', views.index, name="index"),
    path('adminDashboard', views.adminDashboard, name="adminDashboard"),
    path('agents', views.agents, name="agents"),
    path('members', views.members, name="members"),
    path('newMember', views.newMember, name="newMember"),
    path('newAgent', views.newAgent, name="newAgent"),
    path('saveAgent', views.saveAgent, name="saveAgent"),

    # path('enrollment', views.enroll, name="jomutech-enrollment"),
	# path('authentication', views.authenticate, name="jomutech-authentication"),
	# path('enrolluser', views.registeruser, name="jomutech-register-user"),
	# path('authenticateuser', views.authenticateuser, name="jomutech-authenticate-user"),
	# path('validateentry', views.validateentry, name='jomutech-validate-user'),





    

]