# sijApp/management/commands/import_currencies.py
from pathlib import Path
import csv

from django.core.management.base import BaseCommand, CommandError
from sijApp.models import Currency

class Command(BaseCommand):
    help = "Import mata uang dari CSV (name, alpha_code, symbol)"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help="Path ke file CSV")
        parser.add_argument(
            "--update",
            action="store_true",
            help="Update baris lama bila alpha_code sudah ada",
        )

    def handle(self, *args, **opts):
        path = Path(opts["csv_path"])
        if not path.exists():
            raise CommandError(f"File {path} tidak ditemukan")

        created, updated = 0, 0
        bulk = []
        with path.open(newline="", encoding="utf-8") as f:
            for row_no, row in enumerate(csv.reader(f), start=1):
                try:
                    name, alpha, symbol = [c.strip() for c in row]
                except ValueError:
                    self.stderr.write(
                        self.style.WARNING(f"Baris {row_no} diabaikan: format tidak valid → {row}")
                    )
                    continue

                if opts["update"]:
                    obj, is_created = Currency.objects.update_or_create(
                        alpha_code=alpha,
                        defaults={"name": name, "symbol": symbol},
                    )
                    created += is_created
                    updated += (not is_created)
                else:
                    bulk.append(Currency(name=name, alpha_code=alpha, symbol=symbol))

        if bulk:
            # ignore_conflicts=True → lewati baris yang alpha_code-nya sudah ada
            Currency.objects.bulk_create(bulk, ignore_conflicts=True)
            created += len(bulk)

        self.stdout.write(self.style.SUCCESS(f"Import selesai: {created} dibuat, {updated} diperbarui."))