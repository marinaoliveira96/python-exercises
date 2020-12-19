x = input('digite uma frase: ').strip().lower()
print('a letra A aparece {} vezes'.format(x.lower().count('a')))
print('a letra a aparece pela primeira vez na posição {}'.format(x.find('a')+1))
print('a letra a aparece pela ultima vez na posição {}'.format(x.rfind('a')+1))