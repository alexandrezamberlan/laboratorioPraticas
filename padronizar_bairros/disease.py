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