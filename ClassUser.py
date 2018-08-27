dicUser = {}
dicLending = {}
mainDic = {'Users': dicUser, 'Lendings': dicLending}


class Lending:
    id = 0
    idUser = 0
    valLending = 0
    fee = 0

    def createLending(self):
        self.idUser = int(input('digite el numero de documento de la persona solicitante: '))
        self.valLending = int(input('Que valor desea solicitar para este prestamo: '))
        self.fee = int(input('en cuantas cuotas desea cancelar el prestamo? '))
        val = self.valLending / self.fee

        dicFee = {}


        for fee in range(0, self.fee):
            dicFee[fee] = {'value': val, 'status': False}

        dicLending[self.idUser] = {'valLending': self.valLending, 'fee': dicFee}


# class Pay:
#
#
#     def payFee:





class User(Lending):
    name = ''
    lastName = ''
    document = 0
    address = ''

    def createUser(self):
        self.name = input('digite su nombre: ')
        self.lastName = input('digite sus apellidos: ')
        self.document = int(input('digite el numero de documento: '))
        self.address = input('digite su direccion de recidensia: ')
        dicUser[self.document] = {'name': self.name, 'lastName': self.lastName, 'address': self.address}


user = User()
user.createUser()
user.createLending()
print(dicUser)
print()
print(dicLending)

print()

print(mainDic)
