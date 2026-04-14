---
title: "UNIFAC"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

UNIFAC
    
    
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
  
  
    
      
        
          
            
              
## UNIFAC

            
            
            
              
                

              

              
El método UNIFAC (De sus siglas en inglés UNIQUAC Functional-group Activity Coefficients, no confundir con UNIQUAC)[1]​ es un sistema semi-empírico para la predicción de la actividad de no-electrolitos en mezclas no ideales. La UNIFAC utiliza los grupos funcionales presentes en las moléculas que componen la mezcla líquida para calcular los coeficientes de actividad. Utilizando interacciones para cada uno de los grupos funcionales presentes en las moléculas, así como algunos coeficientes de interacción binaria, se puede calcular la actividad de cada una de las soluciones. Esta información puede ser usada para obtener información sobre los equilibrios de líquidos, lo cual es útil en muchos cálculos termodinámicos, tales como el diseño de reactores químicos y  en la destilación.

El modelo UNIFAC fue publicado por primera vez en 1975 por Fredenslund, Jones y Prausnitz, un grupo de investigadores de ingeniería química de la Universidad de California. Posteriormente, ellos y otros autores han publicado una amplia gama de documentos de la FPNUL, ampliando las capacidades del modelo; esto ha sido mediante el desarrollo de nuevos parámetros del modelo de la FPNUL o la revisión de los ya existentes. UNIFAC es un intento de estos investigadores de proporcionar un modelo de equilibrio líquido flexible para un uso más amplio en las disciplinas de química, ingeniería química e ingeniería de procesos.

## Introducción

Un problema particular en el área de la termodinámica en estado líquido es la obtención de constantes termodinámicas fiables. Estas constantes son necesarias para la predicción exitosa del estado energía libre del sistema; sin esta información es imposible modelar las fases equilibrio del sistema.

Obtener estos datos de energía libre no es un problema trivial, y requiere experimentos cuidadosos, tales como calorimetría, para medir con éxito la energía del sistema. Incluso cuando se realiza este trabajo, no es factible intentar realizarlo para cada una de las posibles clases de productos químicos y sus mezclas binarias o superiores. Para aliviar este problema, se emplean modelos de predicción de energía libre, como UNIFAC, para predecir la energía del sistema basándose en unas pocas constantes medidas previamente.

Es posible calcular algunos de estos parámetros usando métodos Ab intio como COSMO-RS, pero los resultados deben ser tratados con precaución, porque las predicciones de ab initio pueden estar desactivadas. Del mismo modo, la UNIFAC puede estar apagada, y para ambos métodos es aconsejable validar experimentalmente las energías obtenidas de estos cálculos.

## Correlación de la UNIFAC

La correlación de la UNIFAC intenta romper el problema de predecir las interacciones entre moléculas describiendo las interacciones moleculares basándose en los grupos funcionales unidos a la molécula. Esto se hace para reducir el mero número de interacciones binarias que se necesitarían medir para predecir el estado del sistema.

## Actividad química

La actividad de los componentes de un sistema es un factor de corrección que tiene en cuenta las desviaciones de los sistemas reales con respecto a un solución ideal, que puede medirse mediante experimentos o estimarse a partir de modelos químicos (como UNIFAC). Añadiendo un factor de corrección, conocido como la actividad (
  
    
      
        
          a
          
            i
          
        
      
    
    {\displaystyle a_{i}}
  
, la actividad del componente ith) a la fracción en fase líquida de una mezcla líquida, se pueden explicar algunos de los efectos de la solución real. La actividad de una sustancia química real depende del estado termodinámico del sistema, es decir, de la temperatura y la presión.

Equipado con los coeficientes de actividad y un conocimiento de los constituyentes y sus cantidades relativas, se pueden calcular fenómenos como separación de fases y equilibrio vapor-líquido. La FPNUL intenta ser un modelo general para predecir con éxito los coeficientes de actividad.

## Parámetros del modelo

El modelo de la UNIFAC divide el coeficiente de actividad para cada especie en el sistema en dos componentes: un componente combinatorio 
  
    
      
        
          γ
          
            c
          
        
      
    
    {\displaystyle \gamma ^{c}}
  
 y un componente residual 
  
    
      
        
          γ
          
            r
          
        
      
    
    {\displaystyle \gamma ^{r}}
  
. Para la molécula 
  
    
      
        
          i
          
            
              t
              h
            
          
        
      
    
    {\displaystyle i^{\mathrm {th} }}
  
, los coeficientes de actividad se desglosan según la siguiente ecuación:

  
    
      
        ln
        ⁡
        
          γ
          
            i
          
        
        =
        ln
        ⁡
        
          γ
          
            i
          
          
            c
          
        
        +
        ln
        ⁡
        
          γ
          
            i
          
          
            r
          
        
      
    
    {\displaystyle \ln \gamma _{i}=\ln \gamma _{i}^{c}+\ln \gamma _{i}^{r}}
  

En el modelo UNIFAC, se requieren tres parámetros principales para determinar la actividad de cada molécula del sistema. En primer lugar, la superficie del grupo 
  
    
      
        Q
      
    
    {\displaystyle Q}
  
 y las contribuciones de volumen 
  
    
      
        R
      
    
    {\displaystyle R}
  
 obtenidas a partir de la Van der Waals de la superficie y los volúmenes. Estos parámetros dependen puramente de los grupos funcionales individuales de las moléculas del huésped. Finalmente está el parámetro de interacción binaria 
  
    
      
        
          τ
          
            i
            j
          
        
      
    
    {\displaystyle \tau _{ij}}
  
, que está relacionado con la energía de interacción 
  
    
      
        
          U
          
            i
          
        
      
    
    {\displaystyle U_{i}}
  
 de los pares moleculares (ecuación en la sección "residual"). Estos parámetros deben obtenerse bien mediante experimentos, bien mediante el ajuste de datos o bien mediante simulación molecular.

## Combinatoria

El componente combinatorio de la actividad es aportado por varios términos en su ecuación (abajo), y es el mismo que para el modelo UNIQUAC.

  
    
      
        ln
        ⁡
        
          γ
          
            i
          
          
            c
          
        
        =
        ln
        ⁡
        
          
            
              ϕ
              
                i
              
            
            
              x
              
                i
              
            
          
        
        +
        
          
            z
            2
          
        
        
          q
          
            i
          
        
        ln
        ⁡
        
          
            
              θ
              
                i
              
            
            
              ϕ
              
                i
              
            
          
        
        +
        
          L
          
            i
          
        
        −
        
          
            
              ϕ
              
                i
              
            
            
              x
              
                i
              
            
          
        
        
          
            ∑
            
              j
              =
              1
            
            
              n
            
          
          
            x
            
              j
            
          
          
            L
            
              j
            
          
        
      
    
    {\displaystyle \ln \gamma _{i}^{c}=\ln {\frac {\phi _{i}}{x_{i}}}+{\frac {z}{2}}q_{i}\ln {\frac {\theta _{i}}{\phi _{i}}}+L_{i}-{\frac {\phi _{i}}{x_{i}}}\displaystyle \sum _{j=1}^{n}x_{j}L_{j}}
  

  
    
      
        
          θ
          
            i
          
        
      
    
    {\displaystyle \theta _{i}}
  
 y 
  
    
      
        
          ϕ
          
            i
          
        
      
    
    {\displaystyle \phi _{i}}
  
 son el segmento ponderado molar y el área fraccional para la molécula 
  
    
      
        
          i
          
            
              t
              h
            
          
        
      
    
    {\displaystyle i^{\mathrm {th} }}
  
 en el sistema total y se definen por la siguiente ecuación; 
  
    
      
        
          L
          
            i
          
        
      
    
    {\displaystyle L_{i}}
  
 es un parámetro compuesto de 
  
    
      
        r
      
    
    {\displaystyle r}
  
, 
  
    
      
        z
      
    
    {\displaystyle z}
  
 y 
  
    
      
        q
      
    
    {\displaystyle q}
  
. 
  
    
      
        z
      
    
    {\displaystyle z}
  
 es el número de coordinación del sistema, pero se encuentra que el modelo es relativamente insensible a su valor y es frecuentemente citado como una constante que tiene el valor de 10.

  
    
      
        
          θ
          
            i
          
        
        =
        
          
            
              
                x
                
                  i
                
              
              
                q
                
                  i
                
              
            
            
              
                ∑
                
                  j
                  =
                  1
                
                
                  n
                
              
              
                x
                
                  j
                
              
              
                q
                
                  j
                
              
            
          
        
        
          
          
          ;
          
          
        
        
          ϕ
          
            i
          
        
        =
        
          
            
              
                x
                
                  i
                
              
              
                r
                
                  i
                
              
            
            
              
                ∑
                
                  j
                  =
                  1
                
                
                  n
                
              
              
                x
                
                  j
                
              
              
                r
                
                  j
                
              
            
          
        
        
          
          
          ;
          
          
        
        
          L
          
            i
          
        
        =
        
          
            z
            2
          
        
        (
        
          r
          
            i
          
        
        −
        
          q
          
            i
          
        
        )
        −
        (
        
          r
          
            i
          
        
        −
        1
        )
        
          
          
          ;
          
          
        
        z
        =
        10
      
    
    {\displaystyle \theta _{i}={\frac {x_{i}q_{i}}{\displaystyle \sum _{j=1}^{n}x_{j}q_{j}}}\mathrm {\,\,;\,\,} \phi _{i}={\frac {x_{i}r_{i}}{\displaystyle \sum _{j=1}^{n}x_{j}r_{j}}}\mathrm {\,\,;\,\,} L_{i}={\frac {z}{2}}(r_{i}-q_{i})-(r_{i}-1)\mathrm {\,\,;\,\,} z=10}
  

  
    
      
        
          q
          
            i
          
        
      
    
    {\displaystyle q_{i}}
  
 y 
  
    
      
        
          r
          
            i
          
        
      
    
    {\displaystyle r_{i}}
  
se calculan a partir de las contribuciones de superficie y volumen del grupo 
  
    
      
        Q
      
    
    {\displaystyle Q}
  
 y 
  
    
      
        R
      
    
    {\displaystyle R}
  
 (normalmente obtenidas mediante valores tabulados), así como el número de ocurrencias del grupo funcional en cada molécula 
  
    
      
        
          ν
          
            k
          
        
      
    
    {\displaystyle \nu _{k}}
  
 de tal manera que:

  
    
      
        
          r
          
            i
          
        
        =
        
          
            ∑
            
              k
              =
              1
            
            
              n
            
          
          
            ν
            
              k
            
          
          
            R
            
              k
            
          
          
            
            
            ;
            
            
          
          
            q
            
              i
            
          
          =
          
            
              ∑
              
                k
                =
                1
              
              
                n
              
            
            
              ν
              
                k
              
            
            
              Q
              
                k
              
            
          
        
      
    
    {\displaystyle r_{i}=\displaystyle \sum _{k=1}^{n}\nu _{k}R_{k}\mathrm {\,\,;\,\,} q_{i}=\displaystyle \sum _{k=1}^{n}\nu _{k}Q_{k}}
  

## Residuo

El componente residual de la actividad 
  
    
      
        
          γ
          
            r
          
        
      
    
    {\displaystyle \gamma ^{r}}
  
 se debe a las interacciones entre los grupos presentes en el sistema, y el trabajo original se refiere al concepto de solución de grupos. El componente residual de la actividad para la molécula 
  
    
      
        
          i
          
            t
            h
          
        
      
    
    {\displaystyle i^{th}}
  
 que contiene 
  
    
      
        n
      
    
    {\displaystyle n}
  
 grupos funcionales únicos puede escribirse de la siguiente manera:

  
    
      
        ln
        ⁡
        
          γ
          
            i
          
          
            r
          
        
        =
        
          
            ∑
            
              k
            
            
              n
            
          
          
            ν
            
              k
            
            
              (
              i
              )
            
          
          
            [
            
              ln
              ⁡
              
                Γ
                
                  k
                
              
              −
              ln
              ⁡
              
                Γ
                
                  k
                
                
                  (
                  i
                  )
                
              
            
            ]
          
        
      
    
    {\displaystyle \ln \gamma _{i}^{r}=\displaystyle \sum _{k}^{n}\nu _{k}^{(i)}\left[\ln \Gamma _{k}-\ln \Gamma _{k}^{(i)}\right]}
  

donde 
  
    
      
        
          Γ
          
            k
          
          
            (
            i
            )
          
        
      
    
    {\displaystyle \Gamma _{k}^{(i)}}
  
 es la actividad de un grupo aislado en una solución formada únicamente por moléculas de tipo 
  
    
      
        i
      
    
    {\displaystyle i}
  
. La formulación de la actividad residual asegura que la condición para el caso límite de una sola molécula en una solución de componente puro, la actividad es igual a 1; como por la definición de 
  
    
      
        
          Γ
          
            k
          
          
            (
            i
            )
          
        
      
    
    {\displaystyle \Gamma _{k}^{(i)}}
  
, uno encuentra que 
  
    
      
        ln
        ⁡
        
          Γ
          
            k
          
        
        −
        ln
        ⁡
        
          Γ
          
            k
          
          
            (
            i
            )
          
        
      
    
    {\displaystyle \ln \Gamma _{k}-\ln \Gamma _{k}^{(i)}}
  
 será cero. La siguiente fórmula se utiliza tanto para 
  
    
      
        
          Γ
          
            k
          
        
      
    
    {\displaystyle \Gamma _{k}}
  
 y 
  
    
      
        
          Γ
          
            k
          
          
            (
            i
            )
          
        
      
    
    {\displaystyle \Gamma _{k}^{(i)}}
  

  
    
      
        ln
        ⁡
        
          Γ
          
            k
          
        
        =
        
          Q
          
            k
          
        
        
          [
          
            1
            −
            ln
            
              
                ∑
                
                  m
                
              
              
                Θ
                
                  m
                
              
              
                Ψ
                
                  m
                  k
                
              
              −
              
                
                  ∑
                  
                    m
                  
                
                
                  
                    
                      
                        Θ
                        
                          m
                        
                      
                      
                        Ψ
                        
                          k
                          m
                        
                      
                    
                    
                      
                        ∑
                        
                          n
                        
                      
                      
                        Θ
                        
                          n
                        
                      
                      
                        Ψ
                        
                          n
                          m
                        
                      
                    
                  
                
              
            
          
          ]
        
      
    
    {\displaystyle \ln \Gamma _{k}=Q_{k}\left[1-\ln \displaystyle \sum _{m}\Theta _{m}\Psi _{mk}-\displaystyle \sum _{m}{\frac {\Theta _{m}\Psi _{km}}{\displaystyle \sum _{n}\Theta _{n}\Psi _{nm}}}\right]}
  

## Véase también

- Equilibrio químico

- Termodinámica química

- Fugacidad

- UNIQUAC - Coeficientes de Actividad Cuasi Química Universales (de sus siglas en inglés UNIversal QUasi-chemical Activity Coefficients)

- Consorcio UNIFAC

- PSRK - Predictive Soave-Redlich-Kwong

- MOSCED - Separación Modificada del Modelo de Densidad de Energía Cohesiva (Estimación de coeficientes de actividad a dilución infinita)
Equipado con los coeficientes de actividad y un conocimiento de los constituyentes y sus cantidades relativas, se pueden calcular fenómenos como separación de fases y equilibrio vapor-líquido. La UNIFAC intenta ser un modelo general para predecir con éxito los coeficientes de actividad.

## Referencias

- ↑ Aage Fredenslund, Russell L. Jones and John M. Prausnitz, “Group-Contribution Estimation of Activity Coefficients in Nonideal Liquid Mixtures”, AIChE Journal, vol. 21 (1975), p. 1086

## Bibliografía

- Aage Fredenslund, Jürgen Gmehling y Peter Rasmussen, Vapor-liquid equilibria using UNIFAC : a group contribution method, Elsevier Scientific, New York, 1979

## Enlaces externos

- UNIFAC structural groups and parameters

- AIOMFAC online-model Modelo de contribución de grupos basado en la UNIFAC para el cálculo de los coeficientes de actividad en mezclas orgánicas e inorgánicas.
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q906212

-  Multimedia: UNIFAC / Q906212

-  Datos: Q906212

-  Multimedia: UNIFAC / Q906212

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.