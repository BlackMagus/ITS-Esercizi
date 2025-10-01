class Pagamento:

    def setImporto(self, importo:float):
        self.importo = importo

    def getImporto(self) -> float:
        return self.importo

        
    def dettagliPagamento(self):
        print(f"Importo del pagamento: {self.importo: .2f}")