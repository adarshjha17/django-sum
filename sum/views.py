from django.shortcuts import render

# Create your views here.

def index(request):
	a = request.POST.get('txt1',False)
	b = request.POST.get('txt2',False)
	c = int(a)+int(b)
	context = {'sum':c}
	return render(request,'sum/index.html',context)
