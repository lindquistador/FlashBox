from django.http import Http404
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .parsefunc import flash

import hashlib
import sys

def home(request):
    """ Handles the home page and the upload handling. """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print form
        if form.is_valid():
            if not request.FILES['file'].name.endswith(".docx") or \
               not request.FILES['file'].name.endswith(".doc"):
                   # TODO: throw error here
                   pass
            url = handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/'+url)
        # if failed, form should fall through with custom error
    else:
        form = UploadFileForm()
        print form
    c = { 'title': 'FlashBox',
          'form': form }
    c.update(csrf(request))
    # TODO: display form error
    return render_to_response('home', c)

def view_cards(request, url):
    """ Searches the database for a particular
        url which corresponds to their cards and
        renders them. """
    c = { 'title': 'View Your Cards',
          'cards':  None }
    c.update(csrf(request))
    return render_to_response('view_cards', c)

def handle_uploaded_file(f):
    """ Helper function for home.
        Sends the file to the database after parsing
        and returns the automagically generated url """


    array = flash(f)
    counter = 0;

    title = array[0]
    for i in range(1, len(array)):
        key = array[i][0]
        definition = array[i][1]
       
    hash_object = hashlib.md5(b'{0}{1}{2}'.format(title, array[1][0], array[1][1]))
    return hash_object
