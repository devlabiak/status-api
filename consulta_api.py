import time
from funcao import status_api

#Função que consulta se uma API esta no ar

inicio = time.time()


dados_saude = ('https://apidadosabertos.saude.gov.br/cnes/tipounidades')
status = status_api(dados_saude)
print(status)


fim = time.time()
#Tempo de resposta
tempo = fim - inicio
print('Tempo de execução {:.2f} MS' .format(tempo))


