from disease import Disease
from neighborhood import Neighborhood

import os

os.system("cls")

neighborhoods = []
Neighborhood.list_read_file(neighborhoods)
# Neighborhood.list_show(neighborhoods)

diseases = []
file_name = input('Enter the name of the file downloaded from the city hall in the format .csv: ') #"dengue_julho.csv"
Disease.list_read_file(diseases, file_name)
# Disease.list_show(diseases)

Neighborhood.correct_neighborhood_name(diseases, neighborhoods)
# Disease.list_show(diseases)

Disease.create_new_file(diseases, file_name)