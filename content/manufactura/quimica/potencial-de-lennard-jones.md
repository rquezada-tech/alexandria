---
title: "Potencial de Lennard-Jones"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Potencial de Lennard-Jones
    
    
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
  
  
    
      
        
          
            
              
## Potencial de Lennard-Jones

            
            
            
              
                

              

              
Un par de átomos o moléculas neutros están sujetos a dos fuerzas distintas en el límite de una gran separación y de una pequeña separación: una fuerza atractiva actúa a grandes distancias (fuerzas de dispersión) y una fuerza repulsiva actuando a pequeñas distancias (el resultado de la sobreposición de los orbitales electrónicos, conocido como la repulsión de Pauli). El potencial de Lennard-Jones (también conocido como el potencial L-J, el potencial 6-12 o, con menor frecuencia, como el potencial 12-6) es un modelo matemático sencillo para representar este comportamiento.

Fue propuesto en 1924 por el  matemático y físico teórico inglés  John Lennard-Jones (1894-1954).[1]​

## Formulación

El potencial de Lennard-Jones es de la forma:

  
    
      
        V
        (
        r
        )
        =
        4
        ϵ
        
          [
          
            
              
                (
                
                  
                    σ
                    r
                  
                
                )
              
              
                12
              
            
            −
            
              
                (
                
                  
                    σ
                    r
                  
                
                )
              
              
                6
              
            
          
          ]
        
      
    
    {\displaystyle V(r)=4\epsilon \left[\left({\frac {\sigma }{r}}\right)^{12}-\left({\frac {\sigma }{r}}\right)^{6}\right]}
  

donde:

- 
  
    
      
        
        ϵ
      
    
    {\displaystyle \,\epsilon }
  
 es la profundidad del potencial,

- 
  
    
      
        
        σ
      
    
    {\displaystyle \,\sigma }
  
 es la distancia (finita) en la que el potencial entre partículas es un mínimo y

- r es la distancia entre partículas.
Estos parámetros pueden ser ajustados para reproducir datos experimentales o pueden ser deducidos de resultados muy precisos de cálculos de química cuántica. El término 
  
    
      
        
          r
          
            −
            12
          
        
      
    
    {\displaystyle r^{-12}}
  
 describe la repulsión y el término 
  
    
      
        
          r
          
            −
            6
          
        
      
    
    {\displaystyle r^{-6}}
  
 describe la atracción.

La función que describe la fuerza a la que están sujetas las partículas es opuesta al gradiente del potencial arriba descrito:

  
    
      
        
          
            
              F
              →
            
          
        
        (
        r
        )
        =
        −
        
          
            
              ∇
              →
            
          
        
        V
        (
        r
        )
        =
        −
        
          
            
              d
              V
              (
              r
              )
            
            
              d
              r
            
          
        
        
          
            
              r
              ^
            
          
        
        =
        4
        ϵ
        
          (
          
            12
            
            
              
                
                  
                    σ
                  
                  
                    12
                  
                
                
                  
                    r
                  
                  
                    13
                  
                
              
            
            −
            6
            
            
              
                
                  
                    σ
                  
                  
                    6
                  
                
                
                  
                    r
                  
                  
                    7
                  
                
              
            
          
          )
        
        
          
            
              r
              ^
            
          
        
      
    
    {\displaystyle {\vec {F}}(r)=-{\vec {\nabla }}V(r)=-{\frac {dV(r)}{dr}}{\hat {r}}=4\epsilon \left(12\,{\frac {{\sigma }^{12}}{{r}^{13}}}-6\,{\frac {{\sigma }^{6}}{{r}^{7}}}\right){\hat {r}}}
  

El potencial de Lennard-Jones es una aproximación. La forma del término que describe la repulsión no tiene ninguna justificación teórica; la fuerza repulsiva debe depender exponencialmente de la distancia, pero el término de la fórmula de L-J es más conveniente debido a la facilidad y eficiencia de calcular r12 como el cuadrado de r6. Su origen físico está relacionado al principio de exclusión de Pauli: cuando dos nubes electrónicas circulando los átomos se empiezan a sobreponer, la energía del sistema aumenta abruptamente. El exponente 12 fue elegido exclusivamente por su facilidad de cálculo.

## Formas alternativas

La función del potencial de Lennard-Jones comúnmente se escribe de la siguiente forma:

  
    
      
        V
        (
        r
        )
        =
        ϵ
        
          [
          
            
              
                (
                
                  
                    
                      r
                      
                        m
                        i
                        n
                      
                    
                    r
                  
                
                )
              
              
                12
              
            
            −
            2
            
              
                (
                
                  
                    
                      r
                      
                        m
                        i
                        n
                      
                    
                    r
                  
                
                )
              
              
                6
              
            
          
          ]
        
      
    
    {\displaystyle V(r)=\epsilon \left[\left({\frac {r_{min}}{r}}\right)^{12}-2\left({\frac {r_{min}}{r}}\right)^{6}\right]}
  

donde 
  
    
      
        
        
          r
          
            m
            i
            n
          
        
      
    
    {\displaystyle \,r_{min}}
  
 = 
  
    
      
        
        
          2
          
            1
            
              /
            
            6
          
        
        σ
      
    
    {\displaystyle \,2^{1/6}\sigma }
  
 es la distancia en la que el potencial se encuentra en un mínimo.

La formulación más sencilla, usada comúnmente por software de simulación, es:

  
    
      
        V
        (
        r
        )
        =
        
          
            A
            
              r
              
                12
              
            
          
        
        −
        
          
            B
            
              r
              
                6
              
            
          
        
      
    
    {\displaystyle V(r)={\frac {A}{r^{12}}}-{\frac {B}{r^{6}}}}
  

donde:

- 
  
    
      
        
        A
        =
        4
        ϵ
        
          σ
          
            12
          
        
        
        B
        =
        4
        ϵ
        
          σ
          
            6
          
        
        
        σ
        =
        
          
            (
            
              
                A
                B
              
            
            )
          
          
            
              1
              6
            
          
        
        
        ϵ
        =
        
          
            
              B
              
                2
              
            
            
              4
              A
            
          
        
      
    
    {\displaystyle \,A=4\epsilon \sigma ^{12}\qquad B=4\epsilon \sigma ^{6}\qquad \sigma =\left({\frac {A}{B}}\right)^{\frac {1}{6}}\qquad \epsilon ={\frac {B^{2}}{4A}}}
  

## Simulación de dinámica molecular: potencial truncado

En general, para ahorrar tiempo computacional, el potencial de Lennard-Jones es truncado en la distancia límite de 
  
    
      
        
          
            r
            
              c
            
          
          =
          2.5
          σ
        
      
    
    {\displaystyle \displaystyle r_{c}=2.5\sigma }
  
, donde

  
    
      
        
          V
          (
          
            r
            
              c
            
          
          )
          =
          V
          (
          2.5
          σ
          )
          =
          4
          ϵ
          
            [
            
              
                
                  (
                  
                    
                      σ
                      
                        2.5
                        σ
                      
                    
                  
                  )
                
                
                  12
                
              
              −
              
                
                  (
                  
                    
                      σ
                      
                        2.5
                        σ
                      
                    
                  
                  )
                
                
                  6
                
              
            
            ]
          
          =
          −
          0.0163
          ϵ
          =
          −
          
            
              1
              61.3
            
          
          ϵ
        
      
    
    {\displaystyle \displaystyle V(r_{c})=V(2.5\sigma )=4\epsilon \left[\left({\frac {\sigma }{2.5\sigma }}\right)^{12}-\left({\frac {\sigma }{2.5\sigma }}\right)^{6}\right]=-0.0163\epsilon =-{\frac {1}{61.3}}\epsilon }
  

i.e., en 
  
    
      
        
          
            r
            
              c
            
          
          =
          2.5
          σ
        
      
    
    {\displaystyle \displaystyle r_{c}=2.5\sigma }
  
, el potencial LJ 
  
    
      
        
          V
        
      
    
    {\displaystyle \displaystyle V}
  
 es aproximadamente 1/60 de su valor mínimo 
  
    
      
        
          ϵ
        
      
    
    {\displaystyle \displaystyle \epsilon }
  
 (profundidad del potencial).

Después de 
  
    
      
        
          
            r
            
              c
            
          
        
      
    
    {\displaystyle \displaystyle r_{c}}
  
, se le asigna el valor 0 al potencial computacional.

Por otro lado, para evitar una discontinuidad en 
  
    
      
        
          
            r
            
              c
            
          
        
      
    
    {\displaystyle \displaystyle r_{c}}
  
, como se muestra en la ecuación 1, el potencial de LJ es desplazado ligeramente hacia arriba, de tal forma que el potencial computacional sea 0 exactamente en la distancia límite 
  
    
      
        
          
            r
            
              c
            
          
        
      
    
    {\displaystyle \displaystyle r_{c}}
  
.

## Potencial de Mie

El potencial de Lennard-Jones es un caso especial del potencial de Mie

  
    
      
        V
        (
        r
        )
        =
        
          
            
              C
              
                n
              
            
            
              r
              
                n
              
            
          
        
        −
        
          
            
              C
              
                m
              
            
            
              r
              
                m
              
            
          
        
      
    
    {\displaystyle V(r)={\frac {C_{n}}{r^{n}}}-{\frac {C_{m}}{r^{m}}}}
  
,
ya propuesto en 1903 por el físico alemán Gustav Mie[2]​

## Referencias

- ↑ Lennard-Jones, J. E. Cohesion. Proceedings of the Physical Society 1931, 43, 461-482.

- ↑ Potencial de Mie (en inglés).

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q898493

-  Multimedia: Lennard-Jones potentials / Q898493

- Identificadores

- GND: 4329539-3

-  Datos: Q898493

-  Multimedia: Lennard-Jones potentials / Q898493

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.