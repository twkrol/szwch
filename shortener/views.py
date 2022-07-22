from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import LinkResolveSerializer, LinkShortenSerializer
from .models import Link


@api_view(['POST'])
def shorten(request):
    '''Metoda tworzy skrót dla url przesłanego w JSON jako parametr target, np.:
        {"target":"https://ubuntu.com"}
    '''
    serializer = LinkShortenSerializer(data=request.data)
    if serializer.is_valid():
        link = serializer.save()
        result = f'{request.build_absolute_uri(link.short)}'
        return Response(result)
    else:
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def resolve(request):
    '''Metoda znajduje url dla skrótu podanego w JSON jako parametr short, np.:
        {"short":"http://127.0.0.1:8000/shusxisd"}
    '''
    serializer = LinkResolveSerializer(data=request.data)
    if serializer.is_valid():
        short_code = serializer.validated_data.get("short").partition(request.build_absolute_uri("/"))[2]
        if link := Link.objects.filter(short=short_code).first():
            return Response(link.target)
        else:
            return Response(f"Link {short_code} not found", status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
