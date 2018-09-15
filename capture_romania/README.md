# Capture Romania – Broken RSA

O sistema de criptografía RSA, como parte da fase de geracão de chaves públicas e privadas, deve gerar dois números primos grandes p e q e um número n = p * q que será usado logo para encriptar e desencriptar mensagens (ver https://simple.wikipedia.org/wiki/RSA_algorithm).
Uma famosa empresa de Belo Horizonte decidiu fazer sua própria implementação deste sistema. Decidiram gerar os primos p e q com dois algoritmos diferentes pensando que desse jeito iriam obter maior segurança.

A engenheira Melanie S. programou a seguinte função:
```
def generate_p():
    '''
    algoritmo eficiente, seguro e testado para gerar primos grandes
    '''
    ...
    ...
    return p
```

O engenheiro N. Álvarez, sem muita vontade de programar, decidiu tomar um atalho e programar o seguinte:

```
def generate_q():
    '''
    gera un primo
    '''
    return 1094782941871623486260250734009229761
```

Você ganhou acesso a uma das mensagens encriptadas assim como a um PEM que contém a chave pública de criptografía. Você é capaz de descobrir o conteúdo da mensagem original?

https://s3.amazonaws.com/it.challenge.18/problem20.zip
