from django.shortcuts import render

# Create your views here.

def index(request):
	a = request.POST.get('txt1',False)
	b = request.POST.get('txt2',False)
	context = {}
	if request.POST.get('add',False):
		c = int(a)+int(b)
		context = {'sum':c}		
	elif request.POST.get('sub',False):
		c = int(a)-int(b)
		context = {'sum':c}	
	elif request.POST.get('mul',False):
		c = int(a)*int(b)
		context = {'sum':c}	
	elif request.POST.get('div',False):
		c = int(a)/int(b)
		context = {'sum':c}	
	
	return render(request,'sum/index.html',context)
