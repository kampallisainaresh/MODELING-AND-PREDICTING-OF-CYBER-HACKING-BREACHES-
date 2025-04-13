from django.shortcuts import render,redirect
from django.contrib import messages
from users.models import UserRegistrationModel
from users.forms import UserRegistrationForm
# ,UserAdd_Model



# Create your views here.
def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return redirect( 'AdminHome')

        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})


def AdminHome(request):
    return render(request, 'admins/AdminHome.html')

def RegisterUsersView(request):
    data = UserRegistrationModel.objects.all()
    return render(request,'admins/viewregisterusers.html',{'data':data})


def ActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request,'admins/viewregisterusers.html',{'data':data})

def base(request):
    return render(request,'admins/adminbase.html')

def adminViewResults(request):
    from users.utility.process_ml import start_arma_model
    rslt = start_arma_model()
    return render(request, 'admins/results.html', {'rslt': rslt})
