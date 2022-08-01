from tipos import Classic, Black, Gold


def menu():

    opcion = int(input("Bienvenido: \nIngrese su DNI:\n"))

    if opcion == 41:
        black()
    elif opcion == 42:
        gold()
    elif opcion == 43:
        classic()
    else:
        print("Su DNI no se encuentra en nuestra base de datos,\nIntente nuevamente")


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
            valor_html = valor_html + "Monto: " + f"transferencias['monto']" + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            valor_html = valor_html + "Fecha: " + transferencias['fecha'] + "</br>"
            f.write(valor_html)
            valor_html = "</p>"
            f.write(valor_html)
            valor_html = "<p>"
            

        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO" and transferencias['monto'] > transferencias['cupoDiarioRestante'] :

            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Limite de Cupo Diario excedido")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")
    
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "ALTA_CHEQUERA" and transferencias['totalChequerasActualmente'] <= clienteB.chequera:
            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Limite de Chequeras excedido")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")
        
        
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "ALTA_TARJETA_CREDITO" and transferencias["totalTarjetasDeCreditoActualmente"] <= clienteB.tarjetaC:    
            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Limite de Tarjetas de Credito excedido")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")
        
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "TRANSFERENCIA_ENVIADA" and transferencias["monto"] > transferencias["saldoEnCuenta"]:    
            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Monto en cuenta insuficiente")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")   
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "COMPRA_DOLAR" and transferencias["monto"] > transferencias["saldoEnCuenta"]:    
            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Monto para comprar dolares insuficiente")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")  
    html_pie_template="""
    </body>
    </html>
    """
    f.write(html_pie_template)
    f.close()

def classic():
    

    
    import json

    datos = open("presentarSprint5/classic.json", "r")
    cuentaClassic = json.load(datos)

    for transferencias in cuentaClassic['transacciones']:
    
        clienteC = Classic(cuentaClassic['nombre'], cuentaClassic['apellido'], cuentaClassic['dni'])

        if transferencias['estado'] == "ACEPTADA":
            
            print("\n")
            print("Estado: ", transferencias['estado'])
            print("Tipo: ", transferencias['tipo'])
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")
        
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "ALTA_CHEQUERA" and clienteC.tarjetaC == False:
            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Usted no tiene acceso a Chequeras")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")    
        
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "ALTA_TARJETA_CREDITO" and clienteC.tarjetaC == False: 
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Usted no tiene acceso a Tarjetas de credito")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")    
            
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO" and transferencias['monto'] > clienteC.retiroMax:     
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Solo puede hacer extracciones de 10k")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")
        
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO" and transferencias['monto'] > transferencias['cupoDiarioRestante']: 
            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Cupo diario insuficiente")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")
        
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "COMPRA_DOLAR" and clienteC.dolar == False: 
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Usted no tiene acceso a Tarjetas de credito")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")

        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "TRANSFERENCIA_RECIBIDA" and transferencias['monto'] > clienteC.transMax: 
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Usted no puede recibir transferencias mayores a 150.000 sin previo aviso")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")

def gold(): 
    import json

    datos = open("presentarSprint5/gold.json", "r")
    cuentaGold = json.load(datos)

    for transferencias in cuentaGold['transacciones']:
    
        clienteG = Gold(cuentaGold['nombre'], cuentaGold['apellido'], cuentaGold['dni'])

        if transferencias['estado'] == "ACEPTADA":
            
            print("\n")
            print("Estado: ", transferencias['estado'])
            print("Tipo: ", transferencias['tipo'])
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")

        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO" and transferencias['monto'] > transferencias['cupoDiarioRestante']: 
            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Cupo diario excedido")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")     
            
            
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "ALTA_TARJETA_CREDITO" and transferencias['totalTarjetasDeCreditoActualmente'] >= clienteG.tarjetaC:
            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Solo puede tener 1 tarjeta de credito")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")      

        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "ALTA_CHEQUERA" and transferencias["totalChequerasActualmente"] >= clienteG.chequera:
            
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: Solo puede tener 1 chequera")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")      
        
        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "COMPRA_DOLAR" and transferencias["monto"] > transferencias['saldoEnCuenta']:       
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: No tiene saldo suficiente para comprar dolares")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")  

        elif transferencias['estado'] == "RECHAZADA" and transferencias['tipo'] == "TRANSFERENCIA_RECIBIDA" and transferencias["monto"] > clienteG.transMax:       
            print("Estado: ", transferencias['estado'])
            print("Tipo :", transferencias['tipo'])
            print("Motivo del Rechazo: No puede recibir transferencias mayores a 500k sin previo aviso")
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n") 



menu()

# f = open('cheques.html', 'w')

# html_template = """<html>
# <head>
# <meta charset="UTF-8">
# <meta http-equiv="X-UA-Compatible" content="IE=edge">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>IT_BANK</title>
# <link rel="icon" type="image/x-icon" href="imags/N-ITBANK.jpg">
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
# <link rel="stylesheet" href="css/prueba.css">
# </head>
# <body>
# <main>

# </main>
# </body>
# </html>
# """

# f.write(html_template)
# f.write(valor_html)
# f.close()