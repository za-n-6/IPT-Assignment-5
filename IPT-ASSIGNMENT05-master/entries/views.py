from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

# Create your views here.
def index(request):

    entries = Entry.objects.order_by('-date_posted')

    context = {'entries' : entries}
    
    return render(request, 'entries/index.html', context)


def add(req):

    if req.method == "POST":
        form = EntryForm(req.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form = EntryForm()

    context =  {'form' : form}

    return render(req, 'entries/add.html', context)
 