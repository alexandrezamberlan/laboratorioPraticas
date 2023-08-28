class Doenca:
    cid = 0
    descricao = ""
    cidade = ""
    bairro = ""
    quantidade_casos = 0
    porcentagem = 0
    bairro_tratado = ""

    def __init__(self, cid, descricao, cidade, bairro, quantidade, porcentagem):
        self.cid = cid
        self.descricao = descricao
        self.cidade = cidade
        self.bairro = bairro
        self.quantidade_casos = quantidade
        self.porcentagem = porcentagem


    def __str__(self):
        return self.cid + ";" + self.bairro + ";" + self.bairro_tratado 