# GPX, vídeos y usuarios autorizados

Estado actual: muestra local, sin biblioteca compartida ni autenticación de producción. Subir el código a GitHub no activa estos servicios. Los únicos vídeos incorporados a `public/assets` son simulaciones ilustradas. No colocar grabaciones privadas ni GPX de usuarios en esa carpeta ni en Git.

## Arquitectura propuesta (pendiente de configurar)

- **Aplicación**: sitio web servido por Cloudflare Workers/Pages.
- **Archivos**: bucket privado Cloudflare R2 para GPX, vídeos originales, miniaturas y exportaciones MP4 compartidas. Sin dominio público ni endpoint r2.dev habilitado.
- **Catálogo y permisos**: base de datos D1 con líneas, sentidos, versiones, claves de objetos y permisos por usuario/grupo.
- **Identificación**: proveedor de identidad o Cloudflare Access para el personal autorizado. El servidor verifica la sesión y el permiso sobre cada línea, no solo el inicio de sesión.
- **Reproducción**: endpoint autenticado que transmite el objeto desde R2 y admite solicitudes HTTP Range para avanzar por el vídeo. Para subida directa, URL firmada de corta duración expedida solo a editores autorizados. Las URLs firmadas son credenciales temporales: cualquiera que las posea puede utilizarlas hasta su caducidad.
- **Roles**: administrador (usuarios y permisos), editor (subir y versionar recorridos), lector (ver las líneas asignadas). El permiso para descargar/exportar puede separarse del de visualizar. Una vez descargado un MP4, no se puede revocar la copia local.

Flujo: el editor sube GPX + vídeo → valida y sincroniza → publica una versión en el catálogo interno → el usuario inicia sesión → el servidor verifica su acceso → recibe los archivos permitidos.

Ejemplo de organización interna: `lineas/10/ida/version-id/recorrido.gpx`, `video.mp4` y `miniatura.jpg`. La aplicación utiliza identificadores de la base de datos, no acepta rutas arbitrarias del cliente.

## Qué queda por hacer

Elegir la cuenta y el dominio de Cloudflare, crear y vincular R2/D1, configurar identidad y grupos, implementar la API de catálogo/subida/lectura, migrar los archivos reales y probar denegación de acceso, revocación y reproducción por rangos. No hay credenciales ni recursos de nube creados en esta entrega. No se ha desplegado la aplicación.

Referencias oficiales:
- https://developers.cloudflare.com/r2/api/s3/presigned-urls/
- https://developers.cloudflare.com/r2/api/workers/workers-api-reference/
