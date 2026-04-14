---
title: "Dinámica molecular"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Dinámica molecular
    
    
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
  
  
    
      
        
          
            
              
## Dinámica molecular

            
            
            
              
                

              

              
La dinámica molecular (DM) es una técnica de simulación por computadora en la que se permite que átomos y moléculas interactúen por un período, permitiendo una visualización del movimiento de las partículas. Esta técnica se concibió dentro de la física teórica, y ahora se usa ampliamente en el campo de la biofísica y la ciencia de materiales. Su campo de aplicación va desde superficies catalíticas hasta sistemas biológicos como las proteínas. Si bien los experimentos de cristalografía de rayos X permiten tomar "fotografías estáticas" y la técnica de RMN ofrecen indicios del movimiento molecular, ningún experimento es capaz de acceder a todas las escalas de tiempo involucradas. Resulta tentador, aunque no es enteramente correcto, describir a la DM como un "microscopio virtual" con alta resolución espacial y temporal.[cita requerida]

En general, los sistemas moleculares son complejos y consisten de un gran número de partículas, por lo cual sería imposible encontrar sus propiedades de forma analítica. Para evitar este problema, la DM utiliza métodos numéricos. La DM representa un punto intermedio entre los experimentos y la teoría y es entendida como un experimento en la computadora.[cita requerida]

Se sabe que la materia está constituida de partículas en movimiento e interacción al menos desde la época de Ludwig Boltzmann, en el siglo XIX. Pero muchos aún se imaginan a las moléculas como los modelos estáticos de un museo. Richard Feynman dijo en 1963 que "todo lo que hacen los seres vivos puede ser entendido a través de los saltos y contorsiones de los átomos."[1]​ Una de las contribuciones más importantes de la dinámica molecular es crear conciencia de que el ADN y las proteínas son máquinas en movimiento. Se utiliza para explorar la relación entre estructura, movimiento y función.

La dinámica molecular es un campo multidisciplinario. Sus leyes y teorías provienen de las matemáticas, física y química. Emplea algoritmos de las ciencias de la computación y de la teoría de la información. Permite entender a los materiales y las moléculas no como entidades rígidas, sino como cuerpos animados. También se le ha llamado "estadística mecánica numérica" o "la visión de Laplace de la mecánica newtoniana", en el sentido de predice el futuro al animar las fuerzas de la naturaleza.[cita requerida]

Para utilizar esta técnica de forma correcta, es importante entender las aproximaciones utilizadas y evitar caer en el error conceptual de que estamos simulando el comportamiento real y exacto de un sistema molecular. La integración de las ecuaciones de movimiento están mal condicionadas, lo cual genera errores numéricos acumulativos, que pueden ser minimizados seleccionando apropiadamente los algoritmos, pero no eliminados del todo. Por otro lado, las interacciones entre las partículas se modelan con un campo de fuerza aproximado, que puede o no ser adecuado dependiendo del problema que queremos resolver. De cualquier forma, la dinámica molecular nos permite explorar su comportamiento representativo en el espacio fásico.[cita requerida]

En la DM, hay que balancear el costo computacional y la fiabilidad en los resultados. En la DM clásica, se utilizan las leyes de Newton, cuyo costo computacional es mucho menor que el de las de la mecánica cuántica. Es por ello que muchas propiedades que pueden resultar de interés, como la formación o ruptura de enlaces, no pueden estudiarse mediante este método, ya que no contempla estados excitados o reactividad.[cita requerida]

Existen métodos híbridos, denominados QM/MM (Quantum Mechanics/Molecular Mechanics) en los que un centro reactivo es tratado de modo cuántico mientras que el ambiente que lo rodea se trata de modo clásico. El desafío en este tipo de métodos genera la definición precisa de la interacción entre los dos formas de describir el sistema.[cita requerida]

El resultado de una simulación de dinámica molecular son las posiciones 
  
    
      
        X
      
    
    {\displaystyle X}
  
 y velocidades 
  
    
      
        V
      
    
    {\displaystyle V}
  
 de cada átomo de la molécula, para cada instante en el tiempo discretizado. A esto se le llama trayectoria.[cita requerida]

## Principios físicos

## Colectividad microcanónica (NVE)

La forma más simple de dinámica molecular ocurre en el colectividad microcanónica. En él, el sistema está aislado: su volumen no se altera (V) y no intercambia masa (N) ni energía (E) con el entorno. Para un sistema de N partículas con coordenadas 
  
    
      
        X
      
    
    {\displaystyle X}
  
 y velocidades 
  
    
      
        V
      
    
    {\displaystyle V}
  
, se puede plantear el siguiente par de ecuaciones diferenciales de primer orden

  
    
      
        F
        (
        X
        )
        =
        −
        ∇
        U
        (
        X
        )
        =
        M
        
          
            
              V
              ˙
            
          
        
        (
        t
        )
      
    
    {\displaystyle F(X)=-\nabla U(X)=M{\dot {V}}(t)}
  

  
    
      
        
          
            
              X
              ˙
            
          
        
        (
        t
        )
        =
        V
        (
        t
        )
      
    
    {\displaystyle {\dot {X}}(t)=V(t)}
  

La función de energía potencial 
  
    
      
        U
        (
        X
        )
      
    
    {\displaystyle U(X)}
  
 son las atracciones y repulsiones que sienten los átomos entre sí debido a los enlaces químicos, interacciones electrostáticas, van der Waals, etc. de las moléculas. A 
  
    
      
        U
        (
        X
        )
      
    
    {\displaystyle U(X)}
  
 también se le conoce como campo potencial de fuerza y es una función de las coordenadas de las partículas 
  
    
      
        X
      
    
    {\displaystyle X}
  
. Normalmente proviene de cálculos de química cuántica y/o experimentos espectroscópicos. Sin embargo, el campo de fuerza generalmente tiene una forma funcional que lo hace pertenecer a la mecánica clásica. 

La trayectoria de las partículas es discreta en el tiempo. Normalmente se elige un paso de tiempo suficientemente pequeño (p.ej. 1 femtosegundo) para evitar errores numéricos de discretización. Para cada paso de tiempo, se integra la posición 
  
    
      
        X
      
    
    {\displaystyle X}
  
 y velocidad 
  
    
      
        V
      
    
    {\displaystyle V}
  
 con un método simpléctico como la integración de Verlet. Dadas las posiciones iniciales (p.ej. la estructura de rayos X de una proteína) y las velocidades iniciales (p.ej. aleatorias y Gaussianas), es posible calcular todas las posiciones y velocidades en el futuro.

La colectividad NVE es difícil de realizar experimentalmente. Por ello, generalmente se utiliza la colectividad NVT o NPT en las simulaciones. Sin embargo, las simulaciones NVE son importantes para verificar que un campo de fuerza combinado con un algoritmo de integración conserva la energía del sistema.

## Ensamble canónico (NVT)

En el ensamble canónico, el volumen no se altera (V) y no se intercambia masa (N). La temperatura (T) se mantiene alrededor de la media deseada. La temperatura instantánea del sistema no es constante, sino sólo su promedio. En la colectividad NVT, la energía de los procesos endotérmicos y exotérmicos (transiciones conformacionales entre estados con diferentes energías potenciales) es intercambiada con un termostato.

Existe una gran variedad de termostatos para añadir o remover energía para mantener la temperatura promedio constante. Incluyen la reescalación de velocidades, dinámica Langevin, termostato Nosé-Hoover y el termostato Berendsen. No es fácil obtener una distribución de microestados correspondiente a la colectividad canónica, ya que ello depende del tamaño del sistema, selección del termostato, parámetros del termostato, paso de tiempo e integrador utilizados.

## Potenciales en dinámica molecular

## Potencial Lennard Jones

El potencial Lennard Jones 
  
    
      
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
  
 es un potencial a pares que se usa en simulaciones de dinámica molecular para comprobar la teoría y algoritmos existentes en el área.

## Software

En la actualidad existen varios programas capaces de llevar a cabo las simulaciones de DM, y a su vez existen varios campos de fuerza, que en general pueden utilizarse con diversos programas. LAMMPS, OpenMM, CHARMM, AMBER, NAMD y GROMACS son algunos de los paquetes más populares.

## Referencias

- ↑ Feynman, Richard (1963). Lectures on Physics. (requiere registro). 

## Véase también

- Química computacional

- Modelado molecular

- Potencial de Lennard-Jones

- Categoría:Fuerzas intermoleculares

## Enlaces externos

- Folding@home: Proyecto de cuasisupercómputo distribuido para plegamiento de proteínas..

- dinamol: Material introductorio completo a la Dinámica Molecular.

- PS3Grid: Proyecto similar a Folding@home pero que corre sobre un entorno distribuido de máquinas PlayStation 3.

- Adun: programa (enlace roto disponible en Internet Archive; véase el historial, la primera versión y la última). de dinámica molecular creado en la Universidad Pompeu Fabra.

- Enzimas (eng)

- A great article to get started with molecular dynamics (eng)
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q901663

-  Multimedia: Molecular dynamics simulation / Q901663

- Identificadores

- NKC: ph202577

- Diccionarios y enciclopedias

- Britannica: url

- Identificadores médicos

- MeSH: D056004

- UMLS: C0596957

-  Datos: Q901663

-  Multimedia: Molecular dynamics simulation / Q901663

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.