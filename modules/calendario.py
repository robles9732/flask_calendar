import numpy as np
import calendar
from datetime import date, datetime

def obter_calendario():
    hoje = datetime.now() # data atual
    dia_hoje = hoje.day
    mes = hoje.month # valor mês da data
    ano = hoje.year # valor ano da data 
    qde_dias = calendar.monthrange(ano, mes)[1] # captura a quantidade de dias do mês/ano selecionado, usando a biblioteca calendar
    
    lista_dias=[str(i) for i in range(1,(qde_dias+1))] # popula a lista de dias com os números no formato string
    for dia in range(42-qde_dias): # verifica quandos dias foram preenchidos e quanto faltou para 42, que é a resposta sempre 
        lista_dias.append('')    # Preenche a quantidade de itens faltantes até atingir 42

    matriz = np.array(lista_dias).reshape(6,7)  # Usa a bilbioteca numpy para gerar uma matriz de 6 linhas (semanas) por 7 colunas (dias da semana)

    comeco_do_mes = date(ano, mes, 1)   # Define o dia primeiro do mês como data usando a biblioteca datetime
    dia_da_semana = comeco_do_mes.weekday() # define em que dia da semana o dia primeiro cai, usando a função weekday do datetime 
    lista_meses=['Janeiro',    # gera uma lista com os nomes dos meses
              'Fevereiro', 
              'Março', 
              'Abril', 
              'Maio', 
              'Junho', 
              'Julho',
              'Agosto',
              'Setembro',
              'Outubro',
              'Novembro',
              'Dezembro'
              ]
    nome_mes = lista_meses[mes-1]  # Encontra o mês escolhido no índice da lista, já que os meses estão entre 1 a 12, e os indices entre 0 a 11
    matriz_deslocada = np.roll(matriz, shift=dia_da_semana) # Desloca a matriz usando a função roll() do numpay, para alinhar o dia 1 com o dia da semana, na matriz

    return [matriz_deslocada, nome_mes, str(dia_hoje)] # Retorna a matriz em forma de lista de listas "[0]" o nome do mês "[1]" e o dia atual "[2]"


