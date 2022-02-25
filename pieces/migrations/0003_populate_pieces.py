from django.db import migrations
from pieces.models import Piece


def adding_pieces(apps, schema_editor):
    pieces_name = ['pawn', 'tower', 'bishop', 'queen', 'king', 'knight']
    pieces_object_list = [Piece(name=piece) for piece in pieces_name]

    Piece.objects.bulk_create(pieces_object_list)


class Migration(migrations.Migration):
    dependencies = [
        ('pieces', '0002_populate_colors'),
    ]

    operations = [
        migrations.RunPython(adding_pieces),
    ]