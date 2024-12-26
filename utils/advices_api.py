import requests
import dotenv, os


dotenv.load_dotenv()
site_frases = os.environ['site_frases']

def busca_frase():
    res = requests.get(site_frases)
    
    if res.status_code != 200:
        return None
    
    frase = res.json()['slip']['advice']

    res.close()
    
    return frase