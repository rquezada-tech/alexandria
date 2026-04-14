---
title: "Interacción de configuraciones"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Interacción de configuraciones
    
    
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
  
  
    
      
        
          
            
              
## Interacción de configuraciones

            
            
            
              
                

              

               
En mecánica cuántica, la interacción de configuraciones (IC) es un método post-Hartree-Fock para resolver la ecuación de Schrödinger no relativista, dentro de la aproximación de Born-Oppenheimer, para sistemas multielectrónicos. La principal aplicación es encontrar los niveles energéticos de un átomo con varios electrones.

## Explicación

Si cada configuración electrónica se expresa como un determinante de Slater, la interacción entre configuraciones electrónicas se expresa como mezcla entre esos determinantes. En general, se trata de un método computacionalmente mucho más costoso que Hartree-Fock y que se hace inviable a partir de sistemas de tamaño medio (del orden de decenas de partículas).

En contraste con el método Hartree-Fock, la IC consigue recuperar parte de la correlación electrónica a partir de una función de onda variacional, que es una combinación lineal de determinantes construidos generalmente a partir de espinores,

  
    
      
        Ψ
        =
        
          ∑
          
            i
            =
            0
          
        
        
          c
          
            i
          
        
        
          Φ
          
            i
          
          
            S
            D
          
        
        =
        
          c
          
            0
          
        
        
          Φ
          
            0
          
          
            S
            D
          
        
        +
        
          c
          
            1
          
        
        
          Φ
          
            1
          
          
            S
            D
          
        
        +
        
          .
          .
          .
        
      
    
    {\displaystyle \Psi =\sum _{i=0}c_{i}\Phi _{i}^{SD}=c_{0}\Phi _{0}^{SD}+c_{1}\Phi _{1}^{SD}+{...}}
  

donde Ψ es generalmente el estado electrónico fundamental del sistema, y el superíndice SD indica que se tienen en cuenta las «excitaciones» simples y dobles a partir del estado fundamental (hay muchas otras formas de construir una IC, pero esta es relativamente común). Al resolver las ecuaciones de IC, se obtienen también aproximaciones a los estados excitados, que difieren en los valores de los coeficientes ci. Si la expansión contiene a todos los determinantes de Slater de la simetría adecuada, es una interacción de configuraciones completa (o exhaustiva) da la mejor energía posible dentro de las bases de orbitales utilizadas, y a los niveles de aproximación mencionados. En otros casos, se obtienen mejoras más modestas respecto al nivel Hartree-Fock, a un costo computacional más asequible. En cualquier caso, al ser un método variacional, a cada nivel de cálculo se obtiene una cota superior a la energía exacta.

El procedimiento IC lleva a una ecuación matricial general de valores propios:

  
    
      
        
          
            H
          
        
        
          c
        
        =
        
          e
        
        
          
            S
          
        
        
          c
        
        ,
      
    
    {\displaystyle {\mathcal {H}}\mathbf {c} =\mathbf {e} {\mathcal {S}}\mathbf {c} ,}
  

donde c es el vector de coeficientes, e es la matriz de valores propios, y los elementos del operador hamiltoniano y de las matrices solapamientos son, respectivamente,

  
    
      
        
          
            
              H
            
          
          
            i
            j
          
        
        =
        
          ⟨
          
            
              Φ
              
                i
              
              
                S
                D
              
            
            
              |
            
            
              
                H
              
            
            
              |
            
            
              Φ
              
                j
              
              
                S
                D
              
            
          
          ⟩
        
      
    
    {\displaystyle {\mathcal {H}}_{ij}=\left\langle \Phi _{i}^{SD}|{\mathcal {H}}|\Phi _{j}^{SD}\right\rangle }
  

  
    
      
        
          
            
              S
            
          
          
            i
            j
          
        
        =
        
          ⟨
          
            
              Φ
              
                i
              
              
                S
                D
              
            
            
              |
            
            
              Φ
              
                j
              
              
                S
                D
              
            
          
          ⟩
        
      
    
    {\displaystyle {\mathcal {S}}_{ij}=\left\langle \Phi _{i}^{SD}|\Phi _{j}^{SD}\right\rangle }
  
.
Los determinantes de Slater se construyen a partir de conjuntos de espinores ortonormales, de forma que 
  
    
      
        
          ⟨
          
            
              Φ
              
                i
              
              
                S
                D
              
            
            
              |
            
            
              Φ
              
                j
              
              
                S
                D
              
            
          
          ⟩
        
        =
        
          δ
          
            i
            j
          
        
      
    
    {\displaystyle \left\langle \Phi _{i}^{SD}|\Phi _{j}^{SD}\right\rangle =\delta _{ij}}
  
, haciendo que 
  
    
      
        
          
            S
          
        
      
    
    {\displaystyle {\mathcal {S}}}
  
 sea la matriz identidad y simplificando la ecuación matricial superior.

## El problema de la consistencia con el tamaño

En química, es usual que sea de interés la comparación entre las energías de sistemas de diferente tamaño. Por ejemplo, en una reacción química, es común que los reactivos se combinen, o se intercambien átomos entre sí para dar lugar a productos de mayor o menor nuclearidad.

Suele ser conveniente, por tanto, que el método de cálculo que se usa mantenga la coherencia de sus resultados con independencia del tamaño del problema, esto es, que la suma de las energías calculadas para dos sistemas sea igual a la energía calculada para el sistema suma. La interacción completa de configuraciones lo es, como también lo es, a un nivel inferior, el esquema de Hartree-Fock. Sin embargo, la interacción de configuraciones no completa no es consistente con la talla del problema. Esto se ve con facilidad considerando un ejemplo sencillo, como el cálculo de dos moléculas de dihidrógeno que no interaccionan entre sí. Su energía debería ser la misma que la suma de sus energías calculadas por separado. Si se calcula una interacción de configuraciones a un nivel concreto, por ejemplo, incluyendo todas las excitaciones simples, en el cálculo de las dos moléculas por separado entra la posibilidad de que haya una excitación en cada una, algo que queda fuera del espacio del cálculo de las dos moléculas simultáneamente. Al aumentar el tamaño del sistema, este defecto se agrava considerablemente. Como indicación aproximada, si se tienen en cuenta las excitaciones dobles y cuádruples, el método es razonablemente consistente hasta moléculas de alrededor de 50 electrones.

## Referencias

## Bibliografía adicional

- Cramer, Christopher J. (2002). Essentials of Computational Chemistry. Chichester: John Wiley & Sons, Ltd. pp. 191–232. ISBN 0-471-48552-7. 

- Sherrill, C. David; Schaefer III, Henry F. (1999), «The Configuration Interaction Method: Advances in Highly Correlated Approaches»,  en Löwdin, Per-Olov, ed., Advances in Quantum Chemistry, Vol 34, San Diego: Academic Press, pp. 143-269, ISBN 0-12-034834-9, doi:10.1016/S0065-3276(08)60532-8 .
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q900672

-  Datos: Q900672

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.