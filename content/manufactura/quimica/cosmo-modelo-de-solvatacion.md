---
title: "COSMO modelo de solvatación"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

COSMO modelo de solvatación
    
    
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
  
  
    
      
        
          
            
              
## COSMO modelo de solvatación

            
            
            
              
                

              

              
COSMO es la abreviación de "Conductor-like Screening Model", un método de cálculo para la interacción electrostática de una molécula en un solvente.

En COSMO el solvente es tratado como un medio continuo con una permitividad 
  
    
      
        ε
      
    
    {\displaystyle \varepsilon }
  
 por lo cual se le considera perteneciente al grupo de modelos de solvatación de medio continuo. También se asume que el medio llega hasta la "superficie" de la molécula disuelta. Se asume que esta interfaz consiste de esferas que rodean los átomos individuales (es decir el radio Van der Waals más una distancia fija para las moléculas disueltas). Para el cálculo mismo esta superficie se aproxima por partes planas, por ejemplo triángulos.

Si el solvente fuera un conductor ideal el potencial eléctrico de esta superficie debería desaparecer. Si la distribución de la carga eléctrica en la molécula es conocida entonces debería ser fácil calcular la carga 
  
    
      
        
          q
          
            ∗
          
        
      
    
    {\displaystyle q^{*}}
  
 en la superficie. Para solventes reales uno puede asumir que la carga 
  
    
      
        q
      
    
    {\displaystyle q}
  
 es menor por un factor 
  
    
      
        f
      
    
    {\displaystyle f}
  
:

  
    
      
        q
        =
        f
        
          q
          
            ∗
          
        
      
    
    {\displaystyle q=fq^{*}}
  
.
El factor 
  
    
      
        f
      
    
    {\displaystyle f}
  
 es aproximadamente

  
    
      
        f
        (
        ε
        )
        =
        (
        ε
        −
        1
        )
        
          /
        
        (
        ε
        +
        0.5
        )
      
    
    {\displaystyle f(\varepsilon )=(\varepsilon -1)/(\varepsilon +0.5)}
  

donde el sumando 0.5 en el denominador es una magnitud que se encuentra empíricamente.

Sobre la base de las cargas 
  
    
      
        q
      
    
    {\displaystyle q}
  
 del solvente determinadas de esta forma y a la distribución conocida de cargas de la molécula se puede calcular la energía de la interacción entre el solvente y la molécula disuelta.

El método COSMO se puede usar para todos los métodos en química teórica donde se puede determinar la distribución de la carga de una molécula, por ejemplo cálculos semiempíricos, cálculos del método Hartree-Fock o de la teoría funcional de densidad (mecánica cuántica).

## Comparación con otros métodos

Mientras que moldelos basados en el desarrollo multipolar de la distribución de carga de una molécula están limitados a moléculas pequeñas, quasi esféricas o elipsoidales, el método COSMO tiene la ventaja de poder ser aplicado a estructuras moleculares grandes e irregulares.

El método COSMO es más exacto para solventes que poseen una permitividad elevada ya que un solvente con permitividad infinita se comporta como un conductor ideal. Con agua (
  
    
      
        ε
        ≈
        80
      
    
    {\displaystyle \varepsilon \approx 80}
  
) se obtiene una exactitud muy buena. Para solventes con baja permitividad la solución completa de las ecuaciones electrostáticas sería de mayor exactitud pero esto significaría un mayor esfuerzo.

A diferencia de cálculos de dinámica molecular en los cuales el movimiento de las moléculas se calcula y la posición y densidad se promedian sobre el tiempo el modelo COSMO, como es el caso en todos los modelos de medio continuo, tiene la ventaja de un tiempo de cálculo mucho menor.

## Literatura

- Principios del método: A. Klamt, G. Schürmann, Journal of the Chemical Society, Perkin Transaction 2, 799 (1993) [1]
Fuente: Traducido de Wikipedia en alemán

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q904513

-  Datos: Q904513

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.