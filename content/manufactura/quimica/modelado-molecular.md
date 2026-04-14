---
title: "Modelado molecular"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Modelado molecular
    
    
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
  
  
    
      
        
          
            
              
## Modelado molecular

            
            
            
              
                

              

              
El modelado molecular o simulación molecular es un término general que engloba métodos teóricos y técnicas computacionales para modelar, imitar y predecir el comportamiento de las  moléculas. Las técnicas y métodos utilizados se encuentran en un amplio rango de campos de la física (termodinámica, mecánica clásica, mecánica estadística, mecánica cuántica, física matemática y ciencia de materiales), la química computacional y la bioquímica para el estudio de sistemas moleculares que abarcan desde pequeños sistemas químicos a grandes moléculas biológicas y materiales cristalinos. Los cálculos más simples pueden ser realizados a mano, pero inevitablemente se requieren computadoras para realizar el modelado molecular de cualquier sistema medianamente complicado. La característica particular de las técnicas de modelado es la descripción a nivel atómico de los sistemas moleculares; el menor nivel de información es por átomos individuales (o un pequeño grupo de átomos).

La simulación de sistemas molecular puede realizarse mediante métodos clásicos o cuánticos.

Los métodos de modelado molecular son usados rutinariamente en la actualidad para investigar la estructura, dinámica y termodinámica de sistemas inorgánicos, biológicos y poliméricos. Los tipos de actividad biológica que han sido investigados usando modelado molecular incluyen plegamiento proteico, catálisis de enzimas, estabilidad de proteínas, cambios conformacionales asociados con la función biomolecular, y reconocimiento molecular de proteínas, ADN, y complejos de membranas.

## Mecánica molecular

La Mecánica molecular es parte del modelado molecular, ya que implica el uso de mecánica clásica/mecánica newtoniana para describir las bases físicas tras los modelos. Los modelos moleculares describen normalmente átomos (núcleos y electrones en conjunto) como cargas puntuales con una masa asociada. Las interacciones entre los átomos vecinos son descritas por interacciones tipo oscilador armónico, "resortes", (representando enlaces químicos) y Fuerzas de van der Waals. El Potencial de Lennard-Jones es mayormente usado para describir las Fuerzas de van der Waals. Las interacciones electrostáticas son calculadas por la Ley de Coulomb. A los átomos se les asignan coordenadas en el espacio cartesiano o en lagunasCoordenadas internas, y también se les pueden asignar velocidades al realizar simulaciones dinámicas. Las velocidades atómicas están relacionadas con la temperatura del sistema, una cantidad macroscópica. La expresión matemática completa se conoce como una Función potencial y está relacionada con la energía interna del sistema (U - Entropía), una cantidad termodinámica igual a la suma de las energías potencial y cinética. Los métodos que minimizan la energía potencial, son conocidos como técnicas de disminución energética (como, steepest descent y Gradiente conjugado), mientras que los métodos que recrean el comportamiento del sistema con el correr del tiempo son conocidos como Dinámica molecular.

  
    
      
        E
        =
        
          E
          
            b
            o
            n
            d
            s
          
        
        +
        
          E
          
            a
            n
            g
            l
            e
          
        
        +
        
          E
          
            d
            i
            h
            e
            d
            r
            a
            l
          
        
        +
        
          E
          
            n
            o
            n
            −
            b
            o
            n
            d
            e
            d
          
        
      
    
    {\displaystyle E=E_{bonds}+E_{angle}+E_{dihedral}+E_{non-bonded}}
  

  
    
      
        
          E
          
            n
            o
            n
            −
            b
            o
            n
            d
            e
            d
          
        
        =
        
          E
          
            e
            l
            e
            c
            t
            r
            o
            s
            t
            a
            t
            i
            c
          
        
        +
        
          E
          
            v
            a
            n
            d
            e
            r
            W
            a
            a
            l
            s
          
        
      
    
    {\displaystyle E_{non-bonded}=E_{electrostatic}+E_{vanderWaals}}
  

Esta función, llamada Función potencial, calcula la energía potencial molecular como una suma de cantidades de energía que describen la desviación del largo de los enlaces, los ángulos de enlace y los ángulos de torsión fuera de los valores de equilibrio, más cantidades para los pares de átomos no enlazados, ayudando a describir las interacciones de van der Waals y las electrostáticas. El conjunto de parámetros que incluye las distancias de enlace equilibradas, los ángulos de enlace, valores de carga parciales, constantes de fuerza y parámetros de van der Waals; son conocidos de manera conjunta como un campo de fuerza. Distintas aplicaciones de la mecánica molecular usa expresiones matemáticas que difieren ligeramente y, por ende, distintas constantes para la Función potencial. Los campos de fuerza de uso corriente en la actualidad han sido desarrollados usando cálculos cuánticos de alto nivel y/o ajustándose a los valores experimentales. La técnica conocida como Disminución Energética es usada para encontrar posiciones de "gradiente cero" para todos los átomos; en otras palabras, un mínimo local de energía. Estados de menor energía son más estables y son comúnmente investigados por su función en los procesos químicos y biológicos. Una simulación de Dinámica molecular, por otro lado, calcula el comportamiento de un sistema en función del tiempo. Esto implica resolver las leyes de Newton de movimiento, principalmente la segunda ley, F = ma. La Integración de las leyes de Newton del movimiento, usando diferentes algoritmos de integración, conduce las trayectorias atómicas en el espacio y el tiempo. La fuerza de un átomo es definida como el gradiente negativo de la función potencial de energía. La técnica de disminución de energía es útil para obtener una imagen estática para comparar entre los estados de sistemas similares, mientras que la dinámica molecular provee información sobre los procesos dinámicos con el agregado intrínseco de los efectos de la temperatura.

## Variables

Las moléculas pueden ser modeladas al vacío o en presencia de un solvente como el agua. Las simulaciones de los sistemas al vacío son conocidas como simulaciones de fase gaseosa, mientras que aquellas que incluyen la presencia de moléculas de solvente son conocidas como simulaciones con solvente explícito. En otro tipo de simulaciones, el efecto del solvente es estimado usando una expresión matemática empírica; estas son conocidas como simulaciones de solvatación implícita.

## Software popular para modelado molecular

- CHARMM

- Millsian

- BALLView

- Cerius2

- InsightII

- Sybyl

- MOE

- Ghemical

- MMTK

- Agile Molecule

- Molsoft ICM

- Oscail X

- PyMOL

- VMD

- SPARTAN

- GROMOS

- Gaussian

- Sirius

- NOCH

## Véase también

- Química computacional

- Dinámica molecular

- Mecánica molecular

- Método de Montecarlo

## Referencias

- A. R. Leach, Molecular Modelling: Principles and Applications, 2001, ISBN 0-582-38210-6

- D. Frenkel, B. Smit, Understanding Molecular Simulation: From Algorithms to Applications, 1996, ISBN 0-12-267370-0

- D. C. Rapaport, The Art of Molecular Dynamics Simulation, 2004, ISBN 0-521-82586-7

- R. J. Sadus, Molecular Simulation of Fluids: Theory, Algorithms and Object-Orientation, 2002, ISBN 0-444-51082-6

## Enlaces externos

- Centro para Modelado Molecular del Instituto de Salud Nacional (NIH) (Agencia del Gobierno de EE. UU.) (inglés)

- Simulación Molecular (inglés)

- The [1] (enlace roto disponible en Internet Archive; véase el historial, la primera versión y la última). Red y Comunidad de Práctica en Informática y Modelado

- [2] Italian Web Portal About Molecular Modelling

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q174858

-  Multimedia: Molecular modelling / Q174858

-  Datos: Q174858

-  Multimedia: Molecular modelling / Q174858

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.