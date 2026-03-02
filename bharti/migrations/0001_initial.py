from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Bharti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='शीर्षक')),
                ('url', models.URLField(unique=True, verbose_name='लिंक')),
                ('category', models.CharField(
                    choices=[
                        ('army', 'आर्मी / Army'),
                        ('police', 'पोलीस / Police'),
                        ('maha_police', 'महाराष्ट्र पोलीस'),
                        ('general', 'सामान्य / General'),
                    ],
                    default='general',
                    max_length=20,
                    verbose_name='श्रेणी',
                )),
                ('short_desc', models.TextField(blank=True, verbose_name='थोडक्यात माहिती')),
                ('last_date', models.DateField(blank=True, null=True, verbose_name='शेवटची तारीख')),
                ('scraped_at', models.DateTimeField(auto_now_add=True, verbose_name='स्क्रेप वेळ')),
                ('is_active', models.BooleanField(default=True, verbose_name='सक्रिय')),
            ],
            options={'verbose_name': 'भरती', 'verbose_name_plural': 'भरती अपडेट्स', 'ordering': ['-scraped_at']},
        ),
    ]
