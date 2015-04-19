from django.http import Http404
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from .forms import UploadFileForm

def handle_uploaded_file(f):
    """ Helper function for home.
        Sends the file to the database after parsing
        and returns the automagically generated url """
    pass

def home(request):
    """ Handles the home page and the upload handling. """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            url = handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/'+url)
    else:
        form = UploadFileForm()
    c = { 'title': 'FlashBox',
          'form': form }
    c.update(csrf(request))
    return render_to_response('home', c)

class test:
    pass

def view_cards(request, url):
    """ Searches the database for a particular
        url which corresponds to their cards and
        renders them. """
    _test = test()
    _test.text = "lorem ipsum <> | ^@#$*() : { : & : } ()"
    c = { 'title': 'View Cards',
          'cards':  [_test, _test, _test] }
    c.update(csrf(request))
    return render_to_response('view_cards', c)
