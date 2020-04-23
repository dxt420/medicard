from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponseRedirect

from . models import *
from . serializers import *

# from django.contrib.auth.forms import PasswordResetForm


from allauth.account.views import PasswordResetView

from django.conf import settings
from django.dispatch import receiver
from django.http import HttpRequest
from django.middleware.csrf import get_token




def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('bambi:adminDashboard'))
    else:
        return render(request,"bambi/login.html")

def adminDashboard(request):
    # try:
    #     employee = Employee.objects.get(email=request.user.email)
    #     if employee.status == 'admin':
    #         employee = Employee.objects.get(username=request.user.username)
    #         context = {
    #             'employee': employee
    #         }

    #         return render(request,"bambi/admin-dashboard.html",context)
    #     else:
            
    #         employee = Employee.objects.get(username=request.user.username)
    #         context = {
    #             'employee': employee
    #         }

    #         return render(request,"bambi/admin-dashboard.html",context)
    return render(request,"bambi/admin-dashboard.html")

def agents(request):
    if request.user.is_authenticated:
        # return HttpResponseRedirect(reverse('bambi:adminDashboard'))
        return render(request,"bambi/agents.html")
    else:
        return render(request,"bambi/login.html")

def newAgent(request):
    if request.user.is_authenticated:
        # return HttpResponseRedirect(reverse('bambi:adminDashboard'))
        return render(request,"bambi/new-agent.html")
    else:
        return render(request,"bambi/login.html")

def saveAgent(request):
    newU = UserInviteSerializer()
    # newUser = UserInviteSerializer(data={'email':request.POST.get('email')})
    aa = newU.validate({'email':request.POST.get('email')})
    # newUser.email = request.POST.get('email')
    # newUser.validate({'email':request.POST.get('email')})
    # newUser.email = request.POST.get('email')
    # newUser.is_valid()
    newUser = newU.create(aa)
    print(newUser)
    # print(newUser)

    # if newUser.is_valid():
    #     createdUser = newUser.create(newUser.get_cleaned_data())
    #     print(createdUser)
    # else:
    #     print("Fuckk off")
    
    
    agent = Agent(name=request.POST.get('name'),
                  contact=request.POST.get('contact'),
                  user=newUser,
                  email=request.POST.get('email'),
                  address=request.POST.get('address'),
                  status="invite")
                    
    agent.save()

    # form = PasswordResetForm({'email': request.POST.get('email')})

    # if form.is_valid():
    #     # request = HttpRequest()
    #     request.META['SERVER_NAME'] = 'localhost'
    #     request.META['SERVER_PORT'] = '443'
    #     form.save(
    #         request= request,
    #         use_https=True,
    #         from_email="omonaderrick@gmail.com", 
    #         email_template_name='registration/password_reset_email.html')


    # add the absolute url to be be included in email
    if settings.DEBUG:
        request.META['HTTP_HOST'] = '127.0.0.1:8000'
    else:
        request.META['HTTP_HOST'] = 'bambi.pythonanywhere.com'

    # pass the post form data
    request.POST = {
        'email': request.POST.get('email'),
        'csrfmiddlewaretoken': get_token(HttpRequest())
    }
    PasswordResetView.as_view()(request)  # email will be sent!

   

    return HttpResponseRedirect(reverse('bambi:agents'))
  






def members(request):
    if request.user.is_authenticated:
        # return HttpResponseRedirect(reverse('bambi:adminDashboard'))
        return render(request,"bambi/members.html")
    else:
        return render(request,"bambi/login.html")
        
def newMember(request):
    if request.user.is_authenticated:
        # return HttpResponseRedirect(reverse('bambi:adminDashboard'))
        return render(request,"bambi/new-member.html")
    else:
        return render(request,"bambi/login.html")



#If Fingerprint Authentication is Successful
	# statusVal = 1
	# personPart[0] = row.fname
	# personPart[1] = row.sname
	# personPart[2] = row.empno
	# personPart[3] = row.id
	# personPart[4] = statusVal
	# print(row.fname, row.sname, row.empno, row.id, statusVal)
	# print(personPart[4])
	
	# if statusVal == 1:
	# 	print("SUCCESS")
	# 	print(personPart)
	# 	return JsonResponse({'status':'OK', 'funame':personPart[0], 'suname':personPart[1], 'empno':personPart[2]})
	# elif statusVal < 1:
	# 	print("FAIL")
	# 	print(personPart)
	# 	return JsonResponse({'status':'OK', 'funame':personPart[0], 'suname':personPart[1], 'empno':personPart[2]})




