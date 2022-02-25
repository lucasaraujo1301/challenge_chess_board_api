from django.db import migrations
from pieces.models import Color, Piece


def adding_pieces(apps, schema_editor):
    colors = Color.objects.all()
    pieces = Piece.objects.all()

    pieces_to_colors_link = []

    for piece in pieces:
        pieces_to_colors_link.extend([Piece.color.through(piece_id=piece.id, color_id=color.id) for color in colors])

    Piece.color.through.objects.bulk_create(pieces_to_colors_link)


class Migration(migrations.Migration):
    dependencies = [
        ('pieces', '0003_populate_pieces'),
    ]

    operations = [
        migrations.RunPython(adding_pieces),
    ]
