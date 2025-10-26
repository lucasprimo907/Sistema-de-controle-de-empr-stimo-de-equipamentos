import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='equipamento',
            options={'verbose_name': 'Equipamento', 'verbose_name_plural': 'Equipamentos'},
        ),
        migrations.AddField(
            model_name='equipamento',
            name='data_aquisicao',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data de Aquisição'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome da Categoria'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipamentos.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='disponivel',
            field=models.BooleanField(default=True, verbose_name='Disponível?'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome do Equipamento'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='numero_serie',
            field=models.CharField(max_length=100, unique=True, verbose_name='Número de Série'),
        ),
    ]
