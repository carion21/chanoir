import requests as rq
import pandas as pd
from constants import BASENAME

from offre import Offre


def getCodeSource(url):
    res = rq.get(url)
    return res.text

def save(offre : Offre):
    try:
        try:
            base = pd.read_csv(BASENAME)
            n = base[base["plien"] == offre.plien].shape[0]
            if n == 0:
                base = pd.concat([base,offre.to_df()], ignore_index=True)
                base.to_csv(BASENAME, index=False)
        except:
            odf = offre.to_df()
            odf.to_csv(BASENAME, index=False)
        return True
    except:
        return False