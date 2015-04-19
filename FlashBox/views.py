from django.http import Http404
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from flashcards.models import Cards, FlashCardSet
from .forms import UploadFileForm
from .parsefunc import flash

import hashlib
import sys

def home(request):
    """ Handles the home page and the upload handling. """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if not request.FILES['file'].name.endswith(".docx") or \
               not request.FILES['file'].name.endswith(".doc"):
                   # TODO: throw error here
                   pass
            url = handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/notes/'+url)
        # if failed, form should fall through with custom error
    else:
        form = UploadFileForm()
    c = { 'title': 'FlashBox',
          'form': form }
    c.update(csrf(request))
    # TODO: display form error
    return render_to_response('home', c)

def view_cards(request, url):
    """ Searches the database for a particular
        url which corresponds to their cards and
        renders them. """
    flash_card = FlashCardSet.objects(url__contains=url).first()
    if flash_card == None:
        # TODO: handle error here
        pass

    c = { 'title': 'View Your Cards',
          'flash_card_set_title': flash_card.title,
          'cards':  flash_card.vocabulary }
    c.update(csrf(request))
    return render_to_response('view_cards', c)

def handle_uploaded_file(f):
    """ Helper function for home.
        Sends the file to the database after parsing
        and returns the automagically generated url """

    array = flash(f)
    _title= array[0]
    # just to get a nice url
    _hash_object = hashlib.md5(b'{0}{1}{2}'.format(_title, array[1][0], array[1][1]))
    _url = _hash_object.hexdigest()

    cards = []
    for i in range(1, len(array)):
        _key, _val = array[i][0], array[i][1]
        cards.append(Cards(key=_key, info=_val))
    flash_card = FlashCardSet(title=_title, vocabulary=cards, url=_url)
    flash_card.save()

    return _url
