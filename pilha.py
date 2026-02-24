from elemento import Elemento

class Pilha:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    #fabrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e

    def imprimePilha(self):
        aux = self.primeiro
        if(aux != None):
            while(aux != None):
                print(aux.valor)
                aux = aux.proximo
        else:
            print("--- Pilha Vazia ---")
    
    def addElemento(self, valorQualquer):
        objeto = self.criarNovoElemento(valorQualquer)
        aux = self.primeiro

        if aux == None:
            self.primeiro = objeto
            self.ultimo = self.primeiro
        elif aux.proximo == None:
            self.primeiro.proximo = objeto
            self.ultimo = self.primeiro.proximo
        else:    
            while (aux.proximo != None):
                aux = aux.proximo
            aux.proximo = objeto
            self.ultimo = aux.proximo
    
    def removeElemento(self):
        aux = self.primeiro
        if aux == None:
            print("--- Pilha Vazia ---")
        elif aux.proximo == None:
            del(aux)
            self.primeiro = None
            self.ultimo = self.primeiro
        else:
            while (aux.proximo.proximo != None):
                aux = aux.proximo
            
            del(aux.proximo)
            aux.proximo = None
            self.ultimo = aux