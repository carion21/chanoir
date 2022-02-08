import json
import pandas as pd

class Offre():
    def __init__(self, pnom, plien, pdate, pboite, pdesc, siteweb):
        self.pnom   = pnom
        self.plien  = plien
        self.pdate  = pdate
        self.pboite = pboite
        self.pdesc  = pdesc
        self.siteweb= siteweb

    def to_json(self):
        odict = {
            "pnom"  : [self.pnom],
            "plien" : [self.plien],
            "pdate" : [self.pdate],
            "pboite": [self.pboite],
            "pdesc" : [self.pdesc],
            "siteweb": [self.siteweb]
        }
        return odict

    def to_df(self):
        oj = self.to_json()
        odf = pd.DataFrame(oj)
        return odf
        

        

    