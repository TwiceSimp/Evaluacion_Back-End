from django.shortcuts import render

def inicio(request):
    return render(request,'shop_App/index.html')

def consolas(request):
    data = {"titulo": "Consolas", "foto1": "ps5.png","foto2":"switch.png","foto3":"xbox.png","producto1":"Playstation 5",
            "producto2":"Nintendo Switch ", "producto3": "Xbox series x"}
    return render(request, "shop_App/producto.html", data)

def computacion(request):
    data = {"titulo": "Computación", "foto1": "mac.png","foto2":"notebook.png","foto3":"hp.png","producto1":"Macbook",
            "producto2":"Notebook Asus", "producto3": "HP Pavillion"}
    return render(request,"shop_App/producto.html", data )

def telefonos(request):
    data = {"titulo": "Telefonos", "foto1": "iphone.png","foto2":"samsung.png","foto3":"xiaomi.png","producto1":"Iphone",
            "producto2":"Samsung ", "producto3": "Xiaomi"}
    return render(request,"shop_App/producto.html", data )

def usuario(request):
    data = {"titulo": "Usuario","foto":"usuario.jpg","nombre": "Edinson Aravena", "edad": 20, "carrera": "Ingeniería en informática", "correo":"edinson.aravena@inacapmail.cl"}
    return render(request,"shop_App/usuario.html", data)


