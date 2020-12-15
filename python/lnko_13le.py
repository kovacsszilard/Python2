print('Legnagyobb közös osztó')
a: int=int(input('a= '))
b: int=int(input('b= '))
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(f'LNKO={a}')