from django.shortcuts import render, redirect
from .forms import PostForm


# Create your views here.
def homePage(request):
    return render(request, 'home.html')


def userProfile(request):
    current_user = request.user
    try:
        wasifu = Profile.objects.filter(user=current_user)[
            0:1
        ]  # wasifu is the same as profile
        user_projects = Projects.objects.filter(user=current_user)
    except Exception as e:
        raise Http404()
    if request.method == "POST":
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect("user_profile")
    else:
        form = UpdateForm()
    return render(
        request,
        "user_profile.html",
        {"form": form, "profile": wasifu, "projects": user_projects},
    )    


def post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect("home_page")
    else:
        form = PostForm()
    return render(request, "post.html", {"form": form})