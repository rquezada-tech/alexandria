---
title: "Función de estado"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Función de estado
    
    
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
  
  
    
      
        
          
            
              
## Función de estado

            
            
            
              
                

              

              
En termodinámica, una función de estado es una magnitud física macroscópica que caracteriza el estado de un sistema en equilibrio, y que no depende de la forma en que el sistema llegó a dicho estado.[1]​ Dado un sistema termodinámico en equilibrio puede escogerse un número finito de variables de estado, tal que sus valores determinan unívocamente el estado del sistema.

El valor de una función de estado sólo depende del estado termodinámico actual en que se encuentre el sistema, sin importar cómo llegó a él. Esto significa que si, en un instante dado, tenemos dos sistemas termodinámicos en equilibrio con n grados de libertad y medimos un mismo valor de n funciones de estado independientes, cualquier otra función de estado tendrá el mismo valor en ambos sistemas con independencia del valor de las variables en instantes anteriores. En general, los sistemas fuera del equilibrio no pueden ser representados por un número finito de grados de libertad, y su descripción es mucho más compleja.

En cuanto al trabajo y al calor intercambiados durante una transformación, no pueden asimilarse a la variación de una función de estado porque dependen de la naturaleza de la transformación. En el caso general, el trabajo y el calor son más bien funciones de trayectoria porque sus valores dependen del camino recorrido entre el estado inicial y el estado final del sistema. Sin embargo, hay casos especiales en los que el calor y el trabajo ya no dependen del camino seguido, ya sea reversible o irreversible , cuando las transformaciones tienen lugar ya sea a presión constante (ver entalpía ) o a volumen constante.

Matemáticamente, la posibilidad de representar una cantidad física mediante una función de estado está ligada a las propiedades de su forma diferencial, es decir su variación en una transformación infinitesimal alrededor de un estado de equilibrio.

## Historia

Es probable que el término «funciones de estado» fuera utilizado en un sentido laxo durante las décadas de 1850 y 1860 por personas como Rudolf Clausius, William Rankine, Peter Tait, y William Thomson. En la década de 1870, el término había adquirido un uso propio. En su artículo de 1873 «Métodos gráficos en la termodinámica de los fluidos», Willard Gibbs afirma: «Las cantidades v, p, t, ε, y η se determinan cuando se da el estado del cuerpo, y puede permitirse llamarlas funciones del estado del cuerpo."[2]​

## Sistema termodinámico y espacio de estado

Un sistema termodinámico se describe mediante un número de parámetros termodinámicos (por ejemplo, temperatura, volumen, o presión) que no son necesariamente independientes. El número de parámetros necesarios para describir el sistema es la dimensión del espacio de estados del sistema (D). Por ejemplo, un gas monoatómico con un número fijo de partículas es un caso simple de un sistema bidimensional (D = 2). Cualquier sistema bidimensional está especificado de forma única por dos parámetros. La elección de un par de parámetros diferente, como la presión y el volumen en lugar de la presión y la temperatura, crea un sistema de coordenadas diferente en el espacio de estado termodinámico bidimensional, pero por lo demás es equivalente. La presión y la temperatura pueden usarse para encontrar el volumen, la presión y el volumen pueden usarse para encontrar la temperatura, y la temperatura y el volumen pueden usarse para encontrar la presión. Una afirmación análoga es válida para los espacios de mayor dimensión, descritos por el postulado de estado.

## Funciones de estado

Generalmente, un espacio de estado está definido por una ecuación de la forma 
  
    
      
        F
        (
        P
        ,
        V
        ,
        T
        ,
        …
        )
        =
        0
      
    
    {\displaystyle F(P,V,T,\ldots )=0}
  
, donde P denota la presión, T denota la temperatura, V denota el volumen, y la elipsis denota otras posibles variables de estado como el número de partículas N y la entropía S. Si el espacio de estado es bidimensional, como en el ejemplo anterior, puede visualizarse como un gráfico tridimensional (una superficie en un espacio tridimensional). Sin embargo, las etiquetas de los ejes no son únicas (ya que en este caso hay más de tres variables de estado) y solo se necesitan dos variables independientes para definir el estado.

Cuando un sistema cambia de estado continuamente, traza un "camino" en el espacio de estado. La ruta se puede especificar anotando los valores de los parámetros de estado a medida que el sistema traza la ruta, ya sea en función del tiempo o de alguna otra variable externa. Por ejemplo, tener la presión P(t) y el volumen V(t) como funciones de tiempo a partir de tiempo t0 a t1 especificará una ruta en un espacio de estado bidimensional. Cualquier función del tiempo puede entonces ser integrada sobre el camino. Por ejemplo, para calcular el trabajo realizado por el sistema desde el momento t0 hasta el momento t 1, se calcula 
  
    
      
        W
        (
        
          t
          
            0
          
        
        ,
        
          t
          
            1
          
        
        )
        =
        
          ∫
          
            0
          
          
            1
          
        
        P
        
        d
        V
        =
        
          ∫
          
            
              t
              
                0
              
            
          
          
            
              t
              
                1
              
            
          
        
        P
        (
        t
        )
        
          
            
              d
              V
              (
              t
              )
            
            
              d
              t
            
          
        
        
        d
        t
      
    
    {\textstyle W(t_{0},t_{1})=\int _{0}^{1}P\,dV=\int _{t_{0}}^{t_{1}}P(t){\frac {dV(t)}{dt}}\,dt}
  
. Para calcular el trabajo W en la integral anterior, las funciones P(t) y V(' 't) debe conocerse en cada momento t en toda la ruta. Por el contrario, una función de estado solo depende de los valores de los parámetros del sistema en los puntos finales de la ruta. Por ejemplo, la siguiente ecuación se puede usar para calcular el trabajo más la integral de V dP sobre el camino:

  
    
      
        
          
            
              
                Φ
                (
                
                  t
                  
                    0
                  
                
                ,
                
                  t
                  
                    1
                  
                
                )
              
              
                
                =
                
                  ∫
                  
                    
                      t
                      
                        0
                      
                    
                  
                  
                    
                      t
                      
                        1
                      
                    
                  
                
                P
                
                  
                    
                      d
                      V
                    
                    
                      d
                      t
                    
                  
                
                
                d
                t
                +
                
                  ∫
                  
                    
                      t
                      
                        0
                      
                    
                  
                  
                    
                      t
                      
                        1
                      
                    
                  
                
                V
                
                  
                    
                      d
                      P
                    
                    
                      d
                      t
                    
                  
                
                
                d
                t
              
            
            
              
              
                
                =
                
                  ∫
                  
                    
                      t
                      
                        0
                      
                    
                  
                  
                    
                      t
                      
                        1
                      
                    
                  
                
                
                  
                    
                      d
                      (
                      P
                      V
                      )
                    
                    
                      d
                      t
                    
                  
                
                
                d
                t
                =
                P
                (
                
                  t
                  
                    1
                  
                
                )
                V
                (
                
                  t
                  
                    1
                  
                
                )
                −
                P
                (
                
                  t
                  
                    0
                  
                
                )
                V
                (
                
                  t
                  
                    0
                  
                
                )
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\Phi (t_{0},t_{1})&=\int _{t_{0}}^{t_{1}}P{\frac {dV}{dt}}\,dt+\int _{t_{0}}^{t_{1}}V{\frac {dP}{dt}}\,dt\\&=\int _{t_{0}}^{t_{1}}{\frac {d(PV)}{dt}}\,dt=P(t_{1})V(t_{1})-P(t_{0})V(t_{0}).\end{aligned}}}
  

En la ecuación, el integrando se puede expresar como el diferencial exacto de la función P(t)V(t). Por lo tanto, la integral se puede expresar como la diferencia en el valor de P(t)V(t) en los puntos finales de la integración. El producto PV es por lo tanto una función de estado del sistema.

La notación d se utilizará para un diferencial exacto. En otras palabras, la integral de dΦ será igual a Φ(t1) − Φ(t0). El símbolo δ se reservará para una diferencial inexacta, que no puede integrarse sin un conocimiento completo de la trayectoria. Por ejemplo, δW = PdV se utilizará para denotar un incremento infinitesimal de trabajo.

Las funciones de estado representan cantidades o propiedades de un sistema termodinámico, mientras que las funciones de no estado representan un proceso durante el cual las funciones de estado cambian. Por ejemplo, la función de estado PV es proporcional a la energía interna de un gas ideal, pero el trabajo W es la cantidad de energía transferida cuando el sistema realiza trabajo. La energía interna es identificable; es una forma particular de energía. El trabajo es la cantidad de energía que ha cambiado su forma o ubicación.

## Funciones extensivas e intensivas

Algunas de estas variables de estado son magnitudes de intensividad, como la temperatura y la presión. Esto significa que no dependen de la extensión del sistema, es decir, de la cantidad de materia en el sistema.

Ejemplo: si mezclamos dos botellas que contienen 1 litro de agua cada una, a una temperatura de 20 °C, la temperatura final será de 20 °C y no de 40 °C. Lo mismo ocurriría con la presión, que tampoco tiene la propiedad de aditividad. En cambio, el volumen final V será igual a 2 l. El volumen no es una cantidad intensiva, sino una cantidad extensiva que depende de la extensión del sistema y, por tanto, de la cantidad de materia. La cantidad de materia, n, tiene en sí misma esta propiedad de aditividad y es por tanto también una cantidad extensiva.

Las variables intensivas son importantes para definir el estado de equilibrio de un sistema físico-químico. El equilibrio se alcanza cuando el valor de las variables intensivas es homogéneo en todo el sistema y no varía con el tiempo.

Nota: En el caso de sistemas químicos con varias especies químicas reaccionando, hay que tener en cuenta otra variable. Se trata de la variable de composición ξ que se utiliza para determinar la composición del sistema químico para un progreso de reacción dado.

## Lista de funciones de estado

Las siguientes se consideran funciones de estado en termodinámica:

- Masa

- Energía (E)

- Entalpía (H)

- Energía interna (U)

- Energía libre de Gibbs (G)

- Energía libre de Helmholtz (F)

- Exergía (B)

- Entropía (S)

- Presión (P)

- Temperatura (T)

- Volumen (V)

- Composición química

- Altitud de presión

- Volumen específico (v) o su recíproco densidad (ρ)

- Número de partículas (ni)

## Variables de estado

Algunas variables de estado de un sistema en equilibrio son:[1]​

- la energía interna

- la presión

- la temperatura

- el volumen

- la entalpía

- la entropía

- la densidad

- la polarización

- la energía libre de Gibbs

## Clasificación

Dentro de las variables de estado se pueden establecer dos tipos de subdivisiones básicas: por un lado en externas e internas, y por otro en
variables de estado intensivas y extensivas. Los potenciales termodinámicos se caracterizan por estas últimas.

Las variables de estado extensivas son variables de estado cuya medida escala con el tamaño del sistema. Las variables de estado intensivas son variables de estado cuya medida no depende del tamaño del sistema. Si, por ejemplo, un sistema se divide en dos partes idénticas en todos los aspectos, cada variable de estado extensiva adquiere la mitad de valor; si se combinan dos sistemas idénticos en cuanto a la variable de estado, adquieren el doble de valor. Las variables de estado intensivas no cambian su valor como resultado.[3]​

Ejemplo: La cantidad de líquido en un vaso es una cantidad extensiva, ya que dos vasos contienen el doble de líquido. La temperatura del líquido, en cambio, es una cantidad intensiva, ya que dos vasos no están el doble de calientes que un solo vaso.

## Variables de estado extensivas

## Funciones de estado o potenciales termodinámicos

Los potenciales termodinámicos energía interna, energía libre, entalpía y energía de Gibbs así como el gran potencial canónico son variables de estado extensivas. Describen completamente el sistema termodinámico en términos de su contenido de información.

Los potenciales termodinámicos se miden en relación con un punto cero determinado arbitrariamente, como el estado inicial. El cambio en la energía interna 
  
    
      
        
          U
        
      
    
    {\displaystyle \textstyle U}
  
 con las variables naturales entropía 
  
    
      
        
          S
        
      
    
    {\displaystyle \textstyle S}
  
 y volumen 
  
    
      
        
          V
        
      
    
    {\displaystyle \textstyle V}
  
 corresponde entonces al calor 
  
    
      
        
          Q
        
      
    
    {\displaystyle \textstyle Q}
  
 y trabajo 
  
    
      
        
          W
        
      
    
    {\displaystyle \textstyle W}
  
 suministrados:

  
    
      
        
          Δ
          U
          (
          S
          ,
          V
          )
          =
          Q
          +
          W
        
      
    
    {\displaystyle \textstyle \Delta U(S,V)=Q+W}
  

o expresado como una diferencial completa:

  
    
      
        
          
            d
          
          U
          (
          S
          ,
          V
          )
          =
          T
          
          
            d
          
          S
          −
          p
          
          
            d
          
          V
        
      
    
    {\displaystyle \textstyle \mathrm {d} U(S,V)=T\,\mathrm {d} S-p\,\mathrm {d} V}
  
.

Se diferencian en sus variables naturales, que a su vez son variables de estado y pueden convertirse entre sí mediante la transformación de Legendre. Esto da como resultado, por ejemplo, la entalpía 
  
    
      
        
          H
        
      
    
    {\displaystyle \textstyle H}
  
 con sus variables naturales entropía 
  
    
      
        
          S
        
      
    
    {\displaystyle \textstyle S}
  
 y presión 
  
    
      
        
          p
        
      
    
    {\displaystyle \textstyle p}
  
 como:

  
    
      
        
          H
          (
          S
          ,
          p
          )
          =
          U
          +
          p
          V
        
      
    
    {\displaystyle \textstyle H(S,p)=U+pV}
  

y su diferencial completa es:

  
    
      
        
          
            d
          
          H
          (
          S
          ,
          p
          )
          =
          T
          
          
            d
          
          S
          +
          V
          
          
            d
          
          p
        
      
    
    {\displaystyle \textstyle \mathrm {d} H(S,p)=T\,\mathrm {d} S+V\,\mathrm {d} p}
  
.

## Variables de estado extensivas

Al considerar los potenciales termodinámicos, se incluyen como variables naturales las siguientes variables extensivas de estado: volumen, entropía y número de partículas o cantidad de sustancia. En los sistemas dinámicos o influidos por campos que almacenan energía, los flujos son también variables de estado extensivas.

## Variables intensivas de estado

Al considerar los potenciales termodinámicos, se incluyen como variables naturales las siguientes variables intensivas de estado: presión, temperatura (absoluta) y potencial químico. El cambio de una variable intensiva provoca siempre un cambio del equilibrio termodinámico. En los sistemas dinámicos o influidos por campos que almacenan energía, las velocidades y las intensidades de campo son también variables intensivas de estado.

## Combinaciones

Las combinaciones de variables de estado intensivas de un mismo estado son a su vez variables de estado intensivas. Las que constan de una cantidad extensiva y otra intensiva son extensivas. Tales combinaciones se producen como diferencia de potenciales termodinámicos. En este contexto, una cantidad siempre se multiplica por su cantidad conjugada. Un ejemplo de ello es el trabajo de desplazamiento 
  
    
      
        
          H
          −
          U
          =
          p
          ,
          V
        
      
    
    {\displaystyle \textstyle H-U=p,V}
  
. Representa la diferencia entre la entalpía y la energía interna. Aunque lleva el nombre de un ...trabajo, a diferencia de otros ...trabajos no es una variable de proceso.

## Ejemplo de magnitud que no es función de estado

El trabajo de expansión termodinámico viene dado por la expresión δW=pext ·dV o lo que es lo mismo W= ∫ pext ·dV  detalles en Trabajo (física) 

Véase que usamos la notación δ en lugar de dW precisamente para distinguir que el trabajo no es función de estado, esto se debe a que dicha magnitud no depende sólo de los puntos final e inicial sino también de la trayectoria.

Enfrentando la presión y el volumen de forma gráfica, el trabajo, por definición de integral, viene dado por el área que forma la curva, si vamos variando la línea que une el punto inicial y el final, es decir, la trayectoria, obtenemos valores de W distintos ya que el área podría ser más grande o más pequeña según la curva trazada.

Se deduce entonces que el trabajo depende de la trayectoria y por este motivo no es función de estado.

## Ecuación de estado

Cada sistema o tipo de "substancia" se caracteriza por una ecuación de estado o ecuación constitutiva que relaciona algunas de las variables de estado entre sí, ya que, como se ha dicho, los sistemas en equilibrio termodinámico tienen un número finito de grados de libertad de acuerdo con la regla de las fases de Gibbs.[4]​

## Caracterización matemática

El conjunto de estados de equilibrio puede representarse como una variedad diferenciable 
  
    
      
        
          
            E
          
        
      
    
    {\displaystyle {\mathcal {E}}}
  
 de dimensión n (espacio de estados de equilibrio). El espacio de estados tendrá dimensión igual a las variables de estado menos las ecuaciones de estado. Por ejemplo para un gas ideal el espacio de estados tendrá dimensión 3-1=2, y podemos coger 2 variables independientes, que pueden ser la presión y el volumen.

Una función de estado es cualquier magnitud definida como una función real sobre dicha variedad: 
  
    
      
        M
        :
        
          
            E
          
        
        →
        
          R
        
      
    
    {\displaystyle M:{\mathcal {E}}\to \mathbb {R} }
  
, es decir, hablaremos de funciones de estado en un espacio determinado.[5]​ En el caso anterior, en el espacio P-V.

Nótese que el calor intercambiado, por ejemplo no admite una representación así, ya que en general será una función de la curva que siga el proceso 
  
    
      
        C
        ⊂
        
          
            E
          
        
      
    
    {\displaystyle C\subset {\mathcal {E}}}
  
. 

- En ese sentido las "diferenciales exactas" se corresponde con 1-formas exactas definidas sobre el espacio cotagente a la variedad diferenciable  
  
    
      
        
          
            E
          
        
      
    
    {\displaystyle {\mathcal {E}}}
  
, mientras que las "diferenciales inexactas" se corresponde con una 1-forma que no es exacta.

- La integral de 1-forma no exacta en general dependerá del camino a diferencia de lo que sucede con las 1-formas exactas.

- Nótese que en la terminología de formas diferenciales las variables de estado son precisamente las 0-formas definidas sobre el espacio de estados de equilibrio.
Dado un conjunto de más de n funciones de estado, no todas pueden ser independientes, por lo que una función de estado es una relación funcional entre ellas. Por el teorema de la función implícita un conjunto de m > n funciones de estado diferenciables que satisfacen la ecuación constitutiva pueden ser convertidas en una parametrización local del espacio de estados 
  
    
      
        
          
            E
          
        
      
    
    {\displaystyle {\mathcal {E}}}
  
.

## Véase también

- Ecuación de estado

- Variable de estado (sistema dinámico)

- Potencial termodinámico

- Propiedad de Márkov

- Relaciones de Maxwell

- Campo vectorial conservativo

## Referencias

- ↑ a b Callen, Herbert B. (1985). Thermodynamics and an Introduction to Thermostatistics. Wiley & Sons. ISBN 978-0-471-86256-7.

- ↑ Gibbs, 1873

- ↑ Günter Cerbe, Gernot Wilhelms: Technische Thermodynamik: Theoretische Grundlagen und praktische Anwendungen. (Termodinámica técnica: fundamentos teóricos y aplicaciones prácticas) Munich 2021, ISBN 978-3-446-46519-0, p. 56 (en alemán)

- ↑ Mandl, F. (May 1988). Statistical physics (2nd ed.). Wiley & Sons. ISBN 978-0-471-91533-1.

- ↑ L. T. Klauder. In: American Journal of Physics. Band 36, Nr. 6, 1968, S. 556–557, doi:10.1119/1.1974977

## Bibliografía

- Walter Greiner, Ludwig Neise; et Horst Stöcker, Thermodynamics and statistical mechanics, New York, Springer-Verlag, coll. « Classical theoretical physics », 1995, 463 p. (ISBN 978-0-387-94299-5 et 978-3-540-94299-3, OCLC 30814519, lire en ligne [archive]), p. 25-32

- Paul Arnaud, Cours de chimie physique, Paris, Dunod, 1993, 529 p. (ISBN 978-2-10-001640-2, OCLC 2100016407).

- Peter Atkins et Julio De Paula (trad. de l'anglais par Jean Toullec et Monique Mottet), Chimie Physique, Bruxelles, De Boeck, 2013, 4e éd., 973 p. (ISBN 978-2-8041-6651-9, BNF 43642948, lire en ligne [archive]), p. 47.

- Callen, Herbert B. (1985). Thermodynamics and an Introduction to Thermostatistics. Wiley & Sons. ISBN 978-0-471-86256-7. 

- Gibbs, Josiah Willard (1873). «Graphical Methods in the Thermodynamics of Fluids». Transactions of the Connecticut Academy II  – vía WikiSource. 

- Mandl, F. (May 1988). Statistical physics (2nd edición). Wiley & Sons. ISBN 978-0-471-91533-1. 

## Enlaces externos

- 

-  Wikimedia Commons alberga una categoría multimedia sobre Función de estado.
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q230937

-  Multimedia: State functions / Q230937

- Identificadores

- GND: 4068159-2

- Ontologías

- Número IEV: 113-04-09

-  Datos: Q230937

-  Multimedia: State functions / Q230937

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.