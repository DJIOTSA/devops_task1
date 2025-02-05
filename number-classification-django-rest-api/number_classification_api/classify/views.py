from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
import requests

# Helper functions to classify numbers
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def fetch_fun_fact(num):
    url = f"http://numbersapi.com/{num}?json"
    response = requests.get(url)
    data = response.json()
    return data.get('text', f"No fun fact available for {num}")

# API Viewset using mixins
class NumberClassificationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    @action(detail=False, methods=['get'])
    def classify_number(self, request):
        number = request.query_params.get('number')

        # Validate the input
        if not number or not number.isdigit():
            return Response({"number": number or 'undefined', "error": True}, status=400)

        num = int(number)
        
        # Classify the number
        properties = []

        # Armstrong number
        if is_armstrong(num):
            properties.append("armstrong")
        
        # Even or odd
        if num % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
        
        # Calculate digit sum
        digit_sum = sum(int(digit) for digit in str(num))

        # Get the fun fact from Numbers API
        fun_fact = fetch_fun_fact(num)

        # Return the response
        return Response({
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        })

