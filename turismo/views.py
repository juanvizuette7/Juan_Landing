from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def lugares_turisticos(request):
    # Datos de ejemplo para los destinos (luego los puedes reemplazar con modelos de base de datos)
    destinos = [
        {
            'nombre': 'Destino Montañoso',
            'imagen': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&q=80',
            'descripcion': 'Disfruta de paisajes impresionantes y aire puro en nuestras rutas de montaña.'
        },
        {
            'nombre': 'Destino Playeros',
            'imagen': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&q=80',
            'descripcion': 'Relájate en las mejores playas con aguas cristalinas y arenas blancas.'
        },
        {
            'nombre': 'Destino Urbano',
            'imagen': 'https://images.unsplash.com/photo-1513326738677-b964603b136d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&q=80',
            'descripcion': 'Explora ciudades vibrantes llenas de cultura, historia y vida nocturna.'
        }
    ]
    return render(request, 'lugares.html', {'destinos': destinos})

def servicios(request):
    # Datos de ejemplo para los servicios
    servicios = [
        {
            'nombre': 'Paquete Básico',
            'descripcion': 'Incluye: alojamiento, traslados aeropuerto-hotel-aeropuerto y desayuno.',
            'precio': '$500'
        },
        {
            'nombre': 'Paquete Premium',
            'descripcion': 'Incluye: alojamiento de lujo, traslados, alimentación completa y tours guiados.',
            'precio': '$1000'
        },
        {
            'nombre': 'Paquete Personalizado',
            'descripcion': 'Diseñamos un itinerario según tus preferencias y necesidades específicas.',
            'precio': 'Consultar'
        }
    ]
    return render(request, 'servicios.html', {'servicios': servicios})

def contacto(request):
    return render(request, 'contacto.html')