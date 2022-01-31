from bs4 import BeautifulSoup as bs
from constants import URLS
from offre import Offre

from utils import getCodeSource, save

site = "emploici"

res = getCodeSource(URLS[site])
soup = bs(res, "html.parser")

blocs = soup.find_all("div", class_="job-search-result")

pnames, plinks, pdates, pboites, pdescripts = [[] for _ in range(5)]
for b in blocs:
    print("--------------------------------------")
    #n = 
    pname   = b.find_all("a")[1].get_text()
    plink   = "https://www.emploi.ci"+b.find_all("a")[1]["href"]
    pdate   = b.find_all("p", class_="job-recruiter")[0].get_text()[:10]
    pboite  = b.find_all("a", class_="company-name")[0].get_text()
    pdesc  = b.find_all("div", class_="search-description")[0].get_text()

    offre = Offre(pname,plink,pdate,pboite,pdesc)
    confirm = save(offre)
    if not confirm:
        break

    
    



