from django.core.management.base import BaseCommand
from monitors.models import Monitor


class Command(BaseCommand):
    help = "Regiter monitors"

    def handle(self, *args, **options):
        samsungx1s = Monitor(device='X1-S', version='1.1', type='HEART_RATE')
        samsungx1s.save()
        
        polarmx2 = Monitor(device='X1-S', version='1.0', type='HEART_RATE')
        polarmx2.save()

        samsungbpa = Monitor(device='BPA', version='1.3', type='BLOOD_PRESSURE')
        samsungbpa.save()
            
        self.stdout.write(
            self.style.SUCCESS('Monitors created')
        )
