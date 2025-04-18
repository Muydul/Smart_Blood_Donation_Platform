from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Arequest, Comment
from profiles.models import Aprofile
from .forms import CreateRequestForm,CreateRequestForm2
from sqlalchemy.sql import null

# Create your views here.


def home(request):

    allRequestEmergency = Arequest.objects.filter(type="Emergency")
    allRequestManaged = Arequest.objects.filter(type="Managed")

    allRequest = list(allRequestEmergency)

    for managed in allRequestManaged:
        allRequest.append(managed)

    context = {
        'allRequest': allRequest
    }
    return render(request, 'home.html', context)


def addRequest(request):
    form = CreateRequestForm()
    try:

        profile = Aprofile.objects.filter(user=request.user)[0]

        if request.method == 'POST':
            form = CreateRequestForm(request.POST)
            if form.is_valid:
                try:
                    instance = form.save(commit=False)
                    instance.author = profile
                    instance.save()
                    return redirect('home')
                except:
                    return HttpResponse("You Must need to be logged in")
            else:
                return HttpResponse("Something Went Wrong")

        context = {
            "form": form
        }
        return render(request, "addRequest.html", context)

    except:
        return redirect('login-account')


def seeDetails(request, pk):
    try:

        profile = Aprofile.objects.filter(user=request.user)[0]
    except:
        profile = "Anonymous"
    aReq = Arequest.objects.get(id=pk)
    allCommnets = aReq.comment_set.all()

    context = {
        'arequest': aReq,
        'profile': profile,
        "allCommnets": allCommnets
    }
    return render(request, 'seeDetails.html', context)


def editPost(request, pk):

    profile = Aprofile.objects.filter(user=request.user)[0]
    post = Arequest.objects.get(id=pk)
    if profile != post.author:
        return HttpResponse("You Are Not Authorized")

    form = CreateRequestForm2(instance=post)
    if request.method == "POST":
        form = CreateRequestForm2(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return redirect('see-details', pk=pk)

    context = {
        'form': form,
        'arequest': post
    }
    return render(request, 'editPost.html', context)


def deletePost(request, pk):
    profile = Aprofile.objects.filter(user=request.user)[0]

    post = Arequest.objects.get(id=pk)

    if profile != post.author:
        return HttpResponse("You Are Not Authorized")

    if request.method == "POST":
        post = Arequest.objects.get(id=pk)
        post.delete()
        return redirect('/')

    context = {
        'arequest': post
    }
    return render(request, 'deletePost.html', context)


def arequestAddRemove(request, pk):
    try:

        post = Arequest.objects.get(id=pk)
        profile = Aprofile.objects.filter(user=request.user)[0]

        if profile in post.reqForDonate.all():
            post.reqForDonate.remove(profile)

        else:
            post.reqForDonate.add(profile)
        return redirect('see-details', pk=pk)
    except:
        return redirect('login-account')


def contactNow(request, pk):
    profile = Aprofile.objects.get(id=pk)
    context = {
        'profile': profile
    }
    return render(request, 'contactNow.html', context)


def seeRequestedDonor(request, pk):

    try:

        post = Arequest.objects.get(id=pk)
        profile = Aprofile.objects.filter(user=request.user)[0]

        allDonor = post.reqForDonate.all()
        context = {
            'allDonor': allDonor,
            'profile': profile
        }
        return render(request, 'allDonor.html', context)
    except:
        return redirect('login-account')


def commentPost(request, pk):
    try:

        profile = Aprofile.objects.filter(user=request.user)[0]
        post = Arequest.objects.get(id=pk)

        if request.method == 'POST' and request.POST['commnet-box'] != null:

            Comment.objects.create(user=profile, post=post,
                                body=request.POST['commnet-box'])
            return redirect('see-details', pk=pk)
    except:
        return redirect('login-account')





# ========================================================


def deleteComment(request, pk, ck):
    try:

        profile = Aprofile.objects.filter(user=request.user)[0]
    except:
        profile = "AnonymousUser"

    comment = Comment.objects.get(id=pk)
    if comment.user == profile:
        comment.delete()
        return redirect('see-details', pk=ck)

    else:
        return HttpResponse("You Are Not Authorized")


def about(request):

    return render(request, 'about.html')
