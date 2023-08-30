from util import Util
from neighborhood import Neighborhood

import os

os.system("cls")

neighborhoods = []
Neighborhood.list_read_file(neighborhoods)
for nb in neighborhoods:
    for i in nb.vector_line:
        print(i)


# diseases = []
# file_name = "dengue_julho.csv"
# Util.list_read_file(diseases, file_name)
# Util.list_show(diseases)