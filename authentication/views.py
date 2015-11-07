from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer 
from django.template.context_processors import request


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return(permissions.AllowAny(),)
        
        if self.request.method == 'POST':
            return(permissions.AllowAny(),)
        
        return(permissions.IsAuthenticated(), IsAccountOwner(),)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)
            
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            print('User Creation Error:')
            print(request.data)
            print(serializer.errors)

        return Response({
                         'status': 'Bad Request',
                         'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)