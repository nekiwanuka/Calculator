from django.test import TestCase
from django.urls import reverse

from .models import Calculation


class CalculatorTests(TestCase):
    def test_calculator_view(self):
        # Test the calculator view
        response = self.client.get(reverse("calculator:calculator"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "calculator/calculator.html")

    def test_calculate_view(self):
        # Test the calculate view
        data = {"input_one": 10, "operand": "+", "input_two": 5}
        response = self.client.post(reverse("calculator:calculate"), data)
        self.assertEqual(response.status_code, 302)  # Check for redirection after POST

        calculation = Calculation.objects.first()
        self.assertIsNotNone(calculation)
        self.assertEqual(calculation.result, 15)
