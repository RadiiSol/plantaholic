from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import ExtendUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


# Create your views here.

def sign_up(request):
    if request.method == "POST":
        if 'signup' in request.POST:
            print("Signup Button is clicked")
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            username = request.POST['username']
            email = request.POST['email']
            firstname = request.POST['first-name']
            lastname = request.POST['last-name']
            contact = request.POST['contact']

            context = {
                'uname': username,
                'email': email,
                'fname': firstname,
                'lname': lastname,
                'contact': contact
            }

            if len(pass1) and len(pass2) >= 6:
                if pass1 == pass2:
                    if len(username) > 3:
                        try:
                            user = User.objects.get(username=username)
                            return render(request, 'sign_up.html', {'error': "Username Has Been Taken", 'context': context})
                        except User.DoesNotExist:
                            if User.objects.filter(email=email).exists():
                                return render(request, 'sign_up.html', {'error': "Email Has Been Used", 'context': context})
                            if contact.isnumeric() == False:
                                return render(request, 'sign_up.html', {'error': "Contact Should Be In Numbers", 'context': context})
                            user = User.objects.create_user(username=username,password=pass1, email=email)
                            newextendeduser = ExtendUser(firstname=firstname, lastname=lastname, contact=contact, user=user)
                            newextendeduser.save()
                            return render(request, 'sign_up.html', {'success': "Successfully Signned Up"})
                    else:
                        return render(request, 'sign_up.html', {'error': "Username Should Be Greater Than 3", 'context': context})
                else:
                    return render(request, 'sign_up.html', {'error': "Passwords Do Not Match", 'context': context})
            else:
                return render(request, 'sign_up.html', {'error': "Passwords Should Be Greater Than 6", 'context': context})
    else:
        # print(username, firstname, lastname, email, pass1, pass2)
        return render(request, 'sign_up.html')


def login(request):
    if request.method == "POST":
        email = request.POST['login_email']
        psw = request.POST['login_pass']
        next = request.POST['next']
        if next == "/":
            next = "/sign_up"
        render_next = next + ".html"
        render_next = render_next[1:]
        render_next = render_next.replace('user/', '')
        print(render_next)
        if User.objects.filter(email=email).exists():
            user_details = User.objects.filter(email=email)
            user = authenticate(request, username=user_details[0].username, password=psw)
            if user is not None:
                auth.login(request, user)
                next = request.POST['next']

                return redirect(next)
            else:
                return render(request, render_next, {'lerror': "Invalid Login Details"})
        else:
            return render(request, render_next, {'lerror': "Invalid Login Details"})


def log_out(request):
    logout(request)
    return redirect('index')


@login_required(login_url='sign_up')
def settings(request):
    datas = ExtendUser.objects.filter(user=request.user)
    user_last_login = User.objects.get(id=request.user.id).last_login
    last_login = user_last_login.strftime('%y-%m-%d %a %H:%M:%S')
    if request.method == "POST":
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        contact = request.POST['contact']
        pass1 = request.POST['pass1']

        matchpass = check_password(pass1, request.user.password)

        if matchpass and len(pass1) >= 6:
            data_ext = ExtendUser.objects.get(user=request.user)
            if firstname != '':
                data_ext.firstname = firstname
            if lastname != '':
                data_ext.lastname = lastname
            if contact != '':
                data_ext.contact = contact
            if email != '':
                data = User.objects.get(id=request.user.id)
                data.email = email
                data.save()
            data_ext.save()
            return render(request, 'change_settings.html', {'datas': datas, 'last_login': last_login, 'success': "Successfully Changed"})
        else:
            return render(request, 'change_settings.html', {'datas': datas, 'last_login': last_login, 'error': "Password Do Not Match"})

    return render(request, 'change_settings.html', {'datas': datas, 'last_login': last_login})
