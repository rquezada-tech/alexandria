---
title: Identificación de Componentes Electrónicos Comunes
domain: electronica
subtopic: componentes
has_images: false
---

# Identificación de Componentes Electrónicos Comunes

Conocer los componentes electrónicos básicos permite reutilizar piezas de dispositivos chatarra, fabricar herramientas de supervivencia y reparar equipos cuando no hay acceso a refacciones nuevas.

## Resistencias

Componente que limita el flujo de corriente. Se identifican por un código de colores de 4 o 5 bandas.

Lectura de bandas:
- Banda 1, 2 (y 3): dígitos numéricos
- Banda siguiente: multiplicador
- Última banda: tolerancia

Ejemplo: Rojo (2), Rojo (2), Marrón (×10) = 220 ohmios.

En dispositivos报废 puedes encontrar resistencias de valores comunes: 100Ω, 220Ω, 1kΩ, 10kΩ, 100kΩ.

## Capacitores (Condensadores)

Almacenan carga eléctrica temporalmente. Dos tipos principales:

### Capacitores cerámicos
Pequeños, en forma de lenteja. Sin polaridad. Valores típicos: 10nF a 100nF.
No tienen polaridad — se pueden colocar en cualquier dirección.

### Capacitores electrolíticos
Forma cilíndrica. TIENEN POLARIDAD (+/-). Siempre respetar la marca del polo negativo.
Valores altos: 1µF a 4700µF. Comunes en fuentes de alimentación.

### Capacitores de tantalio
Pequeños, en forma de gota. Tienen polaridad marcada con una stripe.
Valores: 1µF a 100µF. Muy comunes en placas de celulares.

## Diodos

Permiten que la corriente fluya en una sola dirección. Identificación:
- La banda en el cuerpo indica el cátodo (polo negativo).
- Diodo común: 1N4148 (señal), 1N4001-1N4007 (rectificación de potencia).
- LED: diodo emisor de luz. Si conduce luz, está funcionando.

## Transistores

Actúan como interruptores o amplificadores. Tres terminales: Base, Colector, Emisor.
Comunes en chatarra:
- 2N2222: amplificador de señal general
- 2N2904/2N3904: transistor NPN de uso general
- 2N2906/2N3906: transistor PNP de uso general
- TIP120/TIP122: darlington de potencia para motores

## Integrated Circuits (ICs / Chips)

 Circuitos integrados. Cada chip tiene una función específica.
- Buscar el número de modelo grabado en la superficie.
- Los ICs funcionales en chatarra son extremadamente útiles para reparaciones.

## Inductores / Bobinas

Almacenan energía en forma de campo magnético. Aspecto de espiral o solenoide.
Valor medido en Henrios (H). Se miden con multímetro especializado o LCR meter.

## Conectores USB

Los conectores USB hembra se encuentran en casi toda electrónica报废.
Tipos: USB-A, USB-B, USB-C, micro-USB, mini-USB.
Útiles para proyectos de alimentación, carga o comunicación.

## Motores pequeños

Motores DC de bajo voltaje (3V a 12V) se encuentran en:
- Juguetes electrónicos viejos
- Discos duros de computadora (motor de spindle)
- Impresoras (motores paso a paso)
- Ventiladores de PC

Los motores paso a paso tienen 4 o 6 cables y requieren control específico.

## Focos LED y tiras LED

Las tiras LED de 12V se encuentran en letreros, pantallas y decoración.
Los LEDs individuales (5mm, 3mm) se encuentran en casi cualquier aparato luminoso.

## Sensores comunes

- Sensor de temperatura: TMP36, DHT11/DHT22
- Sensor de luz: LDR (resistencia dependiente de luz)
- Acelerómetro: MPU-6050 (de celulares)
- Sensor de corriente: ACS712

## Consejos para recuperar componentes

1. Usar lupa y buena iluminación para leer valores
2. Un multímetro es indispensable para verificar funcionalidad
3. Los componentes que pasan el test de continuidad en diodo/transistor son reutilizables
4. Fotografiar la placa antes de desoldar para referencia
5. Etiquetar todo al sacar — el caos es el mayor enemigo
