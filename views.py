import datetime
from django.http import HttpResponse
from django.template import Template, Con
from django.template import loader


class Persona():
     
     def __init__(self, nombre, apellido):
        #self.nombre = nombre
        #self.apellido = apellido
        pass

    
def saludo(request):
    nombre = "Yosvany"

    apellido = "Hernandez"

    ahora = datetime.datetime.now()

    #doc_externo = open("C:/Users/admininrh/Python/PythonLearning1/PythonLearning1/templates/mytemplate.html")
    
    #tmp=Template(doc_externo.read())
    
    #doc_externo.close()

    doc_externo = loader.get_template('mytemplate.html')

    documento = doc_externo.render({"nombre_persona":nombre, "apellido_persona": apellido, "hora_actual" : ahora})

    return HttpResponse(documento)   


def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    return HttpResponse(fecha_actual)
    