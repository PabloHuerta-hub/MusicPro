# MusicPro
Super admin user:
=
- Correo: admin@gmail.com Pass: 123

URLS: 
=
- Api:'api/'
- Index:' '
- Contacto:'contactanos'
- Blog:'blog'
- Productos:'productos'
- About:'sobrenuestrosproductos'

LOGINS:
=
- Administrador: admin@gmail.com pass: 123 
- Cliente: basth.rojasv@duocuc.cl pass: pelicanoprueba 
- Contador: contador@gmail.com pass: pelicanoprueba
- Bodeguero: bodeguero@gmail.com pass: pelicanoprueba
- Vendedor: vendedor@gmail.com pass: pelicanoprueba

Paypal:
=
- Ingresar a www.sandbox.paypal.com
- Correo: ClienteJhonDoe@personal.example.com
- Contraseña: pelicanoprueba123

Tarjeta de Crédito o Débito
=
- Número de tarjeta: 4032032082597631
- Fecha de Expiración: 11/2026
- CVV: 885

POSIBLES PROBLEMAS:
=
- En caso de problemas con la base de datos ejecutar: python manage.py migrate --run-syncdb

INSTRUCCIONES PARA EL TESTING (Python):
=
- Entrar a la carpeta Test desde el CMD
- Ejecutar comando: pip install selenium
- Ejecutar comando: pip install pytest
- Tener el archivo chromedriver.exe (verifique que la versión que ya está en la carpeta es la que corresponde a su navegador. La que está es la versión Chrome 103.0.5060.66 )
- Ejecutar comando: pytest

INSTRUCCIONES PARA EL TESTING (Selenium IDE):
=
- Descargar Selenium IDE para su navegador
- Abrir Selenium IDE desde su navegador
- Abrir proyecto "Test_MusicPro" que está en la carpeta Test
- Levantar servidor desde CMD
- Ejecutar las pruebas