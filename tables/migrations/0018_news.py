# Generated by Django 3.0.5 on 2020-11-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0017_auto_20201029_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='新闻标题')),
                ('is_show', models.BooleanField(default=1, verbose_name='是否显示')),
                ('text_attached', models.FileField(null=True, upload_to='news/text_part/%Y/%m', verbose_name='正文附件')),
                ('image_attached', models.FileField(null=True, upload_to='news/image/%Y/%m', verbose_name='图片附件')),
                ('text_create_time', models.DateTimeField(null=False, verbose_name='正文发布时间')),
                ('image_create_time', models.DateTimeField(null=True, verbose_name='图片上传时间')),
            ],
            options={
                'verbose_name': '新闻管理',
            },
        ),
    ]