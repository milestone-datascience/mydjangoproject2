from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post(request):
  # data = [
  #   "This is the post about Java",
  #   "This is the post about Javascript",
  #   "This is the post about HTML",
  #   "This is the post about CSS",
  #   "This is the post about Python",
  #   "This is the post about Django"
  #   ]

  if request.method == "GET":
    form = PostForm()
    data = Post.objects.all()
    return render(request,template_name="post.html",context={"data":data,"form":form,"username":request.user})
  elif request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("/post/")


def post_page(request,id):
  post_obj = Post.objects.get(post_id = id)
  return render(request,"post_page.html",{"post":post_obj})