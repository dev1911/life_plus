from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request , "prescription/home.html")
	
def upload(request):
	#upload form. Blockchain logic. Convert into class based view.
	pass	