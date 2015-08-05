from django.shortcuts import render
from .forms import ProfileForm


def handleform(request):
    if request.method=='POST':
        form = ProfileForm(data=request.POST)
        if request.POST.get('submit'):
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
    else:
        form = ProfileForm()
    return render(request, 'index.html', context=locals())
