from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from django.http import JsonResponse
import json

class MultipleImageSerializer(serializers.Serializer):

    images = serializers.ListField(
        child=serializers.ImageField()
    )


def index(request):
    return render(request, "index.html")


def make_collage(request):
    # images = request.FILES.get("images")
    serializer = MultipleImageSerializer(data=request.FILES or None)
    serializer.is_valid(raise_exception=True)
    print(serializer.validated_data.get("images"))
    return JsonResponse({"message": "Success"})
