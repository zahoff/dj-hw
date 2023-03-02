from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20230303_0615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relationship',
            options={'ordering': ['-is_main'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
    ]