# Generated by Django 4.2.5 on 2023-10-03 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_student_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
        ),
        migrations.CreateModel(
            name='ProjectsInPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.project')),
            ],
        ),
    ]
