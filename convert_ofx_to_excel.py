import sys
import ofxparse
import pandas as pd

# Ler o arquivo OFX
with open('file.ofx', encoding='utf-8') as file:
    ofx = ofxparse.OfxParser.parse(file)

# Extraindo as transações
transactions = []
for transaction in ofx.account.statement.transactions:
    transactions.append({
        'Data': transaction.date,
        'Descrição': transaction.memo,
        'Valor': transaction.amount        
    })

# Converter para DataFrame
df = pd.DataFrame(transactions)

# Exportar para Excel
df.to_excel('transacoes.xlsx', index=False)

sys.exit()