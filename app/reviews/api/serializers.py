from rest_framework.serializers import ModelSerializer

from reviews.models import  Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'pk',
            'name',
            'site',
            'date',
            'date_exp',
            'rating',
            'report',
            'access',
        ]

    # converts to JSON
    # validations for passed data
