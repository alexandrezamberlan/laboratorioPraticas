class Disease:
   
    def __init__(self, cid, description, city, neighborhood, amount, percentage):
        self.cid = cid
        self.description = description
        self.city = city
        self.neighborhood = neighborhood
        self.amount_cases = amount
        self.percentage = percentage
        self.neighborhood_corrected = ""


    def __str__(self):
        return self.cid+";"+self.description+";"+self.city+";"+self.neighborhood_corrected+";"+self.amount_cases+";"+self.percentage
    
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
                        vector_line[-1] = vector_line[-1].replace("\n","")
                        diseases.append(Disease(vector_line[0], vector_line[1], vector_line[2], vector_line[3], vector_line[4], vector_line[5]))                            
            reader.close()
        except:
            print("Reading problems..... File not found....\n")
            exit(0)

    @staticmethod
    def create_new_file(diseases, file_name):
        try:
            vetor_name_file = file_name.split('.')
            new_file_name = vetor_name_file[0] + "_corrected." + vetor_name_file[-1]
            print('The original file was kept, but a new file with the modifications was created...', new_file_name)           

            writer = open(new_file_name, "w",encoding='utf8')                        
            for disease in diseases:
                # print(disease)
                writer.write(disease.cid+";"+disease.description+";"+disease.city+";"+disease.neighborhood_corrected+";"+disease.amount_cases+";"+disease.percentage+"\n")
                
            writer.close()
        except:
            print("Writing problems..It was impossible to write in the destination file...\n")  
            

    