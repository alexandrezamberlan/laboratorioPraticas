from disease import Disease
import os

class Util:
    @staticmethod
    def list_show(diseases):
        i = 0
        for item in diseases:
            print(item)
            i += 1
        print("\nTotal records: ", i-1)

    @staticmethod
    def list_read_file(diseases, file_name):
        try:
            print(file_name)
            reader = open(file_name, "r", encoding='utf8')            
            
            for line in reader:
                if (";" in line):
                    vector_line = line.split(";")
                    if (len(vector_line) == 6 and vector_line[0] != ""):
                        vector_line[3].strip() #delete whitespace at the begin and at the end
                        vector_line[3] = vector_line[3].replace("  "," ")
                        diseases.append(Disease(vector_line[0], vector_line[1], vector_line[2], vector_line[3], vector_line[4], vector_line[5]))                
            
            reader.close()
        except:
            print("Reading problems..\n")
            

    @staticmethod
    def correct_neighborhood_name(diseases, neighborhoods):
        for disease in diseases:
            found = False
            for neighborhood in neighborhoods:
                for i in neighborhood.vector_line:
                    if disease.neighborhood.upper() in i.upper() or i.upper() in disease.neighborhood.upper():
                        disease.neighborhood_corrected = neighborhood.name.lower()
                        found = True
                        break
            if (not found):
                print(disease.neighborhood.upper())
                disease.neighborhood_corrected = input("Que bairro gostaria de cadastrar? ")                