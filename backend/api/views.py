from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def AddApplicant(request):
    if(request.method=='POST'):
        serializer=ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Thankyou for your feedback','successs':True},status=status.HTTP_201_CREATED)
        else:
            return Response({'message':serializer.errors,'data':{},'success':False}, status=status.HTTP_400_BAD_REQUEST)