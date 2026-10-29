# Acceso y alojamiento de Bilbobus

El repositorio guarda el código y los vídeos ilustrados de muestra. No es el alojamiento de las grabaciones privadas. No se han contratado recursos, comprado un dominio ni desplegado la web.

## Implementado y probado localmente

- Inicio de sesión con usuario y contraseña, creados por el administrador.
- Duración en días, renovación desde hoy, desactivación y cambio de contraseña. Estos cambios revocan las sesiones anteriores.
- Contraseñas derivadas con PBKDF2, sesiones en cookies HttpOnly, validación de vigencia en el servidor y límite de intentos de acceso.
- Solo el administrador dispone de gestión de usuarios, importación local, exportación MP4 y endpoints de descarga.
- Vídeos de muestra con el logo Bilbobus grabado en sus fotogramas; exportaciones con marca de agua adicional.
- API para lectura autenticada de archivos de un bucket privado R2, con reproducción por rangos.

La muestra abierta con ABRIR-MUESTRA.command funciona como administrador local, sin cuentas reales. No debe usarse ese servidor local para publicar la web. La versión con servidor utiliza server/worker.js y exige iniciar sesión.

## Alojamiento previsto

Cloudflare Workers sirve la aplicación y comprueba cada acceso. D1 guarda usuarios, caducidades, sesiones y el catálogo de medios. R2 privado guarda los GPX y vídeos; no se habilita acceso público al bucket. Un usuario vigente podrá ver los recorridos publicados. En esta versión todos los usuarios vigentes comparten el catálogo, sin asignación individual por línea.

Ejemplo de archivos privados: lineas/10/ida/v1/recorrido.gpx y video.mp4. El servidor resuelve identificadores del catálogo; no acepta claves arbitrarias del usuario.

## Activación futura

1. Crear D1 y R2 en la cuenta elegida y sustituir el identificador provisional de wrangler.jsonc.
2. Aplicar server/schema.sql a D1, configurar ADMIN_SETUP_TOKEN como secreto y publicar el Worker con su dominio HTTPS.
3. Crear el administrador mediante POST /api/setup con Authorization: Bearer y el secreto, Origin del mismo dominio y JSON con username/password. El endpoint solo permite la creación inicial. Retirar el secreto al terminar.
4. Incorporar el panel de subida y selección del catálogo a la interfaz. Los botones actuales de importar GPX/vídeo solo cargan archivos durante la sesión local; todavía no publican medios en R2.
5. Procesar los vídeos reales para grabar permanentemente el logo antes de publicarlos. El campo watermarked del catálogo es una declaración del proceso de preparación, no un detector automático de logos.
6. Probar el despliegue real, copias de seguridad y la reproducción de grabaciones largas antes de dar acceso a clientes.

Los botones y endpoints de descarga se reservan al administrador. Ninguna web puede impedir por completo que un usuario autorizado guarde los bytes reproducidos o grabe la pantalla. La marca de agua queda dentro de los vídeos preparados y de las exportaciones.

## Validación de esta entrega

Compilación de producción correcta. Pruebas locales con Worker y D1: rechazo anónimo, bloqueo de URL directa de medios (incluyendo extensión codificada), alta, sesión, permisos de lector, descarga de administrador, desactivación, caducidad, renovación y reproducción HTTP 206. No se han utilizado cuentas reales para las pruebas.
