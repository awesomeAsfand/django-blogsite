# Generated by Django 4.1.2 on 2022-11-28 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comments_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
