---
title: "Método CASSCF"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Método CASSCF
    
    
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
  
  
    
      
        
          
            
              
## Método CASSCF

            
            
            
              
                

              

              El método CASSCF, en química computacional, fue desarrollado a finales de los años 80 en
la Universidad de Lund, Suecia, por Björn O. Roos y sus colaboradores. Es un caso particular de método de campo autoconsistente multiconfiguracional (MCSCF). CASSCF son las siglas en inglés de Espacio Activo Completo en un Campo Autoconsistente (Complete Active Space Self-Consistent Field), y consiste en el cálculo variacional completo de algunos electrones y algunos orbitales, en el campo promedio del resto de electrones en el resto de orbitales. En rigor, se define el espacio activo como el espacio generado por n electrones y m orbitales, restringido por simetría y por multiplicidad de espín.

## Procedimiento (cualitativo)

Conociendo la interacción en estudio, se divide el total de orbitales en tres conjuntos:

- los orbitales inactivos, que se consideran siempre doblemente ocupados,

- los orbitales activos, a partir de los cuales se construye el espacio activo (Active Space), consistente en un espacio de determinantes que describe e incluye al número de electrones y orbitales que participan con mayor importancia en el fenómeno de interés (por ejemplo, los orbitales magnéticos, en magnetoquímica, o la nube pi en estudios de aromaticidad), y cuya ocupación promedio será fraccionaria, entre cero y dos. Finalmente

- los orbitales virtuales, que estárán siempre vacíos.
Se procede a una interacción completa de configuraciones, restringida al espacio activo, mientras que el resto del sistema se trata a nivel de Hartree-Fock, esto es, de campo autoconsistente.

Existe una formulación más flexible del método CASSCF denominada RASSCF (Restricted Active Space SCF) que 
permite dividir el espacio de orbitales activos en tres subespacios (Ras1, Ras2 y Ras3). Mientras la expansión
configuracional en Ras2 es equivalente a la explicada para el CASSCF, en las expansiones de Ras1 y Ras3 se
permite restringir el nivel de excitación (por ejemplo a simples, dobles, triples... excitaciones).

## Ventajas e inconvenientes

La ventaja del método CASSCF frente al SCF simple es que la descripción de la función de onda de referencia
ha mejorado al incluir más de una configuración electrónica, lo que es clave en un gran número de casos, como situaciones
degeneradas en energía, disociaciones, estados excitados o capas abiertas. En cualquier caso ninguno de los dos métodos
deben ser considerados cuantitativos a la hora de calcular diferencias de energía. Empleando la función de onda calculada
como referencia, bien sea SCF o CASSSF, otro método que incluya la mayor parte de la correlación electrónica,
no considerada aún, tendrá que aplicarse para obtener valores de energía cuantitativos. Métodos posibles son los de interacción de configuraciones (CI), coupled-cluster (CC), o teoría de perturbaciones (PT), que requerirán tanto mayor esfuerzo de cálculo 
cuanto peor sea la referencia. El método CASSCF tan solo incluye una fracción de la energía de correlación electrónica que suele
denominarse estática, mientras al resto de la correlación se la denomina dinámica. El método con más éxito, por económico y
generalista para incluir este tipo de correlación y obtener resultados precisos a partir de una referencia CASSCF es el método CASPT2, teoría multiconfiguracional de perturbaciones a segundo orden. La principal desventaja de los cálculos multiconfiguracionales es que la elección del espacio activo reviste una importancia crucial, y depende tanto de la molécula (o fragmento de cristal) sobre la que se está trabajando como del fenómeno que se esté estudiando. Cuando el espacio activo no incluye toda la física relevante para el fenómeno en estudio, los resultados que se obtienen pueden ser engañosos, y no existe un método sistemático para detectarlo.

## Implementaciones

Entre los paquetes informáticos que implementan CASSCF se encuentran Gaussian, MOLCAS y MOLPRO.

## Referencias

- B. O. Roos, Adv. Chem. Phys., 69, 399 (1987)

- R. McWeeny, Methods Of Molecular Quantum Mechanics
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q2266294

-  Datos: Q2266294

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.