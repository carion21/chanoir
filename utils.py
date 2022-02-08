import requests as rq
import pandas as pd
from os import remove, path

from constants import BASENAME, WKEYS


from offre import Offre

def clean_data():
    if path.isfile(BASENAME):
        remove(BASENAME)
        print("Removing %s" % BASENAME)
    else:
        print("File %s not existing" % BASENAME)

def getCodeSource(url):
    res = rq.get(url)
    return res.text

def save(offre : Offre) -> bool:
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

def verif_key_word(text : str) -> bool:
    text = text.lower()
    verif = False
    for key in WKEYS:
        if key in text:
            verif = True
    return verif

def rm_spec_char(text : str) -> str:
    text = ''.join([l for l in text if l.isalnum() or l == ' '])
    return text