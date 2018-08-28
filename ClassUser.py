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

                    dicLending[self.idUser] = dicFee
                else:
                    print('La persona solicitante no esta registrada')
        self.userExist = False


class Pay:
    idUser = 0
    selection = 0
    arrayFee = []
    pay = False

    def pay_fee(self):

        if not dicUser:
            print('No hay usuarios registrados')
        else:

            if not dicLending:
                print('Hasta el momento no se a realizado ningun prestamo')
            else:

                self.idUser = is_number('Digite el documento de la persona que realizara el pago: ')

                for lending in dicLending:

                    if lending == self.idUser:

                        for fee in dicLending[lending]:

                            if not dicLending[lending][fee]['status']:
                                self.pay = True
                                self.arrayFee.append(fee)
                                print('Cuota sin pagar numero {} por un valor de {} '
                                      .format(fee, dicLending[lending][fee]['value']))

        if self.pay:

            paid = False

            while not paid:

                numFee = is_number('Digite el numero de la cuota que desea pagar: ')

                for nF in self.arrayFee:
                    if nF == numFee:
                        dicLending[self.idUser][numFee]['status'] = True
                        paid = True
        self.pay = False


class Report:
    idUser = 0

    def paid_fees(self):
        if not dicUser:
            print('No existen usuarios registrados en el sistema')
        else:
            if not dicLending:
                print('No hay prestamos registrados')
            else:
                self.idUser = is_number('Digite el numero de documento: ')
                if dicUser[self.idUser]:
                    if dicLending[self.idUser]:
                        totalPaid = 0
                        value = 0
                        pay = 0
                        for fee in dicLending[self.idUser]:
                            if dicLending[self.idUser][fee]['status']:
                                totalPaid = totalPaid + 1
                                pay = dicLending[self.idUser][fee]['value']
                                value = value + dicLending[self.idUser][fee]['value']
                        print("""
                        Usted a pagado {} cuotas por un valor de {} 
                        que suma un total de {}
                        """.format(totalPaid, pay, value))

                    else:
                        print('Este usuario no ha solicitado prestamos')

                else:
                    print('Este usuario no se encuentra registrado')


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


user = User()
user.create_user()
user.create_lending()
user.pay_fee()
user.pay_fee()
user.pay_fee()
user.paid_fees()
print(mainDic)
