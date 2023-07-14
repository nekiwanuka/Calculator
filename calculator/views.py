# views.py
import logging
from django.shortcuts import render, redirect
from .models import Calculation


# Create a logger object
logger = logging.getLogger(__name__)

def calculator(request):
    calculations = Calculation.objects.all().order_by('-created_at')
    latest_calculation = calculations.first()
    return render(
        request,
        'calculator/calculator.html',
        {'calculations': calculations, 'latest_calculation': latest_calculation}
    )

def calculate(request):
    if request.method == 'POST':
        input_one = float(request.POST.get('input_one'))
        operand = request.POST.get('operand')
        input_two = float(request.POST.get('input_two'))

        calculation = Calculation(
            input_one=input_one,
            operand=operand,
            input_two=input_two
        )
        calculation.save()
        
    logger.info('This is an informational message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    
    return redirect('calculator:calculator')
