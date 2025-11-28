Aviso de Privacidade: Este projeto foi desenvolvido seguindo as melhores práticas de LGPD. Nenhum dado financeiro real está contido neste repositório; os scripts de demonstração utilizam dados sintéticos gerados aleatoriamente.

Desenvolvido Gustavo Henrique Santos Pinheiro


### 5. O Gerador de Dados Fictícios (`gerar_bases_teste.py`)
Esse script cria o cenário perfeito: duas planilhas parecidas, mas com erros propositais para seu código achar. Crie o arquivo e cole:

```python
import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Configuração
N_LINHAS = 1000
DATA_INICIO = datetime(2023, 10, 1)
OS_makedirs = os.makedirs
OS_makedirs('data/input', exist_ok=True)

print("--- Gerando Bases Financeiras (Sistema vs Banco) ---")

# Função para gerar datas aleatórias
def daterange(start_date, n):
    return [start_date + timedelta(days=random.randint(0, 30)) for _ in range(n)]

# --- 1. CRIAR A "VERDADE" (Base Sistema ERP) ---
# Vamos simular que o Sistema tem tudo registrado corretamente
dados_sistema = {
    'ID_Transacao': [f'TRX-{10000+i}' for i in range(N_LINHAS)],
    'Data_Lancamento': daterange(DATA_INICIO, N_LINHAS),
    'Historico': [f'PGTO FORNECEDOR {random.randint(1,50)}' for _ in range(N_LINHAS)],
    'Valor': [round(random.uniform(10.0, 5000.0), 2) for _ in range(N_LINHAS)],
    'Departamento': [random.choice(['TI', 'RH', 'MKT', 'OPS']) for _ in range(N_LINHAS)]
}
df_sistema = pd.DataFrame(dados_sistema)
df_sistema.to_excel('data/input/Base_Razao_ERP_Dummy.xlsx', index=False)
print("-> Base ERP gerada com sucesso.")

# --- 2. CRIAR O "PROBLEMA" (Extrato Bancário com Divergências) ---
# Copiamos o sistema, mas vamos bagunçar um pouco
df_banco = df_sistema.copy()
df_banco = df_banco[['ID_Transacao', 'Data_Lancamento', 'Valor']] # Banco tem menos colunas

# CASO 1: Transações que existem no Sistema mas NÃO caíram no Banco (Cheque não compensado?)
# Removemos 5 linhas aleatórias
indices_remover = random.sample(range(N_LINHAS), 5)
df_banco = df_banco.drop(indices_remover)

# CASO 2: Erro de Valor (Tarifa bancária embutida?)
# Alteramos o valor de 3 transações
indices_erro = random.sample(list(df_banco.index), 3)
for idx in indices_erro:
    df_banco.loc[idx, 'Valor'] += 0.50 # Diferença de 50 centavos

# CASO 3: Transação que só existe no Banco (Tarifa ou Depósito não identificado)
novas_linhas = pd.DataFrame({
    'ID_Transacao': ['TAR-001', 'TAR-002'],
    'Data_Lancamento': [DATA_INICIO, DATA_INICIO],
    'Valor': [-15.90, -15.90]
})
df_banco = pd.concat([df_banco, novas_linhas], ignore_index=True)

df_banco.to_csv('data/input/Extrato_Bancario_Dummy.csv', index=False, sep=';')
print("-> Base Bancária (com divergências) gerada com sucesso.")
print("\nPronto! Agora rode seu script de conciliação para achar os erros.")
