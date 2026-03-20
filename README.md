# 🔍 Auditoria Financeira Automatizada — Conferência Integrada
> Sistema completo de conferência financeira entre arquivo de movimento (folha) e prévia da operadora — valida layout, detecta duplicidades, aplica regras de negócio e confronta valores por entidade.

![Python](https://img.shields.io/badge/Python-3.10+-8b5cf6?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-8b5cf6?style=flat-square&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Produção-22c55e?style=flat-square)

---

## 📌 Sobre o Projeto

Sistema de auditoria financeira integrada desenvolvido para conferência mensal entre o **arquivo de movimento posicional** (folha de pagamento) e os **arquivos de prévia da operadora** (PRE_PGTO + COPART).

O script processa múltiplas entidades em sequência (URBEL, HOB, SAMU, BHTRANS, PBH_CONSOLIDADO, etc.), executa 4 camadas de validação e gera um **relatório consolidado final** com as diferenças financeiras por natureza de verba.

**Problema resolvido:** a conferência manual entre movimento e prévia exigia cruzar centenas de linhas de arquivos posicionais com lógica de negócio complexa por entidade. O script executa tudo automaticamente, aponta cada divergência com diagnóstico e gera relatório pronto para análise.

---

## 🚀 Funcionalidades

**Camada 1 — Conferência de Layout:**
- ✅ Valida CPF Titular e CPF Dependente (11 dígitos)
- ✅ Valida CNPJ da operadora (14 dígitos)
- ✅ Detecta Consignação zerada (`00000000000000000`)
- ✅ Exporta inconsistências em CSV com motivo por linha

**Camada 2 — Auditoria de Duplicidade:**
- ✅ Detecta registros duplicados por chave `MATRICULA + COD VERBA`
- ✅ Exporta duplicatas com valor formatado em R$

**Camada 3 — Regras de Negócio (14U3/24U3):**
- ✅ Verifica se as verbas 14U3 e 24U3 estão vinculadas à carteirinha correta do titular (verba 21U1)
- ✅ Sinaliza matrícula sem verba de referência e carteirinha incorreta

**Camada 4 — Conferência Financeira (Movimento × Prévia):**
- ✅ Lê arquivos posicionais de movimento por largura fixa (`read_fwf`)
- ✅ Cruza com tabela de verbas vigentes (`verbas_vigentes.csv`)
- ✅ Agrupa por natureza: MENSALIDADE, SUBSÍDIO, COPARTICIPAÇÃO, PRÓ-RATA, CRÉDITOS
- ✅ Confronta com prévia (PRE_PGTO + COPART) por entidade
- ✅ Calcula diferença `VALOR_MOVIMENTO − VALOR_PRÉVIA` por natureza
- ✅ Detalha divergências de mensalidade e coparticipação individualmente
- ✅ Gera `RELATORIO_CONSOLIDADO_FINAL.csv` com todas as entidades

---

## 🛠️ Stack

| Tecnologia | Uso |
|---|---|
| Python 3.10+ | Lógica principal |
| Pandas | Leitura posicional (`read_fwf`), merge e agregação |
| glob | Descoberta automática de arquivos por prefixo |
| typing | Tipagem de funções para manutenibilidade |

---

## 📁 Estrutura

```
auditoria-financeira-automatizada/
├── conferenciamovimento.py     # Script principal de auditoria integrada
├── requirements.txt
├── .gitignore
└── README.md

# Arquivos esperados na mesma pasta (não versionados — dados sensíveis):
├── verbas_vigentes.csv              # Tabela de códigos e naturezas de verba
├── MOV_URBEL*.txt                   # Arquivo de movimento posicional
├── MOV_HOB*.txt
├── MOV_SAMU*.txt
├── MOV_BHTRANS*.txt
├── MOV_DIRETA*.txt / MOV_AEG*.txt   # PBH Consolidado
├── URBEL*PRE_PGTO*.txt              # Prévia de pagamento
├── URBEL*COPART*.txt                # Prévia de coparticipação
└── ...                              # Idem para cada entidade
```

---

## ⚙️ Como Executar

```bash
pip install -r requirements.txt

# Coloque todos os arquivos .txt e o verbas_vigentes.csv na mesma pasta
python conferenciamovimento.py
```

O script processa todas as entidades configuradas em sequência e ao final solicita confirmação para gerar o relatório consolidado.

---

## 📈 Exemplo de Output

```
********************************************************************************
         INICIANDO CONFERÊNCIA INTEGRADA (ESTRUTURA + FINANCEIRA)
********************************************************************************

********************************************************************************
                        PROCESSANDO ENTIDADE: URBEL
********************************************************************************
✅ CONFERÊNCIA DE LAYOUT: Nenhuma inconsistência estrutural crítica encontrada.
✅ CONFERÊNCIA ESTRUTURAL: Nenhuma duplicidade encontrada.
✅ REGRA DE NEGÓCIO 14U3/24U3: Verbas aderentes à regra de Carteirinha.

=================================================================
RESULTADO DA CONFERÊNCIA FINANCEIRA - URBEL
=================================================================
               NATUREZA  VALOR_MOVIMENTO   VALOR_PREVIA     DIFERENCA
   MENSALIDADE (VALOR CHEIO)  R$ 48.320,00  R$ 48.320,00      R$ 0,00
           COPARTICIPACAO      R$ 3.214,50   R$ 3.214,50      R$ 0,00
                  CREDITO        R$ 890,00     R$ 890,00      R$ 0,00
=================================================================

[...processamento das demais entidades...]

Relatório Consolidado Final gerado com sucesso!
Arquivo salvo em: 'RELATORIO_CONSOLIDADO_FINAL.csv'
```

---

## 🏗️ Entidades Configuradas

O script processa as seguintes entidades por padrão:

| Entidade | Prefixo Movimento | Prefixo Prévia |
|---|---|---|
| URBEL | MOV_URBEL | URBEL |
| SUMOB | MOV_SUMOB | SUMOB |
| BHTRANS | MOV_BHTRANS | BHTRANS |
| HOB | MOV_HOB | HOSP_ODILON |
| PBH_ATIVOS | MOV_ATIVOS | PBH_ATIVOS_LOTE_ |
| PBH_CONSOLIDADO | MOV_DIRETA, MOV_AEG, MOV_APOSENTADOS, MOV_PENSIONISTAS | PBH |

Novas entidades podem ser adicionadas no dicionário `config_entidades` sem alterar a lógica principal.

---

## 👤 Autor

**Gustavo** — Dev & Founder · Inside.co

[![LinkedIn](https://img.shields.io/badge/LinkedIn-8b5cf6?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gustavo-henriquesp/)
[![Portfolio](https://img.shields.io/badge/Portfolio-8b5cf6?style=flat-square&logo=netlify&logoColor=white)](https://seusite.netlify.app)
[![Email](https://img.shields.io/badge/Email-8b5cf6?style=flat-square&logo=gmail&logoColor=white)](mailto:ghspdm@gmail.com)

---
> *"Construo soluções que outros apenas descrevem em planilhas."*
