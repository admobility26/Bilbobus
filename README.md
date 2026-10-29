# Bilbobus · Aula de rutas

Muestra de formación basada en Rutas AD (AD Mobility). Incluye la línea 10 en ambos sentidos, mapa con paradas, vídeos ilustrados de demostración sincronizados y exportación MP4 con mapa + PIP.

## Arranque

```sh
npm ci
npm run build
python3 abrir_muestra.py
```

En Mac, después de compilar, también se puede abrir `ABRIR-MUESTRA.command`. Desarrollo: `npm run dev`. Se necesita Internet para el mapa base. Solo se escucha en el equipo local.

## Exportación

Selecciona el sentido y pulsa **Exportar MP4**. Al terminar aparece **Descargar MP4**. La película contiene la carátula, mapa, recorrido, paradas, posición sincronizada y vídeo PIP. Formato H.264, 1280×720, 20 fps. Si la fuente tiene audio compatible se conserva en AAC. La simulación incluida es muda.

Esta muestra usa exportación en memoria y admite vídeos de hasta 5 minutos. Requiere un navegador compatible con WebCodecs H.264 (por ejemplo Chrome/Edge actualizado). La velocidad de previsualización no modifica la duración de la exportación. Para clases largas se debe integrar la escritura directa a disco de Rutas AD.

Los archivos seleccionados se usan localmente, sin subirse. La biblioteca compartida y la autenticación todavía no están implementadas: véase [propuesta de alojamiento privado](docs/ALOJAMIENTO.md).

## Fuentes y licencia

Nombres de paradas: PDF facilitado por el usuario (01/09/2026). Coordenadas, trazado y catálogo: Ayuntamiento de Bilbao / Bilbao Open Data, descargados el 29/10/2026 (CC BY 3.0 ES). Mapa © OpenStreetMap contributors. Imágenes de identidad facilitadas por el usuario. Los vídeos representan una escena genérica ilustrada, no calles ni tiempos reales.

El código heredado de Rutas AD conserva su licencia y atribución; ver LICENSE y COPYRIGHT.md. `src/main.jsx` carga la pantalla específica de Bilbobus; las pantallas heredadas no se presentan en esta muestra. Este proyecto no modifica el repositorio original de Rutas AD. No es una aplicación oficial de Bilbobus.
