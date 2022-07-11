class Bolan():
    
    N_year_sim = 3
    max_skuldkvot = 6
    
    def __init__(self, kontantinsats=0, bruttolon=0, manadssparande=0,
                 loneokning_pct=0, bolan_ranta=0.02, blanco_ranta=0.05,
                 manadsavgift=0):
        self.kontantinsats = kontantinsats
        self.bruttolon = bruttolon
        self.manadssparande = manadssparande
        self.loneokning_pct = loneokning_pct
        self.bolan_ranta = bolan_ranta
        self.blanco_ranta = blanco_ranta
        self.manadsavgift = manadsavgift
        
        
    
        
        