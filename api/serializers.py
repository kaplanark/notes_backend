from rest_framework import serializers
from .models import Note
from django.contrib.auth import get_user_model
import random
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "group", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
            "password2": {"style": {"input_type": "password"}},
        }
        read_only_fields = ["group"]

    def get_group(self, obj):
        groups = ["Developer", "Maintainer", "Product owner", "Designer"]
        return random.choice(groups)

    def create(self, validated_data):
        validated_data.pop("password2")
        return User.objects.create_user(**validated_data)

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["img", "title", "text", "color", "categories","show","pinned","archived","trashed","user"]