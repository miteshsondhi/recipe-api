from time import sleep

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        print(self.style.MIGRATE_HEADING('Waiting for database'))
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                print(self.style.MIGRATE_HEADING('Database unavailable, waiting 1 second...'))
                sleep(1)

        print(self.style.SUCCESS('Database available!'))
