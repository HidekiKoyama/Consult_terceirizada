class Query():
    def readDoc(self):
        with open('query/teste.txt', 'r') as consulta:
            consult = consulta.read()
            
        return consult