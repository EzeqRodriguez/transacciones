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
    
    import json

    datos = open("black.json", "r")
    cuentaBlack = json.load(datos)

    for transferencias in cuentaBlack['transacciones']:
    
        clienteB = Black(cuentaBlack['nombre'], cuentaBlack['apellido'], cuentaBlack['dni'])
    
        if transferencias['estado'] == "ACEPTADA":
            
            print("\n")
            print("Estado: ", transferencias['estado'])
            print("Tipo: ", transferencias['tipo'])
            print("Monto: ", transferencias['monto'])
            print("Fecha: ", transferencias['fecha'])
            print("Saldo en cuenta: ", transferencias['saldoEnCuenta'])
            print("Cupo diario restante: ", transferencias['cupoDiarioRestante'])
            print("\n")
    
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

def classic():
    

    
    import json

    datos = open("classic.json", "r")
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

    datos = open("gold.json", "r")
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