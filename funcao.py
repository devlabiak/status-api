import requests

def status_api(api):
    dados_saude = requests.get(url= api) #observar status que retorna
    dados_saude = str(dados_saude.status_code)
    
    
    if '2' not in dados_saude:
        return(f'API NÃO ESTA ONLINE : STATUS {dados_saude}')
    else:
        return(f'API ESTA ONLINE : STATUS {dados_saude}')