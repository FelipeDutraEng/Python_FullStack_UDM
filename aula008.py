from datetime import datetime


ano_atual = datetime.now().year
nome = 'Felipe'
sobrenome = 'Oliveira Dutra'
idade = 30
ano_nascimento = ano_atual - idade
maior_de_idade = idade >= 18
altura_metros = 1.71

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)