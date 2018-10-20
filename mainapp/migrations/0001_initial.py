# Generated by Django 2.0.2 on 2018-10-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bottom_footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_1', models.CharField(max_length=128, verbose_name='#1 item')),
                ('item_2', models.CharField(max_length=128, verbose_name='#2 item')),
                ('item_3', models.CharField(max_length=128, verbose_name='#3 item')),
            ],
            options={
                'verbose_name': 'Bottom footer',
                'verbose_name_plural': 'Bottom footer',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('is_paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '1.Consultation',
                'verbose_name_plural': '1.Consultations',
            },
        ),
        migrations.CreateModel(
            name='Form_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=128, verbose_name='Name of the sections')),
                ('price', models.IntegerField(default=50)),
            ],
            options={
                'verbose_name': 'ConsultationOrder',
                'verbose_name_plural': '6.ConsultationOrders',
            },
        ),
        migrations.CreateModel(
            name='MpHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytle_1', models.CharField(max_length=128, verbose_name='First element title')),
                ('vallue1', models.CharField(max_length=128, verbose_name='First element vallue')),
                ('tytle_2', models.CharField(max_length=128, verbose_name='Second element title')),
                ('vallue2', models.CharField(max_length=128, verbose_name='Second element vallue')),
                ('tytle_3', models.CharField(max_length=128, verbose_name='Third element title')),
                ('vallue3', models.CharField(max_length=128, verbose_name='Third element vallue')),
                ('tytle_4', models.CharField(max_length=128, verbose_name='Fourth element title')),
                ('vallue4', models.CharField(max_length=128, verbose_name='Fourth element vallue')),
            ],
            options={
                'verbose_name': 'Header vallue',
                'verbose_name_plural': 'Header vallue',
            },
        ),
        migrations.CreateModel(
            name='MpHeadBlock1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=128, verbose_name='Main title')),
                ('flink_name', models.CharField(max_length=128, verbose_name='First link name')),
                ('flink_url', models.CharField(max_length=128, verbose_name='First link url')),
                ('slink_name', models.CharField(max_length=128, verbose_name='Second link name')),
                ('slink_url', models.CharField(max_length=128, verbose_name='Second link url')),
            ],
            options={
                'verbose_name': 'Top slider',
                'verbose_name_plural': 'Top slider',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='News title')),
                ('date', models.DateField(auto_now=True)),
                ('short_desc', models.TextField(verbose_name='Short description')),
                ('full_desc', models.TextField(verbose_name='Short description')),
                ('image', models.ImageField(upload_to='', verbose_name='News image')),
                ('on_main_page', models.BooleanField(default=False, verbose_name='On main page?')),
            ],
            options={
                'verbose_name': '4.News',
                'verbose_name_plural': '4.News',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='News title')),
                ('link', models.CharField(max_length=128, verbose_name='Link name')),
                ('full_desc', models.TextField(verbose_name='Short description')),
            ],
            options={
                'verbose_name': '5.Page',
                'verbose_name_plural': '5.Pages',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Review title')),
                ('text_1', models.TextField(verbose_name='Text 1')),
                ('text_2', models.TextField(verbose_name='Text 2')),
                ('author_name', models.CharField(max_length=128, verbose_name='Author name')),
                ('author_img', models.ImageField(upload_to='', verbose_name='Author img 120x120')),
            ],
            options={
                'verbose_name': '3.Review',
                'verbose_name_plural': '3.Reviews on the main page',
            },
        ),
        migrations.CreateModel(
            name='Scroll_menu_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=128, verbose_name='Name of the item')),
                ('s_text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Scroll menu section',
                'verbose_name_plural': 'Scroll menu sections',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_title', models.CharField(max_length=128, verbose_name=' Service title')),
                ('s_shortdesc', models.TextField(verbose_name=' Service short description')),
                ('s_desc', models.TextField(verbose_name=' Service full description')),
                ('mp_icon', models.ImageField(upload_to='', verbose_name='Icon for Mainpage')),
                ('sp_icon', models.FileField(upload_to='', verbose_name='Icon for Service page')),
            ],
            options={
                'verbose_name': '2.Service',
                'verbose_name_plural': '2.Services`',
            },
        ),
        migrations.CreateModel(
            name='Services_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_title', models.CharField(max_length=128, verbose_name=' Main page< first service title')),
                ('s_title', models.CharField(max_length=128, verbose_name=' Main page< second service title')),
                ('link', models.CharField(max_length=30, verbose_name=' Main page< name link')),
            ],
            options={
                'verbose_name': 'Service section',
                'verbose_name_plural': 'Service section',
            },
        ),
        migrations.CreateModel(
            name='Slider2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='News title')),
                ('url', models.CharField(max_length=128, verbose_name='Link address')),
                ('full_desc', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_text', models.TextField(verbose_name='Ticker text')),
            ],
            options={
                'verbose_name': 'Ticker',
                'verbose_name_plural': 'Tickers',
            },
        ),
    ]
