import paypalrestsdk
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .views import create_payment, execute_payment

paypalrestsdk.configure({
  "mode": settings.PAYPAL_MODE,  # sandbox or live
  "client_id": settings.PAYPAL_CLIENT_ID,
  "client_secret": settings.PAYPAL_SECRET
})

@csrf_exempt
def create_payment(request):
    if request.method == "POST":
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "http://localhost:8000/payment/execute/",
                "cancel_url": "http://localhost:8000/payment/cancel/"},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "item",
                        "sku": "item",
                        "price": "5.00",
                        "currency": "USD",
                        "quantity": 1}]},
                "amount": {
                    "total": "5.00",
                    "currency": "USD"},
                "description": "This is the payment transaction description."}]})

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    # Capture the approval_url to redirect the user to PayPal for payment approval
                    approval_url = str(link.href)
                    return JsonResponse({"approval_url": approval_url}, safe=False)
        else:
            print(payment.error)
    return JsonResponse({'error': 'Invalid request'}, status=400)