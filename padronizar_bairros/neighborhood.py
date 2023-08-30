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
    def list_read_file(neighborhoods, file_name="neighborhood.dat"):
        try:
            reader = open(file_name, "r", encoding='utf8')            
            
            for line in reader:
                vector_line = line.split(";")
                neighborhoods.append(Neighborhood(vector_line))
            reader.close()
        except:
            print("Reading problems..\n")
    