import os

class Neighborhood:
    def __init__(self, vector_line):
        self.vector_line = vector_line
        self.name = vector_line[0]

    def __str__(self):
        resposta = ""
        for i in self.vector_line:
            resposta = resposta + i + ";"
        
        return resposta

    @staticmethod
    def list_show(neighborhoods):
        for nb in neighborhoods:
            for i in nb.vector_line:
                print(i)
            print()

    @staticmethod
    def list_read_file(neighborhoods, file_name="neighborhood.dat"):
        try:
            reader = open(file_name, "r", encoding='utf8')                        
            for line in reader:
                vector_line = line.split(";")
                vector_line[-1] = vector_line[-1].replace("\n","")
                
                neighborhoods.append(Neighborhood(vector_line))
            reader.close()
        except:
            print("Reading problems..\n")

    @staticmethod
    def correct_neighborhood_name(diseases, neighborhoods):
        for disease in diseases:
            found = False
            for neighborhood in neighborhoods:                
                for i in neighborhood.vector_line:                    
                    if ((disease.neighborhood.upper() == i.upper()) or (disease.neighborhood.upper() in i.upper()) or (i.upper() in disease.neighborhood.upper())):
                        # print(disease.neighborhood.upper(), i.upper())
                        # os.system("pause")
                        disease.neighborhood_corrected = neighborhood.name.upper()
                        found = True
                        break
            if (not found):
                # print(disease.neighborhood.upper())
                disease.neighborhood_corrected = 'DESCONHECIDO'  #input("Que bairro gostaria de cadastrar? ")                
    