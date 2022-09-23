class Cta_Func:
    
    def __init__(self):
        self.arrivals = {}

    def get_arrivals(self, list_of_arrivals):
        """
        Creates dictionary ordered by destination and arrival times
        """
        for arrival in list_of_arrivals:
            if arrival['destNm'] in self.arrivals:
                self.arrivals[arrival['destNm']].append(arrival['arrT'])
            else:
                self.arrivals[arrival['destNm']] = [arrival['arrT']]

        return self.arrivals

    
    #def display_arrivals(self)