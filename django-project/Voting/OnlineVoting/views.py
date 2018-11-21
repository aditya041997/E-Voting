from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import VoteFor
from .forms import VoteForm
def votepage(request):
   return render(request, 'OnlineVoting/vote.html')

def viewall(request):
	votes=VoteFor.objects.all()
	data={'votes':votes}
	return render(request, 'OnlineVoting/viewall.html', data)

def addvote(request):
	#return HttpResponse("add called")
	if request.method=='POST':
		form=VoteForm(request.POST)
		if form.is_valid():
			name=request.POST.get('name')
			party=request.POST.get('party')
			obj=VoteFor(name=name, party=party)
			obj.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('invalid form data')
	else:
		form=VoteForm()
	return render(request, 'OnlineVoting/vote.html', {'form': form})