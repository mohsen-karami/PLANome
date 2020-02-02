def customer(request):
    customer = request.session.get('customer')
    if not customer:
        customer = {}
    return {'customer': customer}
