# Generated by Django 5.1.2 on 2024-11-12 00:24

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


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
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='home_cpusoc_name_84fafa_idx')],
            },
        ),
        migrations.CreateModel(
            name='FormFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='home_formfa_name_b3e50f_idx')],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='home_manufa_name_42441b_idx')],
            },
        ),
        migrations.CreateModel(
            name='Microarchitecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='home_microa_name_aa7616_idx')],
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('cpu_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('socket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cpusockettype')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.manufacturer')),
                ('microarchitecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.microarchitecture')),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('motherboard_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('memory_slots', models.IntegerField(choices=[(2, '2 Slots'), (4, '4 Slots')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('max_memory_capacity', models.IntegerField(default=128, validators=[django.core.validators.MinValueValidator(1)])),
                ('cpu_socket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cpusockettype')),
                ('form_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.formfactor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='CPUMotherboardCompatibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cpu')),
                ('motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.motherboard')),
            ],
        ),
        migrations.AddField(
            model_name='cpu',
            name='motherboards',
            field=models.ManyToManyField(through='home.CPUMotherboardCompatibility', to='home.motherboard'),
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
            name='Build',
            fields=[
                ('build_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Default Build Name', max_length=100, unique=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('cpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cpu')),
                ('motherboard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.motherboard')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('ram_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='BuildRAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.build')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ram')),
            ],
        ),
        migrations.AddField(
            model_name='build',
            name='ram',
            field=models.ManyToManyField(blank=True, through='home.BuildRAM', to='home.ram'),
        ),
        migrations.CreateModel(
            name='RAMCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=10)),
            ],
            options={
                'indexes': [models.Index(fields=['capacity'], name='home_ramcap_capacit_e9fc84_idx')],
            },
        ),
        migrations.AddField(
            model_name='ram',
            name='ram_capacity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ramcapacity'),
        ),
        migrations.CreateModel(
            name='RAMNumberOfModules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_modules', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'indexes': [models.Index(fields=['number_of_modules'], name='home_ramnum_number__9edd58_idx')],
            },
        ),
        migrations.AddField(
            model_name='ram',
            name='ram_number_of_modules',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ramnumberofmodules'),
        ),
        migrations.CreateModel(
            name='RAMSpeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(800), django.core.validators.MaxValueValidator(5000)])),
            ],
            options={
                'indexes': [models.Index(fields=['speed'], name='home_ramspe_speed_d4e099_idx')],
            },
        ),
        migrations.AddField(
            model_name='ram',
            name='ram_speed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ramspeed'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='supported_ram_speeds',
            field=models.ManyToManyField(to='home.ramspeed'),
        ),
        migrations.CreateModel(
            name='RAMType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['type'], name='home_ramtyp_type_eddd11_idx')],
            },
        ),
        migrations.AddField(
            model_name='ram',
            name='ram_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ramtype'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='supported_ram_types',
            field=models.ManyToManyField(to='home.ramtype'),
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0.0)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('storage_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('form_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.formfactor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='BuildStorageConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='Secondary', max_length=50)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.build')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.storage')),
            ],
        ),
        migrations.AddField(
            model_name='build',
            name='storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.storage'),
        ),
        migrations.AddField(
            model_name='build',
            name='storages',
            field=models.ManyToManyField(related_name='build_storages', through='home.BuildStorageConfiguration', to='home.storage'),
        ),
        migrations.CreateModel(
            name='StorageCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['capacity'], name='home_storag_capacit_eb0d08_idx')],
            },
        ),
        migrations.AddField(
            model_name='storage',
            name='capacity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.storagecapacity'),
        ),
        migrations.CreateModel(
            name='StorageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['type'], name='home_storag_type_7aceb9_idx')],
            },
        ),
        migrations.AddField(
            model_name='storage',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.storagetype'),
        ),
        migrations.CreateModel(
            name='SupportedRAMConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supported', models.BooleanField(default=True)),
                ('motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.motherboard')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ram')),
            ],
        ),
        migrations.AddField(
            model_name='motherboard',
            name='rams',
            field=models.ManyToManyField(through='home.SupportedRAMConfiguration', to='home.ram'),
        ),
        migrations.CreateModel(
            name='SupportedStorageConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slots', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.motherboard')),
                ('storage_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.storagetype')),
            ],
        ),
        migrations.AddField(
            model_name='motherboard',
            name='supported_storage_types',
            field=models.ManyToManyField(through='home.SupportedStorageConfiguration', to='home.storagetype'),
        ),
        migrations.AddIndex(
            model_name='cpumotherboardcompatibility',
            index=models.Index(fields=['cpu'], name='home_cpumot_cpu_id_459389_idx'),
        ),
        migrations.AddIndex(
            model_name='cpumotherboardcompatibility',
            index=models.Index(fields=['motherboard'], name='home_cpumot_motherb_0ac58f_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='cpumotherboardcompatibility',
            unique_together={('cpu', 'motherboard')},
        ),
        migrations.AddIndex(
            model_name='cpu',
            index=models.Index(fields=['name'], name='home_cpu_name_a9fc68_idx'),
        ),
        migrations.AddIndex(
            model_name='cpu',
            index=models.Index(fields=['manufacturer'], name='home_cpu_manufac_d83bc1_idx'),
        ),
        migrations.AddIndex(
            model_name='cpu',
            index=models.Index(fields=['microarchitecture'], name='home_cpu_microar_230d1e_idx'),
        ),
        migrations.AddIndex(
            model_name='cpu',
            index=models.Index(fields=['socket_type'], name='home_cpu_socket__8ceebd_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['profile_name'], name='home_profil_profile_3b98e2_idx'),
        ),
        migrations.AddIndex(
            model_name='ram',
            index=models.Index(fields=['name'], name='home_ram_name_f42f49_idx'),
        ),
        migrations.AddIndex(
            model_name='ram',
            index=models.Index(fields=['manufacturer'], name='home_ram_manufac_aeb502_idx'),
        ),
        migrations.AddIndex(
            model_name='buildstorageconfiguration',
            index=models.Index(fields=['build'], name='home_builds_build_i_b69dad_idx'),
        ),
        migrations.AddIndex(
            model_name='buildstorageconfiguration',
            index=models.Index(fields=['storage'], name='home_builds_storage_9f0d3e_idx'),
        ),
        migrations.AddConstraint(
            model_name='buildstorageconfiguration',
            constraint=models.CheckConstraint(condition=models.Q(('role__in', ['Primary', 'Secondary'])), name='role_valid'),
        ),
        migrations.AlterUniqueTogether(
            name='buildstorageconfiguration',
            unique_together={('build', 'storage')},
        ),
        migrations.AddIndex(
            model_name='build',
            index=models.Index(fields=['name'], name='home_build_name_4c33de_idx'),
        ),
        migrations.AddConstraint(
            model_name='build',
            constraint=models.CheckConstraint(condition=models.Q(('is_complete__in', [True, False])), name='is_complete_valid'),
        ),
        migrations.AddIndex(
            model_name='storage',
            index=models.Index(fields=['name'], name='home_storag_name_467eb4_idx'),
        ),
        migrations.AddIndex(
            model_name='storage',
            index=models.Index(fields=['manufacturer'], name='home_storag_manufac_4ea7c7_idx'),
        ),
        migrations.AddIndex(
            model_name='storage',
            index=models.Index(fields=['form_factor'], name='home_storag_form_fa_c5d0e4_idx'),
        ),
        migrations.AddIndex(
            model_name='storage',
            index=models.Index(fields=['type'], name='home_storag_type_id_952f73_idx'),
        ),
        migrations.AddIndex(
            model_name='supportedramconfiguration',
            index=models.Index(fields=['motherboard'], name='home_suppor_motherb_490317_idx'),
        ),
        migrations.AddIndex(
            model_name='supportedramconfiguration',
            index=models.Index(fields=['ram'], name='home_suppor_ram_id_897da4_idx'),
        ),
        migrations.AddConstraint(
            model_name='supportedramconfiguration',
            constraint=models.CheckConstraint(condition=models.Q(('supported__in', [True, False])), name='supported_valid'),
        ),
        migrations.AlterUniqueTogether(
            name='supportedramconfiguration',
            unique_together={('motherboard', 'ram')},
        ),
        migrations.AddIndex(
            model_name='supportedstorageconfiguration',
            index=models.Index(fields=['motherboard'], name='home_suppor_motherb_499d15_idx'),
        ),
        migrations.AddIndex(
            model_name='supportedstorageconfiguration',
            index=models.Index(fields=['storage_type'], name='home_suppor_storage_67f8f5_idx'),
        ),
        migrations.AddConstraint(
            model_name='supportedstorageconfiguration',
            constraint=models.CheckConstraint(condition=models.Q(('slots__gte', 0)), name='slots_positive'),
        ),
        migrations.AlterUniqueTogether(
            name='supportedstorageconfiguration',
            unique_together={('motherboard', 'storage_type')},
        ),
        migrations.AddIndex(
            model_name='motherboard',
            index=models.Index(fields=['name'], name='home_mother_name_ebcba6_idx'),
        ),
        migrations.AddIndex(
            model_name='motherboard',
            index=models.Index(fields=['manufacturer'], name='home_mother_manufac_e8261a_idx'),
        ),
        migrations.AddIndex(
            model_name='motherboard',
            index=models.Index(fields=['cpu_socket_type'], name='home_mother_cpu_soc_fed458_idx'),
        ),
        migrations.AddIndex(
            model_name='motherboard',
            index=models.Index(fields=['form_factor'], name='home_mother_form_fa_64fd34_idx'),
        ),
        migrations.AddConstraint(
            model_name='motherboard',
            constraint=models.CheckConstraint(condition=models.Q(('max_memory_capacity__gte', 0)), name='max_memory_capacity_positive'),
        ),
    ]
