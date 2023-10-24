import pandas as pd
from twilio.rest import Client

account_sid = 'AC383acd65da3f6ae8cdff2d9354f04730'
auth_token = 'ab8ccbc8cd1a1eb82531f495d71e53e2'
client = Client(account_sid, auth_token)
# passo a passo de solução
#instalar as bibliotecas
# openpyxl - twilio - pandas

# abrir os 6 arquivos em excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']
# lista de meses, destacando os resultados
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# para cada arquivo:
# verificar se algum valor na coluna vendas naquele arquivo é maior que 55k
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor},Vendas:{vendas}')
# se for maior que 55k  -> envia um sms com o nome, o mes e as vendas do vendedor
        message = client.messages.create(
            to="+5511972912678",
            from_="+15302987949",
            body =f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor},Vendas:{vendas}')
        print(message.sid)
# caso nao seja maior que 55k nao quero fazer nada