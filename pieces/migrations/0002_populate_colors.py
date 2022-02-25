from django.db import migrations
from pieces.models import Color


def adding_color(apps, schema_editor):
    Color.objects.bulk_create([Color(name='white'),
                               Color(name='black')])


class Migration(migrations.Migration):
    dependencies = [
        ('pieces', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(adding_color),
    ]
