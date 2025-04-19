# contacts/urls.py
from django.urls import path
from .views import ContactListCreateView, ContactDetailView, ContactSearchView

urlpatterns = [
    path('create-contacts', ContactListCreateView.as_view(), name='contact-list-create'),
    path('<int:id>/', ContactDetailView.as_view(), name='contact-detail'),
    path('search/', ContactSearchView.as_view(), name='contact-search'),
]
