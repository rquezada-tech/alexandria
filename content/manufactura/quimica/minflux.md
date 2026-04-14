---
title: "MINFLUX"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

MINFLUX
    
    
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
  
  
    
      
        
          
            
              
## MINFLUX

            
            
            
              
                

              

              

MINFLUX es un método de visualización por fluorescencia que brinda una resolución espacial de 1nm utilizando un mínimo flujo de fotones.[1]​ 

Esta es la máxima resolución que tiene sentido para un método óptico, ya que corresponde al tamaño de las fuentes de luz, en este caso, las moléculas fluorescentes. A diferencia de otros métodos de microscopía de superresolución, este método permite tener una alta resolución con un número muy bajo de fotones, evitando de esta forma el fotoblanqueo de los fluoróforos. Se ha logrado una superresolución microscópica de 1nm de precisión, resolviendo moléculas a 5nm de distancia con una cantidad de 350 fotones menos que las otras técnicas de nanoscopía.[2]​

Esta nueva metodología abre puertas para que este tipo de microscopía pueda competir con la microscopía electrónica, la cual brinda resolución espacial nanométrica pero impone condiciones muy desfavorables para observar organismos vivos. MINFLUX podría implementarse en un laboratorio convencional y el hecho de usar luz en vez de electrones energéticos, es conveniente para observar muestras biológicas.[3]​ 

## Antecedentes

Con el fin de obtener una resolución superior a la impuesta por el límite de difracción a través de la microscopía óptica, se han desarrollado varios métodos de fluorescencia de superresolución. Estos se basan en utilizar diferentes técnicas para generar la emisión de una sola molécula mientras su vecinas se encuentren «apagadas», pudiendo recoger así un conjunto de fotones de una molécula a la vez.
Los métodos dirigidos, como el STED, desarrollado por Stefan W. Hell y Jan Wichmann en 1994, utilizan dos haces de luz, uno con un máximo de intensidad en el centro (el que excitará a las moléculas fluorescentes) y otro con forma de anillo que tienen un mínimo de intensidad en el medio. La intensidad y longitud de onda de este último se ajustan de forma tal que las moléculas que estén iluminadas por él emitan en una longitud de onda que no se esté observando a través del proceso de emisión estimulada. A medida que este patrón se inyecta en la muestra, la posición del emisor siempre es conocida a través del dispositivo que controla la posición de los mínimos, por lo que se sabrá el lugar desde el cual se emiten los fotones registrados. Para formar una imagen con esta metodología, se necesita realizar un barrido de toda la muestra, recibiendo los fotones de las posiciones que se van excitando. Otro ejemplo es la microscopía de GSD, en la cual se aprovecha el tiempo que tarda el electrón en decaer del estado excitado al estado fundamental y se ilumina el fluoróforo con una alta intensidad para mantener a los electrones en estado de mayor energía evitando que emitan fluorescencia.
Por otro lado, se han desarrollado métodos estocásticos como STORM y PALM, que consisten en aprovechar la característica de algunos fluoróforos de poder ser «prendidos» y «apagados». Así, se apagan todas las moléculas fluorescentes de la muestra y luego se activan las moléculas de forma individual y aleatoria en el espacio. Se registran los fotones emitidos por estas moléculas con una cámara, que forman un patrón de difracción, del cual se realiza un ajuste y  se determina la posición del emisor a partir del centro del patrón. 
La resolución de estos métodos se ve restringida al número de fotones que pueden emitir las moléculas fluorescentes, pudiéndose lograr idealmente con una relación señal/fondo infinita una resolución de 5nm con 400 fotones (citar paper minflux). Esto es un problema ya que las moléculas fluorescentes emiten un número finito de fotones, debido al efecto de fotoblanqueo, por lo que no se puede aumentar la resolución infinitamente a costa de ellos. Además, estas técnicas de microscopía presentan grandes dificultades para realizar el rastreo (tracking) de moléculas, debido a que la metodología de PALM/STORM precisa que las moléculas estén fijas para poder realizar un ajuste espacial de la campana de difracción y con el método de STED si bien resultaría difícil realizar el seguimiento, de ser posible se perdería rápidamente a la molécula por el fotoblanqueamiento.
MINFLUX combina varios conceptos de las microscopía de fluorescencia de súper-resolución y aprovecha al máximo la información de cada fotón de fluorescencia para determinar la posición de una molécula, evitando así la necesidad de utilizar muchos fotones para una mejor resolución. Esto, a su vez, permite el seguimiento de moléculas por largos intervalos de tiempo.

## Metodología

## La idea

El concepto del funcionamiento de la técnica de MINFLUX puede entenderse a partir del planteo de un experimento hipotético en el cual se desea seguir la trayectoria de una molécula fluorescente utilizando un haz excitador con forma de rosca, con un mínimo de intensidad en su centro del orden de 1nm (tamaño de un fluoróforo). 
Si el haz se moviera por el plano focal, logrando enfocar siempre el cero de intensidad sobre la molécula, el dispositivo rastrearia a la molécula sin provocar una sola emisión del fluoróforo. Registrar un solo fotón sería suficiente para saber que la molécula no está en el 0 de intensidad. Claramente esto no es posible,  ya que no se puede conocer la posición de la molécula con anticipación y ubicarla en el centro en una sola toma, pero este experimento mental sugiere que el sondeo múltiple sobre una molécula con una zona de intensidad cero, debería reducir las emisiones requeridas para su localización. 
Así, se puede pensar a las emisiones de fluorescencia como el precio que se debe pagar por no conocer la posición de la molécula con exactitud y por lo tanto, cuanto más cerca esté el centro de la rosca de la posición de la molécula, menor será la cantidad de fotones que emitirá. 

## Localización de una molécula en 1D con dos exposiciones

La técnica para ubicar una molécula fluorescente en una dimensión precisa de un patrón de intensidad I(x) que dependa de la posición de forma conocida, con la condición de que I(0)=0 (es decir, que tenga un 0 de intensidad en su centro). Podrían utilizarse, por ejemplo, patrones parabólicos, gaussianos o sinusoidales. La metodología consiste en iluminar primero la zona donde se sabe que hay una sola molécula con el patrón de intensidad, de forma que la molécula recibirá una excitación de intensidad I0 y emitirá n0 fotones. Luego, el foco de luz se desplaza una distancia L y ahora la molécula recibirá una intensidad I1, y emitirá como consecuencia n1 fotones. 
Bajo estas condiciones, la probabilidad de registrar n0 fotones provenientes de la primera excitación, sobre un total de N=n0+n1 fotones detectados es 

  
    
      
        
          p
          
            0
          
        
        =
        
          
            
              n
              
                0
              
            
            
              
                n
                
                  0
                
              
              +
              
                n
                
                  1
                
              
            
          
        
      
    
    {\displaystyle p_{0}={\frac {n_{0}}{n_{0}+n_{1}}}}
  
. 
A su vez, esta probabilidad depende de las intensidades I0 e I1 con las que se excitó a la molécula y, por lo tanto, de su posición:

  
    
      
        
          p
          
            0
          
        
        (
        x
        )
        =
        
          
            
              
                I
                
                  0
                
              
              (
              x
              )
            
            
              
                I
                
                  0
                
              
              (
              x
              )
              +
              
                I
                
                  1
                
              
              (
              x
              )
            
          
        
      
    
    {\displaystyle p_{0}(x)={\frac {I_{0}(x)}{I_{0}(x)+I_{1}(x)}}}
  

De esta manera, midiendo la cantidad de fotones n0 y n1 provenientes de las diferentes emisiones, y calculando p0, se puede obtener a partir de éste la posición x más probable que resulta en obtener esa combinación de n0 y n1. 
La precisión de la localización depende del parámetro p0 y de su dependencia con x, y es óptima cuando la molécula se encuentra exactamente en el medio de los dos ceros de intensidad, por lo que cuanto menor es L, mayor será la precisión.
Por ejemplo, tomando una intensidad de luz parabólica 
  
    
      
        I
        (
        x
        )
        =
        A
        
          x
          
            2
          
        
      
    
    {\displaystyle I(x)=Ax^{2}}
  
, se tiene una probabilidad de 
  
    
      
        
          p
          
            0
          
        
        (
        x
        )
        =
        
          
            
              
                (
                
                  1
                  +
                  
                    
                      x
                      
                        L
                        
                          /
                        
                        2
                      
                    
                  
                
                )
              
              
                2
              
            
            
              2
              
                (
                
                  1
                  +
                  
                    
                      (
                      
                        
                          x
                          
                            L
                            
                              /
                            
                            2
                          
                        
                      
                      )
                    
                    
                      2
                    
                  
                
                )
              
            
          
        
      
    
    {\displaystyle p_{0}(x)={\frac {\left(1+{\frac {x}{L/2}}\right)^{2}}{2\left(1+\left({\frac {x}{L/2}}\right)^{2}\right)}}}
  
. En este caso la varianza en función de x queda determinada por 
  
    
      
        σ
        (
        x
        )
        =
        
          
            L
            
              4
              
                
                  N
                
              
            
          
        
        
          [
          
            1
            +
            
              
                (
                
                  
                    x
                    
                      L
                      
                        /
                      
                      2
                    
                  
                
                )
              
              
                2
              
            
          
          ]
        
      
    
    {\displaystyle \sigma (x)={\frac {L}{4{\sqrt {N}}}}\left[1+\left({\frac {x}{L/2}}\right)^{2}\right]}
  
.

## Dispositivo experimental y localización en dos dimensiones

Para obtener información bidimensional sobre la localización de una partícula, se utiliza el mismo concepto que en una dimensión y, en este caso, un haz de luz con forma de rosca con un cero de intensidad en el centro junto con una detección confocal para eliminar el fondo.[4]​
Se utiliza un láser con la longitud de onda adecuada para la excitación del fluoróforo, cuyo haz atraviesa un modulador de amplitud y un plato retardador con el que se desfasan las ondas produciendo la interferencia destructiva en el centro. De esta manera se forma la dona de intensidad en el plano focal de la lente objetivo. 
Los fotones emitidos por la molécula fluorescente son enviados al detector mediante un espejo dicroico (DM) que transmite las longitudes de onda del láser incidente y refleja la longitud de onda de los fotones emitidos, luego atraviesan un filtro de emisión pasa banda (BPF) y finalmente se coloca un pin-hole confocal. 
Para el realizar el movimiento del cero de intensidad se utiliza un deflector de haz piezoeléctrico que permite movimientos en menos de 5μs con una precisión menor a 1nm.

Para la localización bidimensional se ilumina la muestra con el haz, enfocando el cero de la rosca en al menos 3 posiciones formando un triángulo equilátero inscripto en una circunferencia. Se observó además que una cuarta posición en el centro del círculo mejora la precisión de la medición. Para cada una de esas posiciones se registra el número de fotones emitidos por la molécula y luego se calcula la posición más probable que podría dar esa combinación de fotones. Los parámetros de la medición son el diámetro L de la circunferencia y la cantidad de fotones a detectar, aumentando la intensidad del haz. 

## Precisión del método

Para determinar la precisión de la localización que se puede obtener con este método, se realizaron mediciones con una única molécula fluorescente (ATTO 647N). Se desplazó la misma con un piezoeléctrico, conociendo su posición con una precisión nanométrica, dentro de un círculo de 100 nm de diámetro, se calculó su posición con el método MINFLUX, y se realizó una comparación entre esos valores según el lugar del círculo. 
Para un total de 500 fotones, se obtuvo que cerca del centro de la circunferencia, el error en la localización es de 1nm. Cuanto más lejos del centro se encuentra la molécula, el error aumenta, sin superar, sin embargo, los 9nm. Además, se obtuvo que el error disminuye con un mayor número de fotones y un menor diámetro de la circunferencia. Se observó también que es preferible reducir la separación de las posiciones del láser L en vez de aumentar el número de fotones detectados para mejorar la precisión en la localización. 
Comparando este método con PALM/STORM utilizando una cámara ideal, en la que la relación señal/fondo es infinita, se obtuvo que para alcanzar una precisión de 5nm se necesitan 500 fotones para las técnicas estocásticas, mientras que con MINFLUX, utilizando un L=50nm, se necesitan 27. 

## Aplicaciones

El método de MINFLUX tiene varias aplicaciones, ya sea para la distinción entre moléculas y la localización a escala nanométrica, como para el seguimiento de moléculas fluorescentes en recorridos nanométricos o micrométricos. 
En el caso de la localización nanoscópica se deben utilizar moléculas fluorescentes que puedan activarse o desactivarse con el fin de lograr que solo una de las moléculas que se encuentre en el rango de detección esté activada. En el caso de detectarse más de una, los datos serán descartados. De esta forma se adquieren los fotones correspondientes a cada posición del cero de intensidad y se estima la posición de la molécula.
De la misma manera pueden realizarse seguimientos de moléculas con trayectorias de pocos nanómetros de forma que  siempre se encuentren dentro del área de observación.
Si se quiere realizar un seguimiento con trayectorias de orden micrométrico se utiliza un programa en que al momento en que la molécula se aleja una cierta distancia de r0, la circunferencia formada por los ceros de intensidad se desplaza iterativamente a la última posición estimada de la molécula, manteniendo la molécula cercana a r0.

## Nanoscopía

Se utilizaron ADN origamis inmovilizados, separados a una distancia de 11nm y se los etiquetó con fluoróforos Alexa Fluor 647. Para comenzar la medición y ubicar al ADN origami, primero se utilizó el método PALM/STORM. Luego, se mantuvieron (en general) todas las moléculas apagadas excepto una y se realizaron ciclos de localización a través del método MINFLUX un L=70nm.
Dado que el encendido y apagado de las moléculas es estocástico, se realiza un análisis posterior en el que se filtra a las mediciones que corresponden a más de una molécula. Esto puede realizarse observando el número total de fotones, que va a ser mayor si hay más de una molécula encendida. Se obtuvo un un mapa de localizaciones, en el que pueden distinguirse con claridad las moléculas que se encuentra a 11nm de distancia.
Comparando con la imagen que se obtendría con los métodos PALM/STORM se ve que en dicho caso no podrían distinguirse una molécula de otra y la precisión de localización resultaría σ = 5,4 nm. En cambio para, MINFLUX si se realiza una imagen de intensidades contando la cantidad de fotones en cada sector, se obtiene una imagen más clara donde se distinguen las distintas molécula y la precisión de la localización resulta en promedio de 2,1 nm.[5]​

## Seguimiento de moléculas

Se realizó seguimiento de subunidades de proteína ribosomal 30S fusionada con una proteína fluorescente fotoconvertible mEos2 en una Escherichia coli viva. Al comienzo estaban todas las proteínas apagadas y se las fueron prendiendo de a una para realizar las mediciones. Para la medición, se utilizó la metodología descripta para la localización en 2D, y se utilizó un algoritmo que rápidamente calculaba la posición de la molécula a partir de los fotones emitidos y re-ubicaba el centro del nuevo ciclo de 4 posiciones en ese lugar. Así el campo de visión mantenía en gran medida centrada la molécula.

El seguimiento se realizó verificando que:

- Las proteínas se encontraban en el campo de visión (utilizando por ej PALM/STORM).

- Que el ciclo que el haz en forma de dona realiza sobre las 4 posiciones fuera lo suficientemente rápido como para que el movimiento de la molécula no afectará la medición.[6]​

- El algoritmo que se encargaba de reposicionar el campo de visión lo hiciera lo suficientemente rápido para no perder a la molécula.
Se iluminó la muestra con el fin de encender una molécula y realizar el seguimiento, cuando ésta se apagaba se, volvió a iluminar para encender otra, de esta forma se realizó un mapa con 77 trayectoria realizadas con diferentes subunidades de proteína. Se observó que siempre la cantidad de fotones que se emitía a partir de la excitación en el centro de la circunferencia era pequeña, lo que indica que la misma estuvo siempre bien centrada durante el rastreo.[7]​

## Referencias

- ↑ Francisco Balzarotti, Yvan Eilers, Klaus C. Gwosch, Arvid H. Gynnå, Volker Westphal, Fernando D. Stefani, Johan Elf, Stefan W. Hell. «Nanometer resolution imaging and tracking of fluorescent molecules with minimal photon fluxes». Science. 

- ↑ Pool, Rebecca. «Nanometre imaging with fluorescence microscope». 

- ↑ «Logran la máxima resolución en microscopios de fluorescencia». 

- ↑ Yvan Eilersa, Haisen Taa Klaus C. Gwoscha , Francisco Balzarottia , and Stefan W. Hella. «MINFLUX monitors rapid molecular jumps with superior spatiotemporal resolution». Proceedings of the National Academy of Sciences. doi:10.1073/pnas.1801672115. 

- ↑ «New super-resolution microscope combines Nobel-winning technologies». 

- ↑ F. Balzarotti. «Sharpest Light Microscope Ever». Wiley Online Library. 

- ↑ «Fluorescence microscopy: It cannot get any sharper!». Max-Planck-Gesellschaft. 

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q56377936

-  Datos: Q56377936

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.