## BIENVENIDO AL REPOSITORIO DE API VOTANTES 

**Recursos para la ejecución: **

- python en la version 3.10.2
- Framework Flask
- XAMPP y MySQL Workbench para la ejecucion y administración de la base de datos 
- Se recomieda usar Visual Studio Code o Pycharm para la codificación del codigo.

**INSTALACIÓN**
- Se recomienda crear una carpeta en el Disco local (c:) para almacenar el API.
Ejecutamos XAMPP  y activamos las funciones de Apache y MySQL
Abrimos MySQL Workbench y establecemos conexión con el localhost:3306 o el puerto disponible asignado desde el XAMPP

- Abremos un query editor en MySQL Workbenche y usando la sentencia "Create Database Cebar" creamos la base de datos del aplicativo.

- Para verificar que Python está instalado de manera correcta en el sistema ejecutamos el comando "Python" desde Windows Powershell o CMD, en donde nos arrojará un mensaje que muestra la versión instalada y la simbología ">>>" lo que significa que está listo para usarse, podemos cerrar la ventana o hacer uso del comando "exit()".

- Para realizar la instalación del framework Flask, debemos utilizar el comando de intalación de paquetes de Python "PIP", seguido de la instrucción "install Flask", es decir, debe queda de la siguiente manera "pip install Flask" y presionamos la tecla Enter de nuestro teclado, si el proceso de ejecucion se realizó exitosamente nos arrojará el mensaje "succesfully installed Flask-x.x.x"

- Adicionalmente se debe instalar el paquete que permite la conexión entre el framework "Flask" y nuestro gestor de base de datos "MySQL", el cual se llama "Flask-MySQL", la instalación funciona de la misma manera que en el paso anterior haciendo uso del comando "pip install Flask-MySQL" y presionamos la tecla Enter.

- Se debe instalar el paquete que permite la generación y uso de json el cual se llama "PyJWT", la instalación se realiza haciendo uso del comando "pip install PyJWT" y presionamos la tecla Enter.

**NOTA**

*Para verificiar que la todos los paquetes estén instalados en nuestro sistema debemos hacer uso del comando "pip list" el cual nos mostrará todo lo que tengamos instalado*

**EJECUCIÓN**
- Despues de haber realizado los pasos anteriores procedemos a crear una carpeta en nuestra unidad principal o disco local C: según sea el caso, esta carpeta puede estar en cualquier ruta, una vez creada la carpeta en el lugar que resulte mas cómodo, procedemos a copiar todos los archivos previamente descargador del repositorio.

- Una vez copiado los archivos, para hacer uso del API se debe abrir una terminal directamente en la ruta eso haciendo uso de la combinación de teclas "SHIFT + Clic Derecho" y nos aparecerá la opción abrir Windows Terminal (En caso de tener Windows 11) o Abrir consola de comandos (En caso de tener Windows 10), una vez abierta la terminal procedemos a escribir el comando "python app.py" y presionamos la tecla enter, arrojandonos el siguiente mensaje:

Serving Flask app 'app' (lazy loading)
Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
Debug mode: on
Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
Restarting with stat
Debugger is active!
Debugger PIN: 108-999-397

**NOTA**

*La URL puede cambiar dependiendo de la dirección IP asignada a tu servidor local*



