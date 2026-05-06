import os
import random
import pandas as pd
from datetime import datetime, timedelta

N_LINHAS = 1000
DATA_INICIO = datetime(2023, 10, 1)

os.makedirs('data/input', exist_ok=True)


def daterange(start_date, n):
    return [start_date + timedelta(days=random.randint(0, 30)) for _ in range(n)]


def gerar_base_erp() -> pd.DataFrame:
    dados = {
        'ID_Transacao': [f'TRX-{10000 + i}' for i in range(N_LINHAS)],
        'Data_Lancamento': daterange(DATA_INICIO, N_LINHAS),
        'Historico': [f'PGTO FORNECEDOR {random.randint(1, 50)}' for _ in range(N_LINHAS)],
        'Valor': [round(random.uniform(10.0, 5000.0), 2) for _ in range(N_LINHAS)],
        'Departamento': [random.choice(['TI', 'RH', 'MKT', 'OPS']) for _ in range(N_LINHAS)],
    }
    return pd.DataFrame(dados)


def gerar_extrato_bancario(df_erp: pd.DataFrame) -> pd.DataFrame:
    df = df_erp[['ID_Transacao', 'Data_Lancamento', 'Valor']].copy()

    # Transações presentes no ERP mas ausentes no banco
    indices_remover = random.sample(range(N_LINHAS), 5)
    df = df.drop(indices_remover)

    # Divergências de valor (ex.: tarifas embutidas)
    indices_erro = random.sample(list(df.index), 3)
    df.loc[indices_erro, 'Valor'] += 0.50

    # Lançamentos exclusivos do banco (tarifas ou depósitos não identificados)
    tarifas = pd.DataFrame({
        'ID_Transacao': ['TAR-001', 'TAR-002'],
        'Data_Lancamento': [DATA_INICIO, DATA_INICIO],
        'Valor': [-15.90, -15.90],
    })
    return pd.concat([df, tarifas], ignore_index=True)


if __name__ == '__main__':
    print("Gerando bases financeiras sintéticas...")

    df_erp = gerar_base_erp()
    df_erp.to_excel('data/input/Base_Razao_ERP_Dummy.xlsx', index=False)
    print("  Base ERP gerada.")

    df_banco = gerar_extrato_bancario(df_erp)
    df_banco.to_csv('data/input/Extrato_Bancario_Dummy.csv', index=False, sep=';')
    print("  Extrato bancário (com divergências) gerado.")

    print("\nPronto. Execute o script de conciliação para identificar as diferenças.")
