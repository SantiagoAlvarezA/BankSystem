dicUser = {}
dicLending = {}
mainDic = {'Users': dicUser, 'Lendings': dicLending}


def is_number(msg):
    isNum = False
    num = 0
    while not isNum:
        try:
            num = int(input(msg))
            isNum = True
        except ValueError:
            print('Por favor digite un valor numerico')
    return num


class Lending:
    idUser = 0
    valLending = 0
    fee = 0
    userExist = False

    def create_lending(self):

        if not dicUser:
            print('No existen usuarios registrados en el sistema')
        else:
            while not self.userExist:
                self.idUser = is_number('Digite el número de documento de la persona solicitante: ')

                for us in dicUser:

                    if us == self.idUser:
                        self.userExist = True

                if self.userExist:

                    # validar cuando el usuario aun no termine de pagar las cuotas
                    self.valLending = is_number('Que valor desea solicitar para este prestamo: ')
                    self.fee = is_number('En cuantas cuotas desea cancelar el prestamo? ')
                    val = self.valLending / self.fee

                    dicFee = {}
                    for fee in range(0, self.fee):
                        dicFee[fee + 1] = {'value': val, 'status': False}

                    id = is_number('Digite el numero del prestamo: ')
                    dicLending[id] = {'idUser': self.idUser, 'lending': dicFee}
                else:
                    print('La persona solicitante no esta registrada')
        self.userExist = False


class Pay:
    idUser = 0
    selection = 0
    arrayFee = []
    pay = False
    userExist = False

    def pay_fee(self):
        if not dicUser:
            print('No hay usuarios registrados')
        else:

            if not dicLending:
                print('Hasta el momento no se a realizado ningun prestamo')
            else:

                self.idUser = is_number('Digite el documento de la persona que realizara el pago: ')
                arrFee = []
                for lending in dicLending:
                    if dicLending[lending]['idUser'] == self.idUser:
                        print('Codigo de prestamo N° {}'.format(lending))
                        self.userExist = True
                        arrFee.append(lending)

                if self.userExist:

                    lenExist = False
                    len = 0
                    while not lenExist:
                        len = is_number('Ingrese el codigo del prestamo que desea cancelar: ')
                        for l in arrFee:
                            if len == l:
                                lenExist = True

                    for diclen in dicLending[len]['lending']:

                        if not dicLending[len]['lending'][diclen]['status']:

                            yesNo = False
                            while not yesNo:
                                question = input('Desea realmente pagar esta cuota? y/n: ')
                                if question == 'y':
                                    dicLending[len]['lending'][diclen]['status'] = True
                                    print('El pago se realizo con exito :)')
                                    yesNo = True

                                elif question == 'n':
                                    print('El pago fue cancelado :( ')
                                    yesNo = True

                                else:
                                    yesNo = False
                            break
                else:
                    print('El usuario no tiene deudas pendientes')
        self.pay = False
        self.userExist = False


class Report:
    idUser = 0
    feeExist = False
    paidExiste = False

    def paid_fees(self):
        if not dicUser:
            print('No existen usuarios registrados en el sistema')
        else:
            if not dicLending:
                print('No hay prestamos registrados')
            else:
                self.idUser = is_number('Digite el numero de documento: ')
                arr = []

                if dicUser[self.idUser]:

                    for lend in dicLending:

                        if dicLending[lend]['idUser'] == self.idUser:
                            arr.append(lend)
                            self.feeExist = True

                            print('Codigo del prestamo N° {} que desea mirar '.format(lend))

                if self.feeExist:

                    cp = is_number('Seleccione el codigo del prestamo que desea mirar la informacion')

                    totalPaid = 0
                    valuePaid = 0

                    for cod in arr:
                        if cod == cp:
                            for i in dicLending[cp]['lending']:
                                if dicLending[cp]['lending'][i]['status']:
                                    totalPaid = totalPaid + 1
                                    valuePaid = valuePaid + dicLending[cp]['lending'][i]['value']
                    print("""
                    usted a pagado un total de {} cuotas para un valor total de {} pagados                
                    """.format(totalPaid, valuePaid))
                else:
                    print('No hay datos para mostrar')
        self.feeExist = False

    def un_paid_fees(self):
        if not dicUser:
            print('No existen usuarios registrados en el sistema')
        else:
            if not dicLending:
                print('No hay prestamos registrados')
            else:
                self.idUser = is_number('Digite el numero de documento: ')
                arr = []

                if dicUser[self.idUser]:

                    for lend in dicLending:

                        if dicLending[lend]['idUser'] == self.idUser:
                            arr.append(lend)
                            print('Codigo del prestamo N° {} que desea mirar '.format(lend))
                            self.paidExiste = True

                if self.paidExiste:
                    cp = is_number('Seleccione el codigo del prestamo que desea mirar la informacion')

                    totalPaid = 0
                    valuePaid = 0
                    for cod in arr:
                        if cod == cp:
                            for i in dicLending[cp]['lending']:
                                if not dicLending[cp]['lending'][i]['status']:
                                    totalPaid = totalPaid + 1
                                    valuePaid = valuePaid + dicLending[cp]['lending'][i]['value']
                    print("""
                    usted deve un total de {} cuotas para un valor total de {} en deuda                
                    """.format(totalPaid, valuePaid))
                else:
                    print('No hay datos para mostrar')
        self.paidExiste = False


class User(Lending, Pay, Report):
    name = ''
    lastName = ''
    document = 0
    address = ''

    def create_user(self):
        self.name = input('digite su nombre: ')
        self.lastName = input('digite sus apellidos: ')
        self.document = is_number('digite el numero de documento: ')
        self.address = input('digite su direccion de recidensia: ')
        dicUser[self.document] = {'name': self.name, 'lastName': self.lastName, 'address': self.address}


def menu():
    print("""
    [1] Crear usuario
    [2] Pedir prestamo
    [3] Pagar un prestamo
    [4] Mostrar el listado de cuotas pagadas del prestamo por usuario
    [5] Mostrar el listado de cuotas pendientes por pagar del prestamo de un usuario
    [6] Salir    
    """)
    optionSelected = is_number("Select an option: ")
    return optionSelected


user = User()
optionSelected = menu()
while 0 < optionSelected <= 6:

    if optionSelected == 1:
        user.create_user()

    elif optionSelected == 2:
        user.create_lending()

    elif optionSelected == 3:
        user.pay_fee()

    elif optionSelected == 4:
        user.paid_fees()

    elif optionSelected == 5:
        user.un_paid_fees()

    elif optionSelected == 6:
        exit()

    optionSelected = menu()

print("Error this option does not exist")
for n in range(0, 3, 1):
    print("Bye...")
print(' _____________ ')
