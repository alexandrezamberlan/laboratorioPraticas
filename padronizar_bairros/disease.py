class Disease:
   
    def __init__(self, cid, description, city, neighborhood, amount, percentage):
        self.cid = cid
        self.description = description
        self.city = city
        self.neighborhood = neighborhood
        self.amount_casos = amount
        self.percentage = percentage
        self.neighborhood_corrected = ""


    def __str__(self):
        return self.neighborhood + ";" + self.neighborhood_corrected 
    
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
            # print(file_name)
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
            
            

    