
class Carro():
    def __init__(self, request):
        self.request=request
        self.session=request.session
        self.carro = self.session.get("carro", {})
        self.session["carro"] = self.carro

    def agregar(self, producto):
        producto_id_str = str(producto.id)
        
        if producto_id_str not in self.carro:
            self.carro[producto_id_str] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            self.carro[producto_id_str]["cantidad"] += 1
        self.guardar_carro()
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar_producto(self, producto):
        producto_id_str = str(producto.id)

        if producto_id_str in self.carro:
            del self.carro[producto_id_str]
            self.guardar_carro()

    def restar_producto(self, producto):
        producto_id_str = str(producto.id)

        if producto_id_str in self.carro:
            self.carro[producto_id_str]["cantidad"]=self.carro[producto_id_str]["cantidad"]-1
            if self.carro[producto_id_str]["cantidad"]==0:
                self.eliminar_producto(producto)
            self.guardar_carro()

    def limpiar_carro(self):
        self.carro={}
        self.guardar_carro()

    def __str__(self):
        return f"{self.carro}"