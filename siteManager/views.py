from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *


class ContactView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = ContactPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({'save': True})
        return Response({'save': False, 'message': serialized.errors})

    @staticmethod
    def get(request):
        queryset = Contact.objects.all()
        serialized = ContactGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


# {
#     "message": "This field is required.",
#     "name": "Michael",
#     "email": "mike@gmail.com"
# }

class ApplicationView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = ApplicationPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({'save': True})
        return Response(serialized.errors)

    @staticmethod
    def get(request):
        queryset = Application.objects.all()
        serialized = ApplicationGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class EventView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = EventPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({'save': True})
        return Response({'save': False, 'message': serialized.errors})

    @staticmethod
    def get(request):
        queryset = Event.objects.all()
        serialized = EventGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)




