import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipamentos', '0002_alter_categoria_options_alter_equipamento_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Solicitação')),
                ('data_emprestimo', models.DateTimeField(blank=True, null=True, verbose_name='Data do Empréstimo')),
                ('data_devolucao_prevista', models.DateField(verbose_name='Data de Devolução Prevista')),
                ('data_devolucao_real', models.DateTimeField(blank=True, null=True, verbose_name='Data de Devolução Real')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('aprovado', 'Aprovado'), ('negado', 'Negado'), ('ativo', 'Ativo'), ('finalizado', 'Finalizado'), ('atrasado', 'Atrasado')], default='pendente', max_length=20, verbose_name='Status')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações')),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipamentos.equipamento', verbose_name='Equipamento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Empréstimo',
                'verbose_name_plural': 'Empréstimos',
                'ordering': ['-data_solicitacao'],
            },
        ),
    ]
