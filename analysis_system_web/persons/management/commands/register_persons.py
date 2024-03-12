from django.core.management.base import BaseCommand
from persons.models import Person


class Command(BaseCommand):
    help = "Regiter persons"

    def handle(self, *args, **options):
        person_1 = Person(name='Ronaldinho', surname='Gaucho', age=30)
        person_1.save()

        person_2 = Person(name='Lionel', surname='Messi', age=36)
        person_2.save() 
            
        self.stdout.write(
            self.style.SUCCESS('Persons created')
        )
