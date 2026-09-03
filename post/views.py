from django.shortcuts import render

# Create your views here.
def post(request):
  data = [
    "This is the post about Java",
    "This is the post about Javascript",
    "This is the post about HTML",
    "This is the post about CSS",
    "This is the post about Python",
    "This is the post about Django"
    ]
  
  return render(request,template_name="post.html",context={"data":data})