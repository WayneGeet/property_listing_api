from django.contrib import admin
from django.urls import path
from listings.views import list_create_listings, ListingDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path("listings/", list_create_listings),
    path("listing/<int:pk>/", ListingDetails.as_view())
]
