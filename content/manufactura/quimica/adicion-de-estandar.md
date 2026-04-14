---
title: "Adición de estándar"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Adición de estándar
    
    
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
  
  
    
      
        
          
            
              
## Adición de estándar

            
            
            
              
                

              

              

El método de adición estándar es un tipo de enfoque de análisis cuantitativo que se usa a menudo en química analítica, en el que el estándar se agrega directamente a las alícuotas de la muestra analizada. Este método se usa en situaciones donde la matriz de muestra también contribuye a la señal analítica, una situación conocida como el efecto de matriz, lo que hace que sea imposible comparar la señal analítica entre muestra y estándar utilizando el enfoque tradicional de curva de calibración.[1]​ 

## Aplicaciones

La adición estándar se usa con frecuencia en el análisis químico instrumental, como la espectroscopia de absorción atómica y la cromatografía de gases.[2]​ 

Supongamos que la concentración de plata en muestras de residuos fotográficos se determina mediante espectrometría de absorción atómica. Usando el método de la curva de calibración, un analista podría calibrar el espectrómetro con algunas soluciones acuosas de una sal de plata pura y utilizar el gráfico de calibración resultante en la determinación de la plata en las muestras de prueba. Sin embargo, este método solo es válido si una solución acuosa pura de plata y una muestra de desechos fotográficos que contienen la misma concentración de plata dan los mismos valores de absorbancia. En otras palabras, al usar soluciones puras para establecer el gráfico de calibración, se supone que no hay "efectos de matriz", es decir, no hay reducción o mejora de la señal de absorbancia de plata por parte de otros componentes. En muchas áreas de análisis, tal suposición es frecuentemente inválida. Los efectos de la matriz se producen incluso con métodos como la espectrometría de plasma, que tienen una reputación de estar relativamente libres de interferencias. El método de las adiciones estándar generalmente se sigue para eliminar los efectos de la matriz. Experimentalmente, se toman volúmenes iguales de la solución de la muestra, todos menos uno están "enriquecidos" por separado con cantidades conocidas y diferentes del analito, y todos se diluyen al mismo volumen. Las señales del instrumento se determinan para todas estas soluciones y se trazan los resultados. Como de costumbre, la señal se traza en el eje y; en este caso, el eje x se gradúa en términos de las cantidades de analito agregado (ya sea como un peso absoluto o como una concentración). La línea de regresión (no ponderada) se calcula de la manera normal, pero se proporciona espacio para que se extrapole al punto en el eje x en el que y = 0. Esta intersección negativa en el eje x corresponde a la cantidad de analito en la muestra de prueba. Este valor viene dado por b / a, la relación de la intersección y la pendiente de la línea de regresión. De manera similar, en la cromatografía de gases se utiliza el siguiente procedimiento: 

- Se registra el cromatograma de lo desconocido

- Se agrega una cantidad conocida del (los) analito(s) de interés

- Se analiza la muestra nuevamente en las mismas condiciones y se registra el cromatograma
A partir del aumento en el área del pico (o altura del pico), la concentración original se puede calcular por extrapolación. La respuesta del detector debe ser una función lineal de la concentración de analito y no producir ninguna señal (distinta del fondo) a una concentración cero del analito.

## Procedimiento

Un procedimiento típico consiste en preparar varias soluciones que contienen la misma cantidad de desconocido, pero diferentes cantidades de estándar. Por ejemplo, cinco matraces volumétricos de 25 mL se llenan cada uno con 10 mL de lo desconocido. Luego, el estándar se agrega en cantidades diferentes, como 0, 1, 2, 3 y 4 mL. Los matraces se diluyen entonces hasta la marca y se mezclan bien.

La idea de este procedimiento es que la concentración total del analito es la combinación de lo desconocido y el estándar, y que la concentración total varía linealmente. Si la respuesta de la señal es lineal en este rango de concentración, se genera una gráfica similar a la que se muestra arriba.

## Error[3]​

La intersección con x da la concentración de lo desconocido. Tenga en cuenta que este valor es la concentración diluida. En la sección de procedimiento anterior, se diluyeron 10 ml de desconocido a 25 ml. Es esta concentración diluida la que se encuentra en la intersección con x. Para encontrar la concentración original de lo desconocido, uno debe volver a calcular ese valor. El error en la intersección con x se calcula como se muestra a continuación. 

  
    
      
        
          s
          
            x
          
        
        =
        
          
            
              s
              
                y
              
            
            
              
                |
              
              m
              
                |
              
            
          
        
        
          
            
              
                1
                n
              
            
            +
            
              
                
                  
                    
                      
                        y
                        ¯
                      
                    
                  
                  
                    2
                  
                
                
                  
                    m
                    
                      2
                    
                  
                  ∑
                  
                    (
                    
                      x
                      
                        i
                      
                    
                    −
                    
                      
                        
                          x
                          ¯
                        
                      
                    
                    
                      )
                      
                        2
                      
                    
                  
                
              
            
          
        
      
    
    {\displaystyle s_{x}={\frac {s_{y}}{|m|}}{\sqrt {{\frac {1}{n}}+{\frac {{\bar {y}}^{2}}{m^{2}\sum {(x_{i}-{\bar {x}})^{2}}}}}}}
  

- 
  
    
      
        
          s
          
            y
          
        
      
    
    {\displaystyle s_{y}}
  
 es la desviación estándar en los residuos

  
    
      
        =
        
          
            
              
                ∑
                
                  
                    (
                    
                      y
                      
                        i
                      
                    
                    −
                    m
                    
                      x
                      
                        i
                      
                    
                    −
                    b
                    )
                  
                  
                    2
                  
                
              
              
                n
                −
                2
              
            
          
        
      
    
    {\displaystyle ={\sqrt {\frac {\sum {(y_{i}-mx_{i}-b)}^{2}}{n-2}}}}
  

- 
  
    
      
        m
      
    
    {\displaystyle m}
  
  es la pendiente de la recta

- 
  
    
      
        b
      
    
    {\displaystyle b}
  
  es el intercepto y de la recta

- 
  
    
      
        n
      
    
    {\displaystyle n}
  
  es el número de normas

- 
  
    
      
        
          
            
              y
              ¯
            
          
        
      
    
    {\displaystyle {\bar {y}}}
  
  es la medida promedio de los estándares.

- 
  
    
      
        
          x
          
            i
          
        
      
    
    {\displaystyle x_{i}}
  
  son las concentraciones de las normas

- 
  
    
      
        
          
            
              x
              ¯
            
          
        
      
    
    {\displaystyle {\bar {x}}}
  
  es la concentración media de los estándares.

## Véase también

- Dilución de isótopos

- Estándar interno

## Referencias

- ↑ Harris, Daniel C. (2003). 

- ↑ Bader, Morris (1980). «A systematic approach to standard addition methods in instrumental analysis». Journal of Chemical Education 57 (10): 703. Bibcode:1980JChEd..57..703B. doi:10.1021/ed057p703. 

- ↑ Bruce, Graham R. (June 1999). «Estimates of Precision in a Standard Addition Analysis». Journal of Chemical Education 76 (6): 805-807. Bibcode:1999JChEd..76..805B. doi:10.1021/ed076p805. 

## Bibliografía

- Harris, Daniel C. (2003). Quantitative Chemical Analysis 6th Edition. New York: W.H. Freeman. 
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q660819

-  Datos: Q660819

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.