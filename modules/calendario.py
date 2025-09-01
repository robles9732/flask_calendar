import numpy as np
import calendar
from datetime import date, datetime

class ObterCalendario:
    def __init__(self):
        self.data_atual = datetime.now() # data atual
        #self.data_atual = datetime(yyyy, m, d)  #Teste outros meses com datetime(ano, mês, 1)
        self.dia_hoje = self.data_atual.day
        self.mes = self.data_atual.month # valor mês da data
        self.ano = self.data_atual.year # valor ano da data 
        qde_dias = calendar.monthrange(self.ano, self.mes)[1] # captura a quantidade de dias do mês/ano selecionado, usando a biblioteca calendar       
        self.lista_dias=[str(i) for i in range(1,(qde_dias+1))] # popula a lista de dias com os números no formato string
        for dia in range(42-qde_dias): # verifica quandos dias foram preenchidos e quanto faltou para 42, que é a resposta sempre 
            self.lista_dias.append('')    # Preenche a quantidade de itens faltantes até atingir 42
        self.matriz = np.array(self.lista_dias).reshape(6,7)  # Usa a bilbioteca numpy para gerar uma matriz de 6 linhas (semanas) por 7 colunas (dias da semana)
        self.inicio_do_mes = date(self.ano, self.mes, 1)   # Define o dia primeiro do mês como data usando a biblioteca datetime
        self.dia_da_semana = self.inicio_do_mes.weekday() # define em que dia da semana o dia primeiro cai, usando a função weekday do datetime 
        self.matriz_deslocada = np.roll(self.matriz, shift=self.dia_da_semana) # Desloca a matriz usando a função roll() do numpay, para alinhar o dia 1 com o dia da semana, na matriz
        self.lista_meses=['Janeiro',    # gera uma lista com os nomes dos meses
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
        
    @property 
    def matriz_dias(self):
        return self.matriz_deslocada
        
    @property
    def ano_numero(self):
        return str(self.ano)
    
    @property
    def mes_atual(self):
        return str(self.mes)
    
    @property
    def dia_de_hoje(self):
        return str(self.dia_hoje)
    
    @property
    def mes_nome(self):
        self.mes_nome_atual = self.lista_meses[self.mes-1] # Retorna o mês atual com base na posição da lista
        return self.mes_nome_atual
