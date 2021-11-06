import json
import os
import uuid

from django.db import migrations, models


def load_madrid_data(apps, schema_editor):
    file_path = f'{os.path.abspath(os.path.dirname(__name__))}/data/madrid_dea.json'
    with open(file_path, 'r') as madrid_json:
        json_data = json.load(madrid_json)

    dea_device_model = apps.get_model('desfibrimaps', 'DjangoDea')
    for madrid_dea in json_data.get('data'):
        dea_direccion = f'{madrid_dea.get("direccion_via_codigo", "")} {madrid_dea.get("direccion_via_nombre", "no data")}'
        device = dea_device_model.objects.create(
            id=uuid.uuid4(),
            locality=madrid_dea.get('municipio_nombre', 'Madrid'),
            address=dea_direccion,
            device_location=madrid_dea.get('direccion_ubicacion'),
            postal_code=madrid_dea.get('direccion_codigo_postal', "28012"),
            lat=madrid_dea.get('direccion_coordenada_y'),
            long=madrid_dea.get('direccion_coordenada_x'),
            ownership=madrid_dea.get('tipo_titularidad', "Privada"),
        )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoDea',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('locality', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('device_location', models.CharField(blank=True, max_length=300, null=True)),
                ('postal_code', models.CharField(max_length=5)),
                ('lat', models.IntegerField()),
                ('long', models.IntegerField()),
                ('ownership', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'devices',
            },
        ),
        migrations.RunPython(load_madrid_data),
    ]
