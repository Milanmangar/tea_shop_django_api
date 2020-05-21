from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from items.models import Items
from items.serializers import ItemsSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile
from PIL import Image
from django.shortcuts import get_object_or_404


class ItemsApiTests(TestCase):
    """ test the private ingredients api """
    def setUp(self):
        # items_url = reverse('items')
        self.items_url = '/api/items/'
        image = Image.new('RGB', (100, 100))
        self.image1 = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(self.image1)
        self.image1.seek(0)

        self.image2 = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(self.image2)
        self.image2.seek(0)

        self.tem_img1 = tempfile.NamedTemporaryFile(suffix=".jpg").name
        self.tem_img2 = tempfile.NamedTemporaryFile(suffix=".jpg").name

        self.client = APIClient()


    def test_retrive_items_list(self):
        """ test retrieving the list of ingredients """
        Items.objects.create(name="Green Tea", description="Refreshing and Healthy Tea", price=20, image=self.tem_img1)
        Items.objects.create(name="Egg Roll", description="Egg with roti and veggies", price=40, image=self.tem_img2)
        res = self.client.get(self.items_url)
        all_items = Items.objects.all().order_by('-added_date')
        serializer = ItemsSerializer(all_items, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {"result":{"product_data":serializer.data}})


    def test_items_successfull(self):
        """ test to a add new item """
        payload = {"name": "Green Tea", "description":"Refreshing and Healthy Tea", "price":20, "image":self.image1}
        res = self.client.post(self.items_url, payload, format='multipart')
        exists = Items.objects.filter(
            name=payload['name'],
        ).exists()
        self.assertTrue(exists)

    def test_retrive_one_items(self):
        """ retrieving the one of item from two """
        item1 = Items.objects.create(name="Green Tea", description="Refreshing and Healthy Tea", price=20, image=self.tem_img1)
        item2 = Items.objects.create(name="Egg Roll", description="Egg with roti and veggies", price=40, image=self.tem_img2)
        pk = item1.id
        res = self.client.get(self.items_url+ f'{pk}/')
        queryset = Items.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemsSerializer(item)
        response = serializer.data
        response.update(image='http://192.168.1.108:8000' + response['image'])
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {"result":{"item_detail":response}})
