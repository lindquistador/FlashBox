from django.http import Http404
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from .forms import UploadFileForm
from .parsefunc import flash

import sqlite3 as lite
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

    con = lite.connect('db.db')

    with con:
        cur  = con.cursor()
        array = flash(f)
        counter = 0;

        for i in range(len(array)):
            if i == 0:
                title = array[i]
                i += 1
            for j in range(len(array[i])):
                counter += 1
                cur.execute("INSERT INTO Cards (Key)")
                cur.execute("VALUES ({})".format(array[i][j]))
                #INSERT INTO Cards (Key)
                #VALUES (array[i][j])
                j += 1
                cur.execute("INSERT INTO Cards (Info, Index)")
                cur.execute("VALUES ({0}, {1})".format(array[i][j], counter))
                #INSERT INTO Cards (Info, Index)
                #VALUES (array[i][j], counter)

        cur.execute("INSERT INTO Flashcards (Title, Total_cards)")
        cur.execute("VALUES ({0}, {1}".format(title, counter))
        #INSERT INTO Flashcards (Title, Total_cards)
        #VALUES (title, counter)
        cur.excute("INSERT INTO Flashcards SELECT * FROM Cards")
        #INSERT INTO Flashcards SELECT * FROM Cards
        #Do I need to put in a VALUES line????

    hash_object = hashlib.md5(b'{0}{1}{2}'.format(title, array[1][0], array[1][1]))
    return hash_object
