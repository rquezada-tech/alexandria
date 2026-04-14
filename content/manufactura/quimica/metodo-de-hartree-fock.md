---
title: "Método de Hartree-Fock"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Método de Hartree-Fock
    
    
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
  
  
    
      
        
          
            
              
## Método de Hartree-Fock

            
            
            
              
                

              

              El método de Hartree-Fock (HF) es una forma aproximada de las ecuaciones de mecánica cuántica para fermiones, utilizada en física y química (donde también se conoce como método de campo autoconsistente). Esto se debe a que sus ecuaciones, basadas en orbitales de una partícula, son más accesibles computacionalmente que los métodos basados en funciones de onda de muchas partículas.

La aproximación de Hartree-Fock es el equivalente, en física computacional, a la aproximación de orbitales moleculares, de enorme utilidad conceptual para los físicos. Este esquema de cálculo es un procedimiento iterativo para calcular la mejor solución monodeterminantal a la ecuación de Schrödinger independiente del tiempo, para moléculas aisladas, tanto en su estado fundamental como en estado excitados. La interacción de un único electrón en un problema de muchos cuerpos con el resto de los electrones del sistema se aproxima promediándolo como una interacción entre dos cuerpos (tras aplicar la aproximación de Born-Oppenheimer). De esta forma, se puede obtener una aproximación a la energía total de la molécula. Como consecuencia, calcula la energía de intercambio de forma exacta, pero no tiene en absoluto en cuenta el efecto de la correlación electrónica.

## Descripción cualitativa del método

La base del método de Hartree-Fock es suponer que la función de onda de muchos cuerpos es un determinante de Slater de orbitales de una partícula. Esto garantiza la antisimetría de la función de onda y considera la energía de intercambio. Sin embargo, no considera efectos de correlación que no son despreciables. A partir de esta suposición, se puede aplicar el principio variacional de mecánica cuántica, se encuentra una ecuación de autovalores para los orbitales de una partícula.

El punto de partida para el cálculo Hartree-Fock es un conjunto de orbitales aproximados. Para un cálculo atómico, estos son típicamente los orbitales de un átomo hidrogenoide (un átomo con una carga nuclear cualquiera pero con un solo electrón). Para cálculos moleculares o cristalinos, las funciones de ondas iniciales son típicamente una combinación lineal de orbitales atómicos. Esto da una colección de orbitales monoelectrónicos, que por la naturaleza fermiónica de los electrones, debe ser antisimétrica, lo que se consigue mediante el uso del determinante de Slater. El procedimiento básico fue diseñado por Hartree, y Fock añadió el antisimetrizado.

Una vez se ha construido una función de ondas inicial, se elige un electrón. Se resume el efecto de todos los demás electrones, que se usa para generar un potencial. (Por este motivo, se llama a veces a este método un procedimiento de campo promedio). Esto da un electrón en un campo definido, para el que se puede resolver la ecuación de Schrödinger, dando una función de ondas ligeramente diferente para este electrón. Entonces, el procedimiento se repite para cada uno de los otros electrones, hasta completar un paso del procedimiento. De esta forma, con la nueva distribución electrónica se tiene un nuevo potencial eléctrico. El procedimiento se repite, hasta alcanzar la convergencia (hasta que el cambio entre un paso y el siguiente es lo suficientemente pequeño).

## Formulación Matemática

Las ecuaciones de Hartree-Fock en su forma canónica se asemejan al problema de valores propios:

Ecuaciones de Hartree-Fock Canónicas

  
    
      
        
          
            
              f
              ^
            
          
        
        
          ψ
          
            i
          
        
        =
        
          ε
          
            i
          
        
        
          ψ
          
            i
          
        
      
    
    {\displaystyle {\hat {f}}\psi _{i}=\varepsilon _{i}\psi _{i}}
  

donde 
  
    
      
        
          
            
              f
              ^
            
          
        
      
    
    {\displaystyle {\hat {f}}}
  
 es el operador de Fock, que actúa sobre un electrón en el espín-orbital 
  
    
      
        
          ψ
          
            i
          
        
      
    
    {\displaystyle \psi _{i}}
  
 y depende de la forma de los otros 
  
    
      
        N
        −
        1
      
    
    {\displaystyle N-1}
  
 espín-orbitales, y 
  
    
      
        
          ε
          
            i
          
        
      
    
    {\displaystyle \varepsilon _{i}}
  
 es la energía orbital del espín-orbital 
  
    
      
        
          ψ
          
            i
          
        
      
    
    {\displaystyle \psi _{i}}
  
. Las ecuaciones de Hartree-Fock pierden la linealidad de la ecuación de Schrödinger independiente del tiempo y son ecuaciones integrodiferenciales acopladas, por lo que para encontrar el estado basal de un sistema de 
  
    
      
        N
      
    
    {\displaystyle N}
  
 electrones es necesario utilizar procedimientos iterativos.

## Teoría Básica

El método de Hartree-Fock para un sistema de 
  
    
      
        N
      
    
    {\displaystyle N}
  
 electrones considera como función de onda un determinante de Slater construido a partir de los espín-orbitales del sistema. Debido a esto, sólo se considera la correlación estadística de los electrones con el mismo espín, lo que se refleja en que la probabilidad de encontrar a dos electrones del mismo espín en el mismo punto del espacio sea nula, pero, en cambio, si los electrones tienen espines distintos, entonces la probabilidad de que estén en el mismo punto del espacio es distinta de cero.[1]​

Con este tipo de función de onda, el valor esperado del Hamiltoniano está dado por

  
    
      
        ⟨
        
          
            
              H
              ^
            
          
        
        ⟩
        =
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          h
          
            i
          
        
        +
        
          
            1
            2
          
        
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ∑
          
            j
            ≠
            i
          
          
            N
          
        
        
          J
          
            i
            j
          
        
        −
        
          K
          
            i
            j
          
        
      
    
    {\displaystyle \langle {\hat {H}}\rangle =\sum _{i=1}^{N}h_{i}+{\frac {1}{2}}\sum _{i=1}^{N}\sum _{j\neq i}^{N}J_{ij}-K_{ij}}
  
,

donde 
  
    
      
        
          h
          
            i
          
        
      
    
    {\displaystyle h_{i}}
  
 es la integral monoelectrónica, que contiene la energía cinética y la atracción nuclear del electrón 
  
    
      
        i
      
    
    {\displaystyle i}
  
, 
  
    
      
        
          J
          
            i
            j
          
        
      
    
    {\displaystyle J_{ij}}
  
 es la integral de Coulomb y 
  
    
      
        
          K
          
            i
            j
          
        
      
    
    {\displaystyle K_{ij}}
  
 es la integral de intercambio.

Siguiendo el principio variacional, el valor esperado del Hamiltoniano se minimiza bajo la condición de ortonormalidad de los espín-orbitales. Construyendo un funcional del conjunto de espín-orbitales

  
    
      
        
          
            L
          
        
        [
        {
        
          ψ
          
            i
          
        
        }
        ]
        =
        ⟨
        
          
            
              H
              ^
            
          
        
        ⟩
        −
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ∑
          
            j
            =
            1
          
          
            N
          
        
        
          ε
          
            i
            j
          
        
        
          (
          
            ⟨
            
              ψ
              
                i
              
            
            
              |
            
            
              ψ
              
                j
              
            
            ⟩
            −
            
              δ
              
                i
                j
              
            
          
          )
        
      
    
    {\displaystyle {\mathcal {L}}[\{\psi _{i}\}]=\langle {\hat {H}}\rangle -\sum _{i=1}^{N}\sum _{j=1}^{N}\varepsilon _{ij}\left(\langle \psi _{i}|\psi _{j}\rangle -\delta _{ij}\right)}
  
,

donde 
  
    
      
        
          ε
          
            i
            j
          
        
      
    
    {\displaystyle \varepsilon _{ij}}
  
 son los multiplicadores de Lagrange, se puede minimizar 
  
    
      
        
          
            L
          
        
      
    
    {\displaystyle {\mathcal {L}}}
  
 respecto a variaciones en la forma de los espín-orbitales. Una manera de realizar el proceso es calculando la derivada funcional de 
  
    
      
        
          
            L
          
        
      
    
    {\displaystyle {\mathcal {L}}}
  
 respecto a un espín-orbital en específico, siendo esto:

  
    
      
        
          
            
              δ
              
                
                  L
                
              
              [
              {
              
                ψ
                
                  i
                
              
              }
              ]
            
            
              δ
              
                ψ
                
                  k
                
                
                  ∗
                
              
            
          
        
        =
        
          [
          
            
              
                
                  h
                  ^
                
              
            
            +
            
              ∑
              
                j
                =
                1
              
              
                N
              
            
            
              (
              
                ∫
                
                  
                    
                      
                        |
                      
                      
                        ψ
                        
                          j
                        
                      
                      (
                      
                        
                          x
                        
                        
                          j
                        
                      
                      )
                      
                        
                          |
                        
                        
                          2
                        
                      
                    
                    
                      r
                      
                        k
                        j
                      
                    
                  
                
                d
                
                  
                    x
                  
                  
                    j
                  
                
                −
                ∫
                
                  
                    
                      
                        ψ
                        
                          j
                        
                        
                          ∗
                        
                      
                      (
                      
                        
                          x
                        
                        
                          j
                        
                      
                      )
                      
                        
                          
                            
                              P
                              ^
                            
                          
                        
                        
                          k
                          j
                        
                      
                      
                        ψ
                        
                          j
                        
                      
                      (
                      
                        
                          x
                        
                        
                          j
                        
                      
                      )
                    
                    
                      r
                      
                        k
                        j
                      
                    
                  
                
                d
                
                  
                    x
                  
                  
                    j
                  
                
              
              )
            
          
          ]
        
        
          ψ
          
            k
          
        
        (
        
          
            x
          
          
            k
          
        
        )
        −
        
          ∑
          
            j
            =
            1
          
          
            N
          
        
        
          ε
          
            k
            j
          
        
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            k
          
        
        )
        =
        0
      
    
    {\displaystyle {\frac {\delta {\mathcal {L}}[\{\psi _{i}\}]}{\delta \psi _{k}^{*}}}=\left[{\hat {h}}+\sum _{j=1}^{N}\left(\int {\frac {|\psi _{j}(\mathbf {x} _{j})|^{2}}{r_{kj}}}d\mathbf {x} _{j}-\int {\frac {\psi _{j}^{*}(\mathbf {x} _{j}){\hat {P}}_{kj}\psi _{j}(\mathbf {x} _{j})}{r_{kj}}}d\mathbf {x} _{j}\right)\right]\psi _{k}(\mathbf {x} _{k})-\sum _{j=1}^{N}\varepsilon _{kj}\psi _{j}(\mathbf {x} _{k})=0}
  
,

donde 
  
    
      
        
          
            
              h
              ^
            
          
        
      
    
    {\displaystyle {\hat {h}}}
  
 es el operador monoelectrónico, que incluye el operador de energía cinética y el de atracción nuclear, y 
  
    
      
        
          
            
              
                P
                ^
              
            
          
          
            k
            j
          
        
      
    
    {\displaystyle {\hat {P}}_{kj}}
  
 es el operador de permutación entre los electrones 
  
    
      
        k
      
    
    {\displaystyle k}
  
 y 
  
    
      
        j
      
    
    {\displaystyle j}
  
. La relación se satisface en los puntos estacionarios del funcional, de donde surgen las ecuaciones de Hartree-Fock:

  
    
      
        
          (
          
            
              
                
                  h
                  ^
                
              
            
            +
            
              ∑
              
                j
                =
                1
              
              
                N
              
            
            
              [
              
                ∫
                
                  
                    
                      
                        |
                      
                      
                        ψ
                        
                          j
                        
                      
                      (
                      
                        
                          x
                        
                        
                          j
                        
                      
                      )
                      
                        
                          |
                        
                        
                          2
                        
                      
                    
                    
                      r
                      
                        k
                        j
                      
                    
                  
                
                d
                
                  
                    x
                  
                  
                    j
                  
                
                −
                ∫
                
                  
                    
                      
                        ψ
                        
                          j
                        
                        
                          ∗
                        
                      
                      (
                      
                        
                          x
                        
                        
                          j
                        
                      
                      )
                      
                        
                          
                            
                              P
                              ^
                            
                          
                        
                        
                          k
                          j
                        
                      
                      
                        ψ
                        
                          j
                        
                      
                      (
                      
                        
                          x
                        
                        
                          j
                        
                      
                      )
                    
                    
                      r
                      
                        k
                        j
                      
                    
                  
                
                d
                
                  
                    x
                  
                  
                    j
                  
                
              
              ]
            
          
          )
        
        
          ψ
          
            k
          
        
        (
        
          
            x
          
          
            k
          
        
        )
        =
        
          ∑
          
            j
            =
            1
          
          
            N
          
        
        
          ε
          
            k
            j
          
        
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            k
          
        
        )
      
    
    {\displaystyle \left({\hat {h}}+\sum _{j=1}^{N}\left[\int {\frac {|\psi _{j}(\mathbf {x} _{j})|^{2}}{r_{kj}}}d\mathbf {x} _{j}-\int {\frac {\psi _{j}^{*}(\mathbf {x} _{j}){\hat {P}}_{kj}\psi _{j}(\mathbf {x} _{j})}{r_{kj}}}d\mathbf {x} _{j}\right]\right)\psi _{k}(\mathbf {x} _{k})=\sum _{j=1}^{N}\varepsilon _{kj}\psi _{j}(\mathbf {x} _{k})}
  

Definiendo el operador de Coulomb para el electrón 
  
    
      
        k
      
    
    {\displaystyle k}
  
 como

  
    
      
        
          
            
              
                J
                ^
              
            
          
          
            k
          
        
        [
        {
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            j
          
        
        )
        }
        ]
        =
        ∫
        
          
            
              
                |
              
              
                ψ
                
                  j
                
              
              (
              
                
                  x
                
                
                  j
                
              
              )
              
                
                  |
                
                
                  2
                
              
            
            
              r
              
                k
                j
              
            
          
        
        d
        
          
            x
          
          
            j
          
        
      
    
    {\displaystyle {\hat {J}}_{k}[\{\psi _{j}(\mathbf {x} _{j})\}]=\int {\frac {|\psi _{j}(\mathbf {x} _{j})|^{2}}{r_{kj}}}d\mathbf {x} _{j}}
  
,

el operador de intercambio para el electrón 
  
    
      
        k
      
    
    {\displaystyle k}
  
:

  
    
      
        
          
            
              
                K
                ^
              
            
          
          
            k
          
        
        [
        {
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            j
          
        
        )
        }
        ]
        =
        ∫
        
          
            
              
                ψ
                
                  j
                
                
                  ∗
                
              
              (
              
                
                  x
                
                
                  j
                
              
              )
              
                
                  
                    
                      P
                      ^
                    
                  
                
                
                  k
                  j
                
              
              
                ψ
                
                  j
                
              
              (
              
                
                  x
                
                
                  j
                
              
              )
            
            
              r
              
                k
                j
              
            
          
        
        d
        
          
            x
          
          
            j
          
        
      
    
    {\displaystyle {\hat {K}}_{k}[\{\psi _{j}(\mathbf {x} _{j})\}]=\int {\frac {\psi _{j}^{*}(\mathbf {x} _{j}){\hat {P}}_{kj}\psi _{j}(\mathbf {x} _{j})}{r_{kj}}}d\mathbf {x} _{j}}
  
,

y el operador de Fock para el electrón 
  
    
      
        k
      
    
    {\displaystyle k}
  
 como

  
    
      
        
          
            
              
                f
                ^
              
            
          
          
            k
          
        
        [
        {
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            j
          
        
        )
        }
        ]
        =
        
          
            
              
                h
                ^
              
            
          
          
            k
          
        
        +
        
          ∑
          
            j
            =
            1
          
          
            N
          
        
        
          
            
              
                J
                ^
              
            
          
          
            k
          
        
        [
        {
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            j
          
        
        )
        }
        ]
        −
        
          
            
              
                K
                ^
              
            
          
          
            k
          
        
        [
        {
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            j
          
        
        )
        }
        ]
      
    
    {\displaystyle {\hat {f}}_{k}[\{\psi _{j}(\mathbf {x} _{j})\}]={\hat {h}}_{k}+\sum _{j=1}^{N}{\hat {J}}_{k}[\{\psi _{j}(\mathbf {x} _{j})\}]-{\hat {K}}_{k}[\{\psi _{j}(\mathbf {x} _{j})\}]}
  
,

las ecuaciones de Hartree-Fock para el electrón 
  
    
      
        k
      
    
    {\displaystyle k}
  
 se pueden escribir de forma compacta como

  
    
      
        
          
            
              
                f
                ^
              
            
          
          
            k
          
        
        [
        {
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            j
          
        
        )
        }
        ]
        
          ψ
          
            k
          
        
        (
        
          
            x
          
          
            k
          
        
        )
        =
        
          ∑
          
            j
            =
            1
          
          
            N
          
        
        
          ε
          
            k
            j
          
        
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            k
          
        
        )
      
    
    {\displaystyle {\hat {f}}_{k}[\{\psi _{j}(\mathbf {x} _{j})\}]\psi _{k}(\mathbf {x} _{k})=\sum _{j=1}^{N}\varepsilon _{kj}\psi _{j}(\mathbf {x} _{k})}
  

Esta combinación lineal sugiere que las soluciones a las ecuaciones de Hartree-Fock no son únicas. En general, una transformación unitaria de los elementos de un determinante no cambian el valor del mismo. Esta propiedad se puede aplicar a los espín-orbitales y está permitida por la forma de un único determinante de Slater de la función de onda Hartree-Fock. De acuerdo a esto, se puede demostrar que el operador de Fock y los multiplicadores de Lagrange son invariantes ante transformaciones unitarias de los espín-orbitales. Entonces, identificando a los multiplicadores de Lagrange como los elementos de matriz del operador de Fock,

  
    
      
        ⟨
        
          ψ
          
            m
          
        
        
          |
        
        
          
            
              
                f
                ^
              
            
          
          
            k
          
        
        
          |
        
        
          ψ
          
            n
          
        
        ⟩
        =
        
          ∑
          
            n
          
          
            N
          
        
        
          ε
          
            k
            n
          
        
        ⟨
        
          ψ
          
            m
          
        
        
          |
        
        
          ψ
          
            n
          
        
        ⟩
        =
        
          ε
          
            m
            n
          
        
      
    
    {\displaystyle \langle \psi _{m}|{\hat {f}}_{k}|\psi _{n}\rangle =\sum _{n}^{N}\varepsilon _{kn}\langle \psi _{m}|\psi _{n}\rangle =\varepsilon _{mn}}
  
,

se puede fijar de manera única a los espín-orbitales mediante una transformación unitaria que diagonaliza la matriz de multiplicadores de Lagrange (ya que es hermítica). El conjunto de espín-orbitales que cumple con este propósito se conoce como los espín-orbitales canónicos, que es un conjunto único. Con esto, se obtienen las ecuaciones de Hartree-Fock canónicas que tienen una forma similar al problema de valores propios:

  
    
      
        
          
            
              
                f
                ^
              
            
          
          
            k
          
        
        [
        {
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            j
          
        
        )
        }
        ]
        
          ψ
          
            k
          
        
        (
        
          
            x
          
          
            k
          
        
        )
        =
        
          ε
          
            k
          
        
        
          ψ
          
            k
          
        
        (
        
          
            x
          
          
            k
          
        
        )
      
    
    {\displaystyle {\hat {f}}_{k}[\{\psi _{j}(\mathbf {x} _{j})\}]\psi _{k}(\mathbf {x} _{k})=\varepsilon _{k}\psi _{k}(\mathbf {x} _{k})}
  

Hay que destacar que el operador de Coulomb tanto como el operador de intercambio (y por consecuencia, el operador de Fock), dependen de los espín-orbitales en que se encuentran los 
  
    
      
        N
        −
        1
      
    
    {\displaystyle N-1}
  
 electrones. Por lo tanto, la linealidad de la ecuación de Schrödinger se pierde y las ecuaciones de Hartree-Fock son ecuaciones integrodiferenciales acopladas, ya que el operador de Fock es un operador monoelectrónico que depende de los espín-orbitales de los otros electrones, cada uno con su propio operador de Fock. En otras palabras, para resolver las ecuaciones de HF para el electrón 1, se debe conocer con anticipación los espín-orbitales de los otros electrones, para luego resolver las ecuaciones de HF para los demás electrones con los espín-orbitales mejorados, hasta llegar a un límite de convergencia de la energía Hartree-Fock.

## Operador de Fock

La forma del operador de Fock trae consigo la cancelación de los efectos de autointeracción, es decir, las integrales de Coulomb e intercambio para la interacción de un electrón consigo mismo (
  
    
      
        
          J
          
            i
            i
          
        
      
    
    {\displaystyle J_{ii}}
  
 y 
  
    
      
        
          K
          
            i
            i
          
        
      
    
    {\displaystyle K_{ii}}
  
, respectivamente) se anulan de manera exacta.

  
    
      
        (
        
          
            
              
                J
                ^
              
            
          
          
            i
          
        
        −
        
          
            
              
                K
                ^
              
            
          
          
            i
          
        
        )
        
          ψ
          
            i
          
        
        =
        0
      
    
    {\displaystyle ({\hat {J}}_{i}-{\hat {K}}_{i})\psi _{i}=0}
  

Además, 
  
    
      
        
          
            
              f
              ^
            
          
        
      
    
    {\displaystyle {\hat {f}}}
  
 actúa sobre un electrón a la vez y también se puede definir como la suma entre el operador Hamiltoniano monoelectrónico, 
  
    
      
        
          
            
              
                h
                ^
              
            
          
          
            i
          
        
      
    
    {\displaystyle {\hat {h}}_{i}}
  
, y un operador de potencial efectivo monoelectrónico llamado potencial de Hartree-Fock:

  
    
      
        
          
            
              
                v
                ^
              
            
          
          
            i
          
          
            H
            F
          
        
        [
        
          ψ
          
            j
          
        
        ]
        =
        
          ∑
          
            j
          
          
            N
          
        
        
          
            
              
                J
                ^
              
            
          
          
            i
          
        
        [
        
          ψ
          
            j
          
        
        ]
        −
        
          
            
              
                K
                ^
              
            
          
          
            i
          
        
        [
        
          ψ
          
            j
          
        
        ]
      
    
    {\displaystyle {\hat {v}}_{i}^{HF}[\psi _{j}]=\sum _{j}^{N}{\hat {J}}_{i}[\psi _{j}]-{\hat {K}}_{i}[\psi _{j}]}
  

Al calcular el valor esperado del potencial de Hartree-Fock para el electrón 
  
    
      
        i
      
    
    {\displaystyle i}
  
, hay que considerar que la forma del potencial de Coulomb representa una interacción promedio del electrón 
  
    
      
        i
      
    
    {\displaystyle i}
  
 con los demás electrones. Como 
  
    
      
        
          |
        
        
          ψ
          
            i
          
        
        (
        
          
            x
          
          
            i
          
        
        )
        
          
            |
          
          
            2
          
        
        
          |
        
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          
            j
          
        
        )
        
          
            |
          
          
            2
          
        
        d
        
          
            x
          
          
            i
          
        
        d
        
          
            x
          
          
            j
          
        
      
    
    {\displaystyle |\psi _{i}(\mathbf {x} _{i})|^{2}|\psi _{j}(\mathbf {x} _{j})|^{2}d\mathbf {x} _{i}d\mathbf {x} _{j}}
  
 es la probabilidad de que el electrón 
  
    
      
        i
      
    
    {\displaystyle i}
  
 en el espín-orbital 
  
    
      
        
          ψ
          
            i
          
        
      
    
    {\displaystyle \psi _{i}}
  
 ocupe el elemento de volumen 
  
    
      
        d
        
          
            x
          
          
            i
          
        
      
    
    {\displaystyle d\mathbf {x} _{i}}
  
 y el electrón 
  
    
      
        j
      
    
    {\displaystyle j}
  
 en el espín-orbital 
  
    
      
        
          ψ
          
            j
          
        
      
    
    {\displaystyle \psi _{j}}
  
 ocupe el elemento de volumen 
  
    
      
        d
        
          
            x
          
          
            j
          
        
      
    
    {\displaystyle d\mathbf {x} _{j}}
  
, entonces la integral sobre todo el espacio es el promedio de la interacción de Coulomb 
  
    
      
        
          r
          
            i
            j
          
          
            −
            1
          
        
      
    
    {\displaystyle r_{ij}^{-1}}
  
.

  
    
      
        ⟨
        i
        j
        
          |
        
        i
        j
        ⟩
        =
        ⟨
        
          ψ
          
            i
          
        
        
          ψ
          
            j
          
        
        
          |
        
        
          r
          
            i
            j
          
          
            −
            1
          
        
        
          |
        
        
          ψ
          
            i
          
        
        
          ψ
          
            j
          
        
        ⟩
        =
        ∫
        
          (
          
            
              |
            
            
              ψ
              
                i
              
            
            (
            
              
                x
              
              
                i
              
            
            )
            
              
                |
              
              
                2
              
            
            
              |
            
            
              ψ
              
                j
              
            
            (
            
              
                x
              
              
                j
              
            
            )
            
              
                |
              
              
                2
              
            
          
          )
        
        
          
            1
            
              r
              
                i
                j
              
            
          
        
        d
        
          
            x
          
          
            i
          
        
        d
        
          
            x
          
          
            j
          
        
      
    
    {\displaystyle \langle ij|ij\rangle =\langle \psi _{i}\psi _{j}|r_{ij}^{-1}|\psi _{i}\psi _{j}\rangle =\int \left(|\psi _{i}(\mathbf {x} _{i})|^{2}|\psi _{j}(\mathbf {x} _{j})|^{2}\right){\frac {1}{r_{ij}}}d\mathbf {x} _{i}d\mathbf {x} _{j}}
  

Por lo tanto, se dice que el operador de Coulomb representa el potencial de Coulomb promedio local en 
  
    
      
        
          
            x
          
          
            i
          
        
      
    
    {\displaystyle \mathbf {x} _{i}}
  
, que resulta del electrón en 
  
    
      
        
          ψ
          
            j
          
        
      
    
    {\displaystyle \psi _{j}}
  
. Caso contrario es lo que sucede con el operador de intercambio. Como no existe un potencial simple 
  
    
      
        
          K
          
            i
          
        
        (
        
          
            x
          
          
            j
          
        
        )
      
    
    {\displaystyle K_{i}(\mathbf {x} _{j})}
  
 únicamente definido en un punto en el espacio, se dice que el operador de intercambio es un operador no-local. En otras palabras, el resultado de aplicar 
  
    
      
        
          
            
              
                K
                ^
              
            
          
          
            i
          
        
      
    
    {\displaystyle {\hat {K}}_{i}}
  
 sobre 
  
    
      
        
          ψ
          
            i
          
        
        (
        
          
            x
          
          
            i
          
        
        )
      
    
    {\displaystyle \psi _{i}(\mathbf {x} _{i})}
  
 depende del valor de 
  
    
      
        
          ψ
          
            i
          
        
      
    
    {\displaystyle \psi _{i}}
  
 en todo el espacio y no únicamente en el punto 
  
    
      
        
          
            x
          
          
            i
          
        
      
    
    {\displaystyle \mathbf {x} _{i}}
  
.

## Energías Orbitales

Como se ha mencionado en las secciones anteriores, el operador de Fock depende en forma funcional de los espín-orbitales ocupados. Sin embargo, luego de terminar el proceso autoconsistente, es decir, cuando la forma final de los espín-orbitales ya es conocida (dentro de un cierto margen), el operador de Fock se vuelve un operador hermítico bien definido con un número infinito de funciones propias.[1]​

  
    
      
        
          
            
              f
              ^
            
          
        
        
          |
        
        
          ψ
          
            j
          
        
        ⟩
        =
        
          ε
          
            j
          
        
        
          |
        
        
          ψ
          
            j
          
        
        ⟩
        ,
        
        j
        =
        1
        ,
        2
        ,
        …
        ,
        ∞
      
    
    {\displaystyle {\hat {f}}|\psi _{j}\rangle =\varepsilon _{j}|\psi _{j}\rangle ,\quad j=1,2,\dots ,\infty }
  

Cada una de las soluciones 
  
    
      
        
          |
        
        
          ψ
          
            j
          
        
        ⟩
      
    
    {\displaystyle |\psi _{j}\rangle }
  
 tiene un valor propio 
  
    
      
        
          ε
          
            j
          
        
      
    
    {\displaystyle \varepsilon _{j}}
  
 asociado. La interpretación de los multiplicadores de Lagrange es que representan las energías orbitales de los espín-orbitales, que ahora se pueden separar en dos tipos: los espín-orbitales ocupados y los espín-orbitales virtuales. Para un sistema de 
  
    
      
        N
      
    
    {\displaystyle N}
  
 electrones, los 
  
    
      
        N
      
    
    {\displaystyle N}
  
 espín-orbitales con energías más bajas pasan a llamarse espín-orbitales ocupados, mientras que el resto de los espín-orbitales que pertenece al conjunto solución se les conoce como espín-orbitales virtuales. Estos últimos son importantes cuando se requiere hacer un cálculo post-HF, cuando el determinante de referencia es la solución a las ecuaciones de Hartree-Fock.

La representación matricial del operador de Fock en la base de los espín-orbitales canónicos es diagonal, siendo sus elementos las energías orbitales:

  
    
      
        ⟨
        
          ψ
          
            i
          
        
        
          |
        
        
          
            
              f
              ^
            
          
        
        
          |
        
        
          ψ
          
            j
          
        
        ⟩
        =
        
          ε
          
            j
          
        
        ⟨
        
          ψ
          
            i
          
        
        
          |
        
        
          ψ
          
            j
          
        
        ⟩
        =
        
          ε
          
            j
          
        
        
          δ
          
            i
            j
          
        
      
    
    {\displaystyle \langle \psi _{i}|{\hat {f}}|\psi _{j}\rangle =\varepsilon _{j}\langle \psi _{i}|\psi _{j}\rangle =\varepsilon _{j}\delta _{ij}}
  

Por lo tanto, las energías de los espín-orbitales ocupados (etiquetados como 
  
    
      
        a
        ,
        b
        ,
        …
      
    
    {\displaystyle a,b,\dots }
  
) están dadas por

  
    
      
        
          ε
          
            a
          
        
        =
        
          h
          
            a
          
        
        +
        
          ∑
          
            b
            ≠
            a
          
          
            N
          
        
        
          J
          
            a
            b
          
        
        −
        
          K
          
            a
            b
          
        
      
    
    {\displaystyle \varepsilon _{a}=h_{a}+\sum _{b\neq a}^{N}J_{ab}-K_{ab}}
  
,

mientras que para los espín-orbitales virtuales (etiquetados como 
  
    
      
        r
        ,
        s
        ,
        …
      
    
    {\displaystyle r,s,\dots }
  
) se tiene

  
    
      
        
          ε
          
            r
          
        
        =
        
          h
          
            r
          
        
        +
        
          ∑
          
            b
            =
            1
          
          
            N
          
        
        
          J
          
            r
            b
          
        
        −
        
          K
          
            r
            b
          
        
      
    
    {\displaystyle \varepsilon _{r}=h_{r}+\sum _{b=1}^{N}J_{rb}-K_{rb}}
  

Es importante destacar que los espín-orbitales ocupados tienen una interacción de Coulomb e intercambio con los 
  
    
      
        N
        −
        1
      
    
    {\displaystyle N-1}
  
 orbitales restantes (lo que explica que el índice 
  
    
      
        b
      
    
    {\displaystyle b}
  
 sea distinto de 
  
    
      
        a
      
    
    {\displaystyle a}
  
), mientras que la energía de los espín-orbitales virtuales incluye la interacción con los 
  
    
      
        N
      
    
    {\displaystyle N}
  
 electrones del estado basal Hartree-Fock. Además, la energía total en Hartree-Fock se puede escribir en términos de las energías orbitales como

  
    
      
        
          E
          
            HF
          
        
        =
        
          ∑
          
            a
            =
            1
          
          
            N
          
        
        
          ε
          
            a
          
        
        −
        
          
            1
            2
          
        
        
          ∑
          
            a
            =
            1
          
          
            N
          
        
        
          ∑
          
            b
            ≠
            a
          
          
            N
          
        
        
          J
          
            a
            b
          
        
        −
        
          K
          
            a
            b
          
        
      
    
    {\displaystyle E_{\text{HF}}=\sum _{a=1}^{N}\varepsilon _{a}-{\frac {1}{2}}\sum _{a=1}^{N}\sum _{b\neq a}^{N}J_{ab}-K_{ab}}
  

Que la energía total no sea una suma simple de las energías orbitales se ha considerado como una muestra de que los electrones en la teoría HF están estadísticamente correlacionados. Si bien, los electrones se tratan como partículas independientes moviéndose en un potencial efectivo, el potencial de HF se construye a partir de la interacción promediada con los otros electrones del sistema, por lo que las partículas no se consideran completamente independientes. Sin embargo, se ha encontrado que la energía total de una molécula con todos los electrones apareados por espín, en la geometría de equilibrio, está aproximadamente dada por[2]​[3]​

  
    
      
        
          E
          
            HF
          
        
        ≈
        1.55
        
          ∑
          
            i
            =
            1
          
          
            N
            
              /
            
            2
          
        
        2
        
          ε
          
            i
          
        
      
    
    {\displaystyle E_{\text{HF}}\approx 1.55\sum _{i=1}^{N/2}2\varepsilon _{i}}
  

## Hartree-Fock Generalizado (GHF)

Existen distintos tipos de teorías Hartree-Fock que son clasificados de acuerdo al tipo de restricción a la simetría de la función de onda. La forma más general, conocida como método Hartree-Fock generalizado, consiste en aplicar el principio variacional sin restricciones como que la función de onda final sea función propia de los operadores de espín 
  
    
      
        
          
            
              
                S
                ^
              
            
          
          
            z
          
        
      
    
    {\displaystyle {\hat {S}}_{z}}
  
 y 
  
    
      
        
          
            
              
                S
                ^
              
            
          
          
            2
          
        
      
    
    {\displaystyle {\hat {S}}^{2}}
  
, de reversión temporal, 
  
    
      
        
          
            
              Θ
              ^
            
          
        
      
    
    {\displaystyle {\hat {\Theta }}}
  
, y en general de operadores del grupo puntual del sistema.[4]​ Tiene dos variantes principales que están relacionadas a considerar si la función de onda es compleja o real. 

En la teoría GHF, los espín orbitales tienen la forma

  
    
      
        
          ψ
          
            i
          
        
        (
        
          r
        
        ,
        σ
        )
        =
        
          ϕ
          
            i
          
          
            α
          
        
        (
        
          r
        
        )
        α
        (
        σ
        )
        +
        
          ϕ
          
            i
          
          
            β
          
        
        (
        
          r
        
        )
        β
        (
        σ
        )
      
    
    {\displaystyle \psi _{i}(\mathbf {r} ,\sigma )=\phi _{i}^{\alpha }(\mathbf {r} )\alpha (\sigma )+\phi _{i}^{\beta }(\mathbf {r} )\beta (\sigma )}
  

donde 
  
    
      
        
          
            ϕ
            
              i
            
            
              
            
          
          
            (
            
              
                r
              
            
            )
          
        
      
    
    {\displaystyle {\ce {\phi_{i}({\mathbf {r}})}}}
  
 es la parte espacial del espín-orbital 
  
    
      
        
          ψ
          
            i
          
        
      
    
    {\displaystyle \psi _{i}}
  
 y 
  
    
      
        α
        (
        σ
        )
      
    
    {\displaystyle \alpha (\sigma )}
  
 y 
  
    
      
        β
        (
        σ
        )
      
    
    {\displaystyle \beta (\sigma )}
  
 son funciones de las coordenadas de espín del electrón, 
  
    
      
        σ
      
    
    {\displaystyle \sigma }
  
. Es conveniente analizar las propiedades estadísticas de la función de onda GHF mediante la probabilidad de encontrar a un electrón en un cierto punto del espacio, con los otros electrones en cualquier parte, y la probabilidad de encontrar simultáneamente a un electrón en un punto dado y a otro electrón en otro punto del espacio, que puede ser el mismo que el anterior o no, con los otros electrones en cualquier otra parte. La densidad de probabilidad de encontrar a un electrón con las coordenadas de espacio y espín 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
 para una función de onda GHF está dada por

  
    
      
        
          ρ
          
            1
          
          
            G
            H
            F
          
        
        (
        
          x
        
        )
        =
        
          ∑
          
            i
          
          
            N
          
        
        
          |
        
        
          ψ
          
            i
          
        
        (
        
          x
        
        )
        
          
            |
          
          
            2
          
        
      
    
    {\displaystyle \rho _{1}^{GHF}(\mathbf {x} )=\sum _{i}^{N}|\psi _{i}(\mathbf {x} )|^{2}}
  

Esta función también es conocida como la densidad electrónica cuando se integra sobre las coordenadas de espín, siendo también la diagonal de la matriz de densidad reducida sin espín de primer orden. Por otra parte, la densidad de probabilidad de encontrar simultáneamente a un electrón en las coordenadas 
  
    
      
        
          x
        
      
    
    {\displaystyle \mathbf {x} }
  
, a otro electrón en 
  
    
      
        
          
            x
          
          ′
        
      
    
    {\displaystyle \mathbf {x} '}
  
 y al resto en cualquier parte está dada por

  
    
      
        
          ρ
          
            2
          
          
            G
            H
            F
          
        
        (
        
          x
        
        ,
        
          
            x
          
          ′
        
        )
        =
        
          ρ
          
            1
          
          
            G
            H
            F
          
        
        (
        
          x
        
        )
        
          ρ
          
            1
          
          
            G
            H
            F
          
        
        (
        
          
            x
          
          ′
        
        )
        −
        
          ∑
          
            i
          
          
            N
          
        
        
          ∑
          
            j
          
          
            N
          
        
        
          ψ
          
            i
          
        
        (
        
          x
        
        )
        
          ψ
          
            i
          
          
            ∗
          
        
        (
        
          
            x
          
          ′
        
        )
        
          ψ
          
            j
          
        
        (
        
          
            x
          
          ′
        
        )
        
          ψ
          
            j
          
          
            ∗
          
        
        (
        
          x
        
        )
      
    
    {\displaystyle \rho _{2}^{GHF}(\mathbf {x} ,\mathbf {x} ')=\rho _{1}^{GHF}(\mathbf {x} )\rho _{1}^{GHF}(\mathbf {x} ')-\sum _{i}^{N}\sum _{j}^{N}\psi _{i}(\mathbf {x} )\psi _{i}^{*}(\mathbf {x} ')\psi _{j}(\mathbf {x} ')\psi _{j}^{*}(\mathbf {x} )}
  

Si los electrones fueran completamente independientes, la densidad de pares, 
  
    
      
        
          ρ
          
            2
          
        
        (
        
          x
        
        ,
        
          
            x
          
          ′
        
        )
      
    
    {\displaystyle \rho _{2}(\mathbf {x} ,\mathbf {x} ')}
  
, sólo sería la multiplicación de las funciones de distribución de cada partícula, o sea, solamente el primer término. Sin embargo, para la función de onda GHF se obtiene un término extra que surge debido a la correlación de Fermi (intercambio) de los electrones, lo que se asocia a la forma antisimétrica de la función de onda.

Las ecuaciones de Hartree-Fock generalizadas usando los espín-orbitales canónicos está dada por

  
    
      
        
          
            
              
                f
                ^
              
            
          
          
            i
          
          
            G
            H
            F
          
        
        [
        
          ψ
          
            j
          
        
        ]
        
          ψ
          
            i
          
        
        (
        
          
            x
          
          
            i
          
        
        )
        =
        
          ε
          
            i
          
        
        
          ψ
          
            i
          
        
        (
        
          
            x
          
          
            i
          
        
        )
      
    
    {\displaystyle {\hat {f}}_{i}^{GHF}[\psi _{j}]\psi _{i}(\mathbf {x} _{i})=\varepsilon _{i}\psi _{i}(\mathbf {x} _{i})}
  
,

que es una forma similar a la encontrada en la sección anterior, con la diferencia de que la forma de los espín-orbitales está identificada.

El uso de las funciones de onda GHF es limitado, ya sea en su variante de soluciones complejas o reales. Aun así, se han encontrado soluciones GHF para el átomo de berilio, en el BH, en el H4 y en otros pocos casos.[4]​

## Hartree-Fock Sin Restricción (UHF)

A pesar del nombre, este método impone algunas restricciones a la función de onda comparado con el método generalizado. La forma que tienen los espín-orbitales ya no es una mezcla entre funciones de espín 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 y 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
, y también posee dos variantes en que las soluciones pueden ser reales o complejas. Un espín-orbital en la teoría UHF se escribe como[1]​[2]​[5]​[6]​

  
    
      
        
          ψ
          
            i
          
        
        (
        
          r
        
        ,
        σ
        )
        =
        
          ϕ
          
            i
          
          
            
              s
              
                i
              
            
          
        
        (
        
          r
        
        )
        
          s
          
            i
          
        
        (
        σ
        )
      
    
    {\displaystyle \psi _{i}(\mathbf {r} ,\sigma )=\phi _{i}^{s_{i}}(\mathbf {r} )s_{i}(\sigma )}
  

Es decir, ahora se compone por una parte espacial 
  
    
      
        
          ϕ
          
            i
          
        
      
    
    {\displaystyle \phi _{i}}
  
 asociada a una parte de espín, donde 
  
    
      
        
          s
          
            i
          
        
      
    
    {\displaystyle s_{i}}
  
 puede ser 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 o 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
. Además, la función de onda total es también función propia del operador de espín 
  
    
      
        
          
            
              
                S
                ^
              
            
          
          
            z
          
        
      
    
    {\displaystyle {\hat {S}}_{z}}
  
. La densidad electrónica para la función de onda UHF estará dada por

  
    
      
        
          ρ
          
            1
          
          
            U
            H
            F
          
        
        (
        
          r
        
        )
        =
        
          ∑
          
            a
            =
            1
          
          
            N
          
        
        
          |
        
        
          ϕ
          
            a
          
        
        (
        
          r
        
        )
        
          
            |
          
          
            2
          
        
      
    
    {\displaystyle \rho _{1}^{UHF}(\mathbf {r} )=\sum _{a=1}^{N}|\phi _{a}(\mathbf {r} )|^{2}}
  
 

La densidad de probabilidad de encontrar simultáneamente a un electrón en 
  
    
      
        
          r
        
      
    
    {\displaystyle \mathbf {r} }
  
 y a otro en 
  
    
      
        
          
            r
          
          ′
        
      
    
    {\displaystyle \mathbf {r} '}
  
, con los otros en cualquier parte, será

  
    
      
        
          ρ
          
            2
          
          
            U
            H
            F
          
        
        (
        
          r
        
        ,
        
          
            r
          
          ′
        
        )
        =
        
          ρ
          
            1
          
          
            U
            H
            F
          
        
        (
        
          r
        
        )
        
          ρ
          
            1
          
          
            U
            H
            F
          
        
        (
        
          
            r
          
          ′
        
        )
        −
        
          ∑
          
            a
            =
            1
          
          
            N
          
        
        
          ∑
          
            b
            =
            1
          
          
            N
          
        
        
          δ
          
            σ
            
              σ
              ′
            
          
        
        
          ϕ
          
            a
          
        
        (
        
          r
        
        )
        
          ϕ
          
            a
          
          
            ∗
          
        
        (
        
          
            r
          
          ′
        
        )
        
          ϕ
          
            b
          
        
        (
        
          
            r
          
          ′
        
        )
        
          ϕ
          
            b
          
          
            ∗
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle \rho _{2}^{UHF}(\mathbf {r} ,\mathbf {r} ')=\rho _{1}^{UHF}(\mathbf {r} )\rho _{1}^{UHF}(\mathbf {r} ')-\sum _{a=1}^{N}\sum _{b=1}^{N}\delta _{\sigma \sigma '}\phi _{a}(\mathbf {r} )\phi _{a}^{*}(\mathbf {r} ')\phi _{b}(\mathbf {r} ')\phi _{b}^{*}(\mathbf {r} )}
  

donde 
  
    
      
        
          δ
          
            σ
            
              σ
              ′
            
          
        
      
    
    {\displaystyle \delta _{\sigma \sigma '}}
  
 es la delta de Kronecker para indicar que si los espines de los electrones considerados son iguales, entonces el segundo término que correlaciona el movimiento de éstos existirá (
  
    
      
        
          δ
          
            σ
            σ
          
        
        =
        1
      
    
    {\displaystyle \delta _{\sigma \sigma }=1}
  
). En caso contrario, cuando los dos electrones tienen espines opuestos, la delta es igual a cero y la densidad de probabilidad de pares se vuelve

  
    
      
        
          ρ
          
            2
          
          
            U
            H
            F
          
        
        (
        
          r
        
        ,
        
          
            r
          
          ′
        
        )
        =
        
          ρ
          
            1
          
          
            U
            H
            F
          
        
        (
        
          r
        
        )
        
          ρ
          
            1
          
          
            U
            H
            F
          
        
        (
        
          
            r
          
          ′
        
        )
      
    
    {\displaystyle \rho _{2}^{UHF}(\mathbf {r} ,\mathbf {r} ')=\rho _{1}^{UHF}(\mathbf {r} )\rho _{1}^{UHF}(\mathbf {r} ')}
  

Esto sugiere que los electrones de espín opuesto no están estadísticamente correlacionados, mientras que los electrones del mismo espín si "pueden verse" entre ellos. Además, en el caso en que los dos electrones considerados tengan el mismo espín y la misma posición en el espacio (
  
    
      
        
          
            r
          
          ′
        
        =
        
          r
        
      
    
    {\displaystyle \mathbf {r} '=\mathbf {r} }
  
), la densidad de probabilidad de pares es 0.

Comparando al caso general, en la teoría UHF existen menos multiplicadores de Lagrange debido a la restricción a la simetría respecto al espín sobre un eje. Los espín-orbitales ahora se dividen en dos conjuntos de acuerdo a su espín, por lo que existirán operadores de Fock para los espín-orbitales 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 y operadores de Fock para los espín-orbitales 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
. Esto se hace evidente al aplicar el operador de Fock sobre un espín-orbital 
  
    
      
        ψ
        (
        
          x
        
        )
        =
        
          ϕ
          
            i
          
          
            α
          
        
        (
        
          r
        
        )
        α
        (
        σ
        )
      
    
    {\displaystyle \psi (\mathbf {x} )=\phi _{i}^{\alpha }(\mathbf {r} )\alpha (\sigma )}
  
, donde el superíndice hace explícita la asociación entre el orbital 
  
    
      
        
          ϕ
          
            i
          
        
      
    
    {\displaystyle \phi _{i}}
  
 a su forma cuando el electrón que lo ocupa tiene espín 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
. 

  
    
      
        
          
            
              f
              ^
            
          
        
        ψ
        (
        
          x
        
        )
        =
        
          
            
              f
              ^
            
          
        
        
          ϕ
          
            i
          
          
            α
          
        
        (
        
          r
        
        )
        α
        (
        σ
        )
        =
        
          ε
          
            i
          
          
            α
          
        
        
          ϕ
          
            i
          
          
            α
          
        
        (
        
          r
        
        )
        α
        (
        σ
        )
      
    
    {\displaystyle {\hat {f}}\psi (\mathbf {x} )={\hat {f}}\phi _{i}^{\alpha }(\mathbf {r} )\alpha (\sigma )=\varepsilon _{i}^{\alpha }\phi _{i}^{\alpha }(\mathbf {r} )\alpha (\sigma )}
  

Multiplicando por la izquierda por 
  
    
      
        
          α
          
            ∗
          
        
        (
        σ
        )
      
    
    {\displaystyle \alpha ^{*}(\sigma )}
  
 e integrando esta ecuación respecto a las coordenadas de espín del electrón, se obtiene

  
    
      
        ⟨
        α
        
          |
        
        
          
            
              f
              ^
            
          
        
        
          |
        
        α
        ⟩
        
          ϕ
          
            i
          
          
            α
          
        
        (
        
          r
        
        )
        =
        
          
            
              
                f
                ^
              
            
          
          
            α
          
        
        [
        
          ϕ
          
            j
          
        
        ]
        
          ϕ
          
            i
          
          
            α
          
        
        (
        
          r
        
        )
        =
        
          ε
          
            i
          
          
            α
          
        
        
          ϕ
          
            i
          
          
            α
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle \langle \alpha |{\hat {f}}|\alpha \rangle \phi _{i}^{\alpha }(\mathbf {r} )={\hat {f}}^{\alpha }[\phi _{j}]\phi _{i}^{\alpha }(\mathbf {r} )=\varepsilon _{i}^{\alpha }\phi _{i}^{\alpha }(\mathbf {r} )}
  

donde se define el operador de Fock espacial, 
  
    
      
        
          
            
              
                f
                ^
              
            
          
          
            α
          
        
        [
        
          ϕ
          
            j
          
        
        ]
      
    
    {\displaystyle {\hat {f}}^{\alpha }[\phi _{j}]}
  
 para los electrones de espín 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
, que depende funcionalmente de los orbitales espaciales de los otros electrones. De manera análoga, se define el operador de Fock espacial para los electrones de espín 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
. El operador de Fock para espín 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 contiene al Hamiltoniano monoelectrónico y al potencial efectivo que actúa sobre el electrón de espín 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
, que está dado por la interacción de Coulomb e intercambio con todos los otros electrones de espín 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 y la interacción de Coulomb con los electrones de espín 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
, ya que la correlación de los electrones de espín opuesto no es considerada. Entonces, la forma de los operadores de Fock para ambos espín es

  
    
      
        
          
            
              
                f
                ^
              
            
          
          
            α
          
        
        [
        
          ϕ
          
            a
          
        
        ]
        =
        
          
            
              h
              ^
            
          
        
        +
        
          ∑
          
            a
          
          
            
              N
              
                α
              
            
          
        
        
          
            
              
                J
                ^
              
            
          
          
            α
          
        
        [
        
          ϕ
          
            a
          
          
            α
          
        
        ]
        −
        
          
            
              
                K
                ^
              
            
          
          
            α
          
        
        [
        
          ϕ
          
            a
          
          
            α
          
        
        ]
        +
        
          ∑
          
            a
          
          
            
              N
              
                β
              
            
          
        
        
          
            
              
                J
                ^
              
            
          
          
            α
          
        
        [
        
          ϕ
          
            a
          
          
            β
          
        
        ]
      
    
    {\displaystyle {\hat {f}}^{\alpha }[\phi _{a}]={\hat {h}}+\sum _{a}^{N^{\alpha }}{\hat {J}}^{\alpha }[\phi _{a}^{\alpha }]-{\hat {K}}^{\alpha }[\phi _{a}^{\alpha }]+\sum _{a}^{N^{\beta }}{\hat {J}}^{\alpha }[\phi _{a}^{\beta }]}
  

  
    
      
        
          
            
              
                f
                ^
              
            
          
          
            β
          
        
        [
        
          ϕ
          
            a
          
        
        ]
        =
        
          
            
              h
              ^
            
          
        
        +
        
          ∑
          
            a
          
          
            
              N
              
                β
              
            
          
        
        
          
            
              
                J
                ^
              
            
          
          
            β
          
        
        [
        
          ϕ
          
            a
          
          
            β
          
        
        ]
        −
        
          
            
              
                K
                ^
              
            
          
          
            β
          
        
        [
        
          ϕ
          
            a
          
          
            β
          
        
        ]
        +
        
          ∑
          
            a
          
          
            
              N
              
                α
              
            
          
        
        
          
            
              
                J
                ^
              
            
          
          
            α
          
        
        [
        
          ϕ
          
            a
          
          
            α
          
        
        ]
      
    
    {\displaystyle {\hat {f}}^{\beta }[\phi _{a}]={\hat {h}}+\sum _{a}^{N^{\beta }}{\hat {J}}^{\beta }[\phi _{a}^{\beta }]-{\hat {K}}^{\beta }[\phi _{a}^{\beta }]+\sum _{a}^{N^{\alpha }}{\hat {J}}^{\alpha }[\phi _{a}^{\alpha }]}
  

donde las definiciones para los operadores de Coulomb e interacambio para cada espín son análogas a las formas generales, pero usando los orbitales espaciales. Las energías orbitales del operador de Fock para cada espín son

  
    
      
        
          ε
          
            a
          
          
            α
          
        
        =
        
          h
          
            i
          
          
            α
          
        
        +
        
          ∑
          
            b
          
          
            
              N
              
                α
              
            
          
        
        
          J
          
            a
            b
          
          
            α
            α
          
        
        −
        
          K
          
            a
            b
          
          
            α
            α
          
        
        +
        
          ∑
          
            b
          
          
            
              N
              
                β
              
            
          
        
        
          J
          
            a
            b
          
          
            α
            β
          
        
      
    
    {\displaystyle \varepsilon _{a}^{\alpha }=h_{i}^{\alpha }+\sum _{b}^{N^{\alpha }}J_{ab}^{\alpha \alpha }-K_{ab}^{\alpha \alpha }+\sum _{b}^{N^{\beta }}J_{ab}^{\alpha \beta }}
  

  
    
      
        
          ε
          
            a
          
          
            β
          
        
        =
        
          h
          
            i
          
          
            β
          
        
        +
        
          ∑
          
            b
          
          
            
              N
              
                β
              
            
          
        
        
          J
          
            a
            b
          
          
            β
            β
          
        
        −
        
          K
          
            a
            b
          
          
            β
            β
          
        
        +
        
          ∑
          
            b
          
          
            
              N
              
                α
              
            
          
        
        
          J
          
            a
            b
          
          
            β
            α
          
        
      
    
    {\displaystyle \varepsilon _{a}^{\beta }=h_{i}^{\beta }+\sum _{b}^{N^{\beta }}J_{ab}^{\beta \beta }-K_{ab}^{\beta \beta }+\sum _{b}^{N^{\alpha }}J_{ab}^{\beta \alpha }}
  

Así, la energía total en el método UHF, en términos de las energías orbitales, se lee como

  
    
      
        
          E
          
            U
            H
            F
          
        
        =
        
          ∑
          
            a
          
          
            
              N
              
                α
              
            
          
        
        
          ε
          
            a
          
          
            α
          
        
        +
        
          ∑
          
            a
          
          
            
              N
              
                β
              
            
          
        
        
          ε
          
            a
          
          
            β
          
        
        −
        
          
            1
            2
          
        
        
          ∑
          
            a
          
          
            
              N
              
                α
              
            
          
        
        
          ∑
          
            b
          
          
            
              N
              
                α
              
            
          
        
        
          J
          
            a
            b
          
          
            α
            α
          
        
        −
        
          K
          
            a
            b
          
          
            α
            α
          
        
        −
        
          
            1
            2
          
        
        
          ∑
          
            a
          
          
            
              N
              
                β
              
            
          
        
        
          ∑
          
            b
          
          
            
              N
              
                β
              
            
          
        
        
          J
          
            a
            b
          
          
            β
            β
          
        
        −
        
          K
          
            a
            b
          
          
            β
            β
          
        
        −
        
          ∑
          
            a
          
          
            
              N
              
                α
              
            
          
        
        
          ∑
          
            b
          
          
            
              N
              
                β
              
            
          
        
        
          J
          
            a
            b
          
          
            α
            β
          
        
      
    
    {\displaystyle E_{UHF}=\sum _{a}^{N^{\alpha }}\varepsilon _{a}^{\alpha }+\sum _{a}^{N^{\beta }}\varepsilon _{a}^{\beta }-{\frac {1}{2}}\sum _{a}^{N^{\alpha }}\sum _{b}^{N^{\alpha }}J_{ab}^{\alpha \alpha }-K_{ab}^{\alpha \alpha }-{\frac {1}{2}}\sum _{a}^{N^{\beta }}\sum _{b}^{N^{\beta }}J_{ab}^{\beta \beta }-K_{ab}^{\beta \beta }-\sum _{a}^{N^{\alpha }}\sum _{b}^{N^{\beta }}J_{ab}^{\alpha \beta }}
  

## Hartree-Fock Restringido (RHF)

Para los casos en que el sistema a considerar tiene un número par de electrones, con todos ellos apareados por espín, existe una formulación más sencilla del método Hartree-Fock conocida como Hartree-Fock Restringido. En este método, se requiere que los espín-orbitales sean un producto de funciones espaciales y funciones de espín que sean funciones propias del operador 
  
    
      
        
          
            
              
                S
                ^
              
            
          
          
            z
          
        
      
    
    {\displaystyle {\hat {S}}_{z}}
  
 y el número de electrones 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 debe ser igual al número de electrones 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
. Además, los orbitales espaciales se comparten por dos electrones de distinto espín, es decir, un orbital 
  
    
      
        
          ϕ
          
            i
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle \phi _{i}(\mathbf {r} )}
  
 está multiplicado por 
  
    
      
        α
        (
        σ
        )
      
    
    {\displaystyle \alpha (\sigma )}
  
 para el electrón de espín 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 y el mismo orbital 
  
    
      
        
          ϕ
          
            i
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle \phi _{i}(\mathbf {r} )}
  
 está multiplicado por 
  
    
      
        β
        (
        
          σ
          ′
        
        )
      
    
    {\displaystyle \beta (\sigma ')}
  
 para el electrón de espín 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 que lo ocupa. Esta situación también se conoce como un sistema de capa cerrada, donde los espín-orbitales para el conjunto 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 y para el conjunto 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 están dados por[1]​[2]​

  
    
      
        
          ψ
          
            i
          
        
        (
        
          x
        
        )
        =
        
          ϕ
          
            i
          
        
        (
        
          r
        
        )
        
          s
          
            i
          
        
        (
        σ
        )
      
    
    {\displaystyle \psi _{i}(\mathbf {x} )=\phi _{i}(\mathbf {r} )s_{i}(\sigma )}
  

donde 
  
    
      
        
          s
          
            i
          
        
      
    
    {\displaystyle s_{i}}
  
 puede ser 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 o 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 y la parte espacial será la misma en cualquiera de los dos casos. Debido a esta restricción, la función de onda RHF es también una función propia del operador de espín 
  
    
      
        
          
            
              
                S
                ^
              
            
          
          
            2
          
        
      
    
    {\displaystyle {\hat {S}}^{2}}
  
. Al ser útil solo en sistemas de capa cerrada, la función de onda RHF está asociada al valor propio 0 para los dos operadores de espín. Al igual que en los dos casos anteriores, también posee dos variantes que dependen de si los espín-orbitales son complejos o reales.

En este caso, la densidad electrónica está dada por

  
    
      
        
          ρ
          
            1
          
          
            R
            H
            F
          
        
        (
        
          r
        
        )
        =
        
          ∑
          
            a
            =
            1
          
          
            
              N
              
                α
              
            
          
        
        
          |
        
        
          ϕ
          
            a
          
        
        (
        
          r
        
        )
        
          
            |
          
          
            2
          
        
        +
        
          ∑
          
            a
            =
            1
          
          
            
              N
              
                β
              
            
          
        
        
          |
        
        
          ϕ
          
            a
          
        
        (
        
          r
        
        )
        
          
            |
          
          
            2
          
        
        =
        2
        
          ∑
          
            a
            =
            1
          
          
            N
            
              /
            
            2
          
        
        
          |
        
        
          ϕ
          
            a
          
        
        (
        
          r
        
        )
        
          
            |
          
          
            2
          
        
      
    
    {\displaystyle \rho _{1}^{RHF}(\mathbf {r} )=\sum _{a=1}^{N^{\alpha }}|\phi _{a}(\mathbf {r} )|^{2}+\sum _{a=1}^{N^{\beta }}|\phi _{a}(\mathbf {r} )|^{2}=2\sum _{a=1}^{N/2}|\phi _{a}(\mathbf {r} )|^{2}}
  

donde 
  
    
      
        
          N
          
            α
          
        
        =
        
          N
          
            β
          
        
      
    
    {\displaystyle N^{\alpha }=N^{\beta }}
  
 y, como la parte espacial es igual para ambos espines, se cuenta hasta 
  
    
      
        N
        
          /
        
        2
      
    
    {\displaystyle N/2}
  
 en ambos casos. A su vez, la densidad de probabilidad de pares está dada por

  
    
      
        
          ρ
          
            2
          
          
            R
            H
            F
          
        
        (
        
          r
        
        ,
        
          
            r
          
          ′
        
        )
        =
        
          ρ
          
            1
          
          
            R
            H
            F
          
        
        (
        
          r
        
        )
        
          ρ
          
            1
          
          
            R
            H
            F
          
        
        (
        
          
            r
          
          ′
        
        )
        −
        2
        
          ∑
          
            i
          
          
            N
            
              /
            
            2
          
        
        
          ∑
          
            j
          
          
            N
            
              /
            
            2
          
        
        
          δ
          
            σ
            
              σ
              ′
            
          
        
        
          ϕ
          
            i
          
        
        (
        
          r
        
        )
        
          ϕ
          
            i
          
          
            ∗
          
        
        (
        
          
            r
          
          ′
        
        )
        
          ϕ
          
            j
          
        
        (
        
          
            r
          
          ′
        
        )
        
          ϕ
          
            j
          
          
            ∗
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle \rho _{2}^{RHF}(\mathbf {r} ,\mathbf {r} ')=\rho _{1}^{RHF}(\mathbf {r} )\rho _{1}^{RHF}(\mathbf {r} ')-2\sum _{i}^{N/2}\sum _{j}^{N/2}\delta _{\sigma \sigma '}\phi _{i}(\mathbf {r} )\phi _{i}^{*}(\mathbf {r} ')\phi _{j}(\mathbf {r} ')\phi _{j}^{*}(\mathbf {r} )}
  

donde, al igual que en UHF, existe un término extra debido a la correlación estadística entre los electrones del mismo espín. Cuando los electrones tienen distinto espín, 
  
    
      
        σ
        ≠
        
          σ
          ′
        
      
    
    {\displaystyle \sigma \neq \sigma '}
  
, el último término es cero y los electrones son independientes estadísticamente.

El operador de Fock pasa a ser el operador de Fock espacial como en UHF, sin embargo, ahora los conjuntos 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 y 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 son iguales, por lo que sólo existirá un operador de Fock espacial que actúe sobre electrones 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 y 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
. Entonces, la forma que tiene el operador de Fock es

  
    
      
        
          
            
              f
              ^
            
          
        
        [
        
          ϕ
          
            b
          
        
        ]
        =
        
          
            
              h
              ^
            
          
        
        +
        
          ∑
          
            b
          
          
            N
            
              /
            
            2
          
        
        2
        
          
            
              J
              ^
            
          
        
        [
        
          ϕ
          
            b
          
        
        ]
        −
        
          
            
              K
              ^
            
          
        
        [
        
          ϕ
          
            b
          
        
        ]
      
    
    {\displaystyle {\hat {f}}[\phi _{b}]={\hat {h}}+\sum _{b}^{N/2}2{\hat {J}}[\phi _{b}]-{\hat {K}}[\phi _{b}]}
  

donde los operadores de Coulomb e intercambio están definidos usando las funciones espaciales. Así, las ecuaciones del método Hartree-Fock Restringido se leen como

  
    
      
        
          
            
              f
              ^
            
          
        
        [
        
          ϕ
          
            b
          
        
        ]
        
          ϕ
          
            a
          
        
        (
        
          r
        
        )
        =
        
          ε
          
            a
          
        
        
          ϕ
          
            a
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle {\hat {f}}[\phi _{b}]\phi _{a}(\mathbf {r} )=\varepsilon _{a}\phi _{a}(\mathbf {r} )}
  

Las energías orbitales toman la forma

  
    
      
        
          ε
          
            a
          
        
        =
        
          h
          
            a
          
        
        +
        
          ∑
          
            b
          
          
            N
            
              /
            
            2
          
        
        2
        
          J
          
            a
            b
          
        
        −
        
          K
          
            a
            b
          
        
      
    
    {\displaystyle \varepsilon _{a}=h_{a}+\sum _{b}^{N/2}2J_{ab}-K_{ab}}
  

y la energía total está dada por

  
    
      
        
          
            
              
                
                  E
                  
                    R
                    H
                    F
                  
                
              
              
                =
              
              
                2
                
                  ∑
                  
                    a
                  
                  
                    N
                    
                      /
                    
                    2
                  
                
                
                  h
                  
                    a
                  
                
                +
                
                  ∑
                  
                    a
                  
                  
                    N
                    
                      /
                    
                    2
                  
                
                
                  ∑
                  
                    b
                  
                  
                    N
                    
                      /
                    
                    2
                  
                
                2
                
                  J
                  
                    a
                    b
                  
                
                −
                
                  K
                  
                    a
                    b
                  
                
                =
                2
                
                  ∑
                  
                    a
                  
                  
                    N
                    
                      /
                    
                    2
                  
                
                
                  ε
                  
                    a
                  
                
                −
                
                  ∑
                  
                    a
                  
                  
                    N
                    
                      /
                    
                    2
                  
                
                
                  ∑
                  
                    b
                  
                  
                    N
                    
                      /
                    
                    2
                  
                
                2
                
                  J
                  
                    a
                    b
                  
                
                −
                
                  K
                  
                    a
                    b
                  
                
              
            
            
              
              
                =
              
              
                
                  ∑
                  
                    a
                  
                  
                    N
                    
                      /
                    
                    2
                  
                
                
                  ε
                  
                    a
                  
                
                +
                
                  h
                  
                    a
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{array}{lcl}E_{RHF}&=&2\sum _{a}^{N/2}h_{a}+\sum _{a}^{N/2}\sum _{b}^{N/2}2J_{ab}-K_{ab}=2\sum _{a}^{N/2}\varepsilon _{a}-\sum _{a}^{N/2}\sum _{b}^{N/2}2J_{ab}-K_{ab}\\&=&\sum _{a}^{N/2}\varepsilon _{a}+h_{a}\end{array}}}
  

## Aproximación Algebraica

Una forma de resolver las ecuaciones de Hartree-Fock es mediante la introducción de un conjunto base finito, lo que se conoce como aproximación algebraica. El fundamento de este método está en la combinación lineal de orbitales atómicos introducidos por Lennard-Jones en 1929 para la descripción de moléculas diatomicas. En este sentido, para comenzar a resolver las ecuaciones de Hartree-Fock es necesario tener un conocimiento previo del sistema y así poder tener una forma inicial del operador de Fock, entonces, como los espín-orbitales no tienen una forma conocida, se expanden en términos de funciones que sí son conocidas (como los orbitales de un átomo hidrogenoide), las que pueden incluir parámetros variacionales, además de los coeficientes de expansión, que permitan encontrar el punto estacionario del funcional de energía restringido.

## Ecuaciones de Roothaan-Hall

Para un sistema de capa cerrada, donde es necesario resolver las ecuaciones de HF restringidas sin considerar el espín, los orbitales se pueden expandir en un conjunto finito de 
  
    
      
        K
      
    
    {\displaystyle K}
  
 funciones base, 
  
    
      
        {
        
          χ
          
            μ
          
        
        }
      
    
    {\displaystyle \{\chi _{\mu }\}}
  
:[1]​

  
    
      
        
          ϕ
          
            i
          
        
        (
        
          r
        
        )
        =
        
          ∑
          
            μ
            =
            1
          
          
            K
          
        
        
          C
          
            μ
            i
          
        
        
          χ
          
            μ
          
        
        (
        
          r
        
        )
        ,
        
        i
        =
        1
        ,
        2
        ,
        …
        ,
        
          
            N
            2
          
        
        ;
        
        K
        ≥
        
          
            N
            2
          
        
      
    
    {\displaystyle \phi _{i}(\mathbf {r} )=\sum _{\mu =1}^{K}C_{\mu i}\chi _{\mu }(\mathbf {r} ),\qquad i=1,2,\dots ,{\frac {N}{2}};\quad K\geq {\frac {N}{2}}}
  

donde 
  
    
      
        
          C
          
            μ
            i
          
        
      
    
    {\displaystyle C_{\mu i}}
  
 son los coeficientes de expansión. Si el conjunto base es completo, entonces esta expansión es exacta. Sin embargo, debido a las restricciones computacionales, siempre se restringe este conjunto a un cierto número de funciones base. Introduciendo esta combinación lineal en las ecuaciones de HF, se obtiene

  
    
      
        
          
            
              
                f
                ^
              
            
          
          
            i
          
        
        [
        
          ϕ
          
            b
          
        
        ]
        
          ∑
          
            ν
          
          
            K
          
        
        
          C
          
            ν
            a
          
        
        
          χ
          
            ν
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        =
        
          ε
          
            a
          
        
        
          ∑
          
            ν
          
          
            K
          
        
        
          C
          
            ν
            a
          
        
        
          χ
          
            ν
          
        
        (
        
          
            r
          
          
            i
          
        
        )
      
    
    {\displaystyle {\hat {f}}_{i}[\phi _{b}]\sum _{\nu }^{K}C_{\nu a}\chi _{\nu }(\mathbf {r} _{i})=\varepsilon _{a}\sum _{\nu }^{K}C_{\nu a}\chi _{\nu }(\mathbf {r} _{i})}
  

Multiplicando desde la izquierda por 
  
    
      
        
          χ
          
            μ
          
          
            ∗
          
        
        (
        
          
            r
          
          
            i
          
        
        )
      
    
    {\displaystyle \chi _{\mu }^{*}(\mathbf {r} _{i})}
  
 e integrando, se llega a

  
    
      
        
          ∑
          
            ν
          
        
        
          C
          
            ν
            a
          
        
        ∫
        
          χ
          
            μ
          
          
            ∗
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        
          
            
              
                f
                ^
              
            
          
          
            i
          
        
        
          χ
          
            ν
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        d
        
          
            r
          
          
            i
          
        
        =
        
          ε
          
            a
          
        
        
          ∑
          
            ν
          
        
        
          C
          
            ν
            a
          
        
        ∫
        
          χ
          
            μ
          
          
            ∗
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        
          χ
          
            ν
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        d
        
          
            r
          
          
            i
          
        
      
    
    {\displaystyle \sum _{\nu }C_{\nu a}\int \chi _{\mu }^{*}(\mathbf {r} _{i}){\hat {f}}_{i}\chi _{\nu }(\mathbf {r} _{i})d\mathbf {r} _{i}=\varepsilon _{a}\sum _{\nu }C_{\nu a}\int \chi _{\mu }^{*}(\mathbf {r} _{i})\chi _{\nu }(\mathbf {r} _{i})d\mathbf {r} _{i}}
  

Definiendo la matriz de solapamiento

  
    
      
        
          S
          
            μ
            ν
          
        
        =
        ∫
        
          χ
          
            μ
          
          
            ∗
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        
          χ
          
            ν
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        d
        
          
            r
          
          
            i
          
        
      
    
    {\displaystyle S_{\mu \nu }=\int \chi _{\mu }^{*}(\mathbf {r} _{i})\chi _{\nu }(\mathbf {r} _{i})d\mathbf {r} _{i}}
  

y la matriz de Fock

  
    
      
        
          F
          
            μ
            ν
          
        
        =
        ∫
        
          χ
          
            μ
          
          
            ∗
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        
          
            
              
                f
                ^
              
            
          
          
            i
          
        
        
          χ
          
            ν
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        d
        
          
            r
          
          
            i
          
        
      
    
    {\displaystyle F_{\mu \nu }=\int \chi _{\mu }^{*}(\mathbf {r} _{i}){\hat {f}}_{i}\chi _{\nu }(\mathbf {r} _{i})d\mathbf {r} _{i}}
  

las ecuaciones de Hartree-Fock toman la forma matricial

  
    
      
        
          ∑
          
            ν
          
          
            K
          
        
        
          F
          
            μ
            ν
          
        
        
          C
          
            μ
            a
          
        
        =
        
          ε
          
            a
          
        
        
          ∑
          
            ν
          
          
            K
          
        
        
          S
          
            μ
            ν
          
        
        
          C
          
            ν
            a
          
        
        ,
        
        
          o bien,
        
        
        
          F
          C
        
        =
        
          S
          C
        
        
          ε
        
      
    
    {\displaystyle \sum _{\nu }^{K}F_{\mu \nu }C_{\mu a}=\varepsilon _{a}\sum _{\nu }^{K}S_{\mu \nu }C_{\nu a},\qquad {\text{o bien,}}\qquad \mathbf {FC} =\mathbf {SC} {\boldsymbol {\varepsilon }}}
  

donde 
  
    
      
        
          C
        
      
    
    {\displaystyle \mathbf {C} }
  
 es la matriz de los coeficientes de expansión y 
  
    
      
        
          ε
        
      
    
    {\displaystyle {\boldsymbol {\varepsilon }}}
  
 es la matriz de las energías orbitales. Esta forma es conocida como las ecuaciones de Roothaan-Hall.[7]​[8]​ Hay que destacar que se asume que la base es linealmente independiente y está normalizada, sin embargo, no necesariamente es ortogonal. Por lo tanto, la magnitud de los elementos de la matriz de solapamiento están en el intervalo 
  
    
      
        [
        0
        ,
        1
        ]
      
    
    {\displaystyle [0,1]}
  
, siendo los elementos de la diagonal iguales a 1.

## Ecuaciones de Pople-Nesbet

La expansión de los orbitales en términos de un conjunto base es conocida como aproximación algebraica debido a que el problema se transforma de 
  
    
      
        N
      
    
    {\displaystyle N}
  
 ecuaciones integrodiferenciales acopladas (
  
    
      
        N
        
          /
        
        2
      
    
    {\displaystyle N/2}
  
 para capa cerrada) a 
  
    
      
        N
      
    
    {\displaystyle N}
  
 ecuaciones algebraicas (
  
    
      
        N
        
          /
        
        2
      
    
    {\displaystyle N/2}
  
 para capa cerrada). Las ecuaciones de Roothaan-Hall sólo son útiles en el caso en que se resuelven las ecuaciones de HF restringidas, por lo que es necesario una generalización al caso de sistemas de capa abierta.

Siguiendo un procedimiento similar a la formulación de Roothaan-Hall, los orbitales se expanden en términos de una base 
  
    
      
        {
        
          χ
          
            μ
          
        
        
          |
        
        μ
        =
        1
        ,
        2
        ,
        …
        ,
        K
        }
      
    
    {\displaystyle \{\chi _{\mu }|\mu =1,2,\dots ,K\}}
  
 en que los coeficientes varían dependiendo si el espín-orbital es 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 o 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
.

  
    
      
        
          ϕ
          
            i
          
          
            α
          
        
        =
        
          ∑
          
            μ
          
          
            K
          
        
        
          C
          
            μ
            i
          
          
            α
          
        
        
          χ
          
            μ
          
        
      
    
    {\displaystyle \phi _{i}^{\alpha }=\sum _{\mu }^{K}C_{\mu i}^{\alpha }\chi _{\mu }}
  

  
    
      
        
          ϕ
          
            i
          
          
            β
          
        
        =
        
          ∑
          
            μ
          
          
            K
          
        
        
          C
          
            μ
            i
          
          
            β
          
        
        
          χ
          
            μ
          
        
      
    
    {\displaystyle \phi _{i}^{\beta }=\sum _{\mu }^{K}C_{\mu i}^{\beta }\chi _{\mu }}
  

En este caso, las dos ecuaciones de Hartree-Fock sin restringir para cada espín garantizan que los conjuntos 
  
    
      
        {
        
          ϕ
          
            i
          
          
            α
          
        
        }
      
    
    {\displaystyle \{\phi _{i}^{\alpha }\}}
  
 y 
  
    
      
        {
        
          ϕ
          
            i
          
          
            β
          
        
        }
      
    
    {\displaystyle \{\phi _{i}^{\beta }\}}
  
 sean conjuntos ortonormales por separado, sin embargo, un miembro del conjunto 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 no tiene por qué ser ortogonal a un miembro del conjunto 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
. Sustituyendo esta expansión en las ecuaciones UHF y siguiendo el mismo procedimiento descrito antes, se obtienen dos ecuaciones matriciales, conocidas como las ecuaciones de Pople-Nesbet:[9]​

  
    
      
        
          
            F
          
          
            α
          
        
        
          
            C
          
          
            α
          
        
        =
        
          S
        
        
          
            C
          
          
            α
          
        
        
          
            ε
          
          
            α
          
        
      
    
    {\displaystyle \mathbf {F} ^{\alpha }\mathbf {C} ^{\alpha }=\mathbf {S} \mathbf {C} ^{\alpha }{\boldsymbol {\varepsilon }}^{\alpha }}
  

  
    
      
        
          
            F
          
          
            β
          
        
        
          
            C
          
          
            β
          
        
        =
        
          S
        
        
          
            C
          
          
            β
          
        
        
          
            ε
          
          
            β
          
        
      
    
    {\displaystyle \mathbf {F} ^{\beta }\mathbf {C} ^{\beta }=\mathbf {S} \mathbf {C} ^{\beta }{\boldsymbol {\varepsilon }}^{\beta }}
  

donde las dos matrices de energías orbitales son diagonales.

## Algoritmo

- Especificar el sistema:

- Conjunto de coordenadas nucleares, asociadas a los correspondientes números atómicos

- Número total de electrones

- Funciones de base. La elección de una base puede ser crítico para llegar a una convergencia adecuada, y con sentido físico, y no hay un procedimiento general con garantía de éxito. Los científicos cuánticos hablan del arte de escoger bien la base de funciones.

- Calcular todas las integrales (interacciones) relevantes para las funciones de base: las energías cinéticas medias, la atracción electrón-núcleo, las repulsiones bielectrónicas. Como las funciones de base se mantienen a lo largo de todo el cálculo, no es necesario volver a evaluar las integrales. Dependiendo de las limitaciones técnicas del momento y de la talla del sistema, las integrales pueden o no mantenerse en la RAM. En caso de que no se mantengan, la estrategia óptima puede ser guardarlas en un disco duro o cinta, o bien recalcularlas en cada momento en que son necesarias.

- Construir, con las integrales calculadas, la matriz de traslape S, que mide la desviación de la ortogonalidad de las funciones de la base, y, a partir de ella, la matriz de transformación X, que ortogonaliza la base.

- Obtener una estimación de la matriz densidad P que, a partir de un conjunto de funciones de base, especifica completamente la distribución de densidad electrónica. Nuevamente, la primera estimación no es obvia, y puede precisar de inspiración artística. Un cálculo de Hückel extendido puede suponer una buena aproximación.

- Conociendo la matriz densidad y las integrales bielectrónicas de las funciones de base, calcular el operador de interacción entre electrones, la matriz G.

- Construir la matriz de Fock como suma del hamiltoniano "fijo" (integrales monoelectrónicas) y la matriz G

- Transformar, con la matriz de transformación, la matriz de Fock en su expresión para la base ortonormal, F'

- Diagonalizar F', obtener C' y e (vectores y valores propios)

- De C' y la matriz de transformación, recuperar C, que será la expresión en las funciones de base originales

- C define una nueva matriz densidad P

- Si la nueva matriz densidad difiere de la anterior más que un criterio previamente fijado (no ha convergido), volver al punto 5.

- En caso contrario, usar C, P y F para calcular los valores esperados de magnitudes observables, y otras cantidades de interés.
Si el cálculo diverge, o converge con lentitud, o llega a una solución que no es una descripción adecuada de los fenómenos que son de interés,

- o bien se corrigen los dos puntos artesanales, por ejemplo, dando más flexibilidad a las funciones de base, o, por el contrario, restringiéndolas a la parte fundamental de la física, u obtener una mejor primera estimación de la matriz densidad P

- o bien se aplican métodos que van más allá de la aproximación de Hartree-Fock

## Aplicaciones, problemas y más allá de Hartree-Fock

Se usa a menudo en la misma área de cálculos que la Teoría del Funcional de la Densidad, que puede dar soluciones aproximadas para las energías de intercambio y de correlación. De hecho, es común el uso de cálculos que son híbridos de los dos métodos. Adicionalmente, los cálculos a nivel Hartree-Fock se usan como punto de partida para métodos más sofisticados, como la teoría perturbacional de muchos cuerpos, o cálculos cuánticos de Monte-Carlo.

La inestabilidad numérica es un problema de este método, y hay varias vías para combatirla. Una de las más básicas y más aplicadas es la mezcla-F. Con la mezcla-F, no se usa directamente la función de ondas de un electrón conforme se ha obtenido. En lugar de esto, se usa una combinación lineal de la función obtenida con las previas, por ejemplo con la inmediatamente previa. Otro truco, empleado por Hartree, es aumentar la carga nuclear para comprimir a los electrones; tras la estabilización del sistema, se reduce gradualmente la carga hasta llegar a la carga correcta.

Desarrollos más allá del campo autoconsistente o SCF son el CASSCF y la interacción de configuraciones.
Los cálculos de este tipo son relativamente económicos frente a otros de la química cuántica. De esta forma, en ordenadores personales es posible resolver moléculas pequeñas en muy poco tiempo. Las moléculas más grandes, o los desarrollos más sofisticados, para obtener resultados más exactos, siguen realizándose en superordenadores.
Existen múltiples paquetes informáticos que implementan el método de campo autoconsistente, entre los que pueden destacarse Gaussian, NWChem, MOLPRO, MOLCAS y LOWDIN.

## Referencias

- ↑ a b c d e Szabo, A., Ostlund, N., (1996). Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory (en inglés). Dover Publications, Inc. ISBN 978-0-486-13459-8. Consultado el 29 de octubre de 2020. 

- ↑ a b c Piela, Lucjan, 1943-. Ideas of quantum chemistry (en inglés) (Segunda edición). ISBN 978-0-444-59457-0. OCLC 864552005. Consultado el 6 de noviembre de 2020. 

- ↑ Ruedenberg, Klaus (1977-01). «An approximate relation between orbital SCF energies and total SCF energy in molecules». The Journal of Chemical Physics (en inglés) 66 (1): 375-376. ISSN 0021-9606. doi:10.1063/1.433646. Consultado el 6 de noviembre de 2020. 

- ↑ a b Jiménez-Hoyos, Carlos A.; Henderson, Thomas M.; Scuseria, Gustavo E. (13 de septiembre de 2011). «Generalized Hartree–Fock Description of Molecular Dissociation». Journal of Chemical Theory and Computation 7 (9): 2667-2674. ISSN 1549-9618. doi:10.1021/ct200345a. Consultado el 6 de noviembre de 2020. 

- ↑ Pratt, George W. (1 de junio de 1956). «Unrestricted Hartree-Fock Method». Physical Review (en inglés) 102 (5): 1303-1307. ISSN 0031-899X. doi:10.1103/PhysRev.102.1303. Consultado el 6 de noviembre de 2020. 

- ↑ Fukutome, Hideo (1981-11). «Unrestricted Hartree-Fock theory and its applications to molecules and chemical reactions». International Journal of Quantum Chemistry (en inglés) 20 (5): 955-1065. ISSN 0020-7608. doi:10.1002/qua.560200502. Consultado el 6 de noviembre de 2020. 

- ↑ Roothaan, C. C. J. (1 de abril de 1951). «New Developments in Molecular Orbital Theory». Reviews of Modern Physics 23 (2): 69-89. doi:10.1103/RevModPhys.23.69. Consultado el 6 de noviembre de 2020. 

- ↑ Hall, G. G.; Lennard-Jones, John Edward (7 de marzo de 1951). «The molecular orbital theory of chemical valency VIII. A method of calculating ionization potentials». Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences 205 (1083): 541-552. doi:10.1098/rspa.1951.0048. Consultado el 6 de noviembre de 2020. 

- ↑ Pople, J. A.; Nesbet, R. K. (1954-03). «Self‐Consistent Orbitals for Radicals». The Journal of Chemical Physics (en inglés) 22 (3): 571-572. ISSN 0021-9606. doi:10.1063/1.1740120. Consultado el 6 de noviembre de 2020. 

## Bibliografía

- Atkins, P.W.; Friedman, R. (2005). Molecular Quantum Mechanics (4th edición). Oxford University Press. ISBN 978-0-19-927498-7. 

- Cedillo, A. (2023). Curso de Química Cuántica. Universidad Autónoma Metropolitana. ISBN 978-607-28-2870-4. 
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q7879841

- Identificadores

- GND: 4137025-9

- Diccionarios y enciclopedias

- Britannica: url

-  Datos: Q7879841

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.