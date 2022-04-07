from django.shortcuts import render


# Create your views here.
def homePage(request):
    return render(request, 'home.html')


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