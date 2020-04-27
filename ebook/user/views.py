from django.shortcuts import render,redirect
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			return redirect('mainpage')
	else:		
		form = UserRegisterForm()
	return render(request,'user/register.html',{'form': form})

def pdf(request):
	return render(request,'user/pdf.html')



