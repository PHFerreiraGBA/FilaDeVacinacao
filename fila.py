from elemento import Elemento

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    #fabrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e

    def imprimeFila(self):
        aux = self.primeiro
        if(aux != None):
            while(aux != None):
                print(aux.valor)
                aux = aux.proximo
        else:
            print("--- Fila Vazia ---")
    
    def contaItensFila(self):
        aux = self.primeiro
        if(aux != None):
            itensFila = 1
            while(aux != None):
                itensFila + 1
                aux = aux.proximo
            return itensFila
        else:
            return 0
    
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
        if(aux != None):
            #PEGAR O PONTEIRO PRIMEIRO e apontar para o SEGUNDO
            self.primeiro = self.primeiro.proximo
            #DEPOIS eu apago o aux, pois o aux estava apontando
            #para o primeiro elemento:
            del(aux)
        else:
            # NAO TEM ELEMENTO
            print("--- Fila Vazia ---")