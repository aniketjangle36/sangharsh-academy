from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='AcademyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_mr', models.CharField(default='संघर्ष करिअर अकॅडमी फुलंब्री', max_length=200, verbose_name='नाव (मराठी)')),
                ('name_en', models.CharField(default='Sangharsh Career Academy Fulambri', max_length=200, verbose_name='Name (English)')),
                ('tagline_mr', models.CharField(default='आर्मी व पोलीस भरती पूर्व प्रशिक्षण केंद्र', max_length=300, verbose_name='टॅगलाइन (मराठी)')),
                ('tagline_en', models.CharField(default='Army & Police Pre-Recruitment Training Centre', max_length=300, verbose_name='Tagline (English)')),
                ('address_mr', models.TextField(default='ता. फुलंब्री, जि. छत्रपती संभाजीनगर, महाराष्ट्र', verbose_name='पत्ता (मराठी)')),
                ('address_en', models.TextField(default='Tal. Fulambri, Dist. Chhatrapati Sambhajinagar, Maharashtra', verbose_name='Address (English)')),
                ('phone', models.CharField(default='+91 XXXXX XXXXX', max_length=20, verbose_name='फोन')),
                ('whatsapp', models.CharField(default='+91XXXXXXXXXX', max_length=20, verbose_name='WhatsApp')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='ईमेल')),
                ('established_year', models.IntegerField(default=2018, verbose_name='स्थापना वर्ष')),
                ('logo', models.ImageField(blank=True, upload_to='academy/', verbose_name='लोगो')),
                ('hero_image', models.ImageField(blank=True, upload_to='academy/', verbose_name='Hero Image')),
                ('about_image', models.ImageField(blank=True, upload_to='academy/', verbose_name='About Image')),
                ('about_text_mr', models.TextField(blank=True, verbose_name='आमच्याविषयी (मराठी)')),
                ('about_text_en', models.TextField(blank=True, verbose_name='About Us (English)')),
                ('google_map_embed', models.TextField(blank=True, verbose_name='Google Map Embed Code')),
                ('students_selected', models.IntegerField(default=500, verbose_name='एकूण निवड')),
                ('army_selected', models.IntegerField(default=50, verbose_name='आर्मी निवड')),
                ('police_selected', models.IntegerField(default=200, verbose_name='पोलीस निवड')),
                ('meta_keywords', models.CharField(blank=True, default='army bharti, police bharti, Fulambri, संघर्ष अकॅडमी', max_length=500)),
                ('meta_description', models.TextField(blank=True)),
            ],
            options={'verbose_name': 'अकॅडमी माहिती', 'verbose_name_plural': 'अकॅडमी माहिती'},
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_mr', models.CharField(max_length=200, verbose_name='कोर्स नाव (मराठी)')),
                ('name_en', models.CharField(max_length=200, verbose_name='Course Name (English)')),
                ('category', models.CharField(choices=[('army', 'आर्मी (Army)'), ('police', 'पोलीस (Police)')], max_length=20, verbose_name='प्रकार')),
                ('duration', models.CharField(choices=[('3months', '3 महिने'), ('6months', '6 महिने'), ('1year', '1 वर्ष'), ('2years', '2 वर्षे')], max_length=20, verbose_name='कालावधी')),
                ('fee', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='फी (₹)')),
                ('description_mr', models.TextField(blank=True, verbose_name='वर्णन (मराठी)')),
                ('description_en', models.TextField(blank=True, verbose_name='Description (English)')),
                ('eligibility_mr', models.TextField(blank=True, verbose_name='पात्रता (मराठी)')),
                ('eligibility_en', models.TextField(blank=True, verbose_name='Eligibility (English)')),
                ('subjects', models.TextField(blank=True, verbose_name='विषय')),
                ('image', models.ImageField(blank=True, upload_to='courses/', verbose_name='फोटो')),
                ('is_active', models.BooleanField(default=True, verbose_name='सक्रिय')),
                ('order', models.IntegerField(default=0, verbose_name='क्रम')),
            ],
            options={'verbose_name': 'कोर्स', 'verbose_name_plural': 'कोर्सेस', 'ordering': ['order', 'name_en']},
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='नाव')),
                ('mobile', models.CharField(max_length=15, verbose_name='मोबाईल')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='ईमेल')),
                ('message', models.TextField(verbose_name='संदेश')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={'verbose_name': 'संपर्क संदेश', 'verbose_name_plural': 'संपर्क संदेश', 'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='शीर्षक')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='फोटो')),
                ('category', models.CharField(choices=[('training', 'Training'), ('events', 'Events'), ('results', 'Results'), ('infrastructure', 'Infrastructure')], default='training', max_length=30, verbose_name='श्रेणी')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'verbose_name': 'गॅलरी फोटो', 'verbose_name_plural': 'गॅलरी', 'ordering': ['-uploaded_at']},
        ),
        migrations.CreateModel(
            name='SuccessStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='नाव')),
                ('photo', models.ImageField(blank=True, upload_to='success/', verbose_name='फोटो')),
                ('rank_post', models.CharField(max_length=100, verbose_name='पद / रँक')),
                ('category', models.CharField(choices=[('army', 'Army'), ('police', 'Police')], max_length=20, verbose_name='प्रकार')),
                ('year', models.IntegerField(verbose_name='वर्ष')),
                ('village', models.CharField(blank=True, max_length=100, verbose_name='गाव')),
                ('testimonial_mr', models.TextField(blank=True, verbose_name='अभिप्राय (मराठी)')),
                ('testimonial_en', models.TextField(blank=True, verbose_name='Testimonial (English)')),
                ('is_featured', models.BooleanField(default=False, verbose_name='फीचर')),
            ],
            options={'verbose_name': 'यशोगाथा', 'verbose_name_plural': 'यशोगाथा', 'ordering': ['-year', 'name']},
        ),
    ]
