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

from django.contrib.auth.decorators import login_required

from django.db import IntegrityError
from django.http import JsonResponse


from django.contrib import messages, auth
# from django.shortcuts import render_to_response



@login_required
def index(request):
    if request.user.is_admin: 
        return HttpResponseRedirect(reverse('bambi:adminDashboard'))
    else:
    # elif if request.user.is_admin == Agent.objects.get(email=request.user.email).email: :
        # 
        return HttpResponseRedirect(reverse('bambi:agentDashboard'))

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    
    return HttpResponseRedirect(reverse('bambi:index'))


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
  
    context = {
                'a': "active"
            }
    return render(request,"bambi/admin/admin-dashboard.html",context)

def agentDashboard(request):
    context = {
                'a': "active"
            }
    return render(request,"bambi/agent/agent-dashboard.html",context)

def agents(request):
    agents = Agent.objects.all()
    context = {
        'agents': agents,
        'c': "active"
    }

    return render(request,"bambi/admin/agents.html",context)

def agentDetail(request,id):
    agent = Agent.objects.get(agent_id=id)
    context = {
        'agent': agent,
        'c': "active"
    }


    return render(request,"bambi/admin/agent-detail.html",context)




def newAgent(request):
    context = {
       
        'b': "active"
    }
    return render(request,"bambi/admin/new-agent.html",context)


def saveAgent(request):

    
    newU = UserInviteSerializer()
    aa = newU.validate({'email':request.POST.get('email')})
   
    try:
        newUser = newU.create(aa)
        agent = Agent(name=request.POST.get('name'),
                    contact=request.POST.get('contact'),
                    user=newUser,
                    email=request.POST.get('email'),
                    address=request.POST.get('address'),
                    status="invite")

                    
        agent.save()

        print(agent)
        msg = request.POST.get('name') + " invited to complete Agent Onboarding by admin"
        
        log = Log(log_message=msg,log_user_id=str(request.user.id),log_secondary_user_id=str(agent.agent_id),log_type="Success")

        log.save()
        
        
        # add the absolute url to be be included in email
        if settings.DEBUG:
            request.META['HTTP_HOST'] = '127.0.0.1:8000'
        else:
            request.META['HTTP_HOST'] = 'bambicard.pythonanywhere.com'

        # pass the post form data
        request.POST = {
            'email': request.POST.get('email'),
            'csrfmiddlewaretoken': get_token(HttpRequest())
        }
        PasswordResetView.as_view()(request)  # email will be sent!


        
       

        context = {
            'Mailed': 'Mailed'
            
        }

        return JsonResponse(context, safe=False)

    except IntegrityError as e:
        print(e)
        context = {
            'Integrity Error': "Integrity Error"
            
        }

        return JsonResponse(context, safe=False)

    except Exception as e:
        print(e)
        context = {
            'Exception': "Exception"
            
        }

        return JsonResponse(context, safe=False)



    # return HttpResponseRedirect(reverse('bambi:agents'))

 
   

    


def saveMember(request):

    
  
   
    try:
    
        member = Member(name=request.POST.get('name'),
                    contact=request.POST.get('contact'),
                    status="inactive",
                    email=request.POST.get('email'),
                    address=request.POST.get('address'),
                    dob=request.POST.get('dob'))


                    
        member.save()


        memberFunds = MemberFunds(membership_id=member,balance="0")

        memberFunds.save()


        msg = "New member " + member.name + " added by admin"
        
        log = Log(log_message=msg,log_user_id=str(request.user.id),log_secondary_user_id=str(member.membership_id),log_type="Success")

        log.save()


        context = {
            'Success': 'Success'
            
        }
        messages.success(request, "aa")
        request.session['foo'] = 2
        return JsonResponse(context, safe=False)

    except IntegrityError as e:
        print(e)
        context = {
            'Error': "Integrity Error"
            
        }

        return JsonResponse(context, safe=False)






def deleteMember(request,id):
    Member.objects.get(membership_id=id).delete()



    context = {
        'Success': 'Success'
            
    }

    return JsonResponse(context, safe=False)


def deleteAgent(request,id):
    Agent.objects.get(agent_id=id).delete()



    context = {
        'Success': 'Success'
            
    }

    return JsonResponse(context, safe=False)





def newMember(request):
    context = {
        'd': "active"
    }
    return render(request,"bambi/admin/new-member.html",context)

def members(request):
    members = Member.objects.all()
    context = {
        'members': members,
        'e': "active"
    }

    return render(request,"bambi/admin/members.html",context)


def logs(request):
    logs = Log.objects.all().order_by('-created_at')
    context = {
        'logs': logs,
        'h': "active"
    }

    return render(request,"bambi/admin/logs.html",context)


def accountPage(request,id):

   
    member = Member.objects.get(membership_id=id)
    related_logs = Log.objects.filter(log_secondary_user_id=id,log_type="Fund")
  
    context = {
      'member': member,
        'f': "active",
        'related_logs':related_logs
    }

    return render(request,"bambi/admin/account-page.html",context)

def memberFunds(request):
  
    context = {
      
        'g': "active"
    }

    return render(request,"bambi/admin/member-funds.html",context)



    



def memberDetail(request,id):
    member = Member.objects.get(membership_id=id)
    related_logs = Log.objects.filter(log_secondary_user_id=id)
    context = {
        'member': member,
        'related_logs':related_logs,
        'e': "active"
    }


    return render(request,"bambi/admin/member-detail.html",context)

def editMember(request,id):
    member = Member.objects.get(membership_id=id)
    msg2 = ""
    try:
        if member.name!=request.POST.get('name'):
            msg2 += "Name changed from " + member.name + " to " + request.POST.get('name') + "; "
            member.name=request.POST.get('name')

      
        if member.contact!=request.POST.get('contact'):
            msg2 += "Contact changed from " + member.contact + " to " + request.POST.get('contact') + "; "
            member.contact=request.POST.get('contact') 

        if member.email!=request.POST.get('email'):
            msg2 += "Email changed from " + member.email + " to " + request.POST.get('email') + "; "
            member.email=request.POST.get('email')

        if member.address!=request.POST.get('address'):
            msg2 += "Address changed from " + member.address + " to " + request.POST.get('address') + "; "
            member.address=request.POST.get('address')

        if member.dob!=request.POST.get('dob'):
            msg2 += "Date of Birth changed from " + member.dob + " to " + request.POST.get('dob') + "; "
            member.dob=request.POST.get('dob')
    
 
             
   


                    
        member.save()

        msg = "Member " + member.name + " details modified by admin"

        
        
        log = Log(log_message=msg,log_secondary_message=msg2,log_user_id=str(request.user.id),log_secondary_user_id=str(member.membership_id),log_type="Info")

        log.save()


        context = {
            'Success': 'Success'
            
        }

        return JsonResponse(context, safe=False)

    except Exception as e:
        print(e)
        print("toosie slide")
        context = {
             e
            
        }


        return JsonResponse(context, safe=False)

def editAgent(request,id):
    agent = Agent.objects.get(agent_id=id)
    try:
        agent.name=request.POST.get('name')
        agent.contact=request.POST.get('contact')      
   
        agent.address=request.POST.get('address')



                    
        agent.save()


        context = {
            'Success': 'Success'
            
        }

        return JsonResponse(context, safe=False)

    except Exception as e:
        print(e)
        print("toosie slide")
        context = {
             e
            
        }


        return JsonResponse(context, safe=False)


def log(request):
    agent = Agent.objects.get(agent_id=id)
    try:
        agent.name=request.POST.get('name')
        agent.contact=request.POST.get('contact')      
   
        agent.address=request.POST.get('address')



                    
        agent.save()


        context = {
            'Success': 'Success'
            
        }

        return JsonResponse(context, safe=False)

    except Exception as e:
        print(e)
        print("toosie slide")
        context = {
             e
            
        }


        return JsonResponse(context, safe=False)



def updateBalance(request,id):
    memberFund = MemberFunds.objects.get(membership_id=id)
    msg2 = ""
    try:
        formerFunds = memberFund.balance
        memberFund.balance=request.POST.get('balance') 
        memberFund.save()


        msg2 = "Account balance for member " + memberFund.member.name + " updated from " + formerFunds + " to " + memberFund.balance + " by admin"
        msg = memberFund.member.name + "'s account balance was updated by admin"
        log = Log(log_message=msg,log_secondary_message=msg2,log_user_id=str(request.user.id),log_secondary_user_id=str(memberFund.member.membership_id),log_type="Success")

        log.save()

        context = {
            'Success': 'Success'
            
        }

        return JsonResponse(context, safe=False)

    except Exception as e:
        print(e)
        print("toosie slide")
        context = {
             e
            
        }


        return JsonResponse(context, safe=False)








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




