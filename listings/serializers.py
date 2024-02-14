from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from listings.models import Listing, Location


class LocationSerializer(GeoFeatureModelSerializer):
    geo_field = "location"

    class Meta:
        model = Location
        fields = ["county", "location", "property"]


class ListingSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Listing
        fields = ["name", "price", "date_listed", "location"]
        read_only_fields = ["date_listed"]

        def create(self, validated_data):
            location_data = validated_data.pop("location")
            listing = Listing.objects.create(**validated_data)
            Location.objects.create(property=listing, **location_data)
            return listing

        def update(self, instance, validated_data):
            location_data = validated_data.pop("location")
            location = instance.location

            instance.name = validated_data.get("name", instance.name)
            instance.price = validated_data.get("price", instance.price)
            instance.save()
            location.county = location_data.get("county", location.county)
            location.location = location_data.get(
                "location", location.location)
            location.save()
            return instance
