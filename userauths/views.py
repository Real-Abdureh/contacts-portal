from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, LoginSerializer, UpdateContactSerializer, get_tokens_for_user
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated





class ValidateLoginView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data  # Now this is a User instance
            tokens = get_tokens_for_user(user)
            return Response({
                'access': tokens['access'],
                'refresh': tokens['refresh'],
                'user': UserSerializer(user).data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateContactView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=UpdateContactSerializer)
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        serializer = UpdateContactSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Contact updated successfully'})
        return Response(serializer.errors, status=400)
    

search_param = openapi.Parameter(
    'q', openapi.IN_QUERY, description="Search term (name, contact, or email)",
    type=openapi.TYPE_STRING
)

class SearchContactView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @swagger_auto_schema(manual_parameters=[search_param])
    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return User.objects.filter(
            full_name__icontains=query
        ) | User.objects.filter(
            contact_number__icontains=query
        ) | User.objects.filter(
            email__icontains=query
        )
