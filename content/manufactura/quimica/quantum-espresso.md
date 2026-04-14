---
title: "Quantum ESPRESSO"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Quantum ESPRESSO
    
    
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
  
  
    
      
        
          
            
              
## Quantum ESPRESSO

            
            
            
              
                

              

              Quantum ESPRESSO

Información generalTipo de programa
software libreDesarrollador
Quantum ESPRESSO Foundation (QEF)[1]​Modelo de desarrollo
Software libreLicencia
GNU General Public LicenseIdiomas
EnglishInformación técnicaProgramado en
FortranVersionesÚltima versión estable
7.0 (22 de diciembre de 2021)Enlaces
Sitio web oficial

Repositorio de código

Quantum ESPRESSO es un paquete de programas para el modelado de materiales y cálculos de estructura electrónica utilizando métodos de primeros principios. La suite se distribuida de forma gratuita y como software libre bajo la Licencia Pública General GNU . Implementa la teoría funcional de la densidad, utilizando un conjunto base de ondas planas y pseudopotenciales (tanto de norma conservada como ultrasuaves). La palabra ESPRESSO es un acrónimo de paquete de código abierto para la investigación en estructura electrónica, simulación y optimización (por sus siglas en inglés opEn-Source Package for Research in Electronic Structure, Simulation, and Optimization).[2]​[3]​

PWscf es el paquete de programas que permite a Quantum ESPRESSO utilizar ondas planas en las simulaciones. PWscf existió como un proyecto independiente. El cual permitía realizar cálculos de estructura electrónica implementando la teoría del funcional de la densidad, utilizando un conjunto base de ondas planas y pseudopotenciales. PWscf también implemento la teoría del funcional de la densidad perturbado. PWscf son las siglas en inglés de Plane-Wave Self-Consistent Field y se publicó bajo la Licencia Pública General GNU.

La última versión es QE-7.0 la cual se lanzó el 22 de diciembre de 2021.

## Proyecto Quantum ESPRESSO

Quantum ESPRESSO es una iniciativa abierta del Centro Nacional de Simulación CNR-IOM DEMOCRITOS ubicado en Trieste (Italia) en colaboración con universidades y centros de investigación a nivel mundial como son: el Instituto de Tecnología de Massachusetts (MIT), la Universidad de Princeton, la Universidad de Minnesota y la Ecole Polytechnique Fédérale de Lausanne. Actualmente el proyecto es coordinado por la fundación QUANTUM ESPRESSO, formada por varios centros y grupos de investigación a nivel mundial. La primera versión de Quantum ESPRESSO se llamó pw.1.0.0 y fue lanzada el 15 de junio de 2001.

Quantum ESPRESSO se encuentra desarrollado principalmente en Fortran 90, pero también tiene partes escritas en C y en Fortran 77. Es el resultado de la unión y adaptación de diferentes paquetes anteriores que fueron desarrollados de manera independiente. También tiene paquetes desarrollados con la intención de ser interoperables con los paquetes anteriores, permitiendo realizar tareas más avanzadas.

Los paquetes principales son Pwscf [4]​ que resuelve las ecuaciones de Kohn-Sham utilizando un método de campo autoconsistente , dichas ecuaciones son obtenidas para un sólido periódico, CP que permite realizar dinámica molecular de Car-Parrinello, la cual es dinámica molecular de primeros principios, y PostProc, que permite analizar y graficar los datos. También tiene paquetes adicionales como atomic que permite generar pseudopotenciales, PHonon que implementa la teoría del funcional de la densidad perturbado (TFDP) para el cálculo de las derivadas de segundo y tercer orden de la energía con respecto a los desplazamientos atómicos y NEB para el cálculo de caminos de reacción y barreras de energía.

## Capacidades de modelamiento

Las diferentes tipos de simulación que se pueden realizar incluyen

- Cálculos del estado fundamental

- Optimización estructural

- Estados de transición y trayectorias de energía mínima

- Propiedades de respuesta (DFPT), como frecuencias de fonones, interacciones electrón-fonón y desplazamientos químicos de EPR y NMR

- Dinámica molecular de primeros principios : Car-Parrinello y Born-Oppenheimer MD

- Propiedades espectroscópicas[5]​[6]​

- Importación cuántica

- Creación de pseudopotenciales

## Paralelización

Los componentes principales del paquete de programas QUANTUM ESPRESSO están diseñados para aprovechar la arquitectura moderna de las supercomputadoras, las cuales poseen múltiples niveles y capas de comunicación entre procesadores. La paralelización se logra mediante las librerías de paralelización MPI y OpenMP, lo que permite que los programas principales se ejecuten en forma paralela en la mayoría de computadoras modernas y clusters de supercomputadoras con buen rendimiento.

## Véase también

- Teoría funcional de la densidad

## Referencias

- ↑ «Quantum ESPRESSO Foundation - Home of the Quantum ESPRESSO Foundation». 

- ↑ Paolo Giannozzi; Stefano Baroni; Nicola Bonini; Matteo Calandra; Roberto Car; Carlo Cavazzoni; Davide Ceresoli; Guido L Chiarotti et al. (2009). «QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials». Journal of Physics: Condensed Matter 21 (39): 395502. Bibcode:2009JPCM...21M5502G. PMID 21832390. arXiv:0906.2569. doi:10.1088/0953-8984/21/39/395502.  Se sugiere usar |número-autores= (ayuda)

- ↑ P. Giannozzi; O. Andreussi; T. Brumme; O. Bunau; M. Buongiorno Nardelli; M. Calandra; R. Car; C. Cavazzoni et al. (2017). «Advanced capabilities for materials modelling with Quantum ESPRESSO». Journal of Physics: Condensed Matter 29 (46): 465901. Bibcode:2017JPCM...29T5901G. PMID 29064822. arXiv:1709.10010. doi:10.1088/1361-648X/aa8f79.  Se sugiere usar |número-autores= (ayuda)

- ↑ Corso, Andrea Dal (1996). «A Pseudopotential Plane Waves Program (PWSCF) and some Case Studies». Quantum-Mechanical Ab-initio Calculation of the Properties of Crystalline Materials. Lecture Notes in Chemistry (en inglés) 67. Springer, Berlin, Heidelberg. pp. 155-178. ISBN 9783540616450. doi:10.1007/978-3-642-61478-1_10. 

- ↑ Bunău, Oana; Matteo, Calandra (2013). «Projector augmented wave calculation of x-ray absorption spectra at the L 2, 3 edges.». Physical Review B 87 (20): 205105. Bibcode:2013PhRvB..87t5105B. arXiv:1304.6251. doi:10.1103/PhysRevB.87.205105. 

- ↑ Gougoussis, Christos; Calandra, Matteo; Seitsonen, Ari P.; Mauri, Francesco (2009). «First-principles calculations of X-ray absorption in an ultrasoft pseudopotentials scheme: from $\alpha$-quartz to high-T$_c$ compounds». Phys. Rev. B 80 (7). doi:10.1103/PhysRevB.80.075102. 

## Enlaces externos

- Sitio web de Quantum ESPRESSO

- Sitio web de la Fundación Quantum ESPRESSO (QEF)

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q17096266

- Informática

- Debian: quantum-espresso

- Open Hub: quantum-espresso

-  Datos: Q17096266

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.