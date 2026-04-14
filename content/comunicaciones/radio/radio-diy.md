---
title: Radio FM con Componentes de Aparatos Viejos
domain: comunicaciones
subtopic: radio
has_images: false
---

# Radio FM con Componentes de Aparatos Viejos

La comunicación por radio es crítica en emergencias cuando las redes normales fallan. Es posible construir receptores y transmisores básicos con componentes salvados.

## Radio FM simple con module RDA5807

El chip RDA5807 es un receptor FM completo que se encuentra en:
- Módulos FM económicos (breakout board)
- Radios de juguete baratas
- Bocinas Bluetooth económicas

Conexiones básicas:
- VCC: 3.3V
- GND: tierra
- SDA/SCL: bus I2C (para microcontroller)
- ANT: antena (cable de 75cm funciona)

Se controla via I2C con cualquier microcontroller (Arduino, ESP32).

## Amplificador de audio con LM386

El LM386 es un amplificador de audio de baja tensión usado en:
- Módulos MP3 de casinos
- Radios portátiles
- Pequeñas bocinas USB

Circuito básico:
- Pin 1 y 8: capacitor de gain (1µF = 20dB, 10µF = 200dB)
- Pin 2: entrada inversora (GND)
- Pin 3: entrada no inversora (señal de audio)
- Pin 4: GND
- Pin 5: salida (a parlante)
- Pin 6: VCC (3-12V)
- Capacitor bypass: 0.1µF entre VCC y GND

Potencia típica: 0.5W con parlante de 8Ω.

## Radio de cristal (banda ciudadana AM)

La radio más simple posible no necesita energía:
- Un diodo de germanio (1N34 o equivalente)
- Un audífono de alta impedancia (2000Ω)
- Un alambre largo como antena
- Un terreno como contraparte

Funciona como detector AM: el diodo rectifica la señal AM y el audífono la convierte en sonido.
Solo recibe señales fuertes de estaciones locales.

## Transmisor FM con transistor

Un transmisor FM básico puede construirse con:
- 1 transistor 2N3904 o equivalente NPN
- 1 capacitor 20pF-100pF
- 1 capacitor variable (o capacitor fijos en paralelo)
- 1 inductor (bobina de alambre esmaltado)
- 1 antena corta (20-50cm)
- 1 fuente de 3-9V

El transistor oscila a la frecuencia determinada por el circuito LC (inductor + capacitor).
La señal se modula en FM con la voz captada por un microfonoelectret.

## Antenas de emergencia

Una antena efectiva puede improvisarse con:
- Cable coaxial (RG-58): buen rendimiento para VHF
- Alambre de cobre forrado: para HF y VHF
- Varilla roscada: para HF de emergencia
- reflector parabólico hecho con malla de aluminio

Longitud básica (quart wavelength):
- Para 2m (VHF): λ/4 = 50cm
- Para 70cm (UHF): λ/4 = 17.5cm
- Para radioaficionado banda HF 40m: λ/4 = 10m

## Walkie-talkie salvado

Los walkie-talkies viejos pueden reutilizarse:
- Las baterías se reemplazan por packs de 18650 (2 en serie = 7.4V)
- Antenas originales funcionan para su frecuencia
- Algunos walkie-talkies operan en frecuencias PMR (446MHz, sin licencia en Europa)

Checkear que el dispositivo no esté bloqueado para frecuencias de emergencia.

## Comunicación CW (Morse)

CW es la forma más simple y robusta de comunicación:
- Solo requiere un tono audible
- Funciona con señales extremadamente débiles
- Cualquier transmisor FM o AM puede adaptarse
- Necesita solo una señal de ON/OFF (key)

Circuito keyer simple con Arduino:
- Pin digital → transistor que conecta PTT (push-to-talk)
- Programa que genera puntos y rayas
- Conecta a cualquier radio con entrada de micrófono

## Señales de emergencia internacionales

Conocidas como señales de emergencia en Morse:
- SOS: ···−−−···
- OK: −−−−·
- MAYDAY: voz para emergencia (internacional)
- Canal 16 VHF (156.8 MHz): emergencia marítima internacional

## Herramientas de diagnóstico

- Frecuencímetro: para medir frecuencias exactas
- SWR metro: para medir relación de ondas estacionarias en antenas
- Medidor de campo: para detectar presencia de señal RF

## Normativa

- En la mayoría de países se permite baja potencia sin licencia en ciertas bandas
- Es responsabilidad del operador conocer las regulaciones locales
- En Chile: SUBTEL regula las frecuencias de radioaficionado
- Las frecuencias de emergencia están reservadas y no deben usarse para tráfico no esencial
