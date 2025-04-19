from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer
from django.db.models import Q

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    lookup_field = 'id'

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

class ContactSearchView(generics.ListAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Contact.objects.filter(
            user=self.request.user
        ).filter(
            Q(full_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone_number__icontains=query)
        )
