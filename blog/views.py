from django.http import HttpRequest, HttpResponse
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = (
        Post.objects
        .select_related("author")
        .filter(
            published_at__isnull=False,
        )
        .order_by("-published_at"))
    return render(
        request, 
        "blog/index.html",
        {
            "posts": posts
        })


def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/welcome.html")
