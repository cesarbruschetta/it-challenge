# Capture Italy – The Perfect Team

A Escola de Idiomas e Ciências ensina cinco matérias: Física, Química, Matemática, Botânica e Zoologia. Cada estudante é experto em uma matéria. As habilidades dos alunos são descritas mediante uma string das habilidades citadas, que consta das letras p, c, m, b e z somente. Cada caractere descreve a habilidade de um estudante da seguinte maneira:
p → Física.
c → Química.
m → Matemáticas.
b → Botânica.
z → Zoologia.
 
Sua tarefa é determinar o número total de diferentes equipes que satisfazem as seguintes restrições:
 
Uma equipe consiste em um grupo de exatamente cinco estudantes.
Cada estudate é experto em uma materia diferente.
Um estudante pode estar sozinho em uma equipe.

## Por exemplo 
Se a string de habilidades for pcmbzpcmbz, então há duas equipes possíveis que podem ser formadas de uma vez: 
* habilidades [0-4]
* habilidades [5-9]. 

Não é importante determinar as permutações, já que sempre estaremos limitados a duas equipes com 10 estudantes.
  
Você recebe um arquivo com a entrada que figura no seguinte link https://www.dropbox.com/s/3neyzkiomsb7eh8/Copia%20de%20input013.txt?dl=0

Restrições
5 ≤ n ≤ 5 × 105
skills[i] ∈ {p,c,m,b,z}
