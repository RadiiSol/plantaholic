from django.shortcuts import render
from django.contrib.auth.models import User
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
        message = request.POST['message']
        send_to_email = {
            "mihirpg2014@gmail.com", "shantnu4010@gmail.com"
        }

        email = EmailMessage(
            'Suggestion Form | Plantaholic',
            message,
            settings.EMAIL_HOST_USER,
            send_to_email,
        )

        email.fail_silently = False
        email.send()

        return render(request, 'suggestion.html', {'success': 'Suggestion Sent Successfully'})
    return render(request, 'suggestion.html')


def test(request):
    return render(request, 'test.html')

