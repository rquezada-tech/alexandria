---
title: "Teoría del funcional de la densidad"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Teoría del funcional de la densidad
    
    
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
  
  
    
      
        
          
            
              
## Teoría del funcional de la densidad

            
            
            
              
                

              

              La teoría del funcional de la densidad (TFD o DFT por sus siglas en inglés: Density functional theory), aplicada a sistemas electrónicos, es un procedimiento variacional alternativo a la solución de la ecuación de Schrödinger, donde el funcional de la energía electrónica es minimizado respecto a la densidad electrónica. Es uno de los métodos más utilizados en los cálculos cuánticos de la estructura electrónica de la materia, tanto en la física de la materia condensada como en la química cuántica.

Los orígenes de la teoría del funcional de la densidad electrónica se encuentran en un modelo desarrollado por Llewellyn Thomas y Enrico Fermi a final de los años 1920. Sin embargo, no fue hasta mediados de los años 1960 cuando las contribuciones de Pierre Hohenberg, Walter Kohn y Lu Sham establecieron el formalismo teórico en el que se basa el método usado actualmente. En 1998, Walter Kohn recibió el premio Nobel de Química por sus aportes al desarrollo de esta teoría.[1]​

Los métodos tradicionales dentro de las teorías de la estructura electrónica de la materia, en particular la teoría de Hartree-Fock y los derivados de este formalismo, se basan en una función de onda multielectrónica.[2]​ Si bien esta resolución de la ecuación de Schrödinger permite describir de forma exacta el comportamiento de los sistemas muy pequeños, su capacidad de predicción se ve limitada por el hecho de que sus ecuaciones son demasiado complejas de resolver numéricamente o menos aún analíticamente. La TFD reformula el problema para ser capaz de obtener, por ejemplo, la energía y la distribución electrónica del estado fundamental, trabajando con el funcional de la densidad electrónica en vez de con la función de ondas. Una ventaja es que la densidad es una magnitud mucho más simple que la función de ondas y por lo tanto más fácil de calcular y en la práctica son accesibles sistemas mucho más complejos: la función de ondas de un sistema de N electrones depende de 3N variables, mientras que la densidad electrónica solo depende de 3 variables. Una desventaja es que, salvo los casos más simples, no se conoce de manera exacta el funcional que relaciona esta densidad con la energía del sistema. En la práctica, se usan funcionales que se han comprobado que dan buenos resultados.

Originalmente, la TFD se desarrolló en el marco de la teoría cuántica no relativista (ecuación de Schrödinger independiente del tiempo) y de la aproximación de Born-Oppenheimer. La teoría fue extendida posteriormente al dominio de la mecánica cuántica dependiente del tiempo, y se habla de la TD-DFT o Teoría del Funcional de la Densidad Dependiente del Tiempo y del dominio relativista. Entre otras cosas, esto permite calcular estados excitados.

Este método es uno de los exponentes máximos de la interpretación probabilística de la mecánica cuántica.

## Historia

 
  Las leyes físicas fundamentales que son necesarias para la teoría matemática de una gran parte de la física y la totalidad de la química son pues completamente conocidas, y la dificultad es únicamente que la aplicación exacta de estas leyes lleva a ecuaciones demasiado complicadas como para ser resolubles.

  The underlying physical laws necessary for the mathematical theory of a large part of physics and the whole of chemistry are thus completely known, and the difficulty is only that the exact application of these laws leads to equations much too complicated to be soluble.

 
 Paul A.M. Dirac, 1929[3]​

Las primeras nociones de una teoría del funcional de la densidad fueron desarrolladas por Thomas y Fermi en los años 1920. Calcularon la energía de un átomo, representando su energía cinética como función de su densidad electrónica, y combinando esto con las expresiones clásicas de las interacciones núcleo-electrón y electrón-electrón (que también se pueden representar en términos de densidad electrónica). El modelo fue mejorado por Dirac, que añadió un funcional de energía de intercambio en 1928. Sin embargo, la teoría de Thomas-Fermi-Dirac era imprecisa para la mayoría de las aplicaciones, por la mala representación de la energía cinética como función de la densidad.

La base teórica para la TFD fue dada en 1964 por Hohenberg y Kohn, quienes mostraron que la energía es un funcional de la densidad y que además la densidad del sistema minimiza este funcional. Sin embargo, el desarrollo más importante fue dado el año siguiente, cuando Kohn y Sham demostraron que a partir de la teoría del funcional de la densidad es posible escribir una ecuación para orbitales de una partícula, de los cuales se obtiene la densidad.

La TFD era muy popular para cálculos de física del estado sólido desde los años 1970. Sin embargo, se consideraba que no era lo bastante precisa para la química cuántica hasta los años 1990, cuando se refinaron en gran medida las aproximaciones usadas en la teoría. Ahora la TFD es un método fundamental para los cálculos de estructura electrónica en ambos campos.

## Descripción de la teoría

 
  Si no te gusta la respuesta, cambia la pregunta.

  If you don't like the answer, change the question.

 
Richard M. Martin[4]​

## Teoremas de Hohenberg-Kohn

En la mecánica cuántica estándar, los observables son calculados a partir de la función de onda de muchos cuerpos. El método de la DFT fue sometido a un tratamiento riguroso por Hohenberg y Kohn en 1964,[5]​ quienes demostraron que, para el estado fundamental, existe una relación uno a uno entre la densidad electrónica y el potencial externo, 
  
    
      
        v
        (
        
          r
        
        )
      
    
    {\displaystyle v(\mathbf {r} )}
  
. Esto quiere decir que la densidad electrónica en el estado fundamental contiene la información de un sistema electrónico.[6]​

En particular, Hohenberg y Kohn mostraron que la energía es un funcional de la densidad a través de la relación

  
    
      
        E
        [
        ρ
        ]
        =
        F
        [
        ρ
        ]
        +
        ∫
        d
        
          r
        
        ρ
        (
        
          r
        
        )
        v
        (
        
          r
        
        )
      
    
    {\displaystyle E[\rho ]=F[\rho ]+\int d\mathbf {r} \rho (\mathbf {r} )v(\mathbf {r} )}
  
,

donde 
  
    
      
        F
        [
        ρ
        ]
      
    
    {\displaystyle F[\rho ]}
  
 representa al funcional universal que contiene a la energía cinética, 
  
    
      
        T
        [
        ρ
        ]
      
    
    {\displaystyle T[\rho ]}
  
,
y la interacción electrón-electrón, 
  
    
      
        
          V
          
            e
            e
          
        
        [
        ρ
        ]
      
    
    {\displaystyle V_{ee}[\rho ]}
  
.

Con un segundo teorema los mismos autores demostraron que la densidad electrónica del estado basal es aquella que minimiza al funcional de energía 
  
    
      
        E
        [
        ρ
        ]
      
    
    {\displaystyle E[\rho ]}
  
. Desde el punto de vista numérico, la función de onda es un objeto muy complejo de manipular, pues para N partículas es una función de 3N variables, mientras que la densidad es más fácil de manejar pues es siempre una función de 3 variables, independientemente del número de partículas. El problema, es que no se conoce la forma exacta del funcional 
  
    
      
        F
        [
        ρ
        ]
      
    
    {\displaystyle F[\rho ]}
  
.

## El modelo de Kohn y Sham

Kohn y Sham presentaron una forma de aproximar al funcional universal 
  
    
      
        F
        [
        ρ
        ]
      
    
    {\displaystyle F[\rho ]}
  
. Para lograr este propósito, Kohn y Sham recurrieron a un sistema ficticio el cual está constituido por un sistema de 
  
    
      
        N
      
    
    {\displaystyle N}
  
 electrones no interactuantes. Esto significa que tal sistema puede estar representado por un determinante (determinante de Slater) cuyos elementos son funciones que representan a cada uno de los electrones del sistema (orbitales,
  
    
      
        
          ϕ
          
            i
          
        
      
    
    {\displaystyle \phi _{i}}
  
). Con este punto de partida la energía cinética corresponde a una suma de energías cinéticas individuales

  
    
      
        
          T
          
            s
          
        
        =
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        ∫
        d
        
          r
        
        
          ϕ
          
            i
          
          
            ∗
          
        
        (
        
          r
        
        )
        (
        −
        
          
            1
            2
          
        
        
          ∇
          
            2
          
        
        )
        
          ϕ
          
            i
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle T_{s}=\sum _{i=1}^{N}\int d\mathbf {r} \phi _{i}^{*}(\mathbf {r} )(-{\frac {1}{2}}\nabla ^{2})\phi _{i}(\mathbf {r} )}
  

y la densidad electrónica a la suma de densidades orbitales

  
    
      
        ρ
        (
        
          r
        
        )
        =
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ρ
          
            i
          
        
        (
        
          r
        
        )
        =
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          ϕ
          
            i
          
          
            ∗
          
        
        (
        
          r
        
        )
        
          ϕ
          
            i
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle \rho (\mathbf {r} )=\sum _{i=1}^{N}\rho _{i}(\mathbf {r} )=\sum _{i=1}^{N}\phi _{i}^{*}(\mathbf {r} )\phi _{i}(\mathbf {r} )}
  
[7]​[8]​

Un elemento adicional en el modelo de Kohn y Sham es la aproximación a la interacción electrón-electrón ya que proponen como parte principal de esta a la interacción coulómbica:

  
    
      
        J
        [
        ρ
        ]
        =
        
          
            1
            2
          
        
        ∫
        ∫
        d
        
          r
        
        d
        
          
            r
          
          ′
        
        
          
            
              ρ
              (
              
                r
              
              )
              ρ
              (
              
                
                  r
                
                ′
              
              )
            
            
              
                |
              
              
                r
              
              −
              
                
                  r
                
                ′
              
              
                |
              
            
          
        
      
    
    {\displaystyle J[\rho ]={\frac {1}{2}}\int \int d\mathbf {r} d\mathbf {r} '{\frac {\rho (\mathbf {r} )\rho (\mathbf {r} ')}{|\mathbf {r} -\mathbf {r} '|}}}
  

y con esto el funcional universal es escrito como:

  
    
      
        F
        [
        ρ
        ]
        =
        T
        [
        ρ
        ]
        +
        
          V
          
            e
            e
          
        
        [
        ρ
        ]
        =
        
          T
          
            s
          
        
        [
        ρ
        ]
        +
        J
        [
        ρ
        ]
        +
        
          E
          
            x
            c
          
        
        [
        ρ
        ]
      
    
    {\displaystyle F[\rho ]=T[\rho ]+V_{ee}[\rho ]=T_{s}[\rho ]+J[\rho ]+E_{xc}[\rho ]}
  

donde es claro que el funcional de intercambio y correlación, 
  
    
      
        
          E
          
            x
            c
          
        
        [
        ρ
        ]
      
    
    {\displaystyle E_{xc}[\rho ]}
  
, se define como:

  
    
      
        
          E
          
            x
            c
          
        
        [
        ρ
        ]
        =
        T
        [
        ρ
        ]
        −
        
          T
          
            s
          
        
        [
        ρ
        ]
        +
        
          V
          
            e
            e
          
        
        [
        ρ
        ]
        −
        J
        [
        ρ
        ]
      
    
    {\displaystyle E_{xc}[\rho ]=T[\rho ]-T_{s}[\rho ]+V_{ee}[\rho ]-J[\rho ]}
  

Los orbitales de Kohn y Sham son aquellos que satisfagan las ecuaciones íntegro-diferenciales de Kohn y Sham

  
    
      
        
          (
          
            −
            
              
                1
                2
              
            
            
              ∇
              
                2
              
            
            +
            
              v
              
                
                  e
                  f
                  f
                
              
            
            (
            
              r
            
            )
          
          )
        
        
          ϕ
          
            i
          
        
        (
        
          r
        
        )
        =
        
          ε
          
            i
          
        
        
          ϕ
          
            i
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle \left(-{\frac {1}{2}}\nabla ^{2}+v_{\rm {eff}}(\mathbf {r} )\right)\phi _{i}(\mathbf {r} )=\varepsilon _{i}\phi _{i}(\mathbf {r} )}
  

y que generarán la energía del estado fundamental. El potencial de Kohn—Sham 
  
    
      
        
          v
          
            e
            f
            f
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle v_{eff}(\mathbf {r} )}
  
 incorpora por lo tanto los efectos de 
la interacción entre los electrones (incluyendo los de intercambio-correlación) y también los de un posible potencial externo de confinamiento 
(por ejemplo el potencial atractivo del núcleo atómico sobre los electrones) 
  
    
      
        v
        (
        
          r
        
        )
      
    
    {\displaystyle v(\mathbf {r} )}
  
. Formalmente, el potencial de Kohn-Sham
se define como la derivada funcional

  
    
      
        
          v
          
            
              e
              f
              f
            
          
        
        (
        
          r
        
        )
        =
        
          
            
              δ
              J
              [
              ρ
              ]
            
            
              δ
              ρ
              (
              
                r
              
              )
            
          
        
        +
        
          
            
              δ
              
                E
                
                  x
                  c
                
              
              [
              ρ
              ]
            
            
              δ
              ρ
              (
              
                r
              
              )
            
          
        
        +
        v
        (
        
          r
        
        )
        =
        ∫
        d
        
          
            r
          
          ′
        
        
          
            
              ρ
              (
              
                
                  r
                
                ′
              
              )
            
            
              
                |
              
              
                r
              
              −
              
                
                  r
                
                ′
              
              
                |
              
            
          
        
        +
        
          
            
              δ
              
                E
                
                  x
                  c
                
              
              [
              ρ
              ]
            
            
              δ
              ρ
              (
              
                r
              
              )
            
          
        
        +
        v
        (
        
          r
        
        )
      
    
    {\displaystyle v_{\rm {eff}}(\mathbf {r} )={\frac {\delta J[\rho ]}{\delta \rho (\mathbf {r} )}}+{\frac {\delta E_{xc}[\rho ]}{\delta \rho (\mathbf {r} )}}+v(\mathbf {r} )=\int d\mathbf {r} '{\frac {\rho (\mathbf {r} ')}{|\mathbf {r} -\mathbf {r} '|}}+{\frac {\delta E_{xc}[\rho ]}{\delta \rho (\mathbf {r} )}}+v(\mathbf {r} )}
  

En la práctica, por lo tanto, es para el segundo término (llamado potencial de intercambio-correlación 
  
    
      
        
          v
          
            x
            c
          
        
        [
        ρ
        ]
        =
        
          
            
              δ
              
                E
                
                  x
                  c
                
              
              [
              ρ
              ]
            
            
              δ
              ρ
              (
              
                r
              
              )
            
          
        
      
    
    {\displaystyle v_{xc}[\rho ]={\frac {\delta E_{xc}[\rho ]}{\delta \rho (\mathbf {r} )}}}
  
) 
que se deben emplear expresiones aproximadas.

La idea básica del método de Kohn-Sham, por lo tanto, se puede resumir de la siguiente manera: el problema de N partículas interactuantes entre ellas, y confinadas en un cierto 
potencial externo 
  
    
      
        v
        (
        
          r
        
        )
      
    
    {\displaystyle v(\mathbf {r} )}
  
, se redefine en términos de un sistema artificial donde las partículas no interactúan pero se mueven bajo la acción de un distinto
potencial effectivo 
  
    
      
        
          v
          
            
              e
              f
              f
            
          
        
        (
        
          r
        
        )
      
    
    {\displaystyle v_{\rm {eff}}(\mathbf {r} )}
  
. Este debe modelar los efectos de la interacción del sistema físico original de forma que ambos problemas sean 
equivalentes (es decir, tengan la misma distribución de densidad y por lo tanto la misma energía).

Aunque las ecuaciones de Kohn—Sham son muy similares a las del método de Hartree-Fock y se resuelven también como éstas de manera iterativa y autoconsistente (dado que las soluciones 
  
    
      
        
          ϕ
          
            i
          
        
      
    
    {\displaystyle \phi _{i}}
  
 
vienen determinadas por el potencial 
  
    
      
        
          v
          
            
              e
              f
              f
            
          
        
      
    
    {\displaystyle v_{\rm {eff}}}
  
 y este a su vez depende implícitamente de los 
  
    
      
        
          ϕ
          
            i
          
        
      
    
    {\displaystyle \phi _{i}}
  
 a través de su relación con la densidad), el significado físico de ambos métodos es 
diferente ya que tienen asociados potenciales efectivos diferentes.[9]​

## Energía de intercambio y correlación

Aun cuando el planteamiento de Kohn y Sham es exacto, hasta el momento el funcional de intercambio y correlación exacto, 
  
    
      
        
          E
          
            x
            c
          
        
      
    
    {\displaystyle E_{xc}}
  
, es desconocido y por lo tanto son necesarias aproximaciones a este funcional. La clasificación a estas aproximaciones se puede encontrar en la escalera de Jacob definida por John. P. Perdew.[10]​

La primera aproximación para este funcional se conoce como Aproximación de Densidad Local (LDA) y consiste en suponer que en cada punto, la energía de intercambio y correlación depende solo de la densidad en ese punto. Este valor se considera como el que tendría un gas de electrones libres de esa densidad. Si bien es una aproximación bastante fuerte, se obtienen resultados sorprendentemente precisos para algunas propiedades, y es en parte a eso que se debe el éxito de esta teoría.

Existen aproximaciones más sofisticadas para el funcional de intercambio y correlación, estas se conocen como Aproximaciones de Gradiente Generalizado (GGA), estas son semilocales, ya que consideran en cada punto el valor de la densidad y sus gradientes. Un ejemplo representativo de esta aproximación es el funcional reportado por Perdew, Burke y Ernzerhof,[11]​,[12]​ el cual ha motivado a varias revisiones y mejoras.[13]​ Para algunas propiedades estas aproximaciones dan mejores resultados que LDA, en particular para geometrías moleculares y energías del estado fundamental, aunque para otras no representan una mejora sustancial.

Aun con esta aproximación, no se conoce la forma funcional para las energías de correlación electrónicas y energía de intercambio (también llamado interacción de canje). Estas corresponden a la interacción cuántica entre electrones, la primera debido a la parte cuántica de la repulsión coulombiana y la segunda debido al principio de exclusión de Pauli entre electrones del mismo espín. Una solución a este problema es el desarrollo de métodos híbridos como el B3LYP,[14]​[15]​[16]​ pero existen otros métodos dentro de la propia teoría del funcional de la densidad.

Una serie de funcionales más sofisticados puede obtenerse al suponer que la energía de intercambio y correlación depende explícitamente de los orbitales de Kohn-Sham. El más común de estos funcionales es el de Intercambio Exacto (EXX), que incluye de manera completa la energía de intercambio electrónico y que puede derivarse desde primeros principios. El problema de este tipo de funcionales es que computacionalmente son más costosos de tratar.

## Extensiones

La teoría del funcional de la densidad ha sido generalizada para tratar sistemas más complejos. Una de las generalizaciones más importantes es la teoría del funcional de la densidad tiempo-dependiente (TDDFT por sus siglas en inglés) que permite ampliar la teoría para el estudio de sistemas bajo excitaciones.

## Aplicaciones y comparación con otros métodos

La principal ventaja de la Teoría del Funcional de la Densidad es que las ecuaciones de esta son mucho más simples de resolver que las ecuaciones de muchos cuerpos de mecánica cuántica u otras aproximaciones, por lo que permiten tratar sistemas más grandes y calcular más propiedades. Por lo general es posible llegar a hacer simulaciones con unos pocos miles de átomos.

El principal problema es que si bien es en principio una teoría exacta, solo se puede aplicar de forma aproximada, lo que hace que sus resultados sean menos precisos que otros métodos. Además, diferentes aproximaciones a la energía de intercambio y correlación pueden dar resultados diferentes. Aun así, para muchos métodos más sofisticados se utiliza como punto de partida los resultados de TFD. 

Por este motivo, hay cierta división en la comunidad científica. Los defensores de la TFD indican que sus resultados son muy satisfactorios, y que, por su bajo coste computacional, es la única forma de abordar sistemas más allá de cierta complejidad. Sus detractores apuntan a que es un método semiempírico más, y que no es tan fiable como los métodos ab initio «clásicos».

En este sentido, existe una controversia sobre si la Teoría del Funcional de la Densidad puede ser considerada o no un método ab initio. En general en física se le considera así, debido a que no se requiere ningún tipo de parámetro adicional ni ajuste obtenido de resultados experimentales. En química por el contrario, suele guardarse el término ab initio para métodos derivados de la teoría cuántica de muchos cuerpos que por lo general son más precisos, más costosos computacionalmente y cuyo nivel de aproximación puede ser ajustado.

## Véase también

- Anexo:Software de ayuda para DFT

## Notas y referencias

- ↑ The Nobel Fundation (1998). «The Nobel Prize of Chemistry 1998». Consultado el 16 de junio de 2010. «The Nobel Prize in Chemistry 1998 was divided equally between Walter Kohn "for his development of the density-functional theory" and John A. Pople "for his development of computational methods in quantum chemistry".». 

- ↑ Gázquez, J. L.; Galván, M.; Vela, A. ¿Qué es la química teórica?  http://www.izt.uam.mx/cosmosecm/QUIMICA_TEORICA.html Archivado el 17 de abril de 2013 en Wayback Machine.

- ↑ P.A.M. Dirac (1929). «Quantum Mechanics of Many-Electron Systems». Proceedings of the Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character (en inglés) 123 (792). pp. 714-733. 

- ↑  Martin, Richard M. (2004).  Cambridge University Press, ed. Electronic Structure Basic Theory and Practical Methods (en inglés). pp. 135. ISBN 0521782856. 

- ↑ P. Hohenberg y W. Kohn, Phys. Rev. 136 (1964) B864

- ↑ (Capelle, 2006), pág. 10; se pueden encontrar más detalles en las pp. 10-15.

- ↑ Kohn, Walter; Sham, Lu Jeu (1965). «Self-Consistent Equations Including Exchange and Correlation Effects». Physical Review 140 (4A): A1133-A1138. doi:10.1103/PhysRev.140.A1133. 

- ↑ Parr, Robert G.; Yang, Weitao (1994). Density-Functional Theory of Atoms and Molecules. ISBN 978-0195092769. 

- ↑ Garza, J.; Nichols, Jeffrey A.; Dixon, David A.
The role of the local-multiplicative Kohn-Sham potential on the description of occupied and unoccupied orbitals.
J. Chem. Phys. 113, 6029 (2000)

- ↑ Perdew, J. P.; Ruzsinszky, A.; Tao, J.; Staroverov, V. N.; Scuseria, G. E.; Csonka, G. I. Prescription for the design and selection of density functional approximations: More constraint satisfaction with fewer fits. J. Chem. Phys. 123, 062201 (2005)

- ↑ Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple Phys. Rev. Lett. 77, 3865 (1996)

- ↑ Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple, Errata Phys. Rev. Lett. 78, 1396 (1997).

- ↑ Martín del Campo, J.; Gázquez, J. L.; Trickey, S. B.; Vela, A. Non-empirical improvement of PBE and its hybrid PBE0 for general description of molecular properties J. Chem. Phys. 136, 104108 (2012)

- ↑  A. D. Becke, J. Chem. Phys. 38 (1998) 3089

- ↑ C. Lee, W. Yang, y R. G. Parr, Phys. Rev. B 37 (1988) 785

- ↑ P. J. Stephens, F. J. Devlin, C. F. Chabalowski, y M. J. Frisch, J. Phys. Chem. 98 (1994) 11623

## Fuentes

- Capelle, Klaus (2006). «Una visión a vista de pájaro de la teoría del funcional de densidad». Braz. J. Phys. [online] (en inglés) 36 (4a). doi:10.1590/S0103-97332006000700035. pp. 1318-1343. ISSN 0103-9733. Consultado el 14 de junio de 2010. .

## Bibliografía adicional

- R. M. Dreizler, Eberhard K. U. Gross: Density Functional Theory. Springer, Berlín 1990, ISBN 3-540-51993-9.

- Parr, Robert G; Yang, Weitao (1989). Density-Functional Theory of Atoms and Molecules. Nueva York: Oxford University Press. ISBN 0-19-504279-4. Parr, Robert G.; Yang, Weitao (1994). Density-Functional Theory of Atoms and Molecules (Updated) (en inglés). Oxford University Press. ISBN 0-19-509276-7. 

- Pérez-Jordá, José María (tesis doctoral) Teoría del Funcional Densidad (1992)

- Sancho García, Juan Carlos (tesis doctoral) La teoría del funcional densidad y las ecuaciones variacionales de Kohn-Sham : Aportación de nuevos aspectos sobre sus posibilidades y limitaciones (2004)
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q1048589

- Identificadores

- BNF: 12264261r (data)

- LCCN: sh85036851

- NLI: 987007548285205171

- Diccionarios y enciclopedias

- Britannica: url

- Identificadores médicos

- MeSH: D000077318

-  Datos: Q1048589

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.