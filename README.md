# malha-rodoviaria
Trabalho final de Redes Complexas (SME0130)

Projeto baseado no artigo **"Networks and Cities: An Information Perspective"** (Rosvall et al., 2005 - https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.94.028701), focado na análise de grafos de cidades em termos de informação de navegação.

---
## Integrantes
 - Heitor Carvalho Pinheiro
 - João Gabriel Rego
 - Renan Gonzales                   N

---

## Sobre

O projeto realiza análise de malha rodoviária. Para tanto, toma-se em mente que **nós representam ruas** e **arestas, interseções**. O objetivo deste projeto é:

- Realizar uma análise exploratória básica das redes;
- Calcular a **Search Information** (\(\bar{S}\)) para cada rede;
- Calcular o **Access Information** (\(A(s)\)) para cada nó;
- Identificar propriedades locais como número de triângulos e quadrados;
- Concluir quais países ou cidades são os mais fáceis de se navegar.

---

## Estrutura de Pastas

```plaintext
data/
    arquivos.mtx                   # Arquivo exemplo
notebooks/
    <numero>_<finalidade>.ipynb    # Notebook de análise básica
src/
    basic/                         # Funções para operações básicas
    metrics/                       # Funções para cálculos de métricas
    visualization/                 # Funções para visualização dos grafos
requirements.txt
README.md
```

---

## Instalação dos Requisitos

Para instalar todas as dependências necessárias, execute:

```bash
pip install -r requirements.txt
```

