from django.urls import path
from .views import ValidateLoginView, UpdateContactView, SearchContactView, UpdateProfileView

urlpatterns = [
    path('api/login/', ValidateLoginView.as_view(), name='validate-login'),
    path('profile/', UpdateProfileView.as_view(), name='update-profile'),
    # path('api/update-contact/<int:pk>/', UpdateContactView.as_view(), name='update-contact'),
    # path('api/search-contacts/', SearchContactView.as_view(), name='search-contacts'),
]
