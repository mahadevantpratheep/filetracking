from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from accounts.forms import EditProfileForm
from .models import Permission
from django.core.mail import send_mail


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That username is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    user.save()
                    messages.success(
                        request, 'You are now reegister and can log in now')
                    return redirect('login_user')

        else:
            messages.error(request, 'Password do not match')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff == True:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('dashboard_fac')
            else:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('dashboard_user')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login_user')
    else:
        return render(request, 'accounts/login_user.html')


def dashboard_user(request):
    return render(request, 'accounts/dashboard_user.html')


def edit_user_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('dashboard_user')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_user_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('dashboard_user')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def apply(request):
    if request.method == 'POST' and request.FILES['myfile']:
        u = User.objects.filter(is_staff=False).first()
        apply = Permission()
        apply.evnt_name = request.POST['evnt_name']
        apply.myfile = request.FILES['myfile']
        apply.description = request.POST['description']
        apply.save()
        # send_mail('Response to your' + order.evnt_name + 'request','Your response has been accepted', superuser@gmail.com, s.email)
        messages.success(
            request, 'Your Application for permission has been sent')
        return redirect('dashboard_user')
    else:
        return render(request, 'accounts/apply.html')


def dashboard_fac(request):
    perm = Permission.objects.filter(accepted=False)
    data = {}
    data['det'] = []
    for p in perm:
        r = {}
        r['event_name'] = p.evnt_name
        r['myfile'] = p.myfile
        r['description'] = p.description
        r['id'] = p.id
        r['status'] = p.status
        data['det'].append(r)
    return render(request, 'accounts/dashboard_fac.html', data)


def accept_request(request, product_id):
    t = int(product_id)
    u = User.objects.filter(is_staff=True).first()
    r = User.objects.filter(is_staff=False).first()
    order = Permission.objects.filter(id=t).first()
    order.accepted = True
    order.status = "Accepted"
    order.save()
    #send_mail('Response to your' + order.evnt_name + 'request','Your response has been accepted', u.email, r.email)
    messages.success(request, 'Permission Upadated!')
    return redirect('dashboard_fac')


def reject_request(request, product_id):
    t = int(product_id)
    u = User.objects.filter(is_staff=True).first()
    r = User.objects.filter(is_staff=False).first()
    order = Permission.objects.filter(id=t).first()
    order.accepted = True
    order.status = "Declined"
    order.save()
    # send_mail('Response to your' + order.evnt_name + 'request','Your response has been accepted', u.email, r.email)
    messages.success(request, 'Permission Upadated!' + r.email)
    return redirect('dashboard_fac')


def permission_granted(request):
    perm = Permission.objects.all()
    var = {}
    var['det'] = []
    for pe in perm:
        r = {}
        r['event_name'] = pe.evnt_name
        r['myfile'] = pe.myfile
        r['description'] = pe.description
        r['id'] = pe.id
        r['status'] = pe.status
        var['det'].append(r)
    return render(request, 'accounts/permission_granted.html', var)
