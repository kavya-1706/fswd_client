from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        prod_id = request.POST.get("prod_id")
        api_url = f'http://127.0.0.1:8000/details/{prod_id}/'  
        response = requests.get(api_url)
        prod_data = response.json()
        if response.status_code == 200:
            prod_data = response.json()
            return render(request, 'details.html', {'prod_data': prod_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch product details. Check Again!'})
    
        
    return render(request, 'index.html')
