from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CPUSocketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Microarchitecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RAMCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RAMNumberOfModules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_modules', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RAMSpeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary key=True, serialize=False, verbose name='ID')),
                ('speed', models.CharField(max length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RAMType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary key=True, serialize=False, verbose name='ID')),
                ('type', models.CharField(max length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StorageCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary key=True, serialize=False, verbose name='ID')),
                ('capacity', models.CharField(max length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StorageFormFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary key=True, serialize=False, verbose name='ID')),
                ('name', models.CharField(max length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StorageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary key=True, serialize=False, verbose name='ID')),
                ('type', models.CharField(max length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('storage_id', models.AutoField(primary key=True, serialize=False)),
                ('name', models.CharField(max length=100)),
                ('storage_capacity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.storagecapacity')),
                ('storage_form_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.storageformfactor')),
                ('storage_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.storagetype')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary key=True, serialize=False, verbose name='ID')),
                ('total_price', models.FloatField(default=0.0)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('ram_id', models.AutoField(primary key=True, serialize=False)),
                ('ram_capacity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ramcapacity')),
                ('ram_number_of_modules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ramnumberofmodules')),
                ('ram_speed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ramspeed')),
                ('ram_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ramtype')),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('motherboard_id', models.AutoField(primary key=True, serialize=False)),
                ('name', models.CharField(max length=100)),
                ('memory_slots', models.IntegerField(choices=[(2, '2 Slots'), (4, '4 Slots')])),
                ('max_memory_capacity', models.IntegerField(default=128)),
                ('cpu_socket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cpusockettype')),
                ('motherboard_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.manufacturer')),
                ('storage_form_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.storageformfactor')),
                ('supported_ram_speeds', models.ManyToManyField(to='home.ramspeed')),
                ('supported_ram_types', models.ManyToManyField(to='home.ramtype')),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('cpu_id', models.AutoField(primary key=True, serialize=False)),
                ('cpu_name', models.CharField(max length=100)),
                ('cpu_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.manufacturer')),
                ('cpu_microarchitecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.microarchitecture')),
                ('socket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cpusockettype')),
            ],
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary key=True, serialize=False, verbose name='ID')),
                ('is_complete', models.BooleanField(default=False)),
                ('cpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cpu')),
                ('motherboard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.motherboard')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
                ('ram', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.ram')),
                ('storage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.storage')),
            ],
        ),
        migrations.CreateModel(
            name='BuildRAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary key=True, serialize=False, verbose name='ID')),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.build')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ram')),
            ],
        ),
        migrations.AddField(
            model_name='build',
            name='cpu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cpu'),
        ),
        migrations.AddField(
            model_name='build',
            name='motherboard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.motherboard'),
        ),
        migrations.AddField(
            model_name='build',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
        migrations.AddField(
            model_name='build',
            name='ram',
            field=models.ManyToManyField(blank=True, through='home.BuildRAM', to='home.ram'),
        ),
        migrations.AddField(
            model_name='build',
            name='storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.storage'),
        ),
    ]
