from django.http import Http404
from django.shortcuts import render_to_response
from .forms import UploadFileForm

def handle_uploaded_file(f):
    """ Helper function for home.
        Sends the file to the database after parsing
        and returns the automagically generated url """
    pass

# TODO: implement csrf?
def home(request):
    """ Handles the home page and the upload handling. """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            url = handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/'+url)
    else:
        form = UploadFileForm()
    return render_to_response('home', {
            'title': 'FlashBox',
            'form': form
        })

def view_cards(request, url):
    """ Searches the database for a particular
        url which corresponds to their cards and
        renders them. """
    pass

def handle_uploaded_file(post):
    """ Handles parsing of file and uploading to database """
