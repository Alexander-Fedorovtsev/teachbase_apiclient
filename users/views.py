from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Profile
from .forms import CreatonForm, UserForm, ProfileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import clientapi


class SignUp(CreateView):
    form_class = CreatonForm
    success_url = reverse_lazy("api:index")
    template_name = "users/signup.html"


def showprofilepageview(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == "POST":
        form1 = ProfileForm(request.POST, instance=profile)
        form2 = UserForm(request.POST, instance=user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return HttpResponseRedirect("/auth/user_profile/")
        else:
            print("invalid form")
            return render(
                request,
                "users/user_profile.html",
                {"form1": form1, "form2": form2},
            )
    else:
        template = "users/user_profile.html"
        accesstoken = clientapi.gettoken("/oauth/token")
        form1 = ProfileForm(
            instance=profile, initial={"accesstoken": accesstoken}
        )
        form2 = UserForm(instance=user)
        context = {
            "page_user": user,
            "profile": profile,
            "form1": form1,
            "form2": form2,
        }
        return render(request, template, context)


def teachbaseregister(request):
    template = "includes/message.html"
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    response = clientapi.userregister(
        email=user.email, name=user.first_name, lastname=user.last_name
    )
    if response[0] == 200:
        profile.externalid = response[1].get("id")
        profile.save()
        message = "Вы успешно зарегистрированы на Teachbase, можете записаться на сессию!"
    context = {
        "message": message,
    }
    return render(request, template, context)
