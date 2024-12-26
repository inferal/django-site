from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order

class Command(BaseCommand):
    """
    Creates Order
    """

    def handle(self, *args, **options):
        self.stdout.write("Create orders")

        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_address="Ul. Pupkina, d 8",
            promocode="SALE12345",
            user=user,
        )

        self.stdout.write(f"Orders created {order}")