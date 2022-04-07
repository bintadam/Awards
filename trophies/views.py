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



def projectDetail(request, project_id):
    try:
        projects = Projects.objects.filter(id=project_id)
        all = Votes.objects.filter(project=project_id)
    except Exception as e:
        raise Http404()
    # user single
    count = 0

    for i in all:
        count += i.usability
        count += i.design
        count += i.content

    if count > 0:
        ave = round(count / 3, 1)

    else:
        ave = 0

    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project_id
            # review
            rate.save()
            return redirect("details", project_id)
    else:
        form = RateForm()

    # logic
    votes = Votes.objects.filter(project=project_id)
    usability = []
    design = []
    content = []

    for i in votes:
        usability.append(i.usability)
        design.append(i.design)
        content.append(i.content)

    if len(usability) > 0 or len(design) > 0 or len(content) > 0:

        average_usa = round(sum(usability) / len(usability), 1)
        average_des = round(sum(design) / len(design), 1)
        average_con = round(sum(content) / len(content), 1)

        averageRating = round((average_con + average_des + average_usa) / 3, 1)

    else:
        average_usa = 0.0
        average_des = 0.0
        average_con = 0.0
        averageRating = 0.0

    """Restricting user to rate only once"""
    arr1 = []
    for use in votes:
        arr1.append(use.user_id)

    auth = arr1

    if request.method == "POST":
        review = CommentForm(request.POST)

        if review.is_valid():
            comment = review.save(commit=False)
            comment.user = request.user
            comment.pro_id = project_id
            comment.save()

            return redirect("details", project_id)
    else:
        review = CommentForm()

    try:
        user_comment = Comments.objects.filter(pro_id=project_id)

    except Exception as e:
        raise Http404()

    return render(
        request,
        "details.html",
        {
            "projects": projects,
            "form": form,
            "usability": average_usa,
            "design": average_des,
            "content": average_con,
            "average": averageRating,
            "auth": auth,
            "all": all,
            "ave": ave,
            "review": review,
            "comments": user_comment,
        },
    )    