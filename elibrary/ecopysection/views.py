from .forms import *
from django.shortcuts import render, redirect
from difflib import SequenceMatcher

# Create your views here.


def list_ecopies(request):
    search = SearchForm(request.POST or None)
    ecopies = ECopies.objects.all()
    if request.method == 'POST':
        if search.is_valid():
            search_content = search.cleaned_data
            title = search_content.get('Title')
            author = search_content.get('Author')
            type = search_content.get('type')
            department = search_content.get('department')
            if department is not None:
                ecopies = ecopies.filter(department=department)
            if type is not None:
                ecopies = ecopies.filter(type=type)
            ecopies_clone = ecopies[:]
            ecopies_found = []
            if title is not None:
                for ecopy in ecopies:
                    if SequenceMatcher(None, ecopy.title.lower(), title.lower()).ratio() > 0.5:
                        ecopies_found.append([SequenceMatcher(None, ecopy.title.lower(), title.lower()).ratio(), ecopy])
            if author is not None:
                for ecopy in ecopies_clone:
                    if SequenceMatcher(None, ecopy.author.lower(), author.lower()).ratio() > 0.5:
                        ecopies_found.append([SequenceMatcher(None, ecopy.author.lower(), author.lower()).ratio(), ecopy])
            ecopies_found.sort(key=lambda x: x[0], reverse=True)
            if author is not None or title is not None:
                ecopies = []
                for ecopy in ecopies_found:
                    if ecopy[1] not in ecopies:
                        ecopies.append(ecopy[1])

    count = len(ecopies)
    args = {'form': search, 'ecopies': ecopies, 'count': count}
    return render(request, 'ecopies.html', args, )