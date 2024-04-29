import pandas as pd
import win32com.client as win32



# pegar dados planilha
tabela_vendas = pd.read_excel('Base_Vendas.xlsx')

#ver dados planilha
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# gerar faturamento loja x valor final
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

#quantida loja x lojas
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

#enviar resumos no email

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.TO = 'cnsetestes@gmail.com'
mail.Subject = 'Resumo de Vendas Por Filial'
mail.HTMLBody = f'''

<p>Ao Gerente das Filiais,</p>

<p>Por Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final' : 'R${:,.2f}'.format})}

<p>Por Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Se precisar de mais alguma informação, estou à disposição.</p>

<p>Att,</p>

<p>Thes</p>

'''
mail.Send()

print('Email enviado!!')