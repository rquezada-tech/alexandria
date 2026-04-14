---
title: "Espectroscopía de absorción óptica diferencial"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Espectroscopía de absorción óptica diferencial
    
    
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
  
  
    
      
        
          
            
              
## Espectroscopía de absorción óptica diferencial

            
            
            
              
                

              

              En química atmosférica, la espectroscopía de absorción óptica diferencial (DOAS, del inglés differential optical absorption spectroscopy) se utiliza para medir concentraciones de gases traza. Cuando se combina con espectrómetros ópticos básicos, como prismas o rejillas de difracción, y plataformas de observación terrestres automatizadas, lo que tenemos es un medio barato y poderoso para la medición de especies de gases traza como el ozono y el dióxido de nitrógeno. Las configuraciones típicas permiten límites de detección correspondientes a profundidades ópticas de 0,0001 a lo largo de trayectos de luz de hasta típicamente 15 km y, por lo tanto, permiten la detección también de absorbentes débiles, como vapor de agua, ácido nitroso, formaldehído, tetraoxígeno, óxido de yodo, óxido de bromo y óxido de cloro. 

## Teoría

Los instrumentos DOAS a menudo se dividen en dos grupos principales: pasivos y activos. El sistema DOAS activo, como los sistemas de recorrido largo (LP) y los sistemas DOAS de cavidad mejorada (CE), tienen su propia fuente de luz, mientras que los pasivos utilizan el sol como fuente de luz, por ejemplo, MAX (Multi-axial) -DOAS. Además, la luna se puede utilizar para mediciones DOAS nocturnas, pero aquí, por lo general, es necesario realizar mediciones de luz directa en lugar de mediciones de luz dispersa, como es el caso de los sistemas DOAS pasivos como el MAX-DOAS. 

El cambio en la intensidad de un haz de radiación a medida que viaja a través de un medio que no emite viene dado por la ley de Beers: 

  
    
      
        I
        =
        
          I
          
            0
          
        
        exp
        ⁡
        
          (
          
            
              ∑
              
                i
              
            
            ∫
            
              ρ
              
                i
              
            
            
              β
              
                i
              
            
            
            d
            s
          
          )
        
      
    
    {\displaystyle I=I_{0}\exp \left(\sum _{i}\int \rho _{i}\beta _{i}\,ds\right)}
  

donde I es la intensidad de la radiación, 
  
    
      
        ρ
      
    
    {\displaystyle \rho }
  
 es la densidad de la sustancia, 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 es la sección transversal de absorción y dispersión y s es el camino. El subíndice i denota diferentes especies, asumiendo que el medio está compuesto por múltiples sustancias. Se pueden realizar varias simplificaciones. El primero es sacar la sección transversal de absorción de la integral asumiendo que no cambia significativamente con la trayectoria, es decir, que es una constante. Dado que el método DOAS se usa para medir la densidad total de la columna, y no la densidad per se, el segundo es tomar la integral como un único parámetro al que llamamos densidad de columna: 

  
    
      
        σ
        =
        ∫
        ρ
        
        d
        s
      
    
    {\displaystyle \sigma =\int \rho \,ds}
  

La nueva ecuación considerablemente simplificada ahora se ve así: 

  
    
      
        I
        =
        
          I
          
            0
          
        
        exp
        ⁡
        
          (
          
            
              ∑
              
                i
              
            
            
              β
              
                i
              
            
            
              σ
              
                i
              
            
          
          )
        
        =
        
          I
          
            0
          
        
        
          ∏
          
            i
          
        
        
          e
          
            
              β
              
                i
              
            
            
              σ
              
                i
              
            
          
        
      
    
    {\displaystyle I=I_{0}\exp \left(\sum _{i}\beta _{i}\sigma _{i}\right)=I_{0}\prod _{i}e^{\beta _{i}\sigma _{i}}}
  

Si eso fuera todo, dado cualquier espectro con suficiente resolución y características espectrales, todas las especies podrían resolverse mediante una simple inversión algebraica. Las variantes de DOAS activas pueden utilizar el espectro de la propia fuente de luz como referencia. Desafortunadamente para las mediciones pasivas, donde estamos midiendo desde la parte inferior de la atmósfera y no desde la parte superior, no hay forma de determinar la intensidad inicial, I0. Más bien, lo que se hace es tomar la relación de dos mediciones con diferentes trayectorias a través de la atmósfera y así determinar la diferencia de profundidad óptica entre las dos columnas (como alternativa, se puede emplear un atlas solar, pero esto introduce otra fuente de error importante en el ajuste proceso, la función del instrumento en sí. Si el espectro de referencia en sí también se graba con la misma configuración, estos efectos eventualmente se cancelarán): 

  
    
      
        δ
        =
        ln
        ⁡
        
          (
          
            
              
                I
                
                  1
                
              
              
                I
                
                  2
                
              
            
          
          )
        
        =
        
          ∑
          
            i
          
        
        
          β
          
            i
          
        
        
          (
          
            
              σ
              
                i
                2
              
            
            −
            
              σ
              
                i
                1
              
            
          
          )
        
        =
        
          ∑
          
            i
          
        
        
          β
          
            i
          
        
        
        Δ
        
          σ
          
            i
          
        
      
    
    {\displaystyle \delta =\ln \left({\frac {I_{1}}{I_{2}}}\right)=\sum _{i}\beta _{i}\left(\sigma _{i2}-\sigma _{i1}\right)=\sum _{i}\beta _{i}\,\Delta \sigma _{i}}
  

Un componente significativo de un espectro medido a menudo viene dado por componentes continuos y de dispersión que tienen una variación suave con respecto a la longitud de onda. Dado que estos no proporcionan mucha información, el espectro se puede dividir en dos partes: 

  
    
      
        I
        =
        
          I
          
            0
          
        
        exp
        ⁡
        
          [
          
            
              ∑
              
                i
              
            
            
              (
              
                
                  β
                  
                    i
                  
                  
                    ∗
                  
                
                +
                
                  α
                  
                    i
                  
                
              
              )
            
            
              σ
              
                i
              
            
          
          ]
        
      
    
    {\displaystyle I=I_{0}\exp \left[\sum _{i}\left(\beta _{i}^{*}+\alpha _{i}\right)\sigma _{i}\right]}
  

dónde 
  
    
      
        α
      
    
    {\displaystyle \alpha }
  
 es el componente continuo del espectro y 
  
    
      
        
          β
          
            ∗
          
        
      
    
    {\displaystyle \beta ^{*}}
  
 es lo que queda y lo llamaremos sección transversal diferencial. Por lo tanto: 

  
    
      
        
          δ
          
            d
          
        
        +
        
          δ
          
            c
          
        
        =
        ln
        ⁡
        
          (
          
            
              
                I
                
                  1
                  d
                
              
              
                I
                
                  2
                  d
                
              
            
          
          )
        
        +
        ln
        ⁡
        
          (
          
            
              
                I
                
                  1
                  c
                
              
              
                I
                
                  2
                  c
                
              
            
          
          )
        
        =
        ∑
        
          (
          
            
              β
              
                i
              
              
                ∗
              
            
            +
            
              α
              
                i
              
            
          
          )
        
        
          (
          
            
              σ
              
                i
                2
              
            
            −
            
              σ
              
                i
                1
              
            
          
          )
        
        =
        
          ∑
          
            i
          
        
        
          β
          
            i
          
          
            ∗
          
        
        
          (
          
            
              σ
              
                i
                2
              
            
            −
            
              σ
              
                i
                1
              
            
          
          )
        
        +
        
          ∑
          
            i
          
        
        
          α
          
            i
          
        
        
          (
          
            
              σ
              
                i
                2
              
            
            −
            
              σ
              
                i
                1
              
            
          
          )
        
      
    
    {\displaystyle \delta _{d}+\delta _{c}=\ln \left({\frac {I_{1d}}{I_{2d}}}\right)+\ln \left({\frac {I_{1c}}{I_{2c}}}\right)=\sum \left(\beta _{i}^{*}+\alpha _{i}\right)\left(\sigma _{i2}-\sigma _{i1}\right)=\sum _{i}\beta _{i}^{*}\left(\sigma _{i2}-\sigma _{i1}\right)+\sum _{i}\alpha _{i}\left(\sigma _{i2}-\sigma _{i1}\right)}
  

donde llamamos 
  
    
      
        
          δ
          
            d
          
        
      
    
    {\displaystyle \delta _{d}}
  
 la profundidad óptica diferencial (DOD). Eliminar los componentes del continuo y agregar la dependencia de la longitud de onda produce una ecuación matricial con la que realizar la inversión: 

  
    
      
        
          δ
          
            d
          
        
        (
        λ
        )
        =
        
          ∑
          
            i
          
        
        
          β
          
            i
          
          
            ∗
          
        
        (
        λ
        )
        
        Δ
        
          σ
          
            i
          
        
      
    
    {\displaystyle \delta _{d}(\lambda )=\sum _{i}\beta _{i}^{*}(\lambda )\,\Delta \sigma _{i}}
  

Lo que esto significa es que antes de realizar la inversión, se deben eliminar los componentes del continuo tanto de la profundidad óptica como de las secciones transversales de las especies. Este es el "truco" importante del método DOAS. En la práctica, esto se hace simplemente ajustando un polinomio al espectro y luego restándolo. Obviamente, esto no producirá una igualdad exacta entre las profundidades ópticas medidas y las calculadas con las secciones transversales diferenciales, pero la diferencia suele ser pequeña. Alternativamente, un método común que se aplica para eliminar las estructuras de banda ancha de la densidad óptica son los filtros binomiales de paso alto. 

Además, a menos que la diferencia de trayectoria entre las dos mediciones pueda determinarse estrictamente y tenga algún significado físico (como la distancia del telescopio y el catadióptrico para un sistema DOAS de trayectoria larga), las cantidades recuperadas, 
  
    
      
        {
        Δ
        
          σ
          
            i
          
        
        }
      
    
    {\displaystyle \lbrace \Delta \sigma _{i}\rbrace }
  
 no tendrá sentido. La geometría de medición típica será la siguiente: el instrumento siempre apunta hacia arriba. Las mediciones se toman en dos momentos diferentes del día: una vez con el sol alto en el cielo y una vez cerca del horizonte. En ambos casos, la luz se dispersa en el instrumento antes de atravesar la troposfera, pero toma diferentes caminos a través de la estratosfera, como se muestra en la figura. 

Para lidiar con esto, introducimos una cantidad llamada factor de masa de aire que da la relación entre la densidad de la columna vertical (la observación se realiza mirando hacia arriba, con el sol en el cenit completo) y la densidad de la columna inclinada (el mismo ángulo de observación, el sol en algún otro ángulo): 

  
    
      
        
          σ
          
            i
            0
          
        
        =
        
          
            a
            m
            f
          
          
            i
          
        
        (
        θ
        )
        
          σ
          
            i
            θ
          
        
      
    
    {\displaystyle \sigma _{i0}=\mathrm {amf} _{i}(\theta )\sigma _{i\theta }}
  

donde amfi es el factor de masa de aire de la especie i, 
  
    
      
        
          σ
          
            i
            0
          
        
      
    
    {\displaystyle \sigma _{i0}}
  
 es la columna vertical y 
  
    
      
        
          σ
          
            i
            θ
          
        
      
    
    {\displaystyle \sigma _{i\theta }}
  
 es la columna inclinada con el sol en ángulo cenital 
  
    
      
        θ
      
    
    {\displaystyle \theta }
  
. Los factores de masa de aire se pueden determinar mediante cálculos de transferencia radiativa. 

Algo de álgebra muestra que la densidad de la columna vertical viene dada por: 

  
    
      
        
          σ
          
            i
            0
          
        
        =
        
          
            
              Δ
              
                σ
                
                  i
                
              
            
            
              
                
                  a
                  m
                  f
                
                
                  i
                
              
              (
              
                θ
                
                  2
                
              
              )
              −
              
                
                  a
                  m
                  f
                
                
                  i
                
              
              (
              
                θ
                
                  1
                
              
              )
            
          
        
      
    
    {\displaystyle \sigma _{i0}={\frac {\Delta \sigma _{i}}{\mathrm {amf} _{i}(\theta _{2})-\mathrm {amf} _{i}(\theta _{1})}}}
  

donde 
  
    
      
        
          θ
          
            1
          
        
      
    
    {\displaystyle \theta _{1}}
  
 es el ángulo en la primera geometría de medición y 
  
    
      
        
          θ
          
            2
          
        
      
    
    {\displaystyle \theta _{2}}
  
 es el ángulo en el segundo. Tenga en cuenta que con este método, la columna a lo largo de la ruta común se restará de nuestras mediciones y no se podrá recuperar. Lo que esto significa es que solo se puede recuperar la densidad de la columna en la estratosfera y se debe determinar el punto más bajo de dispersión entre las dos mediciones para determinar dónde comienza la columna. 

## Referencias

- Platt, U.; Stutz, J. (2008). Differential Optical Absorption Spectroscopy. 

- Richter, A. (1999). «DOAS zenith sky observations. 2. Seasonal variation of BrO over Bremen (53°N) 1994–1995» 32. pp. 83-99. 

- Eisinger, M., A. Richter, A. Ladstätter-Weißmayer, and J. P. Burrows (1997). «DOAS zenith sky observations: 1. BrO measurements over Bremen (53°N) 1993–1994» 26. pp. 93-108. 

## Enlaces externos

- Grupo DOAS en IUP, Bremen

- DOAS y grupo de química atmosférica en IUP, Heidelberg
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q1224441

-  Multimedia: Differential optical absorption spectroscopy / Q1224441

-  Datos: Q1224441

-  Multimedia: Differential optical absorption spectroscopy / Q1224441

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.