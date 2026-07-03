# Pesquisa Binária

A primeira coisa que precisamos entender é o que é uma pesquisa binária. Ela é um algoritmo eficiente para encontrar um item específico em uma lista de dados que já está ordenada.

## O que é uma Pesquisa Binária?

Ela começa olhando exatamente para o meio da lista. Se o elemento do meio for o número que estamos procurando, a busca é encerrada imediatamente.

Caso o número do meio seja menor que o alvo, ela entende que o número procurado só pode estar na metade da direita da lista.

Caso o número do meio seja maior que o alvo, ela entende que o número procurado só pode estar na metade da esquerda da lista.

Esse processo continua até encontrar o número procurado ou até não existir mais nenhum elemento para ser verificado.

## Raciocínio Usado

Logo ao ler o exercício, entendi que o `mid` seria calculado da seguinte forma:

```python
mid = (low + high) // 2
```

porque assim conseguimos encontrar o elemento do meio da faixa de busca.

A partir disso, eu precisava comparar `nums[mid]` com o `target` para saber se o valor era maior, menor ou igual ao alvo.

Para conseguir percorrer toda a área de busca, precisamos utilizar um `while`, porque enquanto o menor índice for menor ou igual ao maior índice, ainda existem posições para serem verificadas.

Se `nums[mid]` for igual ao `target`, significa que encontramos o índice correto e podemos retorná-lo.

Caso `nums[mid]` seja menor que o `target`, precisamos atualizar `low = mid + 1`, porque como o valor do `mid` é menor que o alvo, sabemos que o `target` não pode estar antes nem na posição atual. Então, a próxima busca começa a partir do índice `mid + 1`. Se essa nova posição já contiver o valor procurado, a próxima comparação irá encontrá-lo.

Caso `nums[mid]` seja maior que o `target`, precisamos atualizar `high = mid - 1`, porque sabemos que o alvo não pode estar depois da posição atual. Dessa forma, a área de busca passa a terminar uma posição antes do `mid`.

O processo se repete sempre verificando o meio da área de busca e atualizando os valores de `low` ou `high` conforme necessário, até encontrar o `target` ou retornar `-1`, como foi solicitado no enunciado.

> **Observação:** Antes de resolver este exercício, precisei entender o que era uma pesquisa binária. Depois de compreender como ela funciona, consegui resolver o exercício.
