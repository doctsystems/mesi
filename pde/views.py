from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import RegMIPForm
# from .upfiles import main
from .test2metodos import main

def in_file(request):
	error = False
	files=[]
	if request.method == 'POST':
		form = RegMIPForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			try:
				files=main(post.nacional.url, post.regional.url, post.sector.url)
			except ValueError as e:
				error = True
				return render(request, 'pde/in.html', {'form': form, 'error': error, 'msj': e})
			# return HttpResponseRedirect(reverse('pde:out'))
			return render(request, 'pde/out.html', {'files': files})
	else:
		form = RegMIPForm()
	return render(request, 'pde/in.html', {'form': form})

def out_file(request, id=None):
	return render(request, 'pde/out.html')