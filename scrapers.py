from bs4 import BeautifulSoup as bs
from constants import URLS
from offre import Offre

from utils import getCodeSource, rm_spec_char, save, verif_key_word

def scrap(site):
    sites = list(URLS.keys())
    if site == sites[0]:
        check_emploici()
    elif site == sites[1]:
        check_talent()
    else: pass

def check_emploici():
    site = "emploici"
    try:
        res = getCodeSource(URLS[site])
        soup = bs(res, "html.parser")

        blocs = soup.find_all("div", class_="job-search-result")
        for b in blocs:
            #print("-------------------------")
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
    except:
        print(f"checking of {site} is failed...")

def check_talent():
    site = "talent"
    try:
        res = getCodeSource(URLS[site])
        soup = bs(res, "html.parser")

        blocs = soup.find_all("div", class_="card__job")
        for b in blocs:
            #print("-------------------------")
            bc = b.find_all("div", class_="link-job-wrap")[0]
            bd = bc.find_all("div", class_="card__job-c")[0]
            pid= b.get("data-id")
            pname   = bd.select("h2.card__job-title > a.card__job-link.gojob")[0].get_text().lstrip().rstrip()
            pboite  = bd.select("div.card__job-info > div > div.card__job-empname-label")[0].get_text()
            plink   = f"https://ci.talent.com/view?id={pid}"
            pdate   = ""
            pdesc   = bd.select("div.card__job-snippet-logo > p")[0].get_text()
            pname, pboite = rm_spec_char(pname), rm_spec_char(pboite)
            if verif_key_word(pname):
                offre = Offre(pname,plink,pdate,pboite,pdesc,site)
                confirm = save(offre)
        print(f"checking of {site} is ok...")
    except:
        print(f"checking of {site} is failed...")


