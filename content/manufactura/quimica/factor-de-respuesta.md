---
title: "Factor de respuesta"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Factor de respuesta
    
    
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
  
  
    
      
        
          
            
              
## Factor de respuesta

            
            
            
              
                

              

              El factor de respuesta, generalmente en cromatografía y espectroscopia, es la relación entre una señal producida por un analito y la cantidad de analito que produce la señal. Idealmente, y para un cálculo fácil, esta relación es la unidad (uno). En escenarios del mundo real, a menudo este no es el caso.

## Expresión

El factor de respuesta  
  
    
      
        
          f
          
            i
          
        
      
    
    {\displaystyle f_{i}}
  
puede expresarse sobre una base molar, de volumen o de masa.[1]​ Donde la verdadera cantidad de muestra y estándar son iguales: 

  
    
      
        
          f
          
            i
          
        
        =
        
          
            
              A
              
                i
              
            
            
              A
              
                s
                t
              
            
          
        
        
          f
          
            s
            t
          
        
      
    
    {\displaystyle f_{i}={\frac {A_{i}}{A_{st}}}f_{st}}
  

donde A es la señal (por ejemplo, área de pico) y el subíndice i indica la muestra y el subíndice st indica el estándar.[2]​ Al factor de respuesta del estándar se le asigna un factor arbitrario, por ejemplo, 1 o 100. Factor de respuesta de la muestra / Factor de respuesta del estándar = RRF 

## Cromatografía

Una de las principales razones para utilizar los factores de respuesta es compensar la irreproducibilidad de las inyecciones manuales en un cromatógrafo de gases (GC). Los volúmenes de inyección para GC pueden ser de 1 microlitro (µL) o menos y son difíciles de reproducir. Las diferencias en el volumen de analito inyectado conducen a diferencias en las áreas de los picos en el cromatograma y cualquier resultado cuantitativo es sospechoso.

Para compensar este error, se agrega una cantidad conocida de un estándar interno (un segundo compuesto que no interfiere con el análisis del analito primario) a todas las soluciones (estándares y incógnitas). De esta manera, si los volúmenes de inyección (y, por lo tanto, las áreas de los picos) difieren ligeramente, la proporción de las áreas del analito y el estándar interno permanecerá constante de una ejecución a la siguiente.

Esta comparación de ejecuciones también se aplica a soluciones con diferentes concentraciones del analito. El área del estándar interno se convierte en el valor al que se hace referencia a todas las demás áreas. A continuación se muestra la derivación matemática y la aplicación de este método.

Considere un análisis de octano (C8H18) utilizando nonano (C9H20) como estándar interno. Los 3 cromatogramas a continuación son para 3 muestras diferentes. 

La cantidad de octano en cada muestra es diferente, pero la cantidad de nonano es la misma (en la práctica esto no es un requisito). Debido a la escala, las áreas del pico nonano parecen tener diferentes áreas, pero en realidad las áreas son idénticas. Por lo tanto, las cantidades relativas de octano en cada muestra aumentan en el orden de la mezcla 1 (menos) <mezcla 3 <mezcla 2 (más).

Se llega a esta conclusión porque la relación del área de octano a la de nonano es la menor en la mezcla 1 y la mayor cantidad en la mezcla 2. La mezcla 3 tiene una relación intermedia. Esta relación se puede escribir como 

En la cromatografía, el área de un pico es proporcional al número de moles (n) multiplicado por una constante de proporcionalidad (k), Área = k × n . El número de moles de compuesto es igual a la concentración (molaridad, M ) multiplicada por el volumen, n = MV . A partir de estas ecuaciones, se hace la siguiente derivación:

  
    
      
        
          
            
              A
              r
              e
              
                a
                
                  o
                  c
                  t
                  a
                  n
                  o
                
              
            
            
              A
              r
              e
              
                a
                
                  n
                  o
                  n
                  a
                  n
                  o
                
              
            
          
        
        =
        
          
            
              
                k
                
                  o
                  c
                  t
                  a
                  n
                  o
                
              
              ×
              
                M
                
                  o
                  c
                  t
                  a
                  n
                  o
                
              
              ×
              
                V
                
                  o
                  c
                  t
                  a
                  n
                  o
                
              
            
            
              
                k
                
                  n
                  o
                  n
                  a
                  n
                  o
                
              
              ×
              
                M
                
                  n
                  o
                  n
                  a
                  n
                  o
                
              
              ×
              
                V
                
                  n
                  o
                  n
                  a
                  n
                  o
                
              
            
          
        
      
    
    {\displaystyle {{Area_{octano}} \over {Area_{nonano}}}={{k_{octano}\times M_{octano}\times V_{octano}} \over {k_{nonano}\times M_{nonano}\times V_{nonano}}}}
  

Dado que ambos compuestos están en la misma solución y se inyectan juntos, los términos de volumen son iguales y se cancelan. La ecuación anterior se reorganiza para resolver la relación de las k. Esta relación se denomina factor de respuesta, F.

  
    
      
        F
        =
        
          
            
              k
              
                o
                c
                t
                a
                n
                o
              
            
            
              k
              
                n
                o
                n
                a
                n
                o
              
            
          
        
        =
        
          
            
              A
              r
              e
              
                a
                
                  o
                  c
                  t
                  a
                  n
                  o
                
              
              
                /
              
              
                M
                
                  o
                  c
                  t
                  a
                  n
                  o
                
              
            
            
              A
              r
              e
              
                a
                
                  n
                  o
                  n
                  a
                  n
                  o
                
              
              
                /
              
              
                M
                
                  n
                  o
                  n
                  a
                  n
                  o
                
              
            
          
        
      
    
    {\displaystyle F={k_{octano} \over k_{nonano}}={{Area_{octano}/M_{octano}} \over {Area_{nonano}/M_{nonano}}}}
  

El factor de respuesta, F, es igual a las razones de las k, que son constantes. Por lo tanto, F es constante. Lo que esto significa es que, independientemente de las cantidades de octano y nonano en solución, la proporción de las relaciones de área a concentración siempre dará una constante.

En la práctica, una solución que contiene cantidades conocidas de octano y nonano se inyecta en un GC y se calcula un factor de respuesta, F. Luego se inyecta una solución separada con una cantidad desconocida de octano y una cantidad conocida de nonano. El factor de respuesta se aplica a los datos de la segunda solución y se encuentra la concentración desconocida del octano. 

  
    
      
        
          
            
              (
              
                
                  
                    A
                    r
                    e
                    
                      a
                      
                        o
                        c
                        t
                        a
                        n
                        o
                      
                    
                    
                      /
                    
                    
                      M
                      
                        o
                        c
                        t
                        a
                        n
                        o
                      
                    
                  
                  
                    A
                    r
                    e
                    
                      a
                      
                        n
                        o
                        n
                        a
                        n
                        o
                      
                    
                    
                      /
                    
                    
                      M
                      
                        n
                        o
                        n
                        a
                        n
                        o
                      
                    
                  
                
              
              )
            
          
          
            1
          
        
        =
        F
        =
        
          
            
              (
              
                
                  
                    A
                    r
                    e
                    
                      a
                      
                        o
                        c
                        t
                        a
                        n
                        o
                      
                    
                    
                      /
                    
                    
                      M
                      
                        o
                        c
                        t
                        a
                        n
                        o
                      
                    
                  
                  
                    A
                    r
                    e
                    
                      a
                      
                        n
                        o
                        n
                        a
                        n
                        o
                      
                    
                    
                      /
                    
                    
                      M
                      
                        n
                        o
                        n
                        a
                        n
                        o
                      
                    
                  
                
              
              )
            
          
          
            2
          
        
      
    
    {\displaystyle {\left({{Area_{octano}/M_{octano}} \over {Area_{nonano}/M_{nonano}}}\right)}_{1}=F={\left({{Area_{octano}/M_{octano}} \over {Area_{nonano}/M_{nonano}}}\right)}_{2}}
  

Este ejemplo trata el análisis de octano y nonano, pero puede aplicarse a cualquiera de los dos compuestos. 

## Referencias

- ↑ Ramus TL; Hein SJ; Thomas LC (August 1987). «Determinations of polychlorinated biphenyl isomers by response factor calibration». J. Chromatogr. 404 (1): 155-62. PMID 3119645. doi:10.1016/S0021-9673(01)86846-1. 

- ↑ Orange Book. Compendium of Analytical Nomenclature. IUPAC. 

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q7315963

-  Datos: Q7315963

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.