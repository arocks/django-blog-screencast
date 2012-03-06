from blog.models import Post
from django.shortcuts import render_to_response

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {"posts":posts, "tag":tag})
