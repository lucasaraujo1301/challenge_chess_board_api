from pieces.models import Color, Piece
from rest_framework import serializers


class ColoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name']


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ['id']
