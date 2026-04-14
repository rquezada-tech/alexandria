---
title: "Reactor químico"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Reactor químico
    
    
- 
    
-  
- 
    
- 
    
- 
    
- 
    
- 
    
- 
    
    
- 
    
- 
    
- 
    
- 
    
- 
  
  
    
      
        
          
            
              
## Reactor químico

            
            
            
              
                

              

              Un reactor químico es un equipo en cuyo interior tiene lugar una reacción química, diseñado para maximizar la conversión y la selectividad de esa reacción con el menor coste posible. Si la reacción química es catalizada por una enzima purificada o por el organismo que la contiene, se habla de biorreactores. El diseño de un reactor químico requiere conocimientos de termodinámica, cinética química, transferencia de masa y energía, así como de mecánica de fluidos; balances de materia y energía son necesarios. Por lo general se busca conocer el tamaño y el tipo de reactor, así como el método de operación. Además, con base en los parámetros de diseño se espera poder predecir con alguna certidumbre la conducta de un reactor ante ciertas condiciones; por ejemplo, un salto en escalón en la composición de entrada.

## Tipos de reactores químicos

Existen varias formas de clasificarlos:

## Según el modo de operación

- Reactores discontinuos: son aquellos que trabajan por cargas, es decir se introduce una alimentación, y se espera un tiempo dado, que viene determinado por la cinética de la reacción, tras el cual se saca el producto.

- Reactores continuos: son todos aquellos que trabajan de forma continua.

## Según el tipo de flujo interno

- Reactores ideales: suelen ser descritos con ecuaciones ideales sencillas y no consideran efectos físicos más complejos o perturbaciones pequeñas.

- Reactores no ideales: consideran el patrón de flujo, la existencia de zonas muertas dentro del reactor donde el material no circula, además consideran una dinámica de fluidos más compleja, suelen describirse conociendo la cinética de las reacciones, la RTD (distribución de edad del fluido) del flujo, el tipo de mezclado pudiendo ser este tardío o inmediato, y conociendo si el tipo de fluido es micro o macro fluido.

## Según las fases que albergan

- Reactores homogéneos: tienen una única fase, líquida o gas.

- Reactores heterogéneos: tienen varias fases, gas-sólido, líquido-sólido, gas-líquido, gas-líquido-sólido.
Idealmente, pueden suponerse tres tipos de reactores homogéneos:

## Reactor Batch

 
Trabajan en estado no estacionario y el más sencillo sería un tanque agitado. Este reactor tiene la ventaja de que su costo de instrumentación es bajo, además de ser flexible en su uso (se le puede detener de modo fácil y rápido). Tiene la desventaja de un elevado costo en su funcionamiento y de mano de obra debido a la gran cantidad de tiempo que se pasa parado debido a la carga, descarga y limpieza; Además no siempre es posible implementar un sistema de control adecuado. Este reactor suele usarse en pequeñas producciones o pruebas piloto. Asumiendo que en un reactor Batch la composición es uniforme en cualquier instante y basándose en la selección de un componente limitante; Las ecuaciones de diseño para este tipo de reactor en estado estacionario se deducen de la siguiente forma (se toma como ejemplo la especie molar A):

  
    
      
        E
        n
        t
        r
        a
        d
        a
        =
        S
        a
        l
        i
        d
        a
        −
        G
        e
        n
        e
        r
        a
        d
        o
        +
        C
        o
        n
        s
        u
        m
        i
        d
        o
        +
        A
        c
        u
        m
        u
        l
        a
        d
        o
      
    
    {\displaystyle Entrada=Salida-Generado+Consumido+Acumulado}
  
[1]​

  
    
      
        0
        =
        0
        +
        0
        +
        C
        o
        n
        s
        u
        m
        o
        +
        A
        c
        u
        m
        u
        l
        a
      
    
    {\displaystyle 0=0+0+Consumo+Acumula}
  

  
    
      
        (
        
          r
          
            A
          
        
        V
        )
        =
        
          
            
              d
              
                N
                
                  A
                
              
            
            
              d
              t
            
          
        
      
    
    {\displaystyle (r_{A}V)={\frac {dN_{A}}{dt}}}
  

Siendo V el volumen del fluido en el reactor y 
  
    
      
        (
        −
        
          r
          
            A
          
        
        )
      
    
    {\displaystyle (-r_{A})}
  
 la velocidad de reacción para el componente limitante.
Evaluando los términos de la ecuación anterior se puede calcular el tiempo de residencia necesario para alcanzar la conversión deseada. 

  
    
      
        
          r
          
            A
          
        
        V
        =
        
          
            
              d
              
                N
                
                  A
                
              
            
            
              d
              t
            
          
        
      
    
    {\displaystyle r_{A}V={\frac {dN_{A}}{dt}}}
  

  
    
      
        −
        
          r
          
            A
          
        
        V
        =
        
          N
          
            A
            0
          
        
        
          
            
              d
              
                X
                
                  A
                
              
            
            
              d
              t
            
          
        
      
    
    {\displaystyle -r_{A}V=N_{A0}{\frac {dX_{A}}{dt}}}
  

  
    
      
        t
        =
        
          ∫
          
            0
          
          
            
              X
              
                A
              
            
          
        
        
          
            
              N
              
                A
                0
              
            
            
              −
              
                r
                
                  A
                
              
              V
            
          
        
        d
        X
      
    
    {\displaystyle t=\int _{0}^{X_{A}}{\frac {N_{A0}}{-r_{A}V}}dX}
  

donde X representa la conversión lograda y está relacionada con la concentración, están relacionadas por:  

  
    
      
        
          C
          
            A
            0
          
        
        
          X
          
            A
          
        
        =
        
          C
          
            A
            0
          
        
        −
        
          C
          
            A
          
        
      
    
    {\displaystyle C_{A0}X_{A}=C_{A0}-C_{A}}
  

X toma un valor entre 0 y 1

Para aquellas reacciones en las que el volumen de la mezcla cambia proporcionalmente a la conversión la ecuación se transforma en 

  
    
      
        t
        =
        
          ∫
          
            a
          
          
            b
          
        
        
          
            
              N
              
                A
                0
              
            
            
              −
              
                r
                
                  A
                
              
              
                V
                
                  A
                
              
              (
              1
              +
              ε
              
                X
                
                  A
                
              
              )
            
          
        
        d
        X
      
    
    {\displaystyle t=\int _{a}^{b}{\frac {N_{A0}}{-r_{A}V_{A}(1+\varepsilon X_{A})}}dX}
  

Siendo 
  
    
      
        ε
      
    
    {\displaystyle \varepsilon }
  
 una constante representativa del cambio del volumen en relación con la conversión, en términos matemáticos:  

  
    
      
        ε
        =
        
          
            
              
                V
                
                  
                    x
                    
                      A
                    
                  
                  =
                  1
                
              
              −
              
                V
                
                  
                    x
                    
                      A
                    
                  
                  =
                  0
                
              
            
            
              V
              
                
                  x
                  
                    A
                  
                
                =
                0
              
            
          
        
      
    
    {\displaystyle \varepsilon ={\frac {V_{x_{A}=1}-V_{x_{A}=0}}{V_{x_{A}=0}}}}
  

para cambios en otros componentes se tiene:

  
    
      
        
          ε
          
            A
          
        
        
          X
          
            A
          
        
        =
        
          ε
          
            B
          
        
        
          X
          
            B
          
        
      
    
    {\displaystyle \varepsilon _{A}X_{A}=\varepsilon _{B}X_{B}}
  

Aparte del tiempo de reacción, en un proceso industrial debe añadirse el tiempo de carga, descarga y limpieza para un este tipo de reactores y en general procesos en lotes.

El balance de energía para este tipo de reactor ofrece 3 posibilidades que dependen del modo de operación y de las exigencias de producción requeridas.

- modo politrópico:    
  
    
      
        m
        ⋅
        
          C
          
            p
          
        
        ⋅
        
          
            
              d
              T
            
            
              d
              t
            
          
        
        =
        U
        ⋅
        A
        ⋅
        (
        
          T
          
            s
            e
            r
            v
            i
            c
            i
            o
          
        
        −
        
          T
          
            r
            e
            a
            c
            t
            o
            r
          
        
        )
        +
        R
        ⋅
        −
        
          Δ
          
            r
          
        
        H
        ⋅
        V
      
    
    {\displaystyle m\cdot C_{p}\cdot {\frac {dT}{dt}}=U\cdot A\cdot (T_{servicio}-T_{reactor})+R\cdot -\Delta _{r}H\cdot V}
  

- modo isotérmico:       
  
    
      
        0
        =
        U
        ⋅
        A
        ⋅
        (
        
          T
          
            s
            e
            r
            v
            i
            c
            i
            o
          
        
        −
        
          T
          
            r
            e
            a
            c
            t
            o
            r
          
        
        )
        +
        R
        ⋅
        −
        
          Δ
          
            r
          
        
        H
        ⋅
        V
      
    
    {\displaystyle 0=U\cdot A\cdot (T_{servicio}-T_{reactor})+R\cdot -\Delta _{r}H\cdot V}
  

- modo adiabático:     
  
    
      
        m
        ⋅
        
          C
          
            p
          
        
        ⋅
        
          
            
              d
              T
            
            
              d
              t
            
          
        
        =
        R
        ⋅
        −
        
          Δ
          
            r
          
        
        H
        ⋅
        V
      
    
    {\displaystyle m\cdot C_{p}\cdot {\frac {dT}{dt}}=R\cdot -\Delta _{r}H\cdot V}
  

Al mencionar servicio se hace referencia a los servicios térmicos, como ejemplo se puede mencionar el sistema de calentamiento por vapor, o el uso de un intercambiador de chaqueta en un recipiente.

## Reactor continuo de tanque agitado (CSTR)

Estos reactores trabajan en estado estacionario, es decir, que sus propiedades no varían con el tiempo. Este modelo ideal supone que la reacción alcanza la máxima conversión en el instante en que la alimentación entra al tanque. Es decir, que en cualquier punto de este equipo las concentraciones son iguales a las de la corriente de salida. Además para este tipo de reactor se considera que la velocidad de reacción para cualquier punto dentro del tanque es la misma y suele evaluarse a la concentración de salida. Para este reactor suele asumirse que existe un mezclado perfecto, en la práctica esto no es así, pero puede crearse un mezclado de alta eficiencia que se aproxima a las condiciones ideales.  

El balance de materia para este reactor en términos molares es el siguiente.

  
    
      
        
          
            
              d
              
                N
                
                  i
                
              
            
            
              d
              t
            
          
        
        =
        
          F
          
            i
            o
          
        
        −
        
          F
          
            i
          
        
        +
        V
        
          ν
          
            i
          
        
        
          r
          
            i
          
        
      
    
    {\displaystyle {\frac {dN_{i}}{dt}}=F_{io}-F_{i}+V\nu _{i}r_{i}}
  

  
    
      
        
          F
          
            i
          
        
      
    
    {\displaystyle F_{i}}
  
 representa el flujo molar de la especie indicada en el subíndice, está relacionado con el flujo volumétrico

  
    
      
        
          F
          
            i
          
        
        =
        v
        ∗
        
          C
          
            A
          
        
      
    
    {\displaystyle F_{i}=v*C_{A}}
  

suponiendo que el sistema opera en estado estacionario, el cambio de concentración molar tiende a cero.

En términos de conversión molar y tomando como ejemplo la especie reaccionante A de coeficiente estequiométrico igual a 1. El balance se reduce a

  
    
      
        
          F
          
            A
            0
          
        
        −
        
          F
          
            A
            0
          
        
        (
        1
        −
        
          X
          
            A
          
        
        )
        −
        (
        −
        
          r
          
            A
          
        
        V
        )
        =
        0
      
    
    {\displaystyle F_{A0}-F_{A0}(1-X_{A})-(-r_{A}V)=0}
  

una posterior simplificación matemática muestra:

  
    
      
        
          F
          
            A
            0
          
        
        
          X
          
            A
          
        
        =
        (
        −
        
          r
          
            A
          
        
        V
        )
      
    
    {\displaystyle F_{A0}X_{A}=(-r_{A}V)}
  

El diseño de operaciones tanto en sistemas CSTR como en reactores PFR usualmente es deseado determinar el “tiempo de residencia” (representado por la letra 
  
    
      
        τ
      
    
    {\displaystyle \tau }
  
 y dimensionalmente se mide en segundos ) y el factor de escala (representado por la letra S), este último expresado como el volumen por unidad de masa del producto, los problemas de optimización se enfocan en reducir tanto 
  
    
      
        τ
      
    
    {\displaystyle \tau }
  
 como S, esto se logra manipulando la relación de concentración entre los reactantes.

para CSTR

  
    
      
        
          
            
              
                C
                
                  A
                  0
                
              
              
                X
                
                  A
                
              
            
            
              −
              
                r
                
                  A
                
              
            
          
        
        =
        
          
            
              
                C
                
                  A
                  0
                
              
              V
            
            
              F
              
                A
                0
              
            
          
        
        =
        τ
      
    
    {\displaystyle {\frac {C_{A0}X_{A}}{-r_{A}}}={\frac {C_{A0}V}{F_{A0}}}=\tau }
  

Este tipo de reactor resulta muy atractivo para estudios cinéticos debido a su simplicidad del cálculo característica.

La configuración óptima para este tipo de reactor depende de parámetros. La inversión en capital en equipo es importante, pero los costos de energía y el costo del producto es factor determinante,  el uso de reactores en batería es muy común en la industria debido a que suele ser rentable.

Balance de energía:

  
    
      
        0
        =
        ρ
        ⋅
        
          C
          
            p
          
        
        ⋅
        
          
            
              V
              ˙
            
          
        
        ⋅
        (
        
          T
          
            e
            n
            t
            r
            a
            d
            a
          
        
        −
        
          T
          
            r
            e
            a
            c
            t
            o
            r
          
        
        )
        +
        U
        ⋅
        A
        ⋅
        (
        
          T
          
            s
            e
            r
            v
            i
            c
            i
            o
          
        
        −
        
          T
          
            r
            e
            a
            c
            t
            o
            r
          
        
        )
        +
        R
        ⋅
        −
        
          Δ
          
            r
          
        
        H
        ⋅
        V
      
    
    {\displaystyle 0=\rho \cdot C_{p}\cdot {\dot {V}}\cdot (T_{entrada}-T_{reactor})+U\cdot A\cdot (T_{servicio}-T_{reactor})+R\cdot -\Delta _{r}H\cdot V}
  

## Reactores en flujo pistón (PFR)

Estos reactores trabajan en estado estacionario. Es decir, las propiedades en un punto determinado del reactor son constantes con el tiempo. Este modelo supone un flujo ideal de pistón, y la conversión es función de la posición. En este tipo de reactor la composición del fluido varía de un punto a otro a través de la dirección del flujo, esto implica que el balance para un componente dado de la o las reacciones químicas implicadas o debe realizarse en un elemento diferencial de volumen.

Balance de materia:

  
    
      
        E
        n
        t
        r
        a
        d
        a
        −
        s
        a
        l
        i
        d
        a
        +
        g
        e
        n
        e
        r
        a
        c
        i
        o
        n
        −
        c
        o
        n
        s
        u
        m
        o
        =
        0
      
    
    {\displaystyle Entrada-salida+generacion-consumo=0}
  

  
    
      
        
          F
          
            A
          
        
        −
        (
        
          F
          
            A
          
        
        +
        d
        
          F
          
            A
          
        
        )
        −
        (
        −
        
          r
          
            A
          
        
        d
        V
        )
        =
        0
      
    
    {\displaystyle F_{A}-(F_{A}+dF_{A})-(-r_{A}dV)=0}
  

pero 

  
    
      
        
          F
          
            A
          
        
        =
        
          F
          
            A
            0
          
        
        (
        1
        −
        
          X
          
            A
          
        
        )
      
    
    {\displaystyle F_{A}=F_{A0}(1-X_{A})}
  
                      

y 

  
    
      
        d
        
          F
          
            A
          
        
        =
        −
        
          F
          
            A
            0
          
        
        d
        
          X
          
            A
          
        
      
    
    {\displaystyle dF_{A}=-F_{A0}dX_{A}}
  

A fin de encontrar la ecuación de diseño, es necesario integrar la expresión, considerando que la velocidad de alimentación es constante, sustituyendo las ecuaciones anteriores en el balance general, agrupando términos y después integrando, se obtiene:

  
    
      
        τ
        =
        
          C
          
            A
            0
          
        
        
          ∫
          
            0
          
          
            
              X
              
                A
              
            
          
        
        
          
            
              d
              X
            
            
              −
              
                r
                
                  A
                
              
            
          
        
      
    
    {\displaystyle \tau =C_{A0}\int _{0}^{X_{A}}{\frac {dX}{-r_{A}}}}
  
 

Se puede observar que, a diferencia de la ecuación de diseño para el reactor MFR, la velocidad de reacción es variable, por lo general para mecanismos de reacción complejos suelen usarse métodos de integración gráfica, como series de Simpson, método de sumas de trapecios, cuadratura gaussiana, etc., el uso de software computacional suele ser útil para estos procedimientos.

Respecto al balance de energía, también se basa en un modelo diferencial.

Balance de energía (reactor cilíndrico):

  
    
      
        
          
            
              m
              ˙
            
          
        
        ⋅
        
          C
          
            p
          
        
        ⋅
        
          
            
              d
              T
            
            
              d
              V
            
          
        
        =
        U
        ⋅
        d
        A
        ⋅
        (
        
          T
          
            s
            e
            r
            v
            i
            c
            i
            o
          
        
        −
        
          T
          
            r
            e
            a
            c
            t
            o
            r
          
        
        )
        +
        R
        ⋅
        −
        
          Δ
          
            r
          
        
        H
      
    
    {\displaystyle {\dot {m}}\cdot C_{p}\cdot {\frac {dT}{dV}}=U\cdot dA\cdot (T_{servicio}-T_{reactor})+R\cdot -\Delta _{r}H}
  

## Reactores heterogéneos

Existe un tipo especial de reactores que debido a su naturaleza obedece leyes cinéticas diferentes, además de que por su complejidad los balances de materia y energía son más complejos, la diferencia radica en el número de fases físicas involucradas, los mecanismos de transferencia tanto de calor como de energía son más complejos debido a que están presentes más de un mecanismo, pudiendo ser de naturaleza convectiva o conductiva.

## Reactor catalítico

Suelen ser de dos tipos: fluidizado o de lecho empacado, la elección depende de la reacción de interés y del mecanismo cinético observado

Los reactores de lecho fluidizado poseen las siguientes propiedades:

- El flujo es complejo, no es bien conocido, solo se puede estimar de forma aproximada los mecanismos de transferencia de masa, desde el punto de vista de transferencia el contacto no es muy eficiente debido a la diferencia de varias barreras físicas, esto obliga a usar una mayor cantidad de catalizador.

- El control de temperatura se realiza de forma más fácil, comparado con el reactor de lecho empacado.

- La reactivación del catalizador en caso de ser necesaria es más fácil y eficiente debido a la fluidización presente debido a que es posible bombear y transportar el catalizador.

- Este tipo de flujo es adecuado para partículas de tamaño pequeño, ideal para reacciones rápidas en donde se necesita una área de contacto grande.

El reactor de lecho empacado posee las siguientes características:

- La regeneración del catalizador requiere del uso de gases; Es común usar un sistema de re-circulación a fin de aumentar la eficiencia de reactivación

- Este sistema presenta dificultades en el control de temperatura debido a la formación de zonas calientes y frías en el interior del lecho.

- No se puede usar un tamaño de catalizador pequeño debido a la formación de tapones y caídas de presión.
Balance de materia:
Al igual que el PFR, el balance es diferencial, además se toma en cuenta la difusión radial, el balance se realiza tomando en cuenta una geometría radial.

  
    
      
        
          u
          
            0
          
        
        
          C
          
            0
          
        
        [
        
          
            
              ∂
              x
            
            
              ∂
              z
            
          
        
        −
        
          
            D
            u
          
        
        (
        
          
            
              
                ∂
                
                  2
                
              
              x
            
            
              ∂
              
                z
                
                  2
                
              
            
          
        
        +
        
          
            1
            r
          
        
        
          
            
              ∂
              x
            
            
              ∂
              r
            
          
        
        )
        ]
        −
        ρ
        
          r
          
            c
          
        
        =
        0
      
    
    {\displaystyle u_{0}C_{0}[{\frac {\partial x}{\partial z}}-{\frac {D}{u}}({\frac {\partial ^{2}x}{\partial z^{2}}}+{\frac {1}{r}}{\frac {\partial x}{\partial r}})]-\rho r_{c}=0}
  
[2]​

Condiciones límite:

  
    
      
        
          x
          
            0
          
        
        =
        x
        (
        0
        ,
        r
        )
      
    
    {\displaystyle x_{0}=x(0,r)}
  

  
    
      
        
          
            
              ∂
              x
            
            
              ∂
              r
            
          
        
        =
        0
      
    
    {\displaystyle {\frac {\partial x}{\partial r}}=0}
  
,
  
    
      
        r
        =
        R
      
    
    {\displaystyle r=R}
  

Balance de energía:

  
    
      
        
          
            
              m
              ˙
            
          
        
        
          C
          
            p
          
        
        [
        
          
            
              
                ∂
                
                  2
                
              
              T
            
            
              ∂
              
                z
                
                  2
                
              
            
          
        
        −
        
          
            D
            u
          
        
        (
        
          
            
              
                ∂
                
                  2
                
              
              T
            
            
              ∂
              
                z
                
                  2
                
              
            
          
        
        +
        
          
            1
            r
          
        
        
          
            
              ∂
              T
            
            
              ∂
              r
            
          
        
        )
        ]
        +
        ρ
        Δ
        
          H
          
            r
          
        
        
          r
          
            c
          
        
        =
        0
      
    
    {\displaystyle {\dot {m}}C_{p}[{\frac {\partial ^{2}T}{\partial z^{2}}}-{\frac {D}{u}}({\frac {\partial ^{2}T}{\partial z^{2}}}+{\frac {1}{r}}{\frac {\partial T}{\partial r}})]+\rho \Delta H_{r}r_{c}=0}
  

Condiciones límite:

  
    
      
        
          T
          
            0
          
        
        =
        T
        (
        0
        ,
        r
        )
      
    
    {\displaystyle T_{0}=T(0,r)}
  

  
    
      
        k
        
          
            
              ∂
              T
            
            
              ∂
              r
            
          
        
        =
        U
        (
        
          T
          
            e
            n
            t
            o
            r
            n
            o
          
        
        −
        T
        )
      
    
    {\displaystyle k{\frac {\partial T}{\partial r}}=U(T_{entorno}-T)}
  
,
  
    
      
        r
        =
        R
      
    
    {\displaystyle r=R}
  

## Reactores no ideales

En muchas situaciones estos modelos ideales son válidos para casos reales, en caso contrario se habrán de introducir en los balances de materia, energía y presión términos que reflejen la desviación de la idealidad. Si por ejemplo la variación de las propiedades se debe a fenómenos de transporte de materia o calor se pueden introducir las leyes de Fick o Fourier respectivamente.

## Véase también

- Diseño de reactores

## Referencias

- ↑ Schmidt, Lanny D., The Engineering of Chemical Reactions. New York: Oxford University Press, 1998. ISBN 0-19-510588-5.

- ↑ Stanley M. Walas, Chemical Process Equipment, Selection and Design cap.17 ISBN 0-7506-9385-1 

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q557573

-  Multimedia: Chemical reactors / Q557573

- Identificadores

- NKC: ph119151

- NLI: 987007285072005171

- Diccionarios y enciclopedias

- Britannica: url

-  Datos: Q557573

-  Multimedia: Chemical reactors / Q557573

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.