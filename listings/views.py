from .serializers import ListingSerializer, LocationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from listings.models import Listings, Location
from rest_framework import status
from django.http import Http404


@api_view(['GET', 'POST'])
def list_create_listings(request):
    if request.method == 'GET':
        listings = Listings.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        listings = request.data
        serializer = ListingSerializer(data=listings)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListingDetails(APIView):
    def get_object(self, pk):
        try:
            return Listings.objects.get(pk=pk)
        except Listings.DoesNotExist:
            raise Http404

    def get(self, get, pk):
        listing = self.get_object(pk)
        serializer = ListingSerializer(listing, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
