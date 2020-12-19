'''
cid = input('Onde você nasceu? ').strip()
x = cid.lower().find('santo')
if x == 0:
    print(True)
'''

x = input('onde vc nasceu? ').strip()
print(x[:5].lower() == 'santo')