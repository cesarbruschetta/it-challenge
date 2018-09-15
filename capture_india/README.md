# Capture_India – Substring Calculador

Dada uma string de caracteres, s, podemos definir uma sub-string de caracteres como uma string não vazia que pode ser obtida aplicando uma das seguintes operações:
Remova zero ou mais caracteres do lado esquerdo de s.
Remova zero ou mais caracteres do lado direito de s.
Remova zero ou mais caracteres do lado esquerdo de s e remova zero ou mais caracteres do lado direito de s.
 
Por exemplo, vamos s = abcde. Os substrings são:
 1	abcde
 2	abcd
 3	bcde
 4	abc
 5	bcd
 6	cde
 7	ab
 8	bc
 9	cd
10	de
11	a 
12	b
13	c
14	d
15	e

## Restrições
A string s consiste em caracteres no intervalo ascii [a-z].
0 ≤ | s | ≤ 10^5

Sua tarefa é determinar quantos sub-strings podem se obter logo de fazer as operações descritas acima para um string s.
A entrada contém uma única linha que representa o string de caracteres a ser analisado.
A saída consiste em um inteiro com o total de substrings que podem ser obtidos.
