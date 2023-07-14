from django.db import models

class CalculationManager(models.Manager):
    def get_latest_calculation(self):
        return self.order_by('-created_at').first()

class Calculation(models.Model):
    input_one = models.FloatField()
    operand = models.CharField(max_length=1)
    input_two = models.FloatField()
    result = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CalculationManager()

    def save(self, *args, **kwargs):
        if self.result is None:
            self.calculate_result()
        super().save(*args, **kwargs)

    def calculate_result(self):
        if self.operand == '+':
            self.result = self.input_one + self.input_two
        elif self.operand == '-':
            self.result = self.input_one - self.input_two
        elif self.operand == '*':
            self.result = self.input_one * self.input_two
        elif self.operand == '/':
            if self.input_two != 0:
                self.result = self.input_one / self.input_two
            else:
                self.result = None  # Set result to None for division by zero
        else:
            self.result = None  # Set result to None for invalid operand

    def __str__(self):
        return f"{self.input_one} {self.operand} {self.input_two} = {self.result}"
