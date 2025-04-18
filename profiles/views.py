from django.http import HttpResponse
from django.shortcuts import redirect, render
from sqlalchemy import null
from .models import Aprofile
from newsfeed.models import Arequest
from .forms import EditProfileForm

# =============================================================


def myProfile(request):


    try:
        profile = Aprofile.objects.get(user=request.user)
        requestedPosts = profile.arequest_set.all()
        allPosts =Arequest.objects.all()
        donatedPosts = []

        for post in allPosts:
            if post.author != profile:
                if profile in post.reqForDonate.all():
                    donatedPosts.append(post)


        context = {
            "profile": profile,
            'requestedPosts':requestedPosts,
            'donatedPosts':donatedPosts

        }

        return render(request, "my-profile.html", context)

    except:

        return redirect('login-account')


# =============================================================


def editMyProfile(request, pk):

    currentUser = request.user
    profile = Aprofile.objects.get(user=currentUser)
    id = profile.id
    editProfileForm = EditProfileForm(instance=profile)

    if request.method == "POST":
        form = EditProfileForm(
            request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my-profile')

    context = {
        "form": editProfileForm,
        'profileID': id,
    }

    if id == int(pk):
        return render(request, "editProfile.html", context)

    else:
        return HttpResponse("You Can't Edit Other's Profile")




def getProfile(request, pk):
    profile = Aprofile.objects.get(id=pk)

    context = {
        "profile": profile,
    }

    return render(request, "get-profile.html", context)
