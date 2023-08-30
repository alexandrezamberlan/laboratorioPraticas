from disease import Disease

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
                        diseases.append(Disease(vector_line[0], vector_line[1], vector_line[2], vector_line[3], vector_line[4], vector_line[5]))                
            
            reader.close()
        except:
            print("Reading problems..\n")
            