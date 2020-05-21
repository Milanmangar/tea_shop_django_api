from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from items.models import Items
from items.serializers import ItemsSerializer
from django.conf import settings
from rest_framework import status


class HomeView(viewsets.ViewSet):
    """
    View for the items home page
    """
    def list(self, request):
        """ to get all the items"""
        response_dict= self.list_of_items()
        return Response({"result": {"product_data": response_dict}}, status.HTTP_200_OK)

    @staticmethod
    def list_of_items():
        """ helper function to lists all the items
        args : None
        returns :
            list of dictionary of items
        """
        queryset = Items.objects.filter(status='active').order_by('-added_date')
        serializer = ItemsSerializer(queryset, many=True)
        response = serializer.data
        if settings.DEBUG:
            for items_list in response:
                for k, v in items_list.items():
                    if k == 'image':
                        items_list.update(image='http://192.168.1.108:8000' + v)
                        break
        return response

    def create(self, request):
        """to add new item"""
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = "Item Added successfully!"
            response=self.list_of_items()
            return Response({"result": {"product_data": response, "message": message}}, 201)
        error_messages = "Either you have entered invalid input or Server is down!"
        return Response({"result": {'message': error_messages}}, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """ to retrieve specfic item """
        queryset = Items.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemsSerializer(item)
        response = serializer.data
        response.update(image='http://192.168.1.108:8000' + response['image'])
        return Response({'result': {'item_detail': response}}, status.HTTP_200_OK)
