from django import forms
from pics.models import Pic
from pics.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Create your views here.
class PicListView(OwnerListView):
    model = Pic

class PicDetailView(OwnerDetailView):
    model = Pic

class PicCreateView(OwnerCreateView):
    model = Pic
    fields = ['title', 'text', 'picture']

class PicUpdateView(OwnerUpdateView):
    model = Pic
    fields = ['title', 'text']

class PicDeleteView(OwnerDeleteView):
    model = Pic