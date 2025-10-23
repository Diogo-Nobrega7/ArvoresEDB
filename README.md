# Implementação de Árvores AVL e Rubro-Negra

Este projeto contém implementações em Python de uma **Árvore AVL** (auto-balanceada por altura) e uma **Árvore Rubro-Negra** (auto-balanceada por cor). O script fornece um menu interativo de console para criar, manipular e visualizar ambas as estruturas de dados.

## Dependências

Nenhuma dependência externa é necessária. O script utiliza apenas a biblioteca padrão do Python.

## Como Executar

Como é um script Python, não há necessidade de compilação.
1.  Faça o download do arquivo `.py` diretamente do repositório.
2.  Abra um terminal no diretório onde o arquivo foi salvo.
3.  Execute o script:

```bash
py arvores.py
```

## Operações Disponíveis

O programa apresenta um menu principal onde você pode escolher qual tipo de árvore deseja utilizar.

### Menu Principal

1.  **Árvore AVL**: Cria ou utiliza a instância de Árvore AVL.
2.  **Árvore Rubro-Negra**: Cria ou utiliza a instância de Árvore Rubro-Negra.
3.  **Sair**: Encerra o programa.

### Menu de Operações (Para AVL e Rubro-Negra)

Após escolher um tipo de árvore, você terá acesso às seguintes operações:

1.  **Inserir elemento**: Adiciona um novo valor à árvore. 
2.  **Remover elemento**: Remove um valor existente da árvore. 
3.  **Buscar elemento**: Verifica se um valor existe na árvore.
4.  **Imprimir árvore**: Exibe a estrutura da árvore em **pré-ordem**.
5.  **Voltar ao menu principal**: Retorna à tela de seleção de tipo de árvore.

## Exemplo de Uso (Entrada e Saída)

```bash
===== MENU PRINCIPAL =====
Qual tipo de árvore deseja criar/usar?
1. Árvore AVL
2. Árvore Rubro-Negra
3. Sair
Escolha uma opção: 1

Criando uma nova Árvore AVL...

--- Operações ---
1. Inserir elemento
2. Remover elemento
3. Buscar elemento
4. Imprimir árvore
5. Voltar ao menu principal
Escolha uma operação: 1
Digite o valor para inserir: 10
Elemento 10 inserido na AVL.

--- Operações ---
1. Inserir elemento
2. Remover elemento
3. Buscar elemento
4. Imprimir árvore
5. Voltar ao menu principal
Escolha uma operação: 1
Digite o valor para inserir: 20
Elemento 20 inserido na AVL.

--- Operações ---
1. Inserir elemento
2. Remover elemento
3. Buscar elemento
4. Imprimir árvore
5. Voltar ao menu principal
Escolha uma operação: 1
Digite o valor para inserir: 30
Elemento 30 inserido na AVL.

--- Operações ---
1. Inserir elemento
2. Remover elemento
3. Buscar elemento
4. Imprimir árvore
5. Voltar ao menu principal
Escolha uma operação: 4
--- Árvore AVL (Impressão Pré-Ordem) ---
20 (H:2, B:0) | 10 (H:1, B:0) | 30 (H:1, B:0) | 
----------------------------------------

--- Operações ---
1. Inserir elemento
2. Remover elemento
3. Buscar elemento
4. Imprimir árvore
5. Voltar ao menu principal
Escolha uma operação: 5
Voltando ao menu principal...

===== MENU PRINCIPAL =====
Qual tipo de árvore deseja criar/usar?
1. Árvore AVL
2. Árvore Rubro-Negra
3. Sair
Escolha uma opção: 3
Encerrando o programa...
```
