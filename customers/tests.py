from django.test import TestCase
from customers.models import Customer


class CustomerModelTests(TestCase):
    def test_customer_creation(self):
        customer = Customer.objects.create(
            name="Charlie Shell",
            email="charlie@saltandshell.com",
            phone_number="07700 900123"
        )

        self.assertEqual(customer.name, "Charlie Shell")
        self.assertEqual(customer.email, "charlie@saltandshell.com")
        self.assertEqual(customer.phone_number, "07700 900123")
        self.assertIsNotNone(customer.created_at)

    def test_customer_str_representation(self):
        customer = Customer.objects.create(
            name="Nina Coral",
            email="nina@saltandshell.com",
            phone_number="07700 900456"
        )
        expected_str = "Nina Coral (nina@saltandshell.com, 07700 900456)"
        self.assertEqual(str(customer), expected_str)

    def test_email_uniqueness_constraint(self):
        Customer.objects.create(
            name="First",
            email="unique@saltandshell.com",
            phone_number="07700 900789"
        )
        with self.assertRaises(Exception):
            Customer.objects.create(
                name="Second",
                email="unique@saltandshell.com",  # Duplicate email
                phone_number="07700 900000"
            )