# Biblioteca local trasladable

Requiere Node.js 24. Con el código fuente: npm ci y npm run build. Después: npm start. Abre http://127.0.0.1:5190. Este modo pide contraseña y guarda usuarios, recorridos y archivos. El antiguo ABRIR-MUESTRA.command es solo la demostración sin cuentas.

El primer arranque crea admin y una contraseña aleatoria en datos-locales/ACCESO-ADMIN.txt. Cámbiala en Mi contraseña. Esta carpeta es privada, está excluida de Git y no se publica en Cloudflare.

En Biblioteca selecciona la línea, incorpora el PDF y revisa su sentido/paradas. En la ficha del recorrido añade el PDF original, MP4 y GPX opcional. El límite local es 8 GB por archivo; el vídeo debe llevar el logo grabado. Los mapas base siguen requiriendo Internet. Las paradas y trazados oficiales están incluidos en la aplicación. No es un paquete de cartografía sin conexión.

## Exportar

Detén el servidor antes de copiar/exportar la biblioteca. Ejecuta npm run package:local para exportar la aplicación. Ejecuta python3 scripts/package-local.py --with-data para incluir la biblioteca y cuentas existentes. El ZIP privado incluye contraseñas cifradas mediante derivación, sesiones y documentos privados: entrégalo solo al responsable del servidor. No incluye el archivo de contraseña inicial.

En el servidor de destino, descomprime el paquete, instala Node.js 24 y ejecuta node server/local.mjs. No requiere Cloudflare, R2 ni instalar dependencias para ejecutar el servidor empaquetado. Conserva datos-locales en disco persistente y realiza copias de seguridad.

Para acceso externo, el administrador del servidor debe configurar HTTPS mediante proxy inverso, BILBOBUS_ORIGIN=https://dominio-elegido y BILBOBUS_HOST=127.0.0.1 (proxy en la misma máquina). Ajustar el límite de subida del proxy, el cortafuegos, arranque automático y copias. No publiques la carpeta datos-locales como contenido web. Validar rendimiento y acceso externo antes de entregar a usuarios.

La muestra se completará con dos recorridos y cuatro vídeos proporcionados por el administrador; no se crean grabaciones reales ficticias.

## Sincronización y recorridos de una hora

Adaptado del flujo de src/premium/ReviewStudio.jsx de admobility26/elorrietatrack: seleccionar el mismo instante del GPX y vídeo, vincularlo y mantener un reloj común. Carga GPX con tiempos y vídeo, pulsa Ajustar sincronización, mueve la barra del recorrido y el segundo del vídeo por separado, y pulsa Vincular este instante. El desfase se aplica a reproducción, desplazamiento por la barra y exportación. Se conserva en la biblioteca por recorrido y nombres de archivos; al cambiar los archivos hay que comprobarlo de nuevo. Sin tiempos GPX solo hay avance proporcional, no sincronización temporal comprobada.

El exportador acepta hasta 3600 segundos de vídeo por sentido y ofrece guardar directamente en disco en Chrome/Edge. No acumula el MP4 completo en memoria cuando se elige ese archivo. En navegadores sin guardado directo el límite sigue siendo cinco minutos. Mantener la pestaña abierta durante la exportación. Cancelar aborta la escritura. El máximo se refiere a cada vídeo seleccionado, no recorta automáticamente un original más largo. Las grabaciones largas deben comprobarse con material real antes de dar por validada la exportación completa de una hora.

## Flujo actualizado

Crear recorrido desde GPX, añadir vídeo original y PDF opcional de consulta. El PDF ya no determina el itinerario en los recorridos nuevos. Los puntos inicial/final del GPX son referencias del recorrido, no paradas oficiales inferidas. Los originales en el servidor local son accesibles solo por administrador. El logo Bilbobus se graba en la exportación, sin exigir marca previa al original local. Abrir con ABRIR-EDITOR.command o http://127.0.0.1:5190. La cuenta local del propietario se ha sincronizado una vez con su cuenta web; futuros cambios de contraseña son independientes. La contraseña no está en el código ni en Git.
