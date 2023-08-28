from doenca import Doenca

class Util:
    @staticmethod
    def exibir_lista(doencas):
        i = 0
        for item in doencas:
            print(item)
            i += 1
        print("\nTotal de registros: ", i)

    @staticmethod
    def ler_arquivo_popular_lista(doencas):
        try:
            nome_arquivo = "dengue_julho.csv"
            print(nome_arquivo)
            leitor = open(nome_arquivo, "r", encoding='utf8')
            
            for linha in leitor:
                vetor_linha = linha.split(";")
                doencas.append(Doenca(vetor_linha[0], vetor_linha[1], vetor_linha[2], vetor_linha[3], vetor_linha[4], vetor_linha[5]))                
            
            leitor.close()
        except:
            print("Problema de leitura..\n")
            