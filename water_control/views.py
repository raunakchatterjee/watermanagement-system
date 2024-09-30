import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Firebase configuration


FIREBASE_URL= ${{ secrets.Firebase_Url }}    #'https://watermg-e82dd-default-rtdb.firebaseio.com/water.json' 

def index(request):
    # Fetch the current water percentage and pump status from Firebase
    response = requests.get(FIREBASE_URL)
    data = response.json()
    water_percentage = data.get('water_percentage', 0)
    pump_status = data.get('pump_status', 'off')

    context = {
        'water_percentage': water_percentage,
        'pump_status': pump_status,
    }
    return render(request, 'index.html', context)

@csrf_exempt
def control_pump(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        pump_status = 'on' if action == 'on' else 'off'

        # Update the pump status in Firebase
        response = requests.patch(FIREBASE_URL, json={'pump_status': pump_status})
        return redirect('index')

    return redirect('index')
