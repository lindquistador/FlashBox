try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile
WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
 
 
def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)
 
    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))
 
    return '\n\n'.join(paragraphs)


def flash(path):
    x = get_docx_text(path)
    x.encode("ascii")
    length = len(x)
    print length

    s = ""
    flash = []
    array = []

    for i in range(0, length):
        print x[i]
        if x[i] ==':':
        	flash = []
        	flash.append(s)
        	s = ""
        elif x[i] == '&' and len(flash) != 0:
        	flash.append(s)
        	array.append(flash)
        	s = ""
        elif x[i] == '&':
        	array.append(s);
        	s=""
        else:	
        	s = s + x[i]

    return array;

"""
this is how you would call it 
returns array of arrays
first element in the title 

w = flash('demo.docx')
print w[0]

for j in range(1,len(w)): 
    print w[j][0]
"""