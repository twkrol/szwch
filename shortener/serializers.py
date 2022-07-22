from rest_framework import serializers

from .models import Link, TRACKING_CODE_LENGTH


class LinkShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["target", ]


class LinkResolveSerializer(serializers.ModelSerializer):
    short = serializers.CharField(required=True)

    class Meta:
        model = Link
        fields = ["short", ]
