from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader, RequestContext
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from itertools import chain
from django.core.files.base import ContentFile
from io import BytesIO
import urllib.request
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from django.core.mail import send_mass_mail
import json
import datetime
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from difflib import SequenceMatcher
from django.utils import timezone
from datetime import timedelta

# Create your views here.


def list_ecopies(request):
    #search = SearchForm(request.POST or None)
    #if request.method == 'POST':
    #    if search.is_valid():
    #      key_req = search.cleaned_data
    #      key = key_req.get('key')
    #      return HttpResponseRedirect(reverse('forum:search_question', args=(key,)))
    ecopies = ECopies.objects.all()
    count = ecopies.count()
    args = {'ecopies': ecopies, 'count': count}
    return render(request, 'ecopies.html', args, )