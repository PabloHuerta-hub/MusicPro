def total_carrito(request):
    total=0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            acumulado = int(value["acumulado"])
            total += acumulado
    return {"total_carrito": str(total)}