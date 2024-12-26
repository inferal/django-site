from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order, Product

class Command(BaseCommand):
    """
    Update Order
    """

    def handle(self, *args, **options):
        self.stdout.write("Updates orders")

        order = Order.objects.first()
        if not order:
            self.stdout.write("no order found")
            return

        products = Product.objects.all()

        for product in products:
            order.products.add(product)

        order.save()

        self.stdout.write(self.style.SUCCESS(f"Orders update {order.products.all()} to order {order}"))