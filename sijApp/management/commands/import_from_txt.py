from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

class Command(BaseCommand):
    help = 'Import data from txt file into specified model (single field only)'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='Path to the .txt file')
        parser.add_argument('app_label', type=str, help='Django app label where the model is located')
        parser.add_argument('model_name', type=str, help='Target model name (case-insensitive)')
        parser.add_argument('field_name', type=str, help='Field name to insert data into')

    def handle(self, *args, **options):
        filepath = options['filepath']
        app_label = options['app_label']
        model_name = options['model_name']
        field_name = options['field_name']

        # Coba ambil model
        try:
            model = apps.get_model(app_label, model_name)
        except LookupError:
            raise CommandError(f"Model '{model_name}' tidak ditemukan di app '{app_label}'")

        # Coba buka file
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError:
            raise CommandError(f"File '{filepath}' tidak ditemukan")

        count = 0
        for line in lines:
            value = line.strip()
            if value:
                obj, created = model.objects.get_or_create(**{field_name: value})
                if created:
                    count += 1

        self.stdout.write(self.style.SUCCESS(f'Berhasil mengimpor {count} entri ke model {model_name}.'))