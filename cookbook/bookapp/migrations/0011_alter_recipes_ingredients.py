# Generated by Django 4.0.4 on 2022-05-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0010_rename_count_ingredient_recipe_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='ingredients',
            field=models.ManyToManyField(blank=True, null=True, through='bookapp.Ingredient_Recipe', to='bookapp.ingredient'),
        ),
    ]