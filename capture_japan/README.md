# Capture Japan – Maraleja: no implementar tu proproa hash table

Uma hash table é uma estrutura de dados que permite salvar elementos e acessá-los rapidamente usando uma função de hashing, ou seja, uma função que, para cada elemento possível devolve um número dentro de um intervalo especificado.

Uma das maneiras mais famosas de implementar uma hash table é chamada de "hashing fechado". Esta implementação salva os dados em uma matriz de comprimento K prefixado e após o ao receber um novo elemento E, faz o hash e o coloca na posição hash(E) (a função "hash" sempre devolve um inteiro no intervalo [0, K)). Se essa posição já estiver ocupada, tenta salvá-lo na posição hash(E) +1. Se essa também estiver ocupada, tenta na hash(E)+2 e assim em diante, até chegar à última posição do array. Se mesmo assim não encontrar espaço, retorna para a posição 0 do array e segue o mesmo processo até encontrar uma posição livre.
Juan programou sua hash table usando hashing fechado, e utilizou uma função de hashing uniforme (ou seja, para cada elemento é atribuído um valor inteiro no intervalo [0, K) com a mesma probabilidade). Infelizmente, sua implementação tem um bug: se chegar até o final do array e não encontrar espaço para salvar o elemento, ele o descarta diretamente (ou seja, não tenta colocá-lo nas posições 0, 1, 2... como seria correto).

Para testar a implementação de Juan foram selecionados N elementos aleatórios para inseri-los em uma hash table implementada com um array de comprimento K. 
Qual é a probabilidade de que com este teste descubramos que a implementação de Juan tem um bug, se N = 27 e K = 42?

A resposta deve ser inserida como uma fração irredutível (ver o exemplo).

## Exemplo: 

Se N = 2 e K = 2, os possíveis hashes para os N = 2 elementos a serem inseridos são:
```
0 0
0 1
1 0
1 1
```
O único caso em que o bug será exposto é se ambos os hashes forem 1. Nesse caso, primeiro é salvo o primeiro elemento em array[1]. Depois, o seguinte elemento não tem espaço em array[1] e como é a última posição do array, será descartado. Portanto, a resposta para este caso será "1/4" (sem aspas)




