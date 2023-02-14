import csv

from django.core.management.base import BaseCommand
from pokeapi.models import Pokemon


class Command(BaseCommand):
    help = "Load initial Pokemon from CSV file provided by Kaggle"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):

        columns = ["creature_id", "name", "primary_type",
                   "secondary_type", "total", "hp", "attack", "defense",
                   "special_attack", "special_defense", "speed",
                   "generation", "legendary"]

        to_create = []

        with open(options["file_path"], "r") as infile:
            reader = csv.reader(infile)
            count = 0

            for row in reader:
                count += 1
                if count == 1:
                    continue

                ready_row = dict(zip(columns, row))
                ready_row["legendary"] = ready_row["legendary"].lower() == "true"
                to_create.append(Pokemon(**ready_row))

            Pokemon.objects.bulk_create(to_create)
