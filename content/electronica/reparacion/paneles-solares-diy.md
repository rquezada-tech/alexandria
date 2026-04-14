---
title: Panel Solar con Componentes Salvados
domain: manufactura
subtopic: solar
has_images: false
---

# Panel Solar con Componentes Salvados

La energía solar es una de las fuentes más accesibles para generación off-grid. Es posible construir sistemas funcionales con componentes salvados de equipos electrónicos muertos.

## Paneles solares: entender los restos

Los paneles solares de celdas de silicio amorfo se encuentran en:
- Calculadoras solares
- Luces de jardín solares (las pequeñas plaques)
- Cargadores solares USB portátiles
- Paneles de emergencia para autos (battery maintainers)

Para generar energía útil necesitas varios paneles conectados en serie o paralelo.

## Controlador de carga DIY con LM358

El LM358 es un amplificador operacional dual que se encuentra en muchas placas de cargadores solares.
Un controlador de carga básico puede construirse para evitar sobrecargar baterías.

Circuito básico de carga:
-Sensor de voltaje con divisores resistivos
- LM358 como comparador
- MOSFET como interruptor

Para 12V:
- Batería llena: 13.8V
- Batería vacía: 10.5V
- Desconexión por sobrecarga: 14.4V

## Baterías de respaldo de UPS

Las baterías de plomo-ácido selladas (VRLA) de UPS viejos son un recurso valioso.
- Voltaje: 12V nominal
- Capacidad: 7Ah a 24Ah típico
- Carga: 13.5-13.8V float, 14.4-14.7V bulk

Las baterías de UPS viejas pierden capacidad pero pueden almacenar algo de carga útil.

## Inversor básico con 555 y MOSFET

Un inversor simple convierte DC a AC para alimentar equipos domésticos.
Componentes mínimos:
- 555 timer (genera señal cuadrada)
- MOSFET de potencia (IRFZ44N o similar)
- Transformador de audio de radio viejo o transformador de fuente ATX

Configuración con transformador de fuente ATX:
- 12V del transformador → lado de baja tensión (menos vueltas)
- 220V o 110V del lado de alta tensión
- 555 genera la señal que maneja los MOSFETs
- Frecuencia: ~50-60Hz (ajustable con resistor/capacitor del 555)

Precaución: esto genera onda cuadrada, no senoidal. Solo para cargas resistivas (luz, calefacción).

## Generador eólico básico (alternador de disque duro)

Un disco duro viejo contiene un alternador de imanes permanentes.
- Puede generar ~5V sin carga a alta velocidad
- Conectado a una batería via diodo y resistor limitador
- Necesita un rectificador para cargar batería DC

No es una fuente práctica para generación regular pero es un ejercicio valioso de ingeniería.

## Motor de CD como generador

Los motores DC pequeños funcionan como generadores cuando se les aplica rotación.
- Un motor de 12V DC genera ~12V sin carga
- La corriente depende de la velocidad y tamaño
- Rectificar la salida con puente de diodos

Útil para pequeños proyectos de demostración pero no para almacenamiento energético real.

## Circuitos integrados útiles para sistemas solares salvados

- LM358: amplificador operacional, comparador de voltaje
- LM339: cuatro comparadores para monitoreo de batería
- 555: generador de pulsos, PWM para control de carga
- IRFZ44N: MOSFET de potencia para switching
- 1N4007: diodo de rectificación (alta tensión)
- BS250: MOSFET P-channel para switching

## Configuraciones prácticas

### Sistema mínimo: 5V USB desde panel solar
- 1 panel solar 6V (de luz de jardín)
- 1 diodo 1N5819 (previene descarga inversa)
- 1 capacitor 1000µF
- 1 puerto USB
直接 a bateria 5V con diodo.

### Sistema 12V completo
- 1-4 paneles solares 12V (o panels de mayor voltaje en serie)
- 1 batería 12V (lead-acid de UPS o 18650 × 3 en serie)
- 1 controlador de carga (LM358 + MOSFET)
- 1 inversor (opcional, para AC)

### Cargar baterías 18650 con panel solar
- Panel 6V/5W → entrada de TP4056 (que acepta 5V)
- El TP4056 se configura para 4.2V (litio single cell)
- Batería 18650 como almacenamiento
- Output: USB 5V con step-up boost module (MT3608)

## Materiales necesarios para taller solar

- Multímetro digital
- Soldador y estaño
- Pines y alambre de diferentes calibres
- Diodos 1N4007, 1N5819, 1N5408
- MOSFETs IRFZ44N
- Capacitores varios (electrolíticos y cerámicos)
- Protoboard para prototipado
- Conectores Anderson o similar para conexiones robustas

## Precauciones

- Los paneles solares generan voltaje incluso con luz artificial
- Siempre desconectar antes de trabajar en el circuito
- Las baterías de plomo-ácido emiten gases — usar en area ventilada
- No corto-circuitar baterias de litio
- Un sistema sin protección puede causar incendios
