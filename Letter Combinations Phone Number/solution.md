# Explicação

Data de resolução: 27/06/2026

- Criamos o dicionário **telefone** de 2 até 9, incluindo 0 e 1.
- Criamos uma lista vazia onde iremos adicionar as combinações.
- Criamos uma função chamada `backtracking` com os parâmetros `index` e `char`:
- `Index` = posição atual do número que estamos processando.
- `Char` = combinação construída até o momento.

- Criamos uma validação com `IF` para sabermos quando temos que adicionar uma combinação na lista.
- No caso, precisamos que o `index` seja igual ao comprimento de `digits` (já que são strings).
- Assim, adicionamos na lista com `append` e passamos o `char` de parâmetro.
- Utilizamos `return` para encerrar aquela chamada da função e devolver a execução para a chamada anterior (que estava pausada).

- Criamos um `for` para pegarmos cada letra necessária:
- `for c in telephone[digits[index]]`
- Dessa forma, estamos já pegando cada dígito e pegando a letra correta com base no dígito.

- Dentro do `for`, chamamos a função `backtracking` e passamos seus parâmetros adicionando + 1 em `index` e adicionando `c`.
- Por que disso? Faz a recursão avançar para o próximo dígito. A combinação só é adicionada quando todos os dígitos tiverem sido processados.
- Primeiro, o `for` roda e pega o primeiro dígito (`2`, ex: 23) e pega as letras correspondentes (`a`, ex: abc).
- Após isso, ele salva em `backtracking(1, "a")`.
- Tenta rodar o `if`, porém ainda não possui a mesma quantidade de índices que `digits`.
- Começa outro `for`, porém agora pegando o outro número de `digits` (`3`, ex: 23) e pega as letras correspondentes (`d`, ex: def).
- Roda o `backtracking` (que está salvo com o 1 e `"a"`), adiciona +1 e adiciona o `d`.
- Após isso, o nosso `backtracking` fica da seguinte maneira:
- `backtracking(1 + 1, "a" + "d")`
- `backtracking(2, "ad")`

- Agora, quando ele passar pelo `if`, ele terá a quantidade de índices igual à de `digits`.
- E é adicionado na lista.
- Retorna para a última vez antes de ser possível ser adicionado na lista (`backtracking(1, "a")`).
- O `for` sabe que ainda possui o restante para ser percorrido da segunda execução (`e`, ex: def) e o processo se repete até chegar ao final de todas as letras.
- Quando chega ao final de sua execução para `"def"`, ele passa para o primeiro `for` que estava congelado no `"a"`, o `char` passa a valer `"b"` e todo o processo se repete até tudo ser concluído.

- Declaramos a função para ela saber de onde começar: `backtracking(0, "")`.
- Retornamos `combinations` para visualizar as combinações.

---

# Base para backtracking

```python
def backtrack(estado):

    if terminou:
        salvar_resposta()
        return

    for escolha in escolhas_possiveis:
        fazer_escolha()
        backtrack(novo_estado)

```

---

# Mapa da árvore

```text
backtrack(0, "")

├── backtrack(1, "a")
│   ├── backtrack(2, "ad") ✓
│   ├── backtrack(2, "ae") ✓
│   └── backtrack(2, "af") ✓
│
├── backtrack(1, "b")
│   ├── backtrack(2, "bd") ✓
│   ├── backtrack(2, "be") ✓
│   └── backtrack(2, "bf") ✓
│
└── backtrack(1, "c")
    ├── backtrack(2, "cd") ✓
    ├── backtrack(2, "ce") ✓
    └── backtrack(2, "cf") ✓

```
