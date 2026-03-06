from rest_framework import serializers
from .models import Book
from .models import Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

 def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author

        fields = '__all__'
