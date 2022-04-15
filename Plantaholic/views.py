from django.shortcuts import render
from django.contrib.auth.models import User
from account.models import ExtendUser
from django.core.mail import EmailMessage
from django.conf import settings
# from .models import User, ExtendUser


def index(request):
    return render(request, 'home.html')


def indoor_plants(request):
    return render(request, 'indoor_plants.html')


def outdoor_plants(request):
    return render(request, 'outdoor_plants.html')


def gallery(request):
    return render(request, 'gallery.html')


def plant_growth(request):
    return render(request, 'plant_growth.html')


def plant_protection(request):
    return render(request, 'plant_protection.html')


def garden_tools(request):
    return render(request, 'garden_tools.html')


def suggestion(request):
    if request.method == "POST":
        datas = ExtendUser.objects.get(user=request.user)
        message = request.POST['message']
        user_details_message = "\n\n\nUserName = " + str(datas.user) + "\nName = " + datas.firstname + " " + datas.lastname + "\nEmail = " + datas.user.email
        message = message + user_details_message

        email = EmailMessage(
            'Suggestion Form | Plantaholic',
            message,
            to=['mihirpg2014@gmail.com', 'shantnupoonia4010@gmail.com']
        )

        email.fail_silently = False
        email.send()

        return render(request, 'suggestion.html', {'success': 'Suggestion Sent Successfully'})
    return render(request, 'suggestion.html')


def test(request):
    return render(request, 'test.html')

