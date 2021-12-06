from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.forms import MP3AudioForm
from main.models import MP3Audio
def index(request):

    if request.method == 'POST':
        form = MP3AudioForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MP3AudioForm()

    qs = MP3Audio.objects.all()

    return render(request, 'index.html', {'form': form, 'qs': qs})