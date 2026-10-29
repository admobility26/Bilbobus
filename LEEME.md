# Bilbobus · Aula de rutas

Muestra local e independiente basada en una copia de Rutas AD 0.17.0 (AD Mobility), con una nueva pantalla Bilbobus y reutilización de su motor temporal de recorridos. El código de las pantallas originales se conserva como base de desarrollo, pero no forma parte de la navegación de esta muestra. No se ha publicado, conectado al servidor original ni importado su biblioteca o cuentas.

## Abrir

En este Mac, haz doble clic en **ABRIR-MUESTRA.command**. Se abrirá el navegador y una ventana que debes mantener abierta mientras usas la muestra. Para cerrarla, pulsa Ctrl+C en esa ventana. Requiere Python 3. No requiere instalar dependencias para visualizar la versión incluida en `dist`.

El servidor escucha solo en este ordenador. El mapa base de OpenStreetMap y las tipografías requieren Internet. Los GPX y vídeos seleccionados se usan en memoria local y no se suben; se descartan al recargar o cambiar de sentido.

## Contenido

- Línea 10, Elorrieta–Plaza Biribila: 16 paradas de ida y 15 de vuelta, incluyendo las cabeceras.
- Nombres en euskera según el PDF, con códigos y coordenadas del GTFS oficial. Cada punto es seleccionable y se enlaza con su ficha.
- Trazado oficial de referencia, con avance visual simulado. No es un track GPS grabado ni representa velocidades, duración o condiciones reales.
- Identidad e imágenes Bilbobus/Gautxori proporcionadas por el usuario.
- Biblioteca del catálogo de líneas. Solo la línea 10 está habilitada en esta muestra.
- Dos vídeos ilustrados incluidos: 62 segundos de ida y 58 segundos de vuelta. Recrean una vista genérica desde el autobús; no muestran las calles reales ni tiempos de servicio.
- Vídeo, posición en el mapa, tramo recorrido y parada activa sincronizados por un único reloj. Pausa, reinicio, salto al seleccionar una parada y velocidades 0,5×, 1× y 2×.
- Panel flotante de vídeo minimizable y carga local de vídeo. PIP externo sujeto a compatibilidad del navegador.
- Carga de GPX con puntos `trkpt`. Con tiempos válidos puede ajustarse el desfase del vídeo en segundos (momento del vídeo correspondiente al inicio del GPX). Sin tiempos, el avance es proporcional y demostrativo. La simulación incluida funciona sin importar archivos. Para sincronizar una grabación real de la línea hacen falta sus archivos.

## Fuentes y alcance

PDF proporcionado: `public/assets/linea-10.pdf`, fecha impresa 01/09/2026. La vuelta se ordenó en el sentido real Plaza Biribila → Elorrieta, aunque la lista del folleto aparece de arriba abajo desde Elorrieta.

Coordenadas, trazado y catálogo descargados el 29/10/2026 de Bilbao Open Data:
https://www.bilbao.eus/opendata/es/catalogo/dato-bilbobus-gtfs
https://www.bilbao.eus/opendata/datos/bilbobus-gtfs
Licencia del catálogo: Creative Commons Reconocimiento 3.0 España. Publicador: Ayuntamiento de Bilbao. Datos incorporados y adaptados para esta muestra; no se actualizan en directo.

Mapa: © OpenStreetMap contributors. Motor cartográfico: MapLibre.

Se conservan los archivos LICENSE, COPYRIGHT.md y THIRD-PARTY-NOTICES.txt de la base Rutas AD. Muestra de diseño; no es una aplicación oficial de Bilbobus.

## Validación

Compilación completada. Verificados en navegador: mapa con puntos, cambio de sentido (16/15), selección y navegación entre paradas, minimización de vídeo, búsqueda en biblioteca y reproducción simulada. Verificados además: reproducción del vídeo simulado, pausa, salto a parada (segundo 32), vídeo de vuelta (58 s), doble velocidad y coincidencia de las posiciones simuladas con las 31 paradas de ambos sentidos. El servidor local admite solicitudes parciales para permitir saltos en MP4. No se ha validado el PIP externo ni la sincronización de una grabación real no aportada. Los 62 archivos de código originales se contrastaron por hash y permanecen idénticos.

Para editar: instalar las dependencias de package.json en esta carpeta y ejecutar npm run dev. Para reconstruir: npm run build. No hay comandos ni configuración de publicación en esta muestra.

## Encabezado y exportación MP4

La carátula facilitada se muestra completa en el encabezado y en el MP4. Usa **Exportar MP4** y, cuando termine, **Descargar MP4**. Se exporta el sentido seleccionado completo, independientemente de la posición o velocidad de previsualización. H.264, 1280×720, 20 fps; límite de muestra: 5 minutos. Se conserva audio compatible en AAC cuando lo haya. Requiere WebCodecs H.264; admite cancelación sin generar archivos incompletos. Verificada una descarga completa de la simulación de ida: 62 s, 1240 fotogramas decodificados correctamente, con mapa y PIP visibles.

Alojamiento compartido: todavía no configurado. Ver `docs/ALOJAMIENTO.md` para la propuesta R2 privado + API autenticada + permisos por línea.

ACTUALIZACIÓN: se incluye gestión de usuarios con contraseña y caducidad para el futuro servidor, permisos de administrador y marca de agua Bilbobus en vídeos de muestra y MP4 exportados. La muestra local abre como administrador sin crear cuentas reales. El dominio, almacenamiento privado y publicación siguen pendientes; ver docs/ALOJAMIENTO.md.
