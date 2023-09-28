from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Test, Screenplay
from script.messages import Messages

# Create your views here.

class GetSecondSchema(viewsets.ViewSet):

    @action(detail=True, methods=["GET"])
    def getTest(self, request):
        uid = self.request.query_params.get("uid", 0)
        try:
            test = Test.objects.get(test_uid = uid )
            print('test object ', test)
            message, status = Messages.success.value
            data = test.data
        except Test.DoesNotExist:
            print('Test not found')
            message, status = Messages.notFound.value
            data = message
        
        return Response({"data": data},  status )


    @action(detail=True, methods=["GET"])
    def getScreenplay(self, request):
        screenplayuid = self.request.query_params.get("screenplayuid", 0)
        try:
            screenplay = Screenplay.objects.get(screenplay_uid = screenplayuid )
            print('Screenplay object ', screenplay)
            message, status = Messages.success.value
            data = screenplay.title
        except Test.DoesNotExist:
            print('screenplay not found')
            message, status = Messages.notFound.value
            data = message
        
        return Response({"data": data}, status )
    




    # api/views.py
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryItemList(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Item.objects.filter(category=category)
