from django.shortcuts import render
from .models import Subscriptions

# Create your views here.

def all_subscriptions(request):

    subscriptions = Subscriptions.objects.all()

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscription/subscription.html', context)