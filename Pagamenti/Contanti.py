from Pagamenti import Pagamento

class PagamentoContanti(Pagamento):

    def dettagliPagamentoContanti(self):
        print(f"{self.dettagliPagamento()} da pagare in contanti con: ")

    def inPezziDa(self):
        