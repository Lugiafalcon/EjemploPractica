def login(usuario, contraseña):
    if usuario == 'admin' and contraseña == '1234':
        return 'Login exitoso'
    else:
        return 'Credenciales incorrectas'
