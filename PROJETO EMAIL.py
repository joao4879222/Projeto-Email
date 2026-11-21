email = input('Digite seu Email: ').strip()

if '@' in email and ('gmail.com' in email or 'outlook.com' in email) and email [0] != '@' and email [-1] != '@' and ' ' not in email:
    print('E-mail válido')

else:
    print('E-mail inválido')