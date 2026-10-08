from django.shortcuts import render

def home(request):
  return render(request,"home.html",{"username":request.user})

  
def about(request):
  return render(request,"about.html",{"username":request.user})
