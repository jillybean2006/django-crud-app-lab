

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_accessory_alter_feeding_options_alter_feeding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='jellycat',
            name='accessories',
            field=models.ManyToManyField(to='main_app.accessory'),
        ),
    ]