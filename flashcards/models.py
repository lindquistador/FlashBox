from mongoengine import *

class Cards(EmbeddedDocument):
    key = StringField(max_length=250)
    info = StringField(max_length=5000)

class FlashCardSet(Document):
    title = StringField(max_length=200)
    vocabulary = ListField(EmbeddedDocumentField(Cards))
    url = StringField(max_length=32)

