from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import transaction, IntegrityError
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.utils.translation import ugettext, ugettext as _

from market.models import App, UserApp

def index(request):
    context = {}
    return render(request, 'market/index.html', context)

@login_required
def order(request, app_key):
    user = user
    app = get_object_or_404(App, key=app_key)
    try:
        user_app = UserApp.objects.get(user=user, app__key=app_key)
    except UserApp.DoesNotExist:
        context = {}
        context['app'] = app
        return render(request, 'market_price', context)
        #return redirect('market_app', app_key=app_key)
    else:
        pass
        
    
