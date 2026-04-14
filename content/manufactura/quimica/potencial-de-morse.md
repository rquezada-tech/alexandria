---
title: "Potencial de Morse"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Potencial de Morse
    
    
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
  
  
    
      
        
          
            
              
## Potencial de Morse

            
            
            
              
                

              

              
El potencial de Morse, nombrado así en honor al físico Philip M. Morse, es un modelo conveniente para la energía potencial de una molécula diatómica. Es una mejor aproximación para la estructura vibracional de la molécula que el oscilador armónico cuántico porque incluye explícitamente los efectos de la ruptura del enlace, tales como la existencia de estados no enlazados. También da cuenta de la anarmonicidad de los enlaces reales y de la probabilidad de la transición no-cero para los sobretonos y las bandas de combinación. El potencial de Morse también puede usarse para modelar otras interacciones como la que se da entre un átomo y una superficie. Debido a su simplicidad (sólo tres parámetros ajustables), no es utilizada en la espectroscopía moderna. Sin embargo, su forma matemática inspiró el potencial MLR (Morse de largo alcance, Morse/Long-range), el cual es la función de energía potencial más popular para explicar los datos espectroscópicos. 

## Función de energía potencial

La función de la energía potencial de Morse tiene la siguiente forma:[1]​

  
    
      
        
          V
          ′
        
        (
        r
        )
        =
        
          D
          
            e
          
        
        (
        1
        −
        
          e
          
            −
            α
            (
            r
            −
            
              r
              
                e
              
            
            )
          
        
        
          )
          
            2
          
        
      
    
    {\displaystyle V'(r)=D_{e}(1-e^{-\alpha (r-r_{e})})^{2}}
  

Donde 
  
    
      
        r
      
    
    {\displaystyle r}
  
 es la distancia entre los átomos, 
  
    
      
        
          r
          
            e
          
        
      
    
    {\displaystyle r_{e}}
  
 es la distancia de enlace al equilibrio, 
  
    
      
        
          D
          
            e
          
        
      
    
    {\displaystyle D_{e}}
  
 es la profundidad del pozo (definida en relación con los átomos disociados) y 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 es una variable que controla el ancho del potencial (mientras más pequeño sea 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
, más grande es el pozo). La energía de disociación del enlace puede ser calculada al restar la energía de punto cero 
  
    
      
        
          E
          
            0
          
        
      
    
    {\displaystyle E_{0}}
  
 de la profundidad del pozo. La constante de fuerza (rigidez) del enlace puede encontrarse mediante una expansión de Taylor de 
  
    
      
        
          V
          ′
        
        (
        r
        )
      
    
    {\displaystyle V'(r)}
  
 cuando 
  
    
      
        r
        =
        
          r
          
            e
          
        
      
    
    {\displaystyle r=r_{e}}
  
 para la segunda derivada de la función de energía potencial, de al cual puede demostrarse que el parámetro 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 es:

  
    
      
        α
        =
        
          
            
              
                k
                
                  e
                
              
              
                2
                
                  D
                  
                    e
                  
                
              
            
          
        
      
    
    {\displaystyle \alpha ={\sqrt {\frac {k_{e}}{2D_{e}}}}}
  

Donde 
  
    
      
        
          k
          
            e
          
        
      
    
    {\displaystyle k_{e}}
  
 es la constante de fuerza en el mínimo del pozo. 

Debido a que el cero de la energía potencial es arbitrario, la ecuación del potencial de Morse puede ser reescrita en cualquier número de formara agregando o restando un valor constante. Cuando se utiliza para modelar la interacción átomo-superficie, la energía cero puede ser redefinida para que el potencial tenga la forma: 

  
    
      
        
          V
          ′
        
        (
        r
        )
        =
        
          V
          ′
        
        (
        r
        )
        −
        
          D
          
            e
          
        
        =
        
          D
          
            e
          
        
        (
        1
        −
        
          e
          
            −
            α
            (
            r
            −
            
              r
              
                e
              
            
            )
          
        
        
          )
          
            2
          
        
        −
        
          D
          
            e
          
        
      
    
    {\displaystyle V'(r)=V'(r)-D_{e}=D_{e}(1-e^{-\alpha (r-r_{e})})^{2}-D_{e}}
  
 

Lo cual, normalmente se escribe como: 

  
    
      
        V
        (
        r
        )
        =
        
          D
          
            e
          
        
        (
        
          e
          
            −
            2
            α
            (
            r
            −
            
              r
              
                e
              
            
            )
          
        
        −
        2
        
          e
          
            −
            α
            (
            r
            −
            
              r
              
                e
              
            
            )
          
        
        )
      
    
    {\displaystyle V(r)=D_{e}(e^{-2\alpha (r-r_{e})}-2e^{-\alpha (r-r_{e})})}
  
 

Donde 
  
    
      
        r
      
    
    {\displaystyle r}
  
 es la coordenada perpendicular a la superficie. Esta forma aproxima el cero a un valor de 
  
    
      
        r
      
    
    {\displaystyle r}
  
 infinito e iguala 
  
    
      
        −
        
          D
          
            e
          
        
      
    
    {\displaystyle -D_{e}}
  
 en su mínimo. Esto muestra que el potencial de Morse es la combinación de un término repulsivo de corto alcance (el primero) y un término atractivo de largo alcance (el segundo), análogo al potencial de Lennard-Jones.

## Estados vibracionales y energías

De la misma forma que oscilador armónico cuántico, las energías y eigenestados del potencial de Morse pueden encontrarse utilizando operadores.[2]​ Una aproximación involucra aplicar el método de factorización al Hamiltoniano.

## Estados estacionarios

Para escribir los estados estacionarios en el potencial de Morse, por ejemplo las soluciones 
  
    
      
        
          Ψ
          
            n
          
        
        (
        r
        )
      
    
    {\displaystyle \Psi _{n}(r)}
  
 y 
  
    
      
        
          E
          
            n
          
        
      
    
    {\displaystyle E_{n}}
  
 de la siguiente ecuación de Schrödinger:

  
    
      
        
          (
          
            −
            
              
                
                  h
                  
                    2
                  
                
                
                  2
                  m
                
              
            
            
              
                
                  ∂
                  
                    2
                  
                
                
                  ∂
                  
                    r
                    
                      2
                    
                  
                
              
            
            )
            +
            V
            (
            r
            )
          
          )
        
        
          Ψ
          
            n
          
        
        (
        r
        )
        =
        
          E
          
            n
          
        
        
          Ψ
          
            n
          
        
        (
        r
        )
      
    
    {\displaystyle \left(-{\frac {h^{2}}{2m}}{\frac {\partial ^{2}}{\partial r^{2}}})+V(r)\right)\Psi _{n}(r)=E_{n}\Psi _{n}(r)}
  

es conveniente introducir las variables:

  
    
      
        x
        =
        a
        r
        ‖
        
          x
          
            e
          
        
        =
        a
        
          r
          
            e
          
        
        ‖
        λ
        =
        
          
            
              2
              m
              
                D
                
                  e
                
              
            
            
              a
              ℏ
            
          
        
        ‖
        
          ϵ
          
            n
          
        
        =
        
          
            
              2
              m
            
            
              
                a
                
                  2
                
              
              
                ℏ
                
                  2
                
              
            
          
        
        
          E
          
            n
          
        
      
    
    {\displaystyle x=ar\|x_{e}=ar_{e}\|\lambda ={\frac {\sqrt {2mD_{e}}}{a\hbar }}\|\epsilon _{n}={\frac {2m}{a^{2}\hbar ^{2}}}E_{n}}
  

Por lo tanto, la ecuación de Scrhödinger, toma la forma:

  
    
      
        
          (
          
            −
            
              
                
                  ∂
                  
                    2
                  
                
                
                  ∂
                  
                    x
                    
                      2
                    
                  
                
              
            
            +
            V
            (
            x
            )
          
          )
        
        
          Ψ
          
            n
          
        
        (
        x
        )
        =
        
          ε
          
            n
          
        
        
          Ψ
          
            n
          
        
        (
        x
        )
      
    
    {\displaystyle \left(-{\frac {\partial ^{2}}{\partial x^{2}}}+V(x)\right)\Psi _{n}(x)=\varepsilon _{n}\Psi _{n}(x)}
  

y 

  
    
      
        V
        (
        x
        )
        =
        
          λ
          
            2
          
        
        
          (
          
            
              e
              
                −
                2
                (
                x
                −
                
                  x
                  
                    e
                  
                
                )
              
            
            −
            2
            
              e
              
                −
                (
                x
                −
                
                  x
                  
                    e
                  
                
                )
              
            
          
          )
        
      
    
    {\displaystyle V(x)=\lambda ^{2}\left(e^{-2(x-x_{e})}-2e^{-(x-x_{e})}\right)}
  

## Eigenvalores y eigenestados

Y sus eigenvalores y eigenestados pueden ser escritos:[3]​

  
    
      
        
          ε
          
            n
          
        
        =
        −
        
          
            (
            
              λ
              −
              n
              −
              
                
                  1
                  2
                
              
            
            )
          
          
            2
          
        
      
    
    {\displaystyle \varepsilon _{n}=-\left(\lambda -n-{\frac {1}{2}}\right)^{2}}
  

donde

  
    
      
        n
        =
        0
        ,
        1
        ,
        .
        .
        .
        ,
        
          [
          
            λ
            −
            
              
                1
                2
              
            
          
          ]
        
      
    
    {\displaystyle n=0,1,...,\left[\lambda -{\frac {1}{2}}\right]}
  

con 
  
    
      
        x
      
    
    {\displaystyle x}
  
 representando la mayor integral menor a 
  
    
      
        
          x
          
            e
          
        
      
    
    {\displaystyle x_{e}}
  

  
    
      
        
          Ψ
          
            n
          
        
        (
        z
        )
        =
        
          N
          
            n
          
        
        
          z
          
            λ
            −
            n
            −
            
              
                1
                2
              
            
          
        
        
          e
          
            −
            
              
                1
                2
              
            
            z
          
        
        
          L
          
            n
          
          
            (
            2
            λ
            −
            2
            n
            −
            1
            )
          
        
        (
        z
        )
      
    
    {\displaystyle \Psi _{n}(z)=N_{n}z^{\lambda -n-{\frac {1}{2}}}e^{-{\frac {1}{2}}z}L_{n}^{(2\lambda -2n-1)}(z)}
  

donde: 

  
    
      
        z
        =
        2
        λ
        
          e
          
            −
            (
            x
            −
            
              x
              
                e
              
            
            )
          
        
      
    
    {\displaystyle z=2\lambda e^{-(x-x_{e})}}
  

  
    
      
        
          N
          
            n
          
        
        =
        
          
            [
            
              
                
                  n
                  !
                  (
                  2
                  λ
                  −
                  2
                  n
                  −
                  1
                  )
                
                
                  Γ
                  (
                  2
                  λ
                  −
                  n
                  )
                  )
                
              
            
            ]
          
          
            
              1
              2
            
          
        
      
    
    {\displaystyle N_{n}=\left[{\frac {n!(2\lambda -2n-1)}{\Gamma (2\lambda -n))}}\right]^{\frac {1}{2}}}
  

y 
  
    
      
        
          L
          
            n
          
          
            (
            a
            )
          
        
        (
        z
        )
      
    
    {\displaystyle L_{n}^{(a)}(z)}
  
 es un polinomio de Laguerre generalizado de la forma:

  
    
      
        
          L
          
            n
          
          
            (
            a
            )
          
        
        (
        z
        )
        =
        
          
            
              
                z
                
                  −
                  a
                
              
              
                e
                
                  z
                
              
            
            
              n
              !
            
          
        
        
          
            
              d
              
                n
              
            
            
              d
              
                z
                
                  n
                
              
            
          
        
        (
        
          z
          
            n
            +
            a
          
        
        
          e
          
            −
            z
          
        
        )
        =
        
          
            
              
                Γ
                (
                a
                +
                n
                +
                1
                )
                
                  /
                
                Γ
                (
                a
                +
                1
                )
              
              
                n
                !
              
            
          
          
            1
          
        
        
          F
          
            1
          
        
        (
        −
        1
        n
        ,
        α
        +
        )
        ,
        z
        )
      
    
    {\displaystyle L_{n}^{(a)}(z)={\frac {z^{-a}e^{z}}{n!}}{\frac {d^{n}}{dz^{n}}}(z^{n+a}e^{-z})={\frac {\Gamma (a+n+1)/\Gamma (a+1)}{n!}}_{1}F_{1}(-1n,\alpha +),z)}
  

## Expresión analítica

También existe la siguiente expresión analítica para elementos de la matriz del operador coordinado:[4]​

  
    
      
        
          ⟨
          
            
              Ψ
              
                m
              
            
            
              |
            
            x
            
              |
            
            
              Ψ
              
                n
              
            
          
          ⟩
        
        =
        
          
            
              2
              (
              −
              1
              
                )
                
                  m
                  −
                  n
                  +
                  1
                
              
            
            
              (
              m
              −
              n
              )
              (
              2
              N
              −
              n
              −
              m
              )
            
          
        
        
          
            
              
                (
                N
                −
                n
                )
                (
                N
                −
                m
                )
                Γ
                (
                2
                N
                −
                m
                +
                1
                )
                m
                !
              
              
                Γ
                (
                2
                N
                −
                n
                +
                1
                )
                n
                !
              
            
          
        
        .
      
    
    {\displaystyle \left\langle \Psi _{m}|x|\Psi _{n}\right\rangle ={\frac {2(-1)^{m-n+1}}{(m-n)(2N-n-m)}}{\sqrt {\frac {(N-n)(N-m)\Gamma (2N-m+1)m!}{\Gamma (2N-n+1)n!}}}.}
  

que es válido siempre que n}">
  
    
      
        m
        >
        n
      
    
    {\displaystyle m>n}
  
n}" loading="lazy"> y 
  
    
      
        N
        =
        λ
        −
        1
        
          /
        
        2
      
    
    {\displaystyle N=\lambda -1/2}
  
. 

## Energía

Las eigenenergías de las variables iniciales tienen la forma:

  
    
      
        
          E
          
            n
          
        
        =
        h
        
          ν
          
            0
          
        
        (
        n
        +
        1
        
          /
        
        2
        )
        −
        
          
            
              [
              h
              
                ν
                
                  0
                
              
              (
              n
              +
              1
              
                /
              
              2
              )
              
                ]
                
                  2
                
              
            
            
              4
              
                D
                
                  e
                
              
            
          
        
      
    
    {\displaystyle E_{n}=h\nu _{0}(n+1/2)-{\frac {[h\nu _{0}(n+1/2)]^{2}}{4D_{e}}}}
  

donde n es el número cuántico vibracional y 
  
    
      
        
          ν
          
            0
          
        
      
    
    {\displaystyle \nu _{0}}
  
 tiene unidades de frecuencia. Esta última está relacionada matemáticamente a la masa de la partícula (
  
    
      
        m
      
    
    {\displaystyle m}
  
) y a las constantes de Morse mediante la expresión:

  
    
      
        
          ν
          
            0
          
        
        =
        
          
            a
            
              2
              π
            
          
        
        
          
            
              
                2
                
                  D
                  
                    e
                  
                
              
              m
            
          
        
      
    
    {\displaystyle \nu _{0}={\frac {a}{2\pi }}{\sqrt {\frac {2D_{e}}{m}}}}
  

## Espaciamiento de niveles energéticos

Mientras que el espaciamiento de energía entre niveles vibracionales en el oscilador armónico cuántico es constante (con un valor de 
  
    
      
        h
        
          ν
          
            0
          
        
      
    
    {\displaystyle h\nu _{0}}
  
), la energía entre niveles adyacentes en el oscilador de Morse disminuye conforme aumenta 
  
    
      
        ν
      
    
    {\displaystyle \nu }
  
.  Por lo tanto, este espaciamiento entre niveles de Morse puede describirse con la expresión:

  
    
      
        
          E
          
            n
            +
            1
          
        
        −
        
          E
          
            n
          
        
        =
        
          
            
              h
              
                ν
                
                  0
                
              
              −
              (
              n
              +
              1
              )
              (
              h
              
                ν
                
                  0
                
              
              
                )
                
                  2
                
              
            
            
              2
              
                D
                
                  e
                
              
            
          
        
      
    
    {\displaystyle E_{n+1}-E_{n}={\frac {h\nu _{0}-(n+1)(h\nu _{0})^{2}}{2D_{e}}}}
  

Esta tendencia coincide con la anarmonicidad de moléculas reales. Sin embargo, esta ecuación falla por valores arriba de 
  
    
      
        
          n
          
            m
          
        
      
    
    {\displaystyle n_{m}}
  
 donde 
  
    
      
        E
        (
        
          n
          
            m
          
        
        +
        1
        )
        −
        E
        (
        
          n
          
            m
          
        
        )
      
    
    {\displaystyle E(n_{m}+1)-E(n_{m})}
  
 posee valores negativos o cero. Específicamente:

  
    
      
        
          n
          
            m
          
        
        =
        
          
            
              2
              
                D
                
                  e
                
              
              −
              h
              
                ν
                
                  0
                
              
            
            
              h
              
                ν
                
                  0
                
              
            
          
        
      
    
    {\displaystyle n_{m}={\frac {2D_{e}-h\nu _{0}}{h\nu _{0}}}}
  

Esta falla se debe al número finito de niveles enlazados en el potencial de Morse, donde existe un nivel máximo 
  
    
      
        
          n
          
            m
          
        
      
    
    {\displaystyle n_{m}}
  
 que aún permanece enlazado y para energías superiores, el enlace se rompe y todos los niveles de energía posibles son permitidos pues la ecuación para 
  
    
      
        
          E
          
            n
          
        
      
    
    {\displaystyle E_{n}}
  
 cuantizada ya no es válida. 

Por debajo de ese nivel máximo 
  
    
      
        
          n
          
            m
          
        
      
    
    {\displaystyle n_{m}}
  
, 
  
    
      
        
          E
          
            n
          
        
      
    
    {\displaystyle E_{n}}
  
 es una buena aproximación para el valor vibracional verdadero en moléculas diatómicas que no rotan. De hecho, el espectro molecular real generalmente se ajusta a la forma:

  
    
      
        
          
            
              E
              
                n
              
            
            
              h
              c
            
          
        
        =
        
          ω
          
            e
          
        
        (
        n
        +
        1
        
          /
        
        2
        )
        −
        
          ω
          
            e
          
        
        
          χ
          
            e
          
        
        (
        n
        +
        1
        
          /
        
        2
        
          )
          
            2
          
        
      
    
    {\displaystyle {\frac {E_{n}}{hc}}=\omega _{e}(n+1/2)-\omega _{e}\chi _{e}(n+1/2)^{2}}
  

en el que las constantes 
  
    
      
        
          ω
          
            e
          
        
      
    
    {\displaystyle \omega _{e}}
  
 y 
  
    
      
        
          ω
          
            e
          
        
        
          χ
          
            e
          
        
      
    
    {\displaystyle \omega _{e}\chi _{e}}
  
 pueden relacionarse directamente con los parámetros del potencial.

Como puede observarse si se realiza el análisis dimensional, la última ecuación utiliza notación espectroscópica (por razones históricas) en las que 
  
    
      
        
          ω
          
            e
          
        
      
    
    {\displaystyle \omega _{e}}
  
 representa el número de onda según la ecuación 
  
    
      
        E
        =
        h
        c
        ω
      
    
    {\displaystyle E=hc\omega }
  
, en lugar de utilizar frecuencia angular, según la ecuación 
  
    
      
        E
        =
        ℏ
        ω
      
    
    {\displaystyle E=\hbar \omega }
  
 

## Véase también

- Potencial de Morse de largo alcance

- Mecánica molecular

- Potencial de Lennard-Jones

- Potencial interatómico

- Campo de fuerza (química)

## Referencias

- ↑ Morse, Philip M. (1 de julio de 1929). «Diatomic Molecules According to the Wave Mechanics. II. Vibrational Levels». Physical Review 34 (1): 57-64. doi:10.1103/PhysRev.34.57. Consultado el 3 de septiembre de 2021. 

- ↑ Cooper, Fred; Khare, Avinash; Sukhatme, Uday (2001-06). Supersymmetry in Quantum Mechanics (en inglés). WORLD SCIENTIFIC. ISBN 978-981-02-4605-1. doi:10.1142/4687. Consultado el 3 de septiembre de 2021. 

- ↑ Dahl, Jens Peder; Springborg, Michael (1 de abril de 1988). «The Morse oscillator in position space, momentum space, and phase space». The Journal of Chemical Physics 88 (7): 4535-4547. ISSN 0021-9606. doi:10.1063/1.453761. Consultado el 3 de septiembre de 2021. 

- ↑ Lima, Emanuel F de; Hornos, José E M (16 de marzo de 2005). «Matrix elements for the Morse potential under an external field». Journal of Physics B: Atomic, Molecular and Optical Physics 38 (7): 815-825. ISSN 0953-4075. doi:10.1088/0953-4075/38/7/004. Consultado el 8 de septiembre de 2021. 

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q1783557

-  Datos: Q1783557

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.