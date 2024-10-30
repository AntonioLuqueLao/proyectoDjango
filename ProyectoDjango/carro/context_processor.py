from .carro import Carro

def importe_total_carro(request):
    total=0
    carro=Carro(request)
    if request.user.is_authenticated:
        print(carro.carro)
        for key, value in carro.carro.items():
            total+=float(value["precio"])*float(value["cantidad"])

    return {"importe_total_carro": total}

