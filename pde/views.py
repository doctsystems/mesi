from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import RegMIPForm
from .upfiles import main

def in_file(request):
	if request.method == 'POST':
		form = RegMIPForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			# return redirect('post_detail', pk=post.pk)
			# print('post------------> ',post.nacional)
			# _id=post.pk
			main(post.pk, post.nacional.url, post.regional.url, post.sector.url)
			# main(post.pk, post.nacional, post.nacional, post.nacional)
			# main(post.pk)
			return HttpResponseRedirect(reverse('pde:out'))
	else:
		form = RegMIPForm()
	return render(request, 'pde/in.html', {'form': form})

def out_file(request, id=None):
	return render(request, 'pde/out.html')