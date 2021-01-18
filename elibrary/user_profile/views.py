from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .tokens import password_reset_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import *

# Create your views here.


def user_register(request):
    if request.user.is_authenticated :
        return redirect('user_profile:user_register')  # Redirect to Home Page
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if request.POST.get('ajax_check') == "True":
            if form.is_valid():
                if User.objects.filter(email=form.cleaned_data['email']).exists():
                    return HttpResponse("A user with that Email already exists.")
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                subject = 'Register to NIT Durgapur Central Library'
                message = render_to_string('user_profile/account_activation_email.html', {
                      'user': user,
                      'domain': current_site.domain,
                      'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                      'token': account_activation_token.make_token(user),
                })
                user.email_user(subject, message)
                return HttpResponse("Please confirm your email address to complete the Registration.")
            if form.errors:
                for field in form:
                    for error in field.errors:
                        return HttpResponse(error)
            form = SignUpForm(None)

    return render(request, 'user_profile/register.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'user_profile/account_activation_sent.html')


def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('user_profile:edit_profile')
    else:
        return render(request, 'user_profile/account_activation_invalid.html')


@login_required
def edit_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    form = ProfileForm(request.POST or None, request.FILES or None,  instance=profile)
    if form.is_valid():
        form.save()
        return redirect('user_profile:view_profile')
    return render(request, 'user_profile/create.html', {'form': form, })


@login_required
def view_profile(request):
    id = request.user.id
    try:
        user = get_object_or_404(User, pk=id)
    except:
        return HttpResponse("User does not exist!")
    try:
        profile = get_object_or_404(Profile, user=user)
    except:
        return HttpResponse("User has not created a Profile yet!")
    args = {'profile': profile, }
    return render(request, 'user_profile/profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_profile:edit_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user_profile/change_password.html', {
        'form': form
    })


def password_reset(request):
    form = EmailForm(request.POST or None)
    if request.method == 'POST':
        if request.POST.get('ajax_check') == "True":
            if form.is_valid():
                email = form.cleaned_data['email']
                if not User.objects.filter(email=email).exists():
                    return HttpResponse("No user with that Email exists.")
                user = User.objects.get(email=email)
                user.save()
                current_site = get_current_site(request)
                subject = 'Reset Your NIT Durgapur Central Library Account Password'
                message = render_to_string('user_profile/password_reset_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': password_reset_token.make_token(user),
                })
                user.email_user(subject, message)
                return HttpResponse("We've emailed you instructions for setting your password, if an account exists with the email you entered! You should receive them shortly."
                                  "If you don't receive an email, please make sure you've entered the address you registered with, and check your spam folder.")
            form = EmailForm(None)
            return HttpResponse('Invalid')
    return render(request, 'user_profile/password_reset_form.html', {'form': form})


def password_reset_done(request):
    return render(request, 'user_profile/password_reset_done.html')


def password_reset_confirm(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            user.is_active = True
            user.save()
            return redirect('login')
        return render(request, 'user_profile/password_reset_confirm.html', {'form': form})
    else:
        return render(request, 'user_profile/password_reset_invalid.html')


def password_reset_complete(request):
    return render(request, 'user_profile/password_reset_complete.html')