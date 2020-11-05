from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Subscriptions
from django.contrib import messages
from django.db.models.functions import Lower

# Create your views here.

def all_subscriptions(request):

    subscriptions = Subscriptions.objects.all()

    query = None
    sort = None
    direction = None

    


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                subscriptions = subscriptions.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            subscriptions = subscriptions.order_by(sortkey)
         

        

    current_sorting = f'{sort}_{direction}'

    context = {         
        'subscriptions': subscriptions,
        'current_sorting': current_sorting,
    }

    return render(request, 'subscription/subscription.html', context)


def subscription_detail(request, subscription_id):
    """ A view to show individual product details """

    subscriptions = get_object_or_404(Subscriptions, pk=subscription_id)

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'subscription/subscription_detail.html', context)