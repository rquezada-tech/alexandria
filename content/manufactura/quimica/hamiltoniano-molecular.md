---
title: "Hamiltoniano molecular"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Hamiltoniano molecular
    
    
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
  
  
    
      
        
          
            
              
## Hamiltoniano molecular

            
            
            
              
                

              

              En física atómica, molecular y óptica, así como en química cuántica, hamiltoniano molecular es el nombre dado al operador hamiltoniano que representa la energía del sistema constituido por los electrones y el conjunto de núcleos de una molécula. Este es una operador autoadjunto, es decir hermítico, cuya ecuación de Schrödinger asociada juega un papel central en la química computacional y en la física computacional para calcular propiedades de moléculas y agregados de las mismas, tales como conductividad térmica, calor específico, conductividad eléctrica, propiedades ópticas y magnéticas, y reactividad.

## Introducción

Metafóricamente puede decirse, que los "ladrillos" de una molécula son los núcleos atómicos, mientras que su "argamasa" son los electrones. Los núcleos se caracterizan por su número atómico 
  
    
      
        
          Z
          
            i
          
        
      
    
    {\displaystyle Z_{i}}
  
, mientras que los electrones tinen la carga elemental negativa 
  
    
      
        q
      
    
    {\displaystyle q}
  
. La carga del i-ésimo un núcleo es 
  
    
      
        
          Z
          
            i
          
        
        q
      
    
    {\displaystyle Z_{i}q}
  
. Los electrones y núcleos son, de una manera muy aproximada, cargas puntuales y partículas puntuales. El hamiltoniano molecular es un operador cuántico formado por la suma de varios términos; los términos que aportan más a este son la energía cinética de los electrones y las interacciones coulombianas que existen entre el núcleo y los electrones. Esta parte fundamental del hamiltoniano molecular se llama hamiltoniano de Coulomb. A este hamiltoniano hay que agregarle otros términos de una magnitud menor, la mayoría de ellos debidos a los espines electrónicos y nucleares.
A pesar de que generalmente se acepta que la solución de la ecuación de Schrödinger independiente del tiempo asociada al hamiltoniano de Coulomb predecirá la mayor parte de las propiedades, incluyendo la estructura de la molécula, los cálculos exactos que están basados completamente en este hamiltoniano son escasos por la dificultad de resolver la ecuación de Schrödinger. Las aplicaciones están restringidas a pequeños sistemas como la molécula de dihidrógeno. Fuera de los sistemas simples es necesario usar aproximaciones numéricas.

Casi todos los cálculos de funciones de onda de moléculas están basados en la separación del hamiltoniano de Coulomb que fue concebida primeramente por Max Born y Robert Oppenheimer; a dicha simplificación se le conoce como aproximación de Born-Oppenheimer.

En dicha aproximación, los términos de energía cinética de los núcleos son omitidos del hamiltoniano de Coulomb y se considera al hamiltoniano remanente como únicamente el hamiltoniano de los electrones. El núcleo estacionario (fijo) se considera en el análisis únicamente como el generador del potencial eléctrico dentro del que se mueven los electrones, dentro del marco de la mecánica cuántica.

Con esta perspectiva el hamiltoniano molecular ha sido reducido a lo que se conoce como «hamiltoniano de núcleos fijos» (clamped nucleus hamiltonian), que se expresa únicamente en términos de funciones de las coordenadas electrónicas, y por tanto depende paramétricamente de las posiciones de los núcleos.

Una vez que se resuelve la ecuación de Schrödinger asociada al hamiltoniano de núcleo fijo para un número suficiente de configuraciones nucleares, un apropiado autovalor (usualmente el más bajo) se puede ver como una función de las coordenadas de los núcleos, función que corresponde a una superficie de energía potencial. En cálculos prácticos, la superficie se ajusta habitualmente en términos de alguna función analítica. En el segundo paso de la aproximación de Born-Oppenheimer, la parte del hamiltoniano de Coulomb completo que depende de los electrones es reemplazada por la superficie de energía potencial. Esto convierte el hamiltoniano molecular total en un hamiltoniano que solo actúa en las coordenadas nucleares. En el caso se que se dé una singularidad en la aproximación de Born-Oppenheimer, lo que ocurre cuando las energías de diferentes estados electrónicos son cercanas, es necesario conocer el potencial de las superficies de frontera.

La ecuación de Schrödinger del movimiento nuclear se puede resolver para un sistema de referencia fijo (el laboratorio), pero no se encuentran representadas las energía debidas a las traslaciones y rotaciones de los núcleos. Solamente las vibraciones internas de las moléculas entran en el problema. Sin embargo, para moléculas mayores que las triatómicas, es común introducir la aproximación armónica, la cual estima la superficie de potencial como una función cuadrática de los desplazamientos atómicos. Haciendo esta aproximación, se puede convertir el hamiltoniano en una suma de hamiltonianos de osciladores armónicos lineales no acoplados, cada uno de los cuales representa un modo normal de vibración. El oscilador armónico lineal es uno de los pocos sistemas para los que se conocen soluciones exactas de la ecuación de Schrödinger.

Alternativamente, la ecuación de Schrödinger del movimiento nuclear se puede resolver en un sistema de referencia especial llamado sistema de referencia de Eckart, el cual rota y se traslada junto con la molécula. Formulada con respecto a este sistema de referencia fijo a la molécula, el hamiltoniano toma en cuenta la rotación, traslación y vibración del núcleo. Desde que J. K. G. Watson introdujo una importante simplificación a este hamltoniano en 1968, el mismo frecuentemente se denomina como «hamiltoniano del movimiento nuclear de Watson», aunque también se conoce como «hamiltoniano de Eckart».

## Hamiltoniano de Coulomb

La forma algebraica de los operadores correspondientes a muchos observables pueden obtenerse mediante las reglas de la cuantización canónica:

- Escribir el hamiltoniano clásico del observable (como función del momento p y la posición generalizada q). Ambos vectores se expresan con respecto de un sistema de referencia inercial arbitrario, usualmente llamado el «sistema de referencia del laboratorio».

- Reemplazar p por 
  
    
      
        −
        i
        ℏ
        
          ∇
        
      
    
    {\displaystyle -i\hbar {\boldsymbol {\nabla }}}
  
 e interpretar a q como un operador multiplicativo. Aquí 
  
    
      
        
          ∇
        
      
    
    {\displaystyle {\boldsymbol {\nabla }}}
  
 es el operador nabla. Las bien conocidas reglas de conmutación para los operadores p y q se deducen directamente de las reglas de diferenciación.
Clásicamente, los electrones y núcleos de una molécula tienen una energía cinética que puede representarse como p2/(2m) e interaccionan mediante fuerzas electrostáticas, las cuales decrecen proporcionalmente con el inverso del cuadrado de la distancia en el espacio euclídeo entre las partículas cargadas.

Sean las partículas cargadas i y j, y el vector euclídeo que representa la distancia entre ellas r. Se tiene que:

  
    
      
        
          r
          
            i
            j
          
        
        ≡
        
          |
        
        
          
            r
          
          
            i
          
        
        −
        
          
            r
          
          
            j
          
        
        
          |
        
        =
        
          
            (
            
              
                r
              
              
                i
              
            
            −
            
              
                r
              
              
                j
              
            
            )
            ⋅
            (
            
              
                r
              
              
                i
              
            
            −
            
              
                r
              
              
                j
              
            
            )
          
        
        =
        
          
            (
            
              x
              
                i
              
            
            −
            
              x
              
                j
              
            
            
              )
              
                2
              
            
            +
            (
            
              y
              
                i
              
            
            −
            
              y
              
                j
              
            
            
              )
              
                2
              
            
            +
            (
            
              z
              
                i
              
            
            −
            
              z
              
                j
              
            
            
              )
              
                2
              
            
          
        
      
    
    {\displaystyle r_{ij}\equiv |\mathbf {r} _{i}-\mathbf {r} _{j}|={\sqrt {(\mathbf {r} _{i}-\mathbf {r} _{j})\cdot (\mathbf {r} _{i}-\mathbf {r} _{j})}}={\sqrt {(x_{i}-x_{j})^{2}+(y_{i}-y_{j})^{2}+(z_{i}-z_{j})^{2}}}}
  

En la expresión anterior ri puede representar el radiovector de cualquier partícula, sea un electrón o un núcleo. Pero en donde se ha usado la R mayúscula se desea representar las coordenadas del núcleo; y en donde se usa la r minúscula, las de los electrones. Las coordenadas pueden considerarse con respecto a un sistema de referencia cartesiano con origen en un punto arbitrario del espacio, porque la distancia, siendo un producto interno, es invariante bajo rotaciones del sistema de referencia y, siendo la norma de un vector cartesiano, es invariante bajo traslaciones del sistema de referencia.

Mediante la cuantización de la energía clásica del hamiltoniano se obtiene el operador hamiltoniano de la molécula, que usualmente es llamado hamiltoniano de Coulomb. Este hamiltoniano es la suma de cinco términos. Estos son:

- El operador de energía cinética para cada núcleo en el sistema.

- El operador de energía cinética para cada electrón del sistema.

- La energía potencial entre los electrones y el núcleo debida a la interacción de Coulomb en el sistema.

- La energía potencial debida a la interacción de Coulomb de repulsión de los electrones entre sí.

- La energía potencial debida a la repulsión de origen coulombiano de los núcleos entre sí. A este término también se le conoce como energía de repulsión nuclear. Véase potencial eléctrico para más detalles.

- 
  
    
      
        
          
            
              
                T
                ^
              
            
          
          
            n
          
        
        =
        −
        
          ∑
          
            i
          
        
        
          
            
              ℏ
              
                2
              
            
            
              2
              
                M
                
                  i
                
              
            
          
        
        
          ∇
          
            2
          
        
        (
        
          
            R
          
          
            i
          
        
        )
      
    
    {\displaystyle {\hat {T}}_{n}=-\sum _{i}{\frac {\hbar ^{2}}{2M_{i}}}\nabla ^{2}(\mathbf {R} _{i})}
  

- 
  
    
      
        
          
            
              
                T
                ^
              
            
          
          
            e
          
        
        =
        −
        
          ∑
          
            i
          
        
        
          
            
              ℏ
              
                2
              
            
            
              2
              
                m
                
                  e
                
              
            
          
        
        
          ∇
          
            2
          
        
        (
        
          
            r
          
          
            i
          
        
        )
      
    
    {\displaystyle {\hat {T}}_{e}=-\sum _{i}{\frac {\hbar ^{2}}{2m_{e}}}\nabla ^{2}(\mathbf {r} _{i})}
  

- 
  
    
      
        
          
            
              
                U
                ^
              
            
          
          
            e
            n
          
        
        =
        −
        
          ∑
          
            i
          
        
        
          ∑
          
            j
          
        
        
          
            
              
                Z
                
                  i
                
              
              
                e
                
                  2
                
              
            
            
              4
              π
              
                ϵ
                
                  0
                
              
              
                |
                
                  
                    
                      R
                    
                    
                      i
                    
                  
                  −
                  
                    
                      r
                    
                    
                      j
                    
                  
                
                |
              
            
          
        
      
    
    {\displaystyle {\hat {U}}_{en}=-\sum _{i}\sum _{j}{\frac {Z_{i}e^{2}}{4\pi \epsilon _{0}\left|\mathbf {R} _{i}-\mathbf {r} _{j}\right|}}}
  

- i}{\frac {e^{2}}{4\pi \epsilon _{0}\left|\mathbf {r} _{i}-\mathbf {r} _{j}\right|}}}">
  
    
      
        
          
            
              
                U
                ^
              
            
          
          
            e
            e
          
        
        =
        
          
            1
            2
          
        
        
          ∑
          
            i
          
        
        
          ∑
          
            j
            ≠
            i
          
        
        
          
            
              e
              
                2
              
            
            
              4
              π
              
                ϵ
                
                  0
                
              
              
                |
                
                  
                    
                      r
                    
                    
                      i
                    
                  
                  −
                  
                    
                      r
                    
                    
                      j
                    
                  
                
                |
              
            
          
        
        =
        
          ∑
          
            i
          
        
        
          ∑
          
            j
            >
            i
          
        
        
          
            
              e
              
                2
              
            
            
              4
              π
              
                ϵ
                
                  0
                
              
              
                |
                
                  
                    
                      r
                    
                    
                      i
                    
                  
                  −
                  
                    
                      r
                    
                    
                      j
                    
                  
                
                |
              
            
          
        
      
    
    {\displaystyle {\hat {U}}_{ee}={1 \over 2}\sum _{i}\sum _{j\neq i}{\frac {e^{2}}{4\pi \epsilon _{0}\left|\mathbf {r} _{i}-\mathbf {r} _{j}\right|}}=\sum _{i}\sum _{j>i}{\frac {e^{2}}{4\pi \epsilon _{0}\left|\mathbf {r} _{i}-\mathbf {r} _{j}\right|}}}
  
i}{\frac {e^{2}}{4\pi \epsilon _{0}\left|\mathbf {r} _{i}-\mathbf {r} _{j}\right|}}}" loading="lazy">

- i}{\frac {Z_{i}Z_{j}e^{2}}{4\pi \epsilon _{0}\left|\mathbf {R} _{i}-\mathbf {R} _{j}\right|}}}">
  
    
      
        
          
            
              
                U
                ^
              
            
          
          
            n
            n
          
        
        =
        
          
            1
            2
          
        
        
          ∑
          
            i
          
        
        
          ∑
          
            j
            ≠
            i
          
        
        
          
            
              
                Z
                
                  i
                
              
              
                Z
                
                  j
                
              
              
                e
                
                  2
                
              
            
            
              4
              π
              
                ϵ
                
                  0
                
              
              
                |
                
                  
                    
                      R
                    
                    
                      i
                    
                  
                  −
                  
                    
                      R
                    
                    
                      j
                    
                  
                
                |
              
            
          
        
        =
        
          ∑
          
            i
          
        
        
          ∑
          
            j
            >
            i
          
        
        
          
            
              
                Z
                
                  i
                
              
              
                Z
                
                  j
                
              
              
                e
                
                  2
                
              
            
            
              4
              π
              
                ϵ
                
                  0
                
              
              
                |
                
                  
                    
                      R
                    
                    
                      i
                    
                  
                  −
                  
                    
                      R
                    
                    
                      j
                    
                  
                
                |
              
            
          
        
      
    
    {\displaystyle {\hat {U}}_{nn}={1 \over 2}\sum _{i}\sum _{j\neq i}{\frac {Z_{i}Z_{j}e^{2}}{4\pi \epsilon _{0}\left|\mathbf {R} _{i}-\mathbf {R} _{j}\right|}}=\sum _{i}\sum _{j>i}{\frac {Z_{i}Z_{j}e^{2}}{4\pi \epsilon _{0}\left|\mathbf {R} _{i}-\mathbf {R} _{j}\right|}}}
  
i}{\frac {Z_{i}Z_{j}e^{2}}{4\pi \epsilon _{0}\left|\mathbf {R} _{i}-\mathbf {R} _{j}\right|}}}" loading="lazy">
Aquí, Mi es la masa del núcleo i-ésimo, Zi es el número atómico del núcleo i-ésimo y me es la masa del electrón. El operador laplaciano de la partícula i-ésima es: 
  
    
      
        
          ∇
          
            2
          
        
        (
        
          
            r
          
          
            i
          
        
        )
        ≡
        
          ∇
        
        (
        
          
            r
          
          
            i
          
        
        )
        ⋅
        
          ∇
        
        (
        
          
            r
          
          
            i
          
        
        )
        =
        
          
            
              ∂
              
                2
              
            
            
              ∂
              
                x
                
                  i
                
                
                  2
                
              
            
          
        
        +
        
          
            
              ∂
              
                2
              
            
            
              ∂
              
                y
                
                  i
                
                
                  2
                
              
            
          
        
        +
        
          
            
              ∂
              
                2
              
            
            
              ∂
              
                z
                
                  i
                
                
                  2
                
              
            
          
        
      
    
    {\displaystyle \nabla ^{2}(\mathbf {r} _{i})\equiv {\boldsymbol {\nabla }}(\mathbf {r} _{i})\cdot {\boldsymbol {\nabla }}(\mathbf {r} _{i})={\frac {\partial ^{2}}{\partial x_{i}^{2}}}+{\frac {\partial ^{2}}{\partial y_{i}^{2}}}+{\frac {\partial ^{2}}{\partial z_{i}^{2}}}}
  
. 

Debido a que el operador de energía cinética es un producto interno, es invariante bajo la rotación del sistema de referencia cartesiano respecto del cual se mide, donde xi, yi, y zi son expresadas. Sin embargo, el operador de energía cinética, de cualquier forma, no es invariante ante la traslación del sistema de referencia.

## Pequeños términos

En los años 1920 hubo mucha evidencia espectroscópica clara sobre que al hamiltoniano de Coulomb le hacían falta ciertos términos. Especialmente para moléculas que contienen átomos más pesados, estos términos, aunque mucho más pequeños que las energías cinética y de Coulomb, no pueden omitirse. Estas observaciones espectroscópicas llevaron a la introducción de un nuevo grado de libertad para electrones y núcleos, llamado espín. A este concepto empírico se le dio una base teórica por Paul Dirac cuando introdujo una forma relativísticamente correcta (covariancia de Lorentz) de la ecuación de Schrödinger para una partícula. La ecuación de Dirac predice que el espín y el movimiento espacial de una partícula interactúa mediante acoplamiento espín-órbita. En analogía, fue introducido un acoplamiento espín-otra órbita. El hecho de que el espín de la partícula tiene algunas de las características de un dipolo magnético llevó a un acoplamiento espín-espín. Términos adicionales sin una contraparte clásica son el término de interacción de contacto de Fermi (interacción de densidad electrónica en un núcleo de tamaño finito con el núcleo), y el acoplamiento de cuadrupolo nuclear (interacción de un cuadrupolo con el gradiente de un campo eléctrico debido a los electrones). Finalmente, un término de violación de paridad predicho por el modelo estándar de física de partículas debe ser mencionado. Aunque es una interacción extremadamente pequeña, ha atraído una buena cantidad de atención en la literatura científica debido a que da energías diferentes para los enantiómeros en moléculas quirales.

El resto de este artículo ignorará los términos de espín y considerará la solución de la ecuación de autovalor (independiente del tiempo de Schrödinger) del hamiltoniano de Coulomb.

## Ecuación de Schrödinger del hamiltoniano de Coulomb

El hamiltoniano de Coulomb tiene un espectro continuo debido al movimiento del centro de masas de la molécula en un espacio homogéneo. En mecánica clásica es fácil separar el movimiento del centro de masas de un sistema de partículas del movimiento de cada una de las partículas individuales de dicho sistema. Clásicamente, el movimiento del centro de masas está desacoplado de los movimientos de las partículas individuales. El centro de masas se mueve uniformemente a través del espacio como si se tratara de una partícula puntual cuya masa sea igual a la suma de las masas de todas las partículas individuales (Mtot).

En mecánica cuántica una partícula libre tiene como función de estado una función de onda plana, la cual es una función no cuadrática integrable de momento bien definido. La energía cinética de esta partícula tiene un valor dentro de 
  
    
      
        
          
            R
          
          
            +
          
        
      
    
    {\displaystyle \mathbb {R} ^{+}}
  
. El centro de masas tiene una cierta probabilidad de hallarse en cualquier región del espacio. Esto obedece al principio de incertidumbre de Heisenberg.

En la mecánica cuántica separar el movimiento del centro de masas es más complicado que en la mecánica clásica. Introduciendo el vector de coordenadas 
  
    
      
        
          X
        
      
    
    {\displaystyle \mathbf {X} }
  
 del centro de masas con tres de los grados de libertad del sistema y eliminado el vector de coordenadas de una partícula arbitrariamente, de tal modo que el número de grados de libertad del sistema permanezca constante, se puede obtener mediante una transformación lineal un nuevo conjunto de coordenadas ti. Estas coordenadas son una combinación lineal de las anteriores coordenadas de «todas» las partículas (núcleo y electrones). Aplicando la regla de la cadena se puede demostrar que:

  
    
      
        H
        =
        −
        
          
            
              ℏ
              
                2
              
            
            
              2
              
                M
                
                  
                    tot
                  
                
              
            
          
        
        
          ∇
          
            2
          
        
        (
        
          X
        
        )
        +
        
          H
          ′
        
        
        
          
            con
          
        
        
        
          H
          ′
        
        =
        −
        
          ∑
          
            i
            =
            1
          
          
            
              N
              
                
                  tot
                
              
            
            −
            1
          
        
        
          
            
              ℏ
              
                2
              
            
            
              μ
              
                i
                i
              
            
          
        
        
          ∇
          
            2
          
        
        (
        
          
            t
          
          
            i
          
        
        )
        −
        
          ∑
          
            i
            ,
            j
            =
            1
          
          
            
              N
              
                
                  tot
                
              
            
            −
            1
          
        
        
          
            
              ℏ
              
                2
              
            
            
              μ
              
                i
                j
              
            
          
        
        
          ∇
        
        (
        
          
            t
          
          
            i
          
        
        )
        ⋅
        
          ∇
        
        (
        
          
            t
          
          
            j
          
        
        )
        +
        V
        (
        
          t
        
        )
        .
      
    
    {\displaystyle H=-{\frac {\hbar ^{2}}{2M_{\textrm {tot}}}}\nabla ^{2}(\mathbf {X} )+H'\quad {\textrm {con}}\quad H'=-\sum _{i=1}^{N_{\textrm {tot}}-1}{\frac {\hbar ^{2}}{\mu _{ii}}}\nabla ^{2}(\mathbf {t} _{i})-\sum _{i,j=1}^{N_{\textrm {tot}}-1}{\frac {\hbar ^{2}}{\mu _{ij}}}{\boldsymbol {\nabla }}(\mathbf {t} _{i})\cdot {\boldsymbol {\nabla }}(\mathbf {t} _{j})+V(\mathbf {t} ).}
  

El primer término de 
  
    
      
        H
      
    
    {\displaystyle H}
  
 es la energía cinética del centro de masas, la cual puede ser analizada separadamente debido a que 
  
    
      
        
          H
          ′
        
      
    
    {\displaystyle H'}
  
 no depende de 
  
    
      
        
          X
        
      
    
    {\displaystyle \mathbf {X} }
  
. Como una aproximación inicial, sus eigenestados (autovectores) son ondas planas. Las constantes 1/μij son positivas y corresponden a combinaciones lineales de todos los recíprocos de las masas de las partículas 1/mi. Estas son masas reducidas generalizadas. El potencial 
  
    
      
        V
        (
        
          t
        
        )
      
    
    {\displaystyle V(\mathbf {t} )}
  
 consiste en los términos de Coulomb expresados en las nuevas coordenadas. El nuevo término de 
  
    
      
        
          H
          ′
        
      
    
    {\displaystyle H'}
  
 tiene la apariencia usual de un operador de energía cinética. El segundo es el término conocido como «polarización de masa». Puede demostrarse que el hamiltoniano 
  
    
      
        
          H
          ′
        
      
    
    {\displaystyle H'}
  
, invariante ante traslaciones, es auto-adjunto. El autovalor más bajo de 
  
    
      
        
          H
          ′
        
      
    
    {\displaystyle H'}
  
 es real y finito. Aunque 
  
    
      
        
          H
          ′
        
      
    
    {\displaystyle H'}
  
 es necesariamente invariante ante permutaciones de partículas idénticas (debido a que tanto 
  
    
      
        H
      
    
    {\displaystyle H}
  
 como la energía cinética del centro de masas son invariantes), esta invarianza no es manifiesta.

Actualmente, no existen muchas aplicaciones de 
  
    
      
        
          H
          ′
        
      
    
    {\displaystyle H'}
  
. Sin embargo, el trabajo pionero de Kołos y Wolniewicz[1]​ sobre la molécula de hidrógeno da una aplicación temprana. En la mayoría de los cálculos de funciones de onda moleculares, el problema de los electrones es resuelto utilizando el hamiltoniano de núcleo fijo en el primer paso de la aproximación de Born-Oppenheimer.

Véase la referencia de Woolley y Sutcliffe[2]​ para una discusión profunda de las propiedades matemáticas del hamiltoniano de Coulomb. En dicho artículo también se discute si uno puede tomar a priori el concepto de una molécula (entendiendo molécula como un sistema estable de electrones y núcleos con una geometría bien definida) solamente de las propiedades del Hamiltoniano de Coulomb.

## Hamiltoniano de núcleo fijo

El hamiltoniano de núcleo fijo describe la energía de los electrones en el campo electrostático del núcleo atómico, el cual se asume como estacionario con respecto de un sistema de referencia inercial.

La forma del hamiltoniano electrónico es:

  
    
      
        
          
            
              
                H
                ^
              
            
          
          
            
              e
              l
            
          
        
        =
        
          
            
              
                T
                ^
              
            
          
          
            e
          
        
        +
        
          
            
              
                U
                ^
              
            
          
          
            e
            n
          
        
        +
        
          
            
              
                U
                ^
              
            
          
          
            e
            e
          
        
        +
        
          
            
              
                U
                ^
              
            
          
          
            n
            n
          
        
        .
      
    
    {\displaystyle {\hat {H}}_{\mathrm {el} }={\hat {T}}_{e}+{\hat {U}}_{en}+{\hat {U}}_{ee}+{\hat {U}}_{nn}.}
  

Las coordenadas de los electrones y el núcleo están expresadas con respecto a un sistema de referencia que está fijo a este último, por lo que este permanece en reposo con respecto a dicho sistema de referencia. Este es un sistema de referencia inercial porque se asume que no hay fuerzas o torques externos actuando sobre el núcleo, por lo cual no experimenta ninguna aceleración lineal ni angular.

La posición del origen del sistema de coordenadas de este sistema de referencia es arbitraria. Usualmente es posicionado en un núcleo central, o en centro de masas de la molécula.

Algunas veces se afirma que el núcleo está «en reposo con respecto a un sistema de referencia fijo en el espacio». Esta afirmación implica que se ve al núcleo como una partícula clásica, porque una partícula no puede estar en reposo desde el punto de vista de la mecánica cuántica. Esto se debe a que una partícula en reposo tendría un momento lineal bien definido (cero) así como una posición igualmente bien definida, lo cual entraría en contradicción con el principio de incertidumbre de Heisenberg.

Debido a que la posición de los núcleos se considera constante, el operador de energía cinética de los electrones es invariante ante traslaciones de cualquier vector de posición de un núcleo. El potencial de Coulomb, dependiente de la resta de vectores de posición, también es invariante ante dichas traslaciones. En la descripción de los orbitales atómicos y en el cálculo de integrales sobre estos orbitales, esta propiedad de invarianza es usada para asociar cada átomo de la molécula con su propio sistema de referencia asociado al «sistema de referencia fijo al espacio».

Un número suficiente de soluciones de la ecuación de Schrödinger de 
  
    
      
        
          H
          
            
              el
            
          
        
      
    
    {\displaystyle H_{\textrm {el}}}
  
 conduce a una superficie de energía potencial 
  
    
      
        V
        (
        
          
            R
          
          
            1
          
        
        ,
        
          
            R
          
          
            2
          
        
        ,
        …
        ,
        
          
            R
          
          
            N
          
        
        )
      
    
    {\displaystyle V(\mathbf {R} _{1},\mathbf {R} _{2},\ldots ,\mathbf {R} _{N})}
  
. Se asume que la dependencia funcional de V respecto de sus coordenadas es tal que:

  
    
      
        V
        (
        
          
            R
          
          
            1
          
        
        ,
        
          
            R
          
          
            2
          
        
        ,
        …
        ,
        
          
            R
          
          
            N
          
        
        )
        =
        V
        (
        
          
            R
          
          
            1
          
          ′
        
        ,
        
          
            R
          
          
            2
          
          ′
        
        ,
        …
        ,
        
          
            R
          
          
            N
          
          ′
        
        )
      
    
    {\displaystyle V(\mathbf {R} _{1},\mathbf {R} _{2},\ldots ,\mathbf {R} _{N})=V(\mathbf {R} '_{1},\mathbf {R} '_{2},\ldots ,\mathbf {R} '_{N})}
  

Para:

  
    
      
        
          
            R
          
          
            i
          
          ′
        
        =
        
          
            R
          
          
            i
          
        
        +
        
          t
        
        
        
        
          
            (traslacion)\;\;y
          
        
        
        
        
          
            R
          
          
            i
          
          ′
        
        =
        
          
            R
          
          
            i
          
        
        +
        
          
            
              Δ
              ϕ
            
            
              
                |
              
              
                s
              
              
                |
              
            
          
        
        
        (
        
          s
        
        ×
        
          
            R
          
          
            i
          
        
        )
        
        
        
          
            (rotacion\;\;infinitesimal)
          
        
        ,
      
    
    {\displaystyle \mathbf {R} '_{i}=\mathbf {R} _{i}+\mathbf {t} \;\;{\textrm {(traslacion)\;\;y}}\;\;\mathbf {R} '_{i}=\mathbf {R} _{i}+{\frac {\Delta \phi }{|\mathbf {s} |}}\;(\mathbf {s} \times \mathbf {R} _{i})\;\;{\textrm {(rotacion\;\;infinitesimal)}},}
  

Donde t y s son vectores arbitrarios y Δφ es un ángulo infinitesimal, Δφ >> Δφ2. La condición de invarianza de la superficie de energía potencial se cumple completamente cuando dicha superficie de energía potencial es expresada en términos de diferencias de Ri, y entre esos ángulos, lo cual es usualmente el caso.

## Hamiltoniano de movimiento nuclear armónico

En la parte restante del artículo se considerará que la molécula es semi-rígida. En el segundo paso de la aproximación de Born-Oppenheimer la energía cinética del núcleo Tn es reintroducida y se considera a la ecuación de Schrödinger con el hamiltoniano:

  
    
      
        
          
            
              
                H
                ^
              
            
          
          
            
              n
              u
              c
            
          
        
        =
        −
        
          
            
              ℏ
              
                2
              
            
            2
          
        
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ∑
          
            α
            =
            1
          
          
            3
          
        
        
          
            1
            
              M
              
                i
              
            
          
        
        
          
            
              ∂
              
                2
              
            
            
              ∂
              
                R
                
                  i
                  α
                
                
                  2
                
              
            
          
        
        +
        V
        (
        
          
            R
          
          
            1
          
        
        ,
        …
        ,
        
          
            R
          
          
            N
          
        
        )
      
    
    {\displaystyle {\hat {H}}_{\mathrm {nuc} }=-{\frac {\hbar ^{2}}{2}}\sum _{i=1}^{N}\sum _{\alpha =1}^{3}{\frac {1}{M_{i}}}{\frac {\partial ^{2}}{\partial R_{i\alpha }^{2}}}+V(\mathbf {R} _{1},\ldots ,\mathbf {R} _{N})}
  
.
Se pueden reconocer varios términos en esta solución: el movimiento del centro de masas del núcleo (3 grados de libertad), la rotación total de la molécula (3 grados de libertad) y las vibraciones del núcleo. En general, esto no es posible con la energía cinética del núcleo dada, porque no se pueden separar explícitamente los 6 grados externos de libertad respecto de los 3N-6 grados internos de libertad. De hecho, el operador de energía cinética es definido con respecto al sistema de referencia fijo al espacio. Si se mueve el origen del sistema de referencia fijo al centro de masas de la molécula, aplicando la regla de la cadena, aparece el término de polarización de masa. Es común ignorar completamente estos términos y acá se seguirá de esa forma.

Para conseguir una separación se debe distinguir entre coordenadas internas y externas, para lo cual Eckart introdujo condiciones para ser satisfechas por las coordenadas. Se mostrará cómo surgen estas condiciones de forma natural a partir de un análisis armónico en coordenadas cartesianas ponderadas por masa.

Para simplificar la expresión de la energía cinética, se introducen coordenadas de desplazamiento ponderadas por masa:

  
    
      
        
          
            ρ
          
          
            i
          
        
        ≡
        
          
            
              M
              
                i
              
            
          
        
        (
        
          
            R
          
          
            i
          
        
        −
        
          
            R
          
          
            i
          
          
            0
          
        
        )
      
    
    {\displaystyle {\boldsymbol {\rho }}_{i}\equiv {\sqrt {M_{i}}}(\mathbf {R} _{i}-\mathbf {R} _{i}^{0})}
  
.
Debido a que

  
    
      
        
          
            ∂
            
              ∂
              
                ρ
                
                  i
                  α
                
              
            
          
        
        =
        
          
            ∂
            
              
                
                  
                    M
                    
                      i
                    
                  
                
              
              (
              ∂
              
                R
                
                  i
                  α
                
              
              −
              ∂
              
                R
                
                  i
                  α
                
                
                  0
                
              
              )
            
          
        
        =
        
          
            1
            
              
                M
                
                  i
                
              
            
          
        
        
          
            ∂
            
              ∂
              
                R
                
                  i
                  α
                
              
            
          
        
        ,
      
    
    {\displaystyle {\frac {\partial }{\partial \rho _{i\alpha }}}={\frac {\partial }{{\sqrt {M_{i}}}(\partial R_{i\alpha }-\partial R_{i\alpha }^{0})}}={\frac {1}{\sqrt {M_{i}}}}{\frac {\partial }{\partial R_{i\alpha }}},}
  

el operador de energía cinética se vuelve

  
    
      
        T
        =
        −
        
          
            
              ℏ
              
                2
              
            
            2
          
        
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ∑
          
            α
            =
            1
          
          
            3
          
        
        
          
            
              ∂
              
                2
              
            
            
              ∂
              
                ρ
                
                  i
                  α
                
                
                  2
                
              
            
          
        
        .
      
    
    {\displaystyle T=-{\frac {\hbar ^{2}}{2}}\sum _{i=1}^{N}\sum _{\alpha =1}^{3}{\frac {\partial ^{2}}{\partial \rho _{i\alpha }^{2}}}.}
  

Si se hace una expansión de Taylor de V alrededor de la geometría de equilibrio,

  
    
      
        V
        =
        
          V
          
            0
          
        
        +
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ∑
          
            α
            =
            1
          
          
            3
          
        
        
          
            (
          
        
        
          
            
              ∂
              V
            
            
              ∂
              
                ρ
                
                  i
                  α
                
              
            
          
        
        
          
            
              )
            
          
          
            0
          
        
        
        
          ρ
          
            i
            α
          
        
        +
        
          
            1
            2
          
        
        
          ∑
          
            i
            ,
            j
            =
            1
          
          
            N
          
        
        
          ∑
          
            α
            ,
            β
            =
            1
          
          
            3
          
        
        
          
            (
          
        
        
          
            
              
                ∂
                
                  2
                
              
              V
            
            
              ∂
              
                ρ
                
                  i
                  α
                
              
              ∂
              
                ρ
                
                  j
                  β
                
              
            
          
        
        
          
            
              )
            
          
          
            0
          
        
        
        
          ρ
          
            i
            α
          
        
        
          ρ
          
            j
            β
          
        
        +
        ⋯
        ,
      
    
    {\displaystyle V=V_{0}+\sum _{i=1}^{N}\sum _{\alpha =1}^{3}{\Big (}{\frac {\partial V}{\partial \rho _{i\alpha }}}{\Big )}_{0}\;\rho _{i\alpha }+{\frac {1}{2}}\sum _{i,j=1}^{N}\sum _{\alpha ,\beta =1}^{3}{\Big (}{\frac {\partial ^{2}V}{\partial \rho _{i\alpha }\partial \rho _{j\beta }}}{\Big )}_{0}\;\rho _{i\alpha }\rho _{j\beta }+\cdots ,}
  

y se trunca después de tres términos (la así llamada aproximación armónica), se puede describir V con solo el tercer término. El término V0 puede ser absorbido en la energía (da un nuevo cero de energía). El segundo término desaparece debido a la condición de equilibrio. El término restante contiene la matriz hessiana F de V, que es simétrica y puede ser diagonalizada con una matriz 3N × 3N ortogonal con elementos constantes:

  
    
      
        
          Q
        
        
          F
        
        
          
            Q
          
          
            
              T
            
          
        
        =
        
          Φ
        
        
        
          c
          o
          n
        
        
        
          Φ
        
        =
        diag
        ⁡
        (
        
          f
          
            1
          
        
        ,
        …
        ,
        
          f
          
            3
            N
            −
            6
          
        
        ,
        0
        ,
        …
        ,
        0
        )
        .
      
    
    {\displaystyle \mathbf {Q} \mathbf {F} \mathbf {Q} ^{\mathrm {T} }={\boldsymbol {\Phi }}\quad \mathrm {con} \quad {\boldsymbol {\Phi }}=\operatorname {diag} (f_{1},\dots ,f_{3N-6},0,\ldots ,0).}
  

Puede mostrarse a partir de la invarianza de V bajo rotación y traslación que seis de los autovectores de F (las últimas seis filas de Q) tienen autovalor cero (son modos de frecuencia cero). Ellos abarcan el espacio externo. Las primeras 3N − 6 filas de Q son —para moléculas en su estado basal— autovectores con autovalor distinto de cero; son las coordenadas internas y forman una base ortonormal para un subespacio (3N - 6)-dimensional del espacio de configuración nuclear R3N, el espacio interno. Los autovectores de frecuencia cero son ortogonales a los autovectores de frecuencia distinta a cero. Puede mostrarse que estas ortogonalidades son de hecho las condiciones de Eckart. La energía cinética expresada en las coordenadas internas es la energía cinética interna (vibracional).

Con la introducción de coordenadas normales

  
    
      
        
          q
          
            t
          
        
        ≡
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ∑
          
            α
            =
            1
          
          
            3
          
        
        
        
          Q
          
            t
            ,
            i
            α
          
        
        
          ρ
          
            i
            α
          
        
        ,
      
    
    {\displaystyle q_{t}\equiv \sum _{i=1}^{N}\sum _{\alpha =1}^{3}\;Q_{t,i\alpha }\rho _{i\alpha },}
  

la parte vibracional (interna) del hamiltoniano para el movimiento nuclear se vuelve en la aproximación armónica

  
    
      
        
          
            
              
                H
                ^
              
            
          
          
            
              n
              u
              c
            
          
        
        ≈
        
          
            1
            2
          
        
        
          ∑
          
            t
            =
            1
          
          
            3
            N
            −
            6
          
        
        
          [
          
            −
            
              ℏ
              
                2
              
            
            
              
                
                  ∂
                  
                    2
                  
                
                
                  ∂
                  
                    q
                    
                      t
                    
                    
                      2
                    
                  
                
              
            
            +
            
              f
              
                t
              
            
            
              q
              
                t
              
              
                2
              
            
          
          ]
        
        .
      
    
    {\displaystyle {\hat {H}}_{\mathrm {nuc} }\approx {\frac {1}{2}}\sum _{t=1}^{3N-6}\left[-\hbar ^{2}{\frac {\partial ^{2}}{\partial q_{t}^{2}}}+f_{t}q_{t}^{2}\right].}
  

La ecuación de Schrödinger correspondiente es resuelta fácilmente, se factoriza en 3N − 6 ecuaciones para osciladores armónicos unidimensionales. El principal esfuerzo en esta solución aproximada de la ecuación de Schrödinger de movimiento nuclear es el cómputo del hessiano F de V y su diagonalización.

Esta aproximación al problema de movimiento nuclear, descrito en 3N coordenadas cartesianas ponderadas por masa, se volvió estándar en química cuántica, desde los días en que los algoritmos para cálculos precisos del hessiano F estuvieron disponibles (1980s-1990s). Además de la aproximación armónica, hay una deficiencia adicional de los movimientos externos (rotacional y traslacional) de la molécula que es tomada en cuenta. Ella es considerada en un hamiltoniano rovibracional llamado a veces hamiltoniano de Watson.

## Hamiltoniano del movimiento nuclear de Watson

Con el fin de obtener un hamiltoniano para movimientos externos (traslación y rotación) acoplados a los movimientos internos (vibracionales), es común regresar en este punto a la mecánica clásica para formular la energía cinética clásica correspondiente a estos movimientos de los núcleos. Clásicamente es fácil separar el movimiento de traslación —del centro de masas— de los otros movimientos. Sin embargo, la separación de la rotación del movimiento vibratorio es más difícil y no es completamente posible. Esta separación ro-vibracional se logró por primera vez por Eckart[3]​ en 1935 mediante la imposición de lo que es conocido como condiciones Eckart. Dado que el problema se describe en un sistema de referencia (un sistema de referencia de Eckart) que rota con la molécula, y por lo tanto es un sistema de referencia no inercial, en la energía cinética aparecen asociadas energías con fuerzas ficticias: fuerza centrífuga y fuerza de Coriolis.

En general, la energía cinética clásica T define el sensor métrico g = (gij) asociado con las coordenadas curvilineas s = (si) a través

  
    
      
        2
        T
        =
        
          ∑
          
            i
            j
          
        
        
          g
          
            i
            j
          
        
        
          
            
              
                s
                ˙
              
            
          
          
            i
          
        
        
          
            
              
                s
                ˙
              
            
          
          
            j
          
        
      
    
    {\displaystyle 2T=\sum _{ij}g_{ij}{\dot {s}}_{i}{\dot {s}}_{j}}
  
.
El paso de cuantificación es la transformación de esta energía cinética clásica en un operador de la mecánica cuántica. Es común seguir a Podolsky[4]​ al transcribir el operador de Laplace-Beltrami en las mismas coordenadas s (generalizadas, curvilíneas) como se usa para la forma clásica. La ecuación para este operador requiere la inversión del tensor métrico g y su determinante. La multiplicación del operador de Laplace-Beltrami por 
  
    
      
        −
        
          ℏ
          
            2
          
        
      
    
    {\displaystyle -\hbar ^{2}}
  
 da el operador mecanocuántico de energía cinética requerido. Cuando se aplica esta receta a coordenadas cartesianas, que tienen unidad métrica, la misma energía cinética se obtiene mediante la aplicación de las reglas de cuantizacion.

El hamiltoniano de movimiento nuclear fue obtenido por Wilson y Howard en 1936,[5]​ que siguieron este procedimiento, y más tarde fue refinado por Darling y Dennison en 1940.[6]​ Se mantuvo como el estándar hasta 1968, cuando Watson[7]​ fue capaz de simplificarlo drásticamente al conmutar a través de las derivadas el determinante del tensor métrico. Se dará el hamiltoniano ro-vibracional obtenido por Watson, referido ocasionalmente como el «hamiltoniano de Watson». Antes de hacer esto se debe mencionar que una derivación de este hamiltoniano es posible también al iniciar a partir del operador laplaciano en forma cartesiana, la aplicación de transformaciones de coordenadas, y el uso de la regla de la cadena.[8]​ El hamiltoniano de Watson, que describe todos los movimientos de los núcleos N, es

  
    
      
        
          
            
              H
              ^
            
          
        
        =
        −
        
          
            
              ℏ
              
                2
              
            
            
              2
              
                M
                
                  
                    t
                    o
                    t
                  
                
              
            
          
        
        
          ∑
          
            α
            =
            1
          
          
            3
          
        
        
          
            
              ∂
              
                2
              
            
            
              ∂
              
                X
                
                  α
                
                
                  2
                
              
            
          
        
        +
        
          
            1
            2
          
        
        
          ∑
          
            α
            ,
            β
            =
            1
          
          
            3
          
        
        
          μ
          
            α
            β
          
        
        (
        
          
            
              P
            
          
          
            α
          
        
        −
        
          Π
          
            α
          
        
        )
        (
        
          
            
              P
            
          
          
            β
          
        
        −
        
          Π
          
            β
          
        
        )
        +
        U
        −
        
          
            
              ℏ
              
                2
              
            
            2
          
        
        
          ∑
          
            s
            =
            1
          
          
            3
            N
            −
            6
          
        
        
          
            
              ∂
              
                2
              
            
            
              ∂
              
                q
                
                  s
                
                
                  2
                
              
            
          
        
        +
        V
        .
      
    
    {\displaystyle {\hat {H}}=-{\frac {\hbar ^{2}}{2M_{\mathrm {tot} }}}\sum _{\alpha =1}^{3}{\frac {\partial ^{2}}{\partial X_{\alpha }^{2}}}+{\frac {1}{2}}\sum _{\alpha ,\beta =1}^{3}\mu _{\alpha \beta }({\mathcal {P}}_{\alpha }-\Pi _{\alpha })({\mathcal {P}}_{\beta }-\Pi _{\beta })+U-{\frac {\hbar ^{2}}{2}}\sum _{s=1}^{3N-6}{\frac {\partial ^{2}}{\partial q_{s}^{2}}}+V.}
  

El primer término es el del centro de masas

  
    
      
        
          X
        
        ≡
        
          
            1
            
              M
              
                
                  t
                  o
                  t
                
              
            
          
        
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          M
          
            i
          
        
        
          
            R
          
          
            i
          
        
        
        
          c
          o
          n
        
        
        
          M
          
            
              t
              o
              t
            
          
        
        ≡
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          M
          
            i
          
        
        .
      
    
    {\displaystyle \mathbf {X} \equiv {\frac {1}{M_{\mathrm {tot} }}}\sum _{i=1}^{N}M_{i}\mathbf {R} _{i}\quad \mathrm {con} \quad M_{\mathrm {tot} }\equiv \sum _{i=1}^{N}M_{i}.}
  

El segundo término es el de energía rotacional, similar a la energía cinética del rotor rígido. Aquí 
  
    
      
        
          
            
              P
            
          
          
            α
          
        
      
    
    {\displaystyle {\mathcal {P}}_{\alpha }}
  
 es la componente α del operador de momento angular del rotor rígido de cuerpo fijo, véase el artículo de la matriz D de Wigner para su expresión en términos de ángulos de Euler. El operador 
  
    
      
        
          Π
          
            α
          
        
        
      
    
    {\displaystyle \Pi _{\alpha }\,}
  
 es un componente de un operador conocido como el operador de momento angular vibracional (aunque no satisface las relaciones de conmutación de momento angular),

  
    
      
        
          Π
          
            α
          
        
        =
        −
        i
        ℏ
        
          ∑
          
            s
            ,
            t
            =
            1
          
          
            3
            N
            −
            6
          
        
        
          ζ
          
            s
            t
          
          
            α
          
        
        
        
          q
          
            s
          
        
        
          
            ∂
            
              ∂
              
                q
                
                  t
                
              
            
          
        
      
    
    {\displaystyle \Pi _{\alpha }=-i\hbar \sum _{s,t=1}^{3N-6}\zeta _{st}^{\alpha }\;q_{s}{\frac {\partial }{\partial q_{t}}}}
  

con la constante de acoplamiento de Coriolis:

  
    
      
        
          ζ
          
            s
            t
          
          
            α
          
        
        =
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ∑
          
            β
            ,
            γ
            =
            1
          
          
            3
          
        
        
          ϵ
          
            α
            β
            γ
          
        
        
          Q
          
            s
            ,
            i
            β
          
        
        
        
          Q
          
            t
            ,
            i
            γ
          
        
        
        
        
          y
        
        
        α
        =
        1
        ,
        2
        ,
        3.
      
    
    {\displaystyle \zeta _{st}^{\alpha }=\sum _{i=1}^{N}\sum _{\beta ,\gamma =1}^{3}\epsilon _{\alpha \beta \gamma }Q_{s,i\beta }\,Q_{t,i\gamma }\;\;\mathrm {y} \quad \alpha =1,2,3.}
  

Aquí εαβγ es el símbolo de Levi-Civita. Los términos cuadráticos en 
  
    
      
        
          
            
              P
            
          
          
            α
          
        
      
    
    {\displaystyle {\mathcal {P}}_{\alpha }}
  
 son términos centrífugos, los bilineales en 
  
    
      
        
          
            
              P
            
          
          
            α
          
        
      
    
    {\displaystyle {\mathcal {P}}_{\alpha }}
  
 y 
  
    
      
        
          Π
          
            β
          
        
        
      
    
    {\displaystyle \Pi _{\beta }\,}
  
 son términos de Coriolis. Las cantidades Q s, iγ son las componentes de las coordenadas normales introducidas arriba. De manera alternativa, las coordenadas normales pueden obtenerse por aplicación del método GF de Wilson. La matriz simétrica de 3 × 3 
  
    
      
        
          μ
        
      
    
    {\displaystyle {\boldsymbol {\mu }}}
  
 es llamada el tensor de inercia efectivo recíproco. Si todas las q s fueran cero (molécula rígida), el marco de referencia de Eckart coincidiría con un marco de ejes principal (véase rotor rígido) y 
  
    
      
        
          μ
        
      
    
    {\displaystyle {\boldsymbol {\mu }}}
  
 sería la diagonal, con los momentos de inercia recíprocos de equilibrio en la diagonal. Si todas las q s fueran cero, solo las energías cinéticas de traslación y de rotación rígida sobrevivirían.

El término tipo potencial U es el término de Watson:

  
    
      
        U
        =
        −
        
          
            1
            8
          
        
        
          ∑
          
            α
            =
            1
          
          
            3
          
        
        
          μ
          
            α
            α
          
        
      
    
    {\displaystyle U=-{\frac {1}{8}}\sum _{\alpha =1}^{3}\mu _{\alpha \alpha }}
  

proporcional a la traza del tensor de inercia recíproco efectivo.

El cuarto término en el hamiltoniano de Watson es la energía cinética asociada con las vibraciones de los átomos (núcleos) expresada en coordenadas normales qs, que como se mencionó antes, están dadas en términos de desplazamientos nucleares ρiα por

  
    
      
        
          q
          
            s
          
        
        =
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ∑
          
            α
            =
            1
          
          
            3
          
        
        
          Q
          
            s
            ,
            i
            α
          
        
        
          ρ
          
            i
            α
          
        
        
        
          p
          a
          r
          a
        
        
        s
        =
        1
        ,
        …
        ,
        3
        N
        −
        6.
      
    
    {\displaystyle q_{s}=\sum _{i=1}^{N}\sum _{\alpha =1}^{3}Q_{s,i\alpha }\rho _{i\alpha }\quad \mathrm {para} \quad s=1,\ldots ,3N-6.}
  

Finalmente, V es la energía potencial sin expandir, por definición, dependiente solo de las coordenadas internas. En la aproximación armónica toma la forma

  
    
      
        V
        ≈
        
          
            1
            2
          
        
        
          ∑
          
            s
            =
            1
          
          
            3
            N
            −
            6
          
        
        
          f
          
            s
          
        
        
          q
          
            s
          
          
            2
          
        
        .
      
    
    {\displaystyle V\approx {\frac {1}{2}}\sum _{s=1}^{3N-6}f_{s}q_{s}^{2}.}
  

## Hamiltoniano rotacional

Los espectros rotacionales puros son muy difíciles de conseguir experimentalmente, pero pueden ser descritos por una separación adicional de los movimientos vibracionales y electrónicos. Esto requiere dos cosas:

- Asumir que los núcleos solo hacen pequeñas oscilaciones a partir de la configuración de equilibrio tal que el potencial vibracional puede ser considerado como armónico;

- Aproximar el tensor de inercia con 
  
    
      
        
          I
          
            n
            ,
            e
            q
          
        
        
        
      
    
    {\displaystyle I_{n,eq}\,\;}
  
 calculado en la configuración de equilibrio.
Este es el llamado «modelo armónico vibracional y de rotor rígido».

## Hamiltoniano vibrónico

Esta es la forma más prevalente del hamiltoniano molecular porque las vibraciones son esencialmente independientes de los alrededores. De aquí que las transiciones vibracionales son fácilmente observadas. Debido a que las transiciones rotacionales casi nunca se observan, una buena aproximación al hamiltoniano molecular sería obtenida al mantener solo la parte de HM que describa las partes electrónicas y vibracionales. Esto es llamado el «hamiltoniano vibrónico», un portmanteau de «vibracional» y «electrónico». El hamiltoniano vibrónico está dado por

  
    
      
        
          
            
              
                H
                ^
              
            
          
          
            M
            ,
            v
            i
            b
            r
            o
            n
            i
            c
            o
          
        
        =
        
          
            
              
                T
                ^
              
            
          
          
            e
            ,
            v
            i
            b
            r
            o
            n
            i
            c
            o
          
        
        +
        
          
            
              
                T
                ^
              
            
          
          
            n
            ,
            v
            i
            b
            r
            o
            n
            i
            c
            o
          
        
        +
        V
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle {\hat {H}}_{M,vibronico}={\hat {T}}_{e,vibronico}+{\hat {T}}_{n,vibronico}+V(x_{e},X_{n})}
  

con

  
    
      
        
          
            
              
                T
                ^
              
            
          
          
            e
            ,
            v
            i
            b
            r
            o
            n
            i
            c
            o
          
        
        =
        
          
            
              −
              
                ℏ
                
                  2
                
              
            
            
              2
              
                m
                
                  e
                
              
            
          
        
        
          ∑
          
            
              x
              
                e
              
            
          
        
        
          
            
              
                ∇
                ^
              
            
          
          
            
              x
              
                e
              
            
          
          
            2
          
        
        
        
          y
        
        
        
          
            
              
                T
                ^
              
            
          
          
            n
            ,
            v
            i
            b
            r
            o
            n
            i
            c
            o
          
        
        =
        
          
            
              −
              
                ℏ
                
                  2
                
              
            
            2
          
        
        
          ∑
          
            
              X
              
                n
              
            
          
        
        
          
            
              
                
                  
                    ∇
                    ^
                  
                
              
              
                
                  X
                  
                    n
                  
                
              
              
                2
              
            
            
              M
              
                
                  X
                  
                    n
                  
                
              
            
          
        
      
    
    {\displaystyle {\hat {T}}_{e,vibronico}={\frac {-\hbar ^{2}}{2m_{e}}}\sum _{x_{e}}{\hat {\nabla }}_{x_{e}}^{2}\quad \mathrm {y} \quad {\hat {T}}_{n,vibronico}={\frac {-\hbar ^{2}}{2}}\sum _{X_{n}}{\frac {{\hat {\nabla }}_{X_{n}}^{2}}{M_{X_{n}}}}}
  

siendo 
  
    
      
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle (x_{e},X_{n})}
  
 coordenadas internas de vibración electrónica y nuclear. El uso de las coordenadas internas se debe a que la interacción de Coulomb solo depende de la distancia relativa entre las partículas cargadas. Debido a que los movimientos rotacionales y traslacionales están ahora separados, habrá ya sea 
  
    
      
        3
        N
        −
        5
      
    
    {\displaystyle 3N-5}
  
 o 
  
    
      
        3
        N
        −
        6
      
    
    {\displaystyle 3N-6}
  
 vibraciones si 
  
    
      
        N
      
    
    {\displaystyle N}
  
 es el número de los núcleos y si la molécula es lineal o no lineal.

## Resolviendo la ecuación de Schrödinger molecular

La ecuación de Schrödinger molecular está dada por

  
    
      
        
          
            
              
                H
                ^
              
            
          
          
            M
          
        
        
          ψ
          
            a
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
        =
        
          E
          
            a
          
        
        
          ψ
          
            a
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle {\hat {H}}_{M}\psi _{a}(x_{e},X_{n})=E_{a}\psi _{a}(x_{e},X_{n})}
  

donde 
  
    
      
        
          E
          
            a
          
        
      
    
    {\displaystyle E_{a}}
  
 se refiere a la energía del estado 
  
    
      
        
          ψ
          
            a
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle \psi _{a}(x_{e},X_{n})}
  
. Para resolver la ecuación de Schrödinger se necesita desacoplar el movimiento de los núcleos y electrones. Esto se hace al aproximar la función de onda molecular 
  
    
      
        
          ψ
          
            a
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle \psi _{a}(x_{e},X_{n})}
  
 a un producto de la función de onda electrónica y la función de onda de vibración nuclear. Esto es dado por

  
    
      
        
          ψ
          
            a
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
        =
        
          ϕ
          
            e
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
        ⋅
        
          χ
          
            e
            ,
            ν
          
        
        (
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle \psi _{a}(x_{e},X_{n})=\phi _{e}(x_{e},X_{n})\cdot \chi _{e,\nu }(X_{n})}
  

donde 
  
    
      
        e
        ,
        ν
      
    
    {\displaystyle e,\nu }
  
 es el número cuántico de vibración electrónica y nuclear. Esta formulación es llamada una función de onda adiabática.

Hay dos casos principales en física molecular, un tipo dinámico y uno estático. En el tipo dinámico se asume que las funciones de onda electrónicas siguen las vibraciones de los núcleos. El caso estático usa una configuración de referencia estática para calcular las funciones de onda electrónicas, esto es llamado también la aproximación adiabática cruda.

En la aproximación dinámica la función de onda electrónica es definida como la solución a la ecuación de Schrödinger electrónica

  
    
      
        
          
            
              
                H
                ^
              
            
          
          
            e
          
        
        
          ϕ
          
            e
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
        =
        
          E
          
            e
          
        
        (
        
          X
          
            n
          
        
        )
        ϕ
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle {\hat {H}}_{e}\phi _{e}(x_{e},X_{n})=E_{e}(X_{n})\phi (x_{e},X_{n})}
  

donde

  
    
      
        
          
            
              
                H
                ^
              
            
          
          
            e
          
        
        =
        
          
            
              
                H
                ^
              
            
          
          
            M
          
        
        −
        
          
            
              
                T
                ^
              
            
          
          
            n
          
        
      
    
    {\displaystyle {\hat {H}}_{e}={\hat {H}}_{M}-{\hat {T}}_{n}}
  

con las funciones de onda electrónicas encontradas. Las coordenadas vibracionales nucleares 
  
    
      
        
          X
          
            n
          
        
        =
        {
        
          X
          
            1
          
        
        ,
        
          X
          
            2
          
        
        ,
        …
        ,
        
          X
          
            3
            N
            −
            6
          
        
        }
      
    
    {\displaystyle X_{n}=\{X_{1},X_{2},\ldots ,X_{3N-6}\}}
  
 o 
  
    
      
        
          X
          
            n
          
        
        =
        {
        
          X
          
            1
          
        
        ,
        
          X
          
            2
          
        
        ,
        …
        ,
        
          X
          
            3
            N
            −
            5
          
        
        }
      
    
    {\displaystyle X_{n}=\{X_{1},X_{2},\ldots ,X_{3N-5}\}}
  
 pueden ser tratadas como parámetros y la solución de la ecuación de Schrödinger electrónica define entonces la dependencia de la función de onda electrónica y los autovalores con el conjunto de coordenadas de vibración nuclear 
  
    
      
        
          X
          
            n
          
        
      
    
    {\displaystyle X_{n}}
  
. Las funciones de onda electrónicas definen un conjunto ortonormal completo de funciones para cada 
  
    
      
        
          X
          
            n
          
        
      
    
    {\displaystyle X_{n}}
  
 tal que la función de onda molecular puede ser expandida en la base.

  
    
      
        
          ψ
          
            a
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
        =
        
          ∑
          
            e
            ,
            ν
          
        
        
          ϕ
          
            e
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
        ⋅
        
          χ
          
            e
            ,
            ν
          
        
        (
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle \psi _{a}(x_{e},X_{n})=\sum _{e,\nu }\phi _{e}(x_{e},X_{n})\cdot \chi _{e,\nu }(X_{n})}
  

Usando este resultado en el más usado caso vibrónico, e insertando en la ecuación de Schrödinger electrónica omitiendo el acoplamiento electrónico se obtiene una nueva ecuación de autovalores dada por

  
    
      
        (
        
          
            
              
                T
                ^
              
            
          
          
            n
            ,
            v
            i
            b
            r
            o
            n
            i
            c
            o
          
        
        +
        
          E
          
            
              e
              ′
            
          
        
        (
        
          X
          
            n
          
        
        )
        )
        
          χ
          
            
              e
              ′
            
            ,
            
              ν
              ′
            
          
        
        (
        
          X
          
            n
          
        
        )
        =
        
          E
          
            
              e
              ′
            
            ,
            
              ν
              ′
            
          
        
        
          χ
          
            
              e
              ′
            
            ,
            
              ν
              ′
            
          
        
        (
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle ({\hat {T}}_{n,vibronico}+E_{e'}(X_{n}))\chi _{e',\nu '}(X_{n})=E_{e',\nu '}\chi _{e',\nu '}(X_{n})}
  

donde los coeficientes de expansión 
  
    
      
        
          χ
          
            e
            ,
            ν
          
        
        (
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle \chi _{e,\nu }(X_{n})}
  
 describen las eigenfunciones vibracionales y 
  
    
      
        
          E
          
            e
          
        
        (
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle E_{e}(X_{n})}
  
 describe la energía potencial vibracional. El autovalor 
  
    
      
        
          E
          
            e
          
        
        (
        
          X
          
            n
          
        
        )
      
    
    {\displaystyle E_{e}(X_{n})}
  
 es usualmente aproximado por una función armónica para simplificación.

## Limitaciones

Cuando las asunciones requeridas para la aproximación adiabática de Born–Oppenheimer no se cumplen, se dice que la aproximación «se rompe». Se necesitan otras aproximaciones para describir adecuadamente un sistema que está más allá de la aproximación Born–Oppenheimer.

La consideración explícita del acoplamiento de movimientos electrónico y nuclear (vibracional) es conocida como acoplamiento electrón-fonón en sistemas extendidos tales como sistemas en estado sólido. En sistemas no extendidos tales como moléculas aisladas complejas, es conocida como acoplamiento vibrónico el cual es importante en el caso de cruces evitados o intersecciones cónicas.

La llamada «corrección Born–Oppenheimer diagonal» (DBOC) puede ser obtenida como

  
    
      
        ⟨
        
          ϕ
          
            e
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
        
          |
        
        
          T
          
            n
          
        
        
          |
        
        
          ϕ
          
            e
          
        
        (
        
          x
          
            e
          
        
        ,
        
          X
          
            n
          
        
        )
        ⟩
      
    
    {\displaystyle \langle \phi _{e}(x_{e},X_{n})|T_{n}|\phi _{e}(x_{e},X_{n})\rangle }
  

donde 
  
    
      
        
          T
          
            n
          
        
      
    
    {\displaystyle T_{n}}
  
 es el operador de energía cinética nuclear y la función de onda electrónica 
  
    
      
        
          ϕ
          
            e
          
        
      
    
    {\displaystyle \phi _{e}}
  
 es paramétricamente (no explícitamente) dependiente de las coordenadas nucleares.

## Véase también

- Hamiltoniano (mecánica cuántica)

- Mecánica hamiltoniana

## Referencias

- ↑ W. Kołos; L. Wolniewicz (1963). «Nonadiabatic Theory for Diatomic Molecules and Its Application to the Hydrogen Molecule». Rev. Mod. Phys. 35 (3): 473-483. Bibcode:1963RvMP...35..473K. doi:10.1103/RevModPhys.35.473. 

- ↑ R. G. Woolley; B. T. Sutcliffe (2003). «P.-O. Löwdin and the Quantum Mechanics of Molecules».  En E. J. Brändas; E. S. Kryachko, eds. Fundamental World of Quantum Chemistry 1. Kluwer Academic Publishers. pp. 21-65. 

- ↑ Eckart, C. (1935). «Some studies concerning rotating axes and polyatomic molecules». Physical Review 47: 552-558. doi:10.1103/PhysRev.47.552. 

- ↑ Podolsky, B. (1928). «Quantum-mechanically correct form of Hamiltonian function for conservative system». Phys. Rev. 32: 812. 

- ↑ E. Bright Wilson Jr.; J. B. Howard (1936). «The Vibration–Rotation Energy Levels of Polyatomic Molecules I. Mathematical Theory of Semirigid Asymmetrical Top Molecules». J. Chem. Phys. 4 (4): 260-268. Bibcode:1936JChPh...4..260W. doi:10.1063/1.1749833. 

- ↑ B. T. Darling; D. M. Dennison (1940). «The water vapor molecule». Phys. Rev. 57 (2): 128-139. Bibcode:1940PhRv...57..128D. doi:10.1103/PhysRev.57.128. 

- ↑ Watson, James K. G. (1968). «Simplification of the molecular vibration-rotation hamiltonian». Molecular Physics 15 (5): 479. Bibcode:1968MolPh..15..479W. doi:10.1080/00268976800101381. 

- ↑ Biedenharn, L. C.; Louck, J. D. (1981). «Angular Momentum in Quantum Physics». Encyclopedia of Mathematics 8. Reading: Addison–Wesley. ISBN 978-0-201-13507-7. 

## Bibliografía adicional

- Born, Max; Oppenheimer, Robert (25 de agosto de 1927). «Zur Quantentheorie der Molekeln». Annalen der Physik 389 (20): 457-484. Bibcode:1927AnP...389..457B. doi:10.1002/andp.19273892002. 

- Moss, R. E. (1973). Advanced Molecular Quantum Mechanics. Chapman & Hall. ISBN 0-412-10490-3. 

- Tinkham, Michael (2003). Group Theory and Quantum Mechanics. Dover Publications. ISBN 0-486-43247-5. 

- Una discusión amena y rigurosa sobre los términos de espín del hamiltoniano molecular se halla en: McWeeny, R. (1989). Methods of Molecular Quantum Mechanics (2.ª edición). Londres: Academic. ISBN 0-12-486550-X. 

## Enlaces externos

- Esta obra contiene una traducción  derivada de «Molecular Hamiltonian» de Wikipedia en inglés, concretamente de esta versión, publicada por sus editores bajo la Licencia de documentación libre de GNU y la Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional.

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q2379331

-  Datos: Q2379331

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.