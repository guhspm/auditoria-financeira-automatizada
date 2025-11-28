# Automação de Conciliação Financeira (Financial Reconciliation) 💰🔍

## 📋 Sobre o Projeto
Este projeto resolve um dos maiores gargalos de departamentos financeiros: a **conferência manual de movimentações** (Conciliação Bancária vs. Sistema ERP).

Utilizando Python e Pandas, o script realiza o cruzamento ("matching") de milhares de transações em segundos, identificando divergências de valores, datas ou lançamentos não contabilizados que passariam despercebidos pelo olho humano.

**Impacto:** Redução de risco operacional, garantia de compliance e fechamento mensal mais ágil.

## 🚀 Funcionalidades
- **Ingestão de Dados:** Leitura flexível de extratos (OFX/CSV) e relatórios de ERP (Excel).
- **Normalização Inteligente:** Padronização de datas e limpeza de caracteres em descrições históricas.
- **Algoritmo de Matching:** Cruzamento baseado em Chaves Únicas (ID Transação) ou Chaves Compostas (Data + Valor + CNPJ).
- **Relatório de Exceções:** Gera um Excel contendo **apenas** as divergências encontradas (Sobra de Caixa / Falta de Caixa).

## 🛠 Stack Tecnológica
- **Python 3.x**
- **Pandas:** O motor de processamento de dados (DataFrames, Merge, GroupBy).
- **NumPy:** Vetorização para cálculos rápidos de ponto flutuante.

## ⚡ Como testar (Simulação)
Para garantir a privacidade dos dados financeiros reais, incluí um gerador de dados fictícios.

1. Clone o repositório.
2. Gere as bases de teste (Sistema vs Banco):
   ```bash
   python gerar_bases_teste.py
