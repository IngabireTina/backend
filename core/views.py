from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializers
from .models import Post
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class TestView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        # data = {
        #     'name': 'John',
        #     'age': '23'
        # }
        qs = Post.objects.all()
        serializer = PostSerializers(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# def test_view(request):
#     data = {
#         'name': 'John',
#         'age': '23'
#     }
#     return JsonResponse(data)
