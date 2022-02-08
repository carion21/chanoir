
from time import sleep
from constants import ACTIVATION, PERIOD_IN_HOUR, PERIOD_IN_SECS, URLS
from scrapers import scrap
from utils import clean_data

clean_data()

while ACTIVATION:
    for site in URLS:
        scrap(site)
    #period_in_seconds
    pis = PERIOD_IN_SECS
    print(f"Je me met en attente pour {pis} secondes...")
