from bs4 import BeautifulSoup as bs
from constants import BASENAME, URLS
from offre import Offre

from utils import clean_data, getCodeSource, rm_spec_char, save, verif_key_word

clean_data()

site = "emploici"

res = getCodeSource(URLS[site])
soup = bs(res, "html.parser")

blocs = soup.find_all("div", class_="job-search-result")
for b in blocs:
    print("-------------------------")
    bc = b.find_all("a")
    bd = bc[1] if len(bc) > 1 else bc[0]
    pname   = bd.get_text()
    plink   = "https://www.emploi.ci"+bd["href"]
    pdate   = b.find_all("p", class_="job-recruiter")[0].get_text()[:10]
    be = b.find_all("a", class_="company-name")
    pboite = be[0].get_text() if len(be) > 1 else "Inconnue"
    pdesc   = b.find_all("div", class_="search-description")[0].get_text()
    pname, pboite = rm_spec_char(pname), rm_spec_char(pboite)
    if verif_key_word(pname):
        offre = Offre(pname,plink,pdate,pboite,pdesc,site)
        confirm = save(offre)
print(f"checking of {site} is ok...")


    

    
    



