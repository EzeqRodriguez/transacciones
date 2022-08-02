from tipos import Classic, Black, Gold


def menu1():

    menu1 = int(input("Bienvenido: \nIngrese 1, para ver todas sus transferencias\nIngrese 2, para ver sus transferencias APROBADAS\nIngrese 3, para ver sus transferencias RECHAZADOS\n"))
    if menu1 == 1 :
        menuT()
    elif menu1 == 2 :
        menuA()
    elif menu1 == 3:
        menuR()
        
        
def menuT():
    
    menuDNI = int(input("Ingrese su DNI: "))
    
    if menuDNI == 41:
        black()
    elif menuDNI == 42:
        gold()
    elif menuDNI == 43:
        classic()
    else:
        print("Su DNI no esta en nuestra base de datos")
        
def menuA():
    
    menu2 = int(input("Ingrese su dni"))
    
    if menu2 == 41:
        blackA()
        
    elif menu2 == 42:
        classicA()
    elif menu2 == 43:
        goldA()
    else:
        print("Su DNI no esta en nuestra base de datos")
        

def menuR():
    
    menu3 = int(input("Ingrese su dni"))
    
    if menu3 == 41:
        blackR()
        
    elif menu3 == 42:
        classicR()
    elif menu3 == 43:
        goldR()
    else:
        print("Su DNI no esta en nuestra base de datos")
        





def blackA():
    f = open('cheques.html', 'w')
    html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
"""
    f.write(html_template)
    import json

    datos = open("presentarSprint5/black.json", "r")
    cuentaBlack = json.load(datos)

    for transferencias in cuentaBlack['transacciones']:
    
        clienteB = Black(cuentaBlack['nombre'], cuentaBlack['apellido'], cuentaBlack['dni'])
    
        if transferencias['estado'] == "ACEPTADA":
            
            # print("\n")
            # print("Estado: ", transferencias['estado'])
            # print("Tipo: ", transferencias['tipo'])
            # print("Monto: ", transferencias['monto'])
            # print("Fecha: ", transferencias['fecha'])
            # print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            # print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            # print("\n")
            
            valor_html = "<p>"
            valor_html = valor_html + "Estado: " + transferencias['estado'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Tipo: " + transferencias['tipo'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Monto: " + transferencias['monto'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"

def black():

    f = open('cheques.html', 'w')
    html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
"""
    f.write(html_template)
    import json

    datos = open("presentarSprint5/black.json", "r")
    cuentaBlack = json.load(datos)

    for transferencias in cuentaBlack['transacciones']:
    
        clienteB = Black(cuentaBlack['nombre'], cuentaBlack['apellido'], cuentaBlack['dni'])
    
        if transferencias['estado'] == "ACEPTADA" or transferencias['estado'] == "RECHAZADA":
            
            # print("\n")
            # print("Estado: ", transferencias['estado'])
            # print("Tipo: ", transferencias['tipo'])
            # print("Monto: ", transferencias['monto'])
            # print("Fecha: ", transferencias['fecha'])
            # print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            # print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            # print("\n")
            
            valor_html = "<p>"
            valor_html = valor_html + "Estado: " + transferencias['estado'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Tipo: " + transferencias['tipo'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Monto: " + transferencias['monto'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
 
    html_pie_template="""
    </body>
    </html>
    """
    f.write(html_pie_template)
    f.close()

def blackR():
    f = open('cheques.html', 'w')
    html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
"""
    f.write(html_template)
    import json

    datos = open("presentarSprint5/black.json", "r")
    cuentaBlack = json.load(datos)

    for transferencias in cuentaBlack['transacciones']:
    
        clienteB = Black(cuentaBlack['nombre'], cuentaBlack['apellido'], cuentaBlack['dni'])
    
        if transferencias['estado'] == "RECHAZADA":
            
            # print("\n")
            # print("Estado: ", transferencias['estado'])
            # print("Tipo: ", transferencias['tipo'])
            # print("Monto: ", transferencias['monto'])
            # print("Fecha: ", transferencias['fecha'])
            # print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            # print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            # print("\n")
            
            valor_html = "<p>"
            valor_html = valor_html + "Estado: " + transferencias['estado'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Tipo: " + transferencias['tipo'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Monto: " + transferencias['monto'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
 
    html_pie_template="""
    </body>
    </html>
    """
    f.write(html_pie_template)
    f.close()

###################################################################################

def classicA():
    f = open('cheques.html', 'w')
    html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
"""
    f.write(html_template)
    import json

    datos = open("presentarSprint5/classic.json", "r")
    cuentaClassic = json.load(datos)

    for transferencias in cuentaClassic['transacciones']:
    
        clienteB = Black(cuentaClassic['nombre'], cuentaClassic['apellido'], cuentaClassic['dni'])
    
        if transferencias['estado'] == "ACEPTADA":
            
            # print("\n")
            # print("Estado: ", transferencias['estado'])
            # print("Tipo: ", transferencias['tipo'])
            # print("Monto: ", transferencias['monto'])
            # print("Fecha: ", transferencias['fecha'])
            # print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            # print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            # print("\n")
            
            valor_html = "<p>"
            valor_html = valor_html + "Estado: " + transferencias['estado'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Tipo: " + transferencias['tipo'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Monto: " + transferencias['monto'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"

def classicR():
    f = open('cheques.html', 'w')
    html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
"""
    f.write(html_template)
    import json

    datos = open("presentarSprint5/classic.json", "r")
    cuentaClassic = json.load(datos)

    for transferencias in cuentaClassic['transacciones']:
    
        clienteB = Black(cuentaClassic['nombre'], cuentaClassic['apellido'], cuentaClassic['dni'])
    
        if transferencias['estado'] == "RECHAZADA":
            
            # print("\n")
            # print("Estado: ", transferencias['estado'])
            # print("Tipo: ", transferencias['tipo'])
            # print("Monto: ", transferencias['monto'])
            # print("Fecha: ", transferencias['fecha'])
            # print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            # print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            # print("\n")
            
            valor_html = "<p>"
            valor_html = valor_html + "Estado: " + transferencias['estado'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Tipo: " + transferencias['tipo'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Monto: " + transferencias['monto'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"

def classic():

    f = open('cheques.html', 'w')
    html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
"""
    f.write(html_template)
    import json

    datos = open("presentarSprint5/classic.json", "r")
    cuentaClassic = json.load(datos)

    for transferencias in cuentaClassic['transacciones']:
    
        clienteC = Classic(cuentaClassic['nombre'], cuentaClassic['apellido'], cuentaClassic['dni'])
    
        if transferencias['estado'] == "ACEPTADA" or transferencias['estado'] == "RECHAZADA":
            
            
            
            valor_html = "<p>"
            valor_html = valor_html + "Estado: " + transferencias['estado'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Tipo: " + transferencias['tipo'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Monto: " + transferencias['monto'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"


    html_pie_template="""
    </body>
    </html>
    """
    f.write(html_pie_template)
    f.close()

####################################################################################

def gold():

    f = open('cheques.html', 'w')
    html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
"""
    f.write(html_template)
    import json

    datos = open("presentarSprint5/gold.json", "r")
    cuentaGold = json.load(datos)

    for transferencias in cuentaGold['transacciones']:
    
        clienteG = Gold(cuentaGold['nombre'], cuentaGold['apellido'], cuentaGold['dni'])
    
        if transferencias['estado'] == "ACEPTADA" or transferencias['estado'] == "RECHAZADA":
            
            
            
            valor_html = "<p>"
            valor_html = valor_html + "Estado: " + transferencias['estado'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Tipo: " + transferencias['tipo'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Monto: " + transferencias['monto'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"


    html_pie_template="""
    </body>
    </html>
    """
    f.write(html_pie_template)
    f.close()


def goldA():

    f = open('cheques.html', 'w')
    html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
"""
    f.write(html_template)
    import json

    datos = open("presentarSprint5/gold.json", "r")
    cuentaGold = json.load(datos)

    for transferencias in cuentaGold['transacciones']:
    
        clienteG = Gold(cuentaGold['nombre'], cuentaGold['apellido'], cuentaGold['dni'])
    
        if transferencias['estado'] == "ACEPTADA" :
            
            
            
            valor_html = "<p>"
            valor_html = valor_html + "Estado: " + transferencias['estado'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Tipo: " + transferencias['tipo'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Monto: " + transferencias['monto'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"


    html_pie_template="""
    </body>
    </html>
    """
    f.write(html_pie_template)
    f.close()


def goldR():
    f = open('cheques.html', 'w')
    html_template = """<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT_BANK</title>
<link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<link rel="stylesheet" href="css/prueba.css">
</head>
<body>
"""
    f.write(html_template)
    import json

    datos = open("presentarSprint5/gold.json", "r")
    cuentaGold = json.load(datos)

    for transferencias in cuentaGold['transacciones']:
    
        clienteG = Gold(cuentaGold['nombre'], cuentaGold['apellido'], cuentaGold['dni'])
    
        if transferencias['estado'] == "RECHAZADA" :
            
            
            
            valor_html = "<p>"
            valor_html = valor_html + "Estado: " + transferencias['estado'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Tipo: " + transferencias['tipo'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Monto: " + transferencias['monto'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"


    html_pie_template="""
    </body>
    </html>
    """
    f.write(html_pie_template)
    f.close()




menu1()