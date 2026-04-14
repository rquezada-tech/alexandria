---
title: Fuentes de Alimentación con Componentes Salvados
domain: electronica
subtopic: reparacion
has_images: false
---

# Fuentes de Alimentación con Componentes Salvados

Una fuente de alimentación confiable es fundamental para cualquier taller de electrónica o laboratorio de supervivencia. Casi cualquier fuente de un aparato muerto puede reformarse.

## Usar la fuente de un celular viejo (5V USB)

La manera más simple de obtener 5V:
- Cualquier cargador de celular viejo (micro-USB, USB-C, Lightning)
- Puedes tomar 5V directamente del pin USB correspondiente o del cable interno
- Los cargadores de celular vieja proporcionan 5V a 0.5A hasta 3A

## Fuente ATX de PC de escritorio

Las fuentes ATX de PCs de escritorio son una mina de oro para el laboratorio de supervivencia. Suministran:
- 12V (amarillo): motores, tiras LED, ventiladores
- 5V (rojo): lógica, ICs, conectores USB
- 3.3V (naranja): chips, memorias
- -12V (azul): puertos serial RS232
- 5VSB (púrpura): standby — siempre activo si hay energía

Pinout ATX estándar (24 pines):
- Amarillo + Negro = 12V (hasta 20A)
- Rojo + Negro = 5V (hasta 20A)
- Naranja + Negro = 3.3V (hasta 18A)

Cómo probar una fuente ATX sin motherboard:
1. Conecta el cable verde (PS_ON) a cualquier cable negro (GND) con un jumper
2. La fuente debe encender
3. Mide voltajes con multímetro en los pines correspondientes

## Regulador 7805: De 7-35V a 5V estable

El 7805 es un regulador de voltaje clásico que convierte cualquier entrada de 7V a 35V en 5V estables.
Circuito mínimo:
- Input: 7V a 35V al pin izquierdo
- GND: común en el pin central
- Output: 5V constantes en el pin derecho
- Capacitor de entrada: 0.33µF (no crítico)
- Capacitor de salida: 0.1µF (no crítico)

Datasheet: hasta 1.5A de corriente de salida continua.

## Regulador LM317: Voltaje ajustable

El LM317 puede regular cualquier voltaje entre 1.25V y 37V.
Fórmula: Vout = 1.25 × (1 + R2/R1)
Con R1=240Ω y R2=470Ω → ~2.9V
Con R1=240Ω y R2=1200Ω → ~6.9V

Útil para alimentar circuitos que requieren voltajes específicos no estándar.

## Convertidor Buck de teléfonos viejos

Los módulos Step-Down Buck basados en MP1584 o LM2596 se encuentran en cargadores de celular y pueden reutilizarse.
- Input: 4.5V a 40V
- Output: ajustable 0.8V a 37V
- Eficiencia: hasta 92%
- Corriente: hasta 3A con disipador

Circuito: solo necesitas dos capacitores y dos resistores para ajustar el voltaje de salida.

## Transformadores de fuentes de alimentación rotas

Los transformadores de fuentes ATX, radios antiguos y TVs old pueden usarse para obtener voltajes personalizados.
- Alimentar un LED de alta potencia
- Cargar baterías de litio (con rectificación y regulación)
- Alimentar circuitos de baja potencia

Precaución: los transformadores pueden almacenar carga peligrosa incluso apagados.

## Baterías de litio salvadas de laptops

Las celdas 18650 de baterías de laptops muertas son reutilizables si no están dañadas.
- Voltaje nominal: 3.6-3.7V
- Voltaje de carga: 4.2V
- Capacidad típica: 2000-4400mAh

Test básico de celda:
1. Mide voltaje en circuito abierto: debe estar >3.0V
2. Carga con TP4056 (módulo cargador USB)
3. Mide que alcance 4.2V sin sobrecalentarse

Nunca usar celdas dañadas, hinchadas o con voltaje <2.5V.

## Módulo TP4056: Recargador de litio USB

El TP4056 es un módulo pequeño que se encuentra en casi toda batería de celular.
Conecta:
- BAT+: al positivo de la celda
- BAT-: al negativo de la celda
- OUT+: a负载 (USB output)
- OUT-: GND

El módulo incluye protección de sobre-descarga y regulación de carga a 1A.

## Consideraciones de seguridad

- Nunca curto-circuitar una batería de litio
- Siempre usar protección para corrientes excesivas
- Los capacitores grandes pueden almacenar carga lethal
- Usar goggles al trabajar con capacitores
- Tener agua cerca al soldar
- No mezclar capacitores de diferentes voltajes en fuentes de alta potencia
