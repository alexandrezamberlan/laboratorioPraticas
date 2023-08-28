from util import Util
import os

doencas = []

os.system("cls")
Util.ler_arquivo_popular_lista(doencas)
Util.exibir_lista(doencas)