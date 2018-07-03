from rest_framework import generics

from reviews.models import Review
from .serializers import ReviewSerializer

class ReviewGetView(generics.RetrieveAPIView): # Detail View
    lookup_field = 'pk'
    serializer_class = ReviewSerializer
    # queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.all()

