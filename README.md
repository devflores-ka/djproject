Crear intancia EC2
Seleccionar AMI Ubuntu
Seleccionar capa gratuita
Habilitar traafico http y https
Configurar almacenamiento
Detalles avanzados -> Datos de usuario (final de la página)
Copiar y pegar contenido del archivo UserData.sh
Recordar que si se usa el mismo proyecto base de este repositorio no debe cambiar nada, de lo contrario deberá adaptar su propia app 
Si copiar y pegar el contenido fallo (verificar una vez iniciada la instancia) conectese vía SSH a su instancia y copie y pegue cada comando manualmente, cumplira el mismo objetivo

Este proyecto trabaja su base de datos en RDS por lo que necesita lo siguiente:
Diríjase al servicio RDS -> Bases de datos -> Crear base de datos
Seleccionar MySQL
Seleccionar Capa gratuita (free tier)
Dar nombre al servicio
Cambiar usuario (opcional)
Seleccionar contraseña autoadministrada (recomendado)
Acceso público: SI
Crear
