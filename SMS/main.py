import pandas as pd
from twilio.rest import Client

# pandas
# openpyxl
# twilio

# Your Account SID from twilio.com/console
account_sid = "AC635c51734268a4a28e6078e3dd9bbf99"
# Your Auth Token from twilio.com/console
auth_token  = "cc216c13fad44c87ef9172ac3009ba39"

client = Client(account_sid, auth_token)

# Abrir os arquivos
# Verificar se algum valor da coluna 'vendas' é maior do que R$55.000,00
# Se for maior do que 55 mil -> Envia um SMS com o nome, o mês e as vendas do vendedor
lista_meses = ['janeiro', 'fevereiro','março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] >= 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000,'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: R$ {vendas:.2f}')
        message = client.messages.create(
            to="+5561991611255", 
            from_="+19402897558",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: R$ {vendas:.2f}')

print(message.sid)
