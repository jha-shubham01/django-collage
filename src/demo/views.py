from django.shortcuts import render
from rest_framework import serializers
from django.http import JsonResponse
from .collage import create_collage

class MultipleImageSerializer(serializers.Serializer):

    images = serializers.ListField(
        child=serializers.ImageField()
    )


def index(request):
    return render(request, "index.html")


def make_collage(request):

    serializer = MultipleImageSerializer(data=request.FILES or None)
    try:
        serializer.is_valid(raise_exception=True)
    except Exception as e:
        return JsonResponse({"message": "Some error occurred", "details": str(e)}, status=400)
    link = create_collage(serializer.validated_data.get("images"))
    return JsonResponse({"link": link})
