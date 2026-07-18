
Logo de começo acabei indo pesquisar como se verificava se o item de um array estava dentro do outro e no geekforce me deu uma explicação parecida com essa, a partir dai eu implemente no leetcode e deu certo, fazendo por meio de força bruta ele verifica se os numeros de i são iguais ao de j e se i já não está presente em newArray, caso contrario ele adiciona dentro de newArray com append e retorna o newArray

````python
newArray = []

        for i in nums1:

            for j in nums2:

  

                if i == j and i not in newArray:

                    newArray.append(i)

        return newArray
`````

Depois de resolver dessa forma e explicar meu modo de pensar, o gpt me perguntou se eu conhecia o set, na hora nem me lembrava, mas dai lembrei que ele armazenva um conjunto de numeros unicos, e a partir dai resolvi dessa seguinte forma

````python
		newSet = set(nums1)

        newSet2 = set(nums2)

        List = list(newSet & newSet2)

        return List
`````

Dai ele falou q tinha como resumir mais ainda em só uma linha da seguinte forma, e realmente faz sentido
````python
return list(set(nums1) & set(nums2))
`````

Tanto na primeira forma usando `set` como na segunda, eles estão transformando a lista em conjuntos de numeros unicos, fazendo a interseção deles, e depois juntando em uma lista e retornando os mesmos.
