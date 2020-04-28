#DICCIONARIOS
cliente = {
    '':['','','']
}
estadoProyecto = {
    '':''
}
departamento = {
    '':''
}
municipio = {
    '':''
}
reporte = {
    #id = idClient, idEstado, idDepartamento,idMuni
    '':['','','','']
}

import os

#INSERTAR1

#CLIENTES
def insertarCliente():
    id = input("INGESE CODIGO DE CLIENTE")
    if id in cliente:
        print("CLIENTE YA REGISTRADO")
    else:
        nombre = input("INGRESE NOMBRE")
        direccion = input("INGRESE DIRECCION")
        telefono = input("INGRESE NUMERO DE TELEFONO")

        cliente[id] = [nombre,direccion,telefono]

#ESTADO DE PROYECTOS
def insertarEstado():
    id = input("CODIGO DE ESTADO DE PROYECTO")
    if id in estadoProyecto:
       print("ESTADO EN EXISTENCIA ")
    else:
        nombre = input("INGRESE EL TIPO DE ESTADO")
        estadoProyecto[id]=nombre

#PROYECTOS
def insertarProyectos():
    id = input("INGRESE CODIGO DE PROYECTO")
    if id in reporte:
        print("PROYECTO YA REGISTRADO")
    else:
        idCliente = input("INGRESE CODIGO DE CLIENTE")
        idEstado = input("INGRESE CODIGO DE ESTADO DE PROYECTP")
        idDepartamento = input("INGRESE CODIGO DE DEPARTAMENTO")
        idMunicipio = input("INGRESE CODIGO DE MUNICIPIO")
        reporte[id]=[idCliente,idEstado,idDepartamento,idMunicipio]


#DEPARTAMENTOS
def insertarDepartamento():
    id = input("INGRESE CODIGO DE DEPARTAMENTO")
    if id in departamento:
       print("DEPARTAMENTO YA REGISTRADO")
    else:
        nombre = input("EN QUE DEPARTAMENTO ESTA UBICADO?")
        departamento[id]=nombre

#MUNICIPIO
def insertarMuni():
    id = input("INGRESE CODIGO DE MUNICIPIO")
    if id in municipio:
       print("MUNICIPIO YA REGISTRADO")
    else:
        nombre = input("EN QUE MUNICIPIO ESTA UBICADO?")
        municipio[id]=nombre


#MOSTRAR

#CLIENTES
def mostrarClientes():

    for k,v in cliente.items():
        print("" + k.ljust(16, " "), end="")
        print(""+v[0].ljust(14," ") ,end="")
        print(""+v[1].ljust(25," "), end="")
        print(""+v[2].ljust(10," "),end="")
        print("")

#ESTADO DE PROYECTOS
def mostrarEstado():
    for k in estadoProyecto:
        print(k.ljust(20, " "), end="")
        print("" + estadoProyecto[k].ljust(15, " "), end="")
        print("")

#DEPARTAMENTOS
def mostrarDepartamento():
    for k in departamento:
        print(k.ljust(20, " "), end="")
        print("" + departamento[k].ljust(15, " "), end="")
        print("")

#MUNICIPIO
def mostrarMuni():
    for k in municipio:
        print(k.ljust(20, " "), end="")
        print("" + municipio[k].ljust(15, " "), end="")
        print("")

#REPORTE DE PROYECTO
def mostrarRegistros():

    for k,v in reporte.items():
        print("" + k.ljust(16, " "), end="")
        print(""+cliente[v[0]][0].ljust(18," ") ,end="")
        print(""+estadoProyecto[v[1]].ljust(22," "), end="")
        print(""+departamento[v[2]].ljust(15," "),end="")
        print("" + municipio[v[3]].ljust(15, " "), end="")
        print("")

#MENU
def menu():

    while True:
        print("***************************************************************************")
        print("\t\t\t\t\t\t\tBIENVENIDO A PINTADOS EXPRESS")
        print("***************************************************************************")
        print("\t\t\t\t\t\t\t\tMENU PRINCIPAL")
        print("\t\t\t\t\t1 - INGRESO DE CLIENTES")
        print("\t\t\t\t\t2 - REGISTRO DE CLIENTES")
        print("\t\t\t\t\t3 - INGRESO DE ESTADO DE PROYECTOS")
        print("\t\t\t\t\t4 - MOSTRAR ESTADO DE PROYECTOS")
        print("\t\t\t\t\t5 - IGRESO DE DEPARTAMENTOS")
        print("\t\t\t\t\t6 - MOSTRAR DEPARTAMENTOS")
        print("\t\t\t\t\t7 - IGRESO DE MUNICIPIOS")
        print("\t\t\t\t\t8 - MOSTRAR MUNICIPIOS")
        print("\t\t\t\t\t9 - CREACION DE PROYECTO")
        print("\t\t\t\t\t10 - REPORTE DE PROYECTO")
        print("\t\t\t\t\t0 - Salir")
        print("***************************************************************************")

        optionMenu = input("QUE DESEA REALIZAR>>  ")
        if optionMenu == "1":
            opcion = "1"
            print("***************************************************************************")
            insertarCliente()

        elif optionMenu == "2":
            print("***************************************************************************")
            print(
                ("CODIGO").ljust(15, " ") +("CLIENTE").ljust(15, " ") + ("DIRECCION").ljust(25, " ") + ("TELEFONO").ljust(15, " "))
            print("***************************************************************************")

            mostrarClientes()
            print("***************************************************************************")

            input("\npulsa una tecla para continuar")

        elif optionMenu == "3":
            print("***************************************************************************")
            insertarEstado()
        elif optionMenu == "4":
            print("***************************************************************************")
            print(
                ("ESTADO DE PROYECTO").ljust(15, " "))
            print("***************************************************************************")

            mostrarEstado()
            print("***************************************************************************")


            input("\npulsa una tecla para continuar")

        elif optionMenu == "5":
            print("***************************************************************************")
            insertarDepartamento()
        elif optionMenu == "6":
            print("***************************************************************************")
            print(
                ("DEPARTAMENTO").ljust(15, " "))
            print("***************************************************************************")

            mostrarDepartamento()
            print("***************************************************************************")


            input("\npulsa una tecla para continuar")

        elif optionMenu == "7":
            print("***************************************************************************")
            insertarMuni()
        elif optionMenu == "8":
            print("***************************************************************************")
            print(
                ("MUNICIPIO").ljust(15, " "))
            print("***************************************************************************")

            mostrarMuni()
            print("***************************************************************************")


            input("\npulsa una tecla para continuar")


        elif optionMenu == "9":
            print("***************************************************************************")
            insertarProyectos()

        elif optionMenu == "10":
            print("***********************************************************************************************")
            print(
                ("CODIGO").ljust(15, " ") +("CLIENTE").ljust(15, " ") + ("ESTADO DE PROYECTO").ljust(25, " ") + ("DEPARTAMENTO").ljust(15, " ")+ ("MUNICIPIO").ljust(15, " "))
            print("***********************************************************************************************")

            mostrarRegistros()
            print("***********************************************************************************************")


            input("\npulsa una tecla para continuar")


        elif optionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

menu()