# Generated by Django 3.1.5 on 2021-05-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('time', models.CharField(default='morning', max_length=100)),
                ('joinplan', models.BooleanField(default=False)),
                ('BMI', models.FloatField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
