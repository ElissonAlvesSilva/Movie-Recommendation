from recomendacao import *

base = carregaMovieLens()

#print (getRecomendacoes(base,'212'))
#print (getSimilares(base, '1'))
#print (calculaItensSimilares(avaliacoesFilme))
#print (getRecomendacoes(avaliacoesUsuario, 'Leonardo'))
listaItens = calculaItensSimilares(avaliacoesFilme)
print (getRecomendacoesItens(avaliacoesUsuario,listaItens, 'Leonardo'))