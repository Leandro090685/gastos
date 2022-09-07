from flask import Flask,request

from models.gasto import Gasto
from servicies.service_gasto import ServiceGasto

from models.rubro import Rubro
from servicies.service_rubro import ServiceRubro

def suma(monto):
    total = 0
    for a in monto:
        total = total + a[0]
    return total

rubros = ServiceRubro().get_all()
lista = []
for a in rubros:
    lista.append(a[0])

options_list = ''
for a in range(len(lista)):
    options_list = str(options_list) + f'<option value="{lista[a]}">{lista[a]}</option>\n'



index = f"""
<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Gastos Soft Online Module v1.0</title>

    </head>
    <body>
        <h1 style="text-align: center;"><strong>Gastos Soft Online Module v1.0</strong></h1>
        <p style="text-align: left;"><strong>Seleccione opcion:</strong></p>
        <ul>
        <li style="text-align: left;"><a title="Agregar Gasto" href="../agregar_gasto">Agregar Gasto</a></li>
        <li style="text-align: left;"><a title="Agregar Rubro" href="/agregar_rubro">Agregar Rubro</a></li>
        <li style="text-align: left;"><a title="Eliminar Rubro" href="/eliminar_rubro">Eliminar Rubro</a></li>
        <li style="text-align: left;"><a title="Ver Todos Los Gastos" href="/todos_los_gastos">Ver Todos Los Gastos</a></li>
        <li style="text-align: left;"><a title="Buscar gastos por Rubro" href="/buscar_por_rubro">Buscar gastos por Rubro</a></li>
        <li style="text-align: left;"><a title="Borrar Gasto" href="/borrar_gasto">Borrar Gasto</a></li>
        </ul>
    </body>
</html>
"""

error_datos_vacios = """
<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Vacios</title>
        <meta http-equiv="refresh" content="3";URL="http://localhost:8880/">
    </head>
    <body>
        Campos Vacios, o hay un error...
        Regresando al Index...
    </body>
</html>
"""


agregar_rubro_page = f""" 
<!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"></head>
    <body>
        <form method="POST">
                Nombre Rubro Nuevo:<br>
                <input type="text" name="item">
                <br><br>
                <input type="submit" value="Enviar">
         </form> 
                <br><h4 style="text-align: left;"><a title="INDEX" href="/">Regresar al inicio</a></h4>

    </body>
</html>
"""


enviado_registro = """
<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Enviado</title>
        <meta http-equiv="refresh" content="4;URL=http://localhost:8880/">
    </head>
    <body>
        Nuevo Gasto Registrado con exito!
        <br>
        En breves se redigirá al index....
    </body>
</html>
"""

enviado_rubro = """
<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Enviado</title>
        <meta http-equiv="refresh" content="4;URL=http://localhost:8880/">
    </head>
    <body>
        Nuevo Rubro Registrado con exito!
        <br>
        En breves se redigirá al index....
    </body>
</html>
"""

borrado_rubro = """
<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Enviado</title>
        <meta http-equiv="refresh" content="4;URL=http://localhost:8880/">
    </head>
    <body>
        Rubro Eliminado con exito!
        <br>
        En breves se redigirá al index....
    </body>
</html>
"""

borrado_gastos = """
<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Enviado</title>
        <meta http-equiv="refresh" content="4;URL=http://localhost:8880/">
    </head>
    <body>
        Gasto Eliminado con exito!
        <br>
        En breves se redigirá al index....
    </body>
</html>
"""

app = Flask(__name__)

@app.route("/")
def home():
    return index.encode("utf-8")

@app.route("/agregar_gasto",  methods=["GET","POST"])
def add_report():
    rubros = ServiceRubro().get_all()
    lista = []
    for a in rubros:
        lista.append(a[0])

    options_list = ''
    for a in range(len(lista)):
        options_list = str(options_list) + f'<option value="{lista[a]}">{lista[a]}</option>\n'
    agregar_gasto_page = f""" 
    <!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"></head>
        <body>
            <form method="POST">
                Fecha:<br>
                <input type="date" id="start" name="fecha"  min="2022-01-01" max="2025-12-31"> <br>
                Rubro: <br>
                <select name="categoria">
                {options_list}
                </select>
                <br>
                Importe:<br>
                <input type="text" name="importe">
                <br>

                Observaciones:<br>
                <textarea name="obs"></textarea>
                <br><br>
                <input type="submit" value="Enviar">
            </form>
                    <br><h4 style="text-align: left;"><a title="INDEX" href="/">Regresar al inicio</a></h4>
    
        </body>
    </html>
    """

    if request.method == "GET":
        return agregar_gasto_page.encode("utf-8")
    elif request.method == "POST":
        try:
            body = dict(request.form)
            if body["categoria"] and body["importe"] and body["fecha"] and body["obs"]:
                a = Gasto(body["fecha"],body["categoria"],body["obs"],body["importe"])
                ServiceGasto().save_gasto(a)
                return enviado_registro.encode("utf-8")
                
            else:
                return error_datos_vacios.encode("utf-8")
        except Exception:
            return error_datos_vacios.encode("utf-8")
    else:
        return error_datos_vacios.encode("utf-8")

@app.route("/agregar_rubro", methods=["GET","POST"])
def add_item():
    if request.method == "GET":
        return agregar_rubro_page.encode("utf-8")
    elif request.method == "POST":
        try:
            body = dict(request.form)
            if body["item"]:
                rubro = Rubro(body["item"])
                ServiceRubro().save(rubro)
                return enviado_rubro.encode("utf-8")
            else:
                return error_datos_vacios.encode("utf-8")
        except Exception:
            return error_datos_vacios.encode("utf-8")
    else:
        return error_datos_vacios.encode("utf-8")

@app.route("/eliminar_rubro", methods=["GET","POST"])
def delete_item():
    rubros = ServiceRubro().get_all()
    lista = []
    for a in rubros:
        lista.append(a[0])

    options_list = ''
    for a in range(len(lista)):
        options_list = str(options_list) + f'<option value="{lista[a]}">{lista[a]}</option>\n'
    eliminar_rubro_page = f""" 
    <!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"></head>
        <body>
            <form method="POST">
                    Seleccione rubro a eliminar:<br>
                    <select name="categoria">
                    {options_list}
                    </select>
                    <br><br>
                    <input type="submit" value="Enviar">
            </form> 
                    <br><h4 style="text-align: left;"><a title="INDEX" href="/">Regresar al inicio</a></h4>

        </body>
    </html>
    """
    if request.method == "GET":
        return eliminar_rubro_page.encode("utf-8")
    elif request.method == "POST":
        try:
            body = dict(request.form)
            if body["categoria"]:
                ServiceRubro().clear_rubro(body["categoria"])
                return borrado_rubro.encode("utf-8")

            else:
                return error_datos_vacios.encode("utf-8")
        except Exception:
            return error_datos_vacios.encode("utf-8")
    else:
        return error_datos_vacios.encode("utf-8")

@app.route("/todos_los_gastos")
def total_report(): 
    tabla_total=ServiceGasto().get_all_table()
    total = suma(ServiceGasto().total())
    tabla_total=tabla_total.replace('\n',"<br>")

    ver_todos_los_gastos_page = f"""
    <!doctype html>
    <html lang="es">
        <head>
            <meta charset="utf-8">
            <title>Reporte</title>

        </head>
        <body>
            {tabla_total}
            <br><br>
                    Total de gastos: {total}
                    <br><h4 style="text-align: left;"><a title="INDEX" href="/">Regresar al inicio</a></h4>

        </body>
    </html>
    """
    return ver_todos_los_gastos_page.encode("utf-8")

@app.route("/buscar_por_rubro", methods=["GET","POST"])
def search_item():
    rubros = ServiceRubro().get_all()
    lista = []
    for a in rubros:
        lista.append(a[0])

    options_list = ''
    for a in range(len(lista)):
        options_list = str(options_list) + f'<option value="{lista[a]}">{lista[a]}</option>\n'
    buscar_rubro_page = f""" 
    <!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"></head>
        <body>
            <form method="POST">
                    Seleccione rubro a Buscar:<br>
                    <select name="categoria">
                    {options_list}
                    </select>
                    <br><br>
                    <input type="submit" value="Enviar">
            </form> 
                    <br><h4 style="text-align: left;"><a title="INDEX" href="/">Regresar al inicio</a></h4>

        </body>
    </html>
    """
    if request.method == "GET":
        return buscar_rubro_page.encode("utf-8")
    elif request.method == "POST":
        try:
            body = dict(request.form)
            if body["categoria"]:
                tabla = ServiceGasto().get_one(body["categoria"])
                total = suma(ServiceGasto().total_rubro(body["categoria"]))
                tabla=tabla.replace('\n',"<br>")
                ver_todos_los_gastos_page = f"""
                <!doctype html>
                <html lang="es">
                    <head>
                        <meta charset="utf-8">
                        <title>Reporte</title>

                    </head>
                    <body>
                        {tabla}
                        <br><br>
                                Total de gastos por rubro {body["categoria"]}: {total}
                                <br><h4 style="text-align: left;"><a title="INDEX" href="/">Regresar al inicio</a></h4>

                    </body>
                </html>
                """
                return ver_todos_los_gastos_page.encode("utf-8")
            else:
                return error_datos_vacios.encode("utf-8")
        except Exception:
            return error_datos_vacios.encode("utf-8")
    else:
        return error_datos_vacios.encode("utf-8")


@app.route("/borrar_gasto", methods=["GET","POST"])
def delete_report():
    tabla_total=ServiceGasto().get_all_table()
    tabla_total=tabla_total.replace('\n',"<br>")

    borrar_gastos_page = f"""
    <!doctype html>
    <html lang="es">
        <head>
            <meta charset="utf-8">
            <title>Reporte</title>

        </head>
        <body>
                    {tabla_total}
                    <br><br>
                    <form method="POST">
                    Seleccione el ID del gasto a borrar:<br>
                    <input type="number" name="id" > <br>
                    <br><br>
                    <input type="submit" value="Enviar">
            </form> 

                    <br><h4 style="text-align: left;"><a title="INDEX" href="/">Regresar al inicio</a></h4>

        </body>
    </html>
    """
    if request.method == "GET":
        return borrar_gastos_page.encode("utf-8")
    elif request.method == "POST":
        try:
            body = dict(request.form)
            if body["id"]:
                ServiceGasto().clear_gasto(body["id"])
                return borrado_gastos.encode("utf-8")
            else:
                return error_datos_vacios.encode("utf-8")
        except Exception:
            return error_datos_vacios.encode("utf-8")
    else:
        return error_datos_vacios.encode("utf-8")

app.run("localhost",port=8880)
