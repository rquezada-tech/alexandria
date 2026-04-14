---
title: "Química computacional"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Química computacional
    
    
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
  
  
    
      
        
          
            
              
## Química computacional

            
            
            
              
                

              

              

La química computacional es una rama de la química que utiliza modelos computacionales para ayudar a estudiar y resolver problemas químicos a través de la aplicación de técnicas y simulaciones computacionales de sistemas moleculares. Utiliza teorías, conceptos y modelos de la química teórica, basados en tratamientos físicos de la materia provenientes de la física clásica, cuántica y la mecánica estadística, incorporados en software científico especialmente diseñado para calcular la estructura y/o las propiedades estáticas y dinámicas de moléculas y agregados moleculares en estado gaseoso y en solución y de cuerpos sólidos. Mientras sus resultados complementan la información que puede obtenerse en experimentos químicos, pueden, en otros casos, predecir fenómenos químicos no observados a la fecha, orientando el diseño de nueva actividad experimental o sustituyendo la ausencia de otro conocimiento empírico en problemas donde el diseño experimental tiene asociado un alto costo económico y/o el experimento empírico resulta impracticable en los términos actuales. La química computacional es ampliamente utilizada desde hace varias décadas en el diseño de nuevos medicamentos y materiales.

Ejemplos de propiedades moleculares estudiadas en este campo son la estructura molecular a nivel atómico (i.e. la posición de los átomos constituyentes de las moléculas en el espacio, que definen su arquitectura molecular) y electrónico (i.e., la distribución de carga electrónica en la molécula, que completa la definición de la forma molecular), la energía absoluta y relativa (asociada a la estabilidad del sistema molecular en estudio), propiedades eléctricas como el dipolo eléctrico y los momentos multipolares de orden superior, frecuencias vibracionales que permiten estudiar el espectro infrarrojo de moléculas y otras magnitudes espectrales y secciones eficaces para la colisión con otras partículas. Adicionalmente es posible anticipar la capacidad de interacción de las moléculas que determinan el reconocimiento molecular (esto puede describirse con métodos clásicos o de mecánica molecular, MM y con métodos de la química cuántica, QM), anticipar su reactividad química general y específica con base en distintos indicadores derivados de la estructura electrónica (esto requiere métodos de la química cuántica QM o mixtos QM/MM) y también analizar mecanismos de reacción.

Los métodos empleados cubren situaciones estáticas y dinámicas. En todos los casos, hay requerimientos computacionales asociados (costo computacional del estudio) que incluyen el tiempo de cálculo (que aumenta rápidamente a medida que el tamaño del sistema estudiado crece y/o se utilizan modelos y métodos más sofisticados, que permiten llegar a describir el sistema con mayor grado de detalle, algo que no siempre es necesario, dependiendo de las propiedades que se pretende estudiar) y la capacidad de almacenamiento de la información en el hardware empleado. El sistema bajo estudio puede ser una única molécula aislada o un grupo de estas en distintos estados de agregación o un cuerpo sólido. En general existe una tensión entre el tamaño del sistema en estudio y el grado de detalle que se puede alcanzar en el mismo.  Todos los métodos de la química computacional implican en su formulación algún grado de aproximación, que implica por lo tanto fortalezas y debilidades que deben conocerse a la hora de seleccionar un método adecuado para estudiar un sistema y propiedades concretas del mismo. Los métodos empleados para estudiar la estructura pueden clasificarse en una primera gran división en métodos clásicos o de mecánica molecular (MM) y métodos cuánticos (QM). En tanto los primeros llegan solamente hasta el detalle atómico, los segundos lo hacen hasta el nivel de detalle electrónico. Dentro de los métodos cuánticos, se pueden distinguir los llamados métodos ab initio, (a primeros principios)  y los métodos semi-empíricos, que introducen un mayor número de aproximaciones y parámetros (que pueden derivarse de información empírica o de cálculos de mayor nivel) en su formulación.

## Historia

Sobre la base de los descubrimientos y la teoría en la historia de la mecánica cuántica, los primeros cálculos teóricos en química fueron los de Walter Heitler y Fritz London en 1927. Los libros que influenciaron los inicios de la química cuántica computacional incluyen: Introduction to Quantum Mechanics – with Applications to Chemistry de Linus Pauling y E. Bright Wilson, 1935; Quantum Chemistry de Henry Eyring, John Walter y George Kimball, 1944; Elementary Wave Mechanics – with Applications to Quantum Chemistry de Walter Heitler, 1945 y más tarde el libro Valence de Charles Coulson, los cuales sirvieron de referencia primaria para los químicos en décadas posteriores.

Con el desarrollo de eficiente tecnología computacional, en los 40' las soluciones de elaboradas ecuaciones de onda para complejos sistemas atómicos comienzan a ser un objetivo realizable. A comienzos de los 50' fueron llevados a cabo los primeros cálculos orbitales atómicos semi-empíricos. Químicos teóricos se convirtieron en una gran cantidad de usuarios de los primeros computadores digitales. Una muy detallada descripción de ese uso en el Reino Unido está dado por Smith y Sutcliffe.[1]​ El primer cálculo ab initio fue el método de Hartree-Fock sobre moléculas diatómicas, el cual se llevó a cabo en 1956 en el MIT usando un conjunto de funciones de base del tipo orbitales de Slater. Para moléculas diatómicas, un estudio sistemático utilizando un conjunto base mínimo y los primeros cálculos de las más grandes conjuntos bases fueron publicados por Ransil y Nesbet respectivamente en 1960.[2]​ El primer cálculo poliatómico usando funciones Gaussianas fueron llevados a cabo a finales de los 50'. Los primeros cálculos de interacción de configuraciones fueron realizadas en Cambridge en el computador EDSAC en los 50' por S. Francis Boys y sus compañeros de trabajo, usando funciones Gaussianas.[3]​ En 1971, cuando una bibliografía de cálculos ab initio fue publicada,[4]​ las moléculas más grandes incluidas fueron la naftalina y el azuleno.[5]​[6]​ Resúmenes de muchos de los primeros desarrollos en la teoría ab initio han sido publicadas por Schaefer.[7]​

En 1964, cálculos del método Hückel, que son un simple método CLOA para la determinación de la energía de electrones de órbitas moleculares de 
  
    
      
        π
      
    
    {\displaystyle \pi }
  
 electrones en sistemas conjugados de hidrocarburos, que van desde sistemas sencillos tales como el butadieno o el benceno hasta el ovaleno con 10 anillos fusionados de a 6, fueron generados en computadores en Berkeley y Oxford.[8]​ Estos métodos empíricos fueron reemplazados en los 60' por métodos semi-empíricos tales como CNDO.[9]​

A comienzos de los 70, eficientes programas computacionales ab initio tales como ATMOL, Gaussian, IBMOL y POLYAYTOM comienzan a ser utilizados para acelerar los cálculos ab initio de órbitas moleculares. De estos programas solo Gaussian, masivamente expandido, está aún en uso, siendo uno de los tantos utilizados hoy en día. Al mismo tiempo, los métodos de mecánica molecular, tales como MM2, fueron desarrollados principalmente por Norman Allinger.[10]​

Una de las primeras veces que el término "química computacional" fue mencionado puede ser encontrado en el libro Computers and Their Role in the Physical Sciences de 1970, escrito por Sidney Fernbach y Abraham Haskell Taub, donde dicen: "Parece, por lo tanto, que la 'química computacional' puede finalmente ser más y más una realidad".[11]​ Durante los 70, diferentes métodos comienzan a ser vistos como parte de una nueva disciplina emergente de química computacional.[12]​ La primera publicación del jornal de química computacional fue publicado en 1980.

## Conceptos

El término química teórica puede ser definido como una descripción matemática de la química o, en forma más amplia, abarcando todo el andamiaje conceptual que atraviesa las teorías, conceptos y modelos de la química (este es un tema en debate dentro del terreno de la filosofía de la química), mientras que el término "química computacional " es usualmente usado cuando un método físico-matemático está lo suficientemente bien desarrollado para su aplicación a sistemas moleculares en forma relativamente automatizada, implementado en un paquete computacional. Si bien muy pocos aspectos de la química pueden ser calculados de manera exacta, estas metodologías tienen errores bastante bien definidos contra los datos experimentales existentes, que permiten la determinación de propiedades moleculares dentro de lo que se conoce como "precisión química". Sin embargo, casi cualquier aspecto de la química puede ser descrito de manera cualitativa, semi-cuantitativa o incluso cuantitativamente mediante un esquema computacional.

Las moléculas están conformadas por núcleos atómicos y electrones, de manera que la teoría y modelos de la mecánica cuántica pueden ser aplicados a su descripción. Lo más frecuente es que los químicos computacionales planteen y resuelvan la ecuación de Schrödinger no relativista, incorporando a posteriori correcciones relativistas cuando esto es indispensable para obtener una correcta descripción del sistema. Teóricamente, es posible resolver en forma exacta la ecuación de Schrödinger molecular, ya sea en su forma dependiente del tiempo o en su forma independiente del tiempo, pero en la práctica esto solo es posible para sistemas muy pequeños. Por lo tanto, se han desarrollado una gran variedad de métodos aproximados dirigidos a alcanzar el mejor equilibrio entre la viabilidad del cálculo, su costo y la precisión del resultado obtenidos. La precisión puede siempre ser mejorada incrementando el costo computacional. La química computacional actual permite calcular con exactitud de manera rutinaria las propiedades de las moléculas que contienen cientos de átomos (y los electrones correspondientes), con errores para la energía que pueden estar por debajo de 1 kcal/mol. En cuanto a los aspectos estructurales a nivel atómico (la geometría molecular) es posible predecir longitudes de enlace con errores de unos pocos picómetros (pm) y los ángulos de enlace con errores del orden de 0,5°. El tratamiento de grandes moléculas es computacionalmente abordable mediante otros métodos aproximados tales como los basados en la teoría del funcional de la densidad (DFT, del inglés density functional theory). Existe alguna controversia en el campo sobre si los métodos teóricos son suficientemente exactos para describir reacciones químicas complejas, como las involucradas en problemas de la bioquímica. Las macromoléculas pueden ser estudiadas por medio de métodos cuánticos semi-empíricos o por métodos de la mecánica clásica, también llamados métodos de mecánica molecular.(MM).

En la química teórica, químicos, físicos, matemáticos e informáticos desarrollan modelos, algoritmos y software para predecir propiedades atómicas y moleculares y para encontrar mecanismos de reacciones químicas. Por el contrario, los químicos computacionales emplean programas y metodologías existentes para dar respuesta a preguntas químicas específicas. 

Hay dos tipos de desafíos diferentes para la química computacional:

- Estudios dirigidos a orientar la síntesis de laboratorio de nuevas sustancias con propiedades deseadas de cara a un determinado uso o para ayudar a entender en mayor profundidad información obtenida experimentalmente (por ejemplo la posición y origen de las señales espectroscópicas de una molécula).

- Estudios dirigidos a predecir moléculas hasta la fecha totalmente desconocidas, propiedades que no se puede determinar experimentalmente o explorar mecanismos de reacción que hasta la fecha no ha sido fácil determinar mediante experimentos.
Así, la química computacional puede ayudar a los químicos experimentales en su trabajo o los puede desafiar a encontrar objetos químicos totalmente nuevos.

Dentro de la química computacional destacan importantes áreas:

- La predicción de la estructura molecular a nivel atómico mediante el uso de métodos clásicos o llegando al detalle electrónico a través de los métodos de la química cuántica. Esto se realiza localizando puntos estacionarios (gradiente nulo) sobre la hipersuperficie de energía potencial correspondiente al sistema que se explora variando la posición de los núcleos atómicos (procedimiento conocido como optimización de geometría).

- Almacenamiento y búsqueda de datos en entidades químicas.

- Determinación de correlaciones entre la estructura química y propiedades de interés químico y/o biológico que permiten construir modelos predictivos cuantitativos (QSPR y QSAR).

- Labor de modelización computacional para ayudar a una eficiente síntesis de componentes.

- Labor de diseño in silico de moléculas capaces de interactuar de forma específica con otras moléculas (e.g. diseño de fármacos).
Véanse también: Análisis retrosintético y  Modelado molecular.

## Métodos

Una misma fórmula molecular puede representar un número amplio de isómeros. Cada isómero se corresponde con un mínimo local de la superficie de energía potencial del sistema molecular (resultante de considerar la energía de los electrones más la energía de repulsión nuclear) como una función de las coordenadas nucleares. Un punto estacionario corresponde a una geometría tal que la derivada de la energía con respecto a todos los desplazamientos de los núcleos vale cero. Un mínimo local (de energía potencial molecular) es un punto estacionario para el que todos los desplazamientos nucleares conducen a un aumento de la energía, por lo tanto se asocian con formas estables del sistema. El mínimo local de más baja energía es llamado mínimo global y corresponde al isómero más estable. Cuando un cambio en una coordenada en particular de la estructura lleva a una disminución de la energía total en ambas direcciones, el punto estacionario corresponde a un estado de transición y la coordenada para la que es un máximo, es la coordenada de reacción. Este proceso de determinar los puntos estacionarios es llamado optimización geométrica.

La determinación de la estructura molecular vía optimización geométrica se convirtió en una rutina solo cuando métodos eficientes para el cálculo de la primera derivada de la energía con respecto a todas las coordenadas atómicas estuviesen disponibles. La evaluación de las segundas derivadas permite la predicción de las frecuencias vibratorias suponiendo movimientos armónicos. Las frecuencias están relacionadas con los valores propios de la matriz de segundas derivadas (la matriz hessiana). Si los valores propios son todos positivos, entonces las frecuencias son todas reales y el punto estacionario es un mínimo local. Si un valor propio es negativo (una frecuencia imaginaria), el punto estacionario es un estado de transición. Si más de un valor propio es negativo el punto estacionario es todavía más complejo, y habitualmente de poco interés. Cuando se encuentra, es necesario mover la búsqueda fuera de él, si se está buscando un mínimo local y un estado de transición.

La energía total está determinada por una solución aproximada de la ecuación de Schrödinger dependiente del tiempo, usualmente incluyendo términos no relativistas, y haciendo uso de la aproximación de Born-Oppenheimer, la cual, basada en las más altas velocidades de los electrones en comparación con los núcleos, permitiendo la separación de movimientos electrónicos y nucleares, simplificando la ecuación de Schrödinger. Esto conduce a la evaluación de la energía total como una suma de energía electrónica en las posiciones fijas del núcleo más la energía de repulsión del mismo. Una notable excepción la constituyen los enfoques llamados química cuántica directa, los cuales tratan a los electrones y los núcleos por igual. Métodos del funcional de densidad y métodos semi-empíricos son variantes del tema principal. Para cada sistema grande, la energía total relativa puede ser comparada utilizando mecánica molecular. Las formas de determinar la energía total para predecir la estructura molecular son:

## Métodos cuánticos ab initio (HF SCF)

Los programas utilizados en química computacional están basados en diferentes métodos de la química cuántica que resuelven la ecuación de Schrödinger asociada al Hamiltoniano molecular. Los métodos que no incluyen ningún parámetro empírico o semi-empírico en sus ecuaciones (siendo derivadas directamente de principios teóricos, sin la inclusión de datos experimentales), son llamados métodos ab initio. Esto no implica que la solución sea exactamente una; son todos cálculos aproximados de mecánica cuántica. Esto significa que una aproximación se define rigurosamente en función de los primeros principios (teoría cuántica) y su resolución es con un margen de error que es cualitativamente conocido de antemano. Si métodos numéricos iterativos han sido empleados, la meta es iterar hasta obtener la máxima precisión que la máquina pueda dar (lo mejor que es posible con un tamaño de palabra del computador finito y con las aproximaciones matemáticas y/o físicas realizadas).

El tipo más simple de cálculo de estructura electrónica ab initio es el método de Hartree-Fock (HF), una extensión de la teoría de orbitales moleculares, en la cual la correlación electrónica, correspondiente a la repulsión electrón-electrón, no es tomada en cuenta en forma instantánea, sino que su efecto promedio es incluido en los cálculos. Como el tamaño de las bases de conjunto es incrementado, la energía y la función de onda tienden a un límite llamado el límite Hartree-Fock. Muchos tipos de cálculos, conocidos como métodos pos Hartree-Fock, comienzan con un cálculo Hartree-Fock para corregir posteriormente la repulsión electrón-electrón, conocida también como correlación electrónica. Ya que estos métodos son llevados al límite, la solución entregada se aproxima a la solución exacta de la ecuación no relativista de Schrödinger. Con el fin de obtener un total acuerdo con los experimentos, se hace necesario incluir términos relativistas y la interacción órbita-espín, ambos solamente importantes para átomos pesados. En todos estos enfoques, además de la elección del método, es necesario elegir un conjunto base. Este es un conjunto de bases, usualmente centrado en alrededor de los diferentes átomos de la molécula, los cuales son usados para expandir las órbitas moleculares con el ansatz CLOA. Los métodos ab initio necesitan definir un nivel de teoría (el método) y un conjunto base.

Dentro del modelo monoelectrónico, la función de onda Hartree-Fock viene descrita por una única configuración electrónica o determinante de Slater. Dicha descripción es adecuada para representar la naturaleza del estado fundamental de las moléculas, en general cerca de las estructuras de equilibrio de los sistemas. A partir de dicha referencia única los métodos químico-cuánticos ab initio añaden los efectos de correlación electrónica a través de procedimientos de interacción de configuraciones, perturbativos u otros.

Existen muchos casos en los que la descripción uniconfiguracional HF es inadecuada para representar la estructura electrónica del sistema, o para estudiar la evolución del sistema químico en diferentes regiones de las superficies de energía potencial.

Situaciones típicas son el estudio de la disociación del enlace químico, el cálculo del estado electrónico excitado, la descripción de situaciones degeneradas entre estados, casos birradicalarios, estados de transición complejos, estructura electrónica en metales de transición, lantánidos o actínidos, con muchas capas electrónicas cercanas en energía, etc. En esas situaciones es necesario describir los estados electrónicos con más de una sola configuración electrónica a través de los métodos multiconfiguracionales, el más conocido de los cuales es el método CASSCF. En ellos tanto los coeficientes de las configuraciones como los coeficientes de los orbitales moleculares se optimizan simultáneamente.

Una vez más, será necesario incluir el resto de la correlación electrónica a partir de dicha función de onda multiconfiguracional. El empleo de métodos uniconfiguracionales en situaciones que requieren descripciones multiconfiguracionales da lugar, en general, a graves defectos en los resultados.

La energía molecular total puede ser evaluada como una función de la geometría molecular, en otras palabras, la energía potencial de superficie. Esta superficie puede ser usada para una reacción dinámica. Los puntos estacionarios de la superficie nos llevan a la predicción de diferentes isómeros y la estructuras de transición para la conversión entre isómeros, pero estos pueden ser determinados sin un conocimiento acabado de la superficie completa.

Un objetivo especialmente importante, llamada termoquímica computacional, es para calcular cantidades termoquímicas tales como la entalpía de formación para la precisión de químicos. La precisión de químicos es la precisión requerida para hacer predicciones químicas realistas y se considera generalmente que es 1 kcal/mol o 4 kJ/mol. Para alcanzar tal precisión de manera económica es necesario utilizar una serie de métodos post Hartree-Fock y combinar los resultados. Estos métodos son llamados métodos compuestos de química cuántica.

## Métodos cuánticos basados en la teoría del funcional de la densidad

Los métodos de la teoría del funcional de la densidad (DFT, del inglés Density Functional Theory) son a menudo considerados por los métodos ab initio para determinar la estructura electrónica molecular, incluso aunque muchos de los más comunes funcionales usen parámetros derivados de datos empíricos, o de cálculos más complejos. Por tanto, también podrían ser llamados métodos semi-empíricos, aunque es más adecuado tratarlos como una clase por sí solos. En DFT, la energía total es expresada en términos de la densidad total en lugar de la función de onda. En este tipo de cálculos, hay un Hamiltoniano aproximado y una expresión aproximada para la densidad electrónica total. Los métodos DFT pueden ser muy precisos por un coste computacional muy bajo. El inconveniente es que, a diferencia de los métodos ab initio, no hay una manera sistemática de mejorar los métodos mejorando la forma del funcional. Algunos métodos combinan el intercambio de densidad del funcional con el intercambio de términos Hartree-Fock y son conocidos como métodos de funcional híbrido.

## Métodos cuánticos semi-empíricos

Los métodos semi-empíricos de química cuántica están basados en el formalismo de Hartree-Fock, pero hacen muchas aproximaciones y obtienen algunos parámetros de datos empíricos. Son muy importantes en química computacional por tratar grandes moléculas donde el método completo de Hartree-Fock sin aproximaciones es muy caro. El uso de parámetros empíricos aparece para permitir la inclusión de algunos efectos de correlación en los métodos.

Los métodos semi-empíricos se basan a menudo en los métodos llamados empíricos donde la parte de dos electrones del Hamiltoniano no es explícitamente incluida. Para sistemas 
  
    
      
        π
      
    
    {\displaystyle \pi }
  
-electrón, el método utilizado es el de Hückel, propuesto por Erich Hückel, y para todos los sistemas de electrones de valencia, el método extendido Hückel, propuesto por Roald Hoffmann.

## Métodos clásicos de Mecánica molecular

En muchos casos, grandes sistemas moleculares pueden ser modelados satisfactoriamente evitando por completo los cálculos requeridos por la mecánica cuántica. Simulaciones de mecánica molecular, por ejemplo, usan una sola expresión para la energía de un compuesto, como un oscilador armónico. Todas las constantes que aparecen en las ecuaciones deberían ser obtenidas de antemano mediante datos experimentales o cálculos ab initio.

La base de datos de compuestos utilizada para la parametrización (el conjunto resultante de parámetros y funciones es llamado campo de fuerza) es crucial para el éxito de los cálculos de la mecánica molecular. Un campo de fuerza parametrizado versus una clase específica de moléculas, por ejemplo proteínas, se espera que tenga alguna relevancia cuando describa a otras moléculas de la misma clase.

Estos métodos pueden ser aplicados a proteínas y otras grandes moléculas biológicas, y permite el estudio de los enfoques e interacciones (acoplamiento) de potenciales moléculas de drogas.

## Métodos para cuerpos sólidos

Método de química computacional pueden ser aplicados a problemas de física de estado sólido. La estructura electrónica de un cristal es en general descrita por una estructura de banda, la cual define la energía de los orbitales electrónicos por cada punto en la zona Brillouin. Cálculos ab initio y semi-empíricos proporcionan energía orbital, por lo tanto pueden ser aplicados a cálculos de estructuras de banda. Dado que se trata del consumo de tiempo para calcular la energía en una molécula, es aún más el tiempo de consumo para calcularlo para la lista completa de puntos en la zona de Brillouin.

## Dinámica química

Una vez que las variables electrónicas y nucleares son separadas (bajo la representación de Born-Oppenheimer) en el enfoque tiempo dependiente, el paquete de ondas correspondientes a los grados de libertad nucleares es propagado mediante un operador de evolución de tiempo asociado a la ecuación de Schrödinger dependiente del tiempo (para el hamiltoniano molecular completo). En la parte complementaria del enfoque energía-dependiente, la ecuación de Schrödinger dependiente del tiempo es resuelta usando la teoría de dispersión. El potencial representando las interacciones interatómicas es dado por la energía potencial de superficie. En general, la energía potencial de superficie están unidas mediante términos de acoplamiento vibrónico.

Los métodos más populares para la propagación de paquetes de onda asociados a la geometría molecular son:

- la técnica del operador de división,

- el método de multiconfiguración Hartree dependiente del tiempo y

- los métodos semiclásicos.
La dinámica molecular (DM) examina (usando las leyes de Newton) el comportamiento de los sistemas dependientes del tiempo, incluyendo vibraciones o movimiento Browniano, usando una descripción de mecánica clásica. DM combinada con la teoría del funcional de la densidad conduce al método Car-Parrinello.

## Interpretación de funciones de ondas moleculares

El modelo átomos en moléculas desarrollado por Richard Bader, fue desarrollado con el fin de unir efectivamente la imagen de la mecánica cuántica de una molécula, como una función de onda electrónica a los modelos más viejos químicamente más utilizados, tales como la teoría del par de electrones de Lewis y la teoría de la unión de valencia. Bader ha demostrado que estos empíricamente modelos útiles están conectados con la topología de la densidad de carga cuántica. Este método mejora en el uso al análisis de población de Mulliken.

## Softwares químicos

Hay muchos autosuficientes usados por químicos computacionales. Algunos incluyen muchos métodos cubriendo una amplia gama de conceptos, mientras que otros cubren solo un área específica y otros incluso un simple método. Los detalles de estos pueden encontrarse en:

- Programas computacionales de química cuántica.

- Programas de la teoría del funcional de la densidad.

- Programas de mecánica molecular.

- Programas semi-empíricos.

- Programas de sistemas de estado sólido con condiciones de borde periódicas.

- Programas para uniones de valencia.

## Véase también

- Molécula

- Bioinformática

- Modelado molecular

- Química cuántica

- Química teórica

- Computación Científica

- Dinámica molecular

- Física estadística

## Referencias

- ↑ Smith, S. J.; Sutcliffe B. T., (1997). "The development of Computational Chemistry in the United Kingdom". Reviews in Computational Chemistry 70: 271 - 316.

- ↑ Schaefer, Henry F. III (1972). The electronic structure of atoms and molecules. Reading, Massachusetss: Addison-Wesley Publishing Co., 146.

- ↑ Boys, S. F.; Cook G. B., Reeves C. M., Shavitt, I. (1956). "Automatic fundamental calculations of molecular structure". Nature 178 (2): 1207.

- ↑ Richards, W. G.; Walker T. E. H and Hinkley R. K. (1971). A bibliography of ab initio molecular wave functions. Oxford: Clarendon Press.

- ↑ Preuss, H. (1968). International Journal of Quantum Chemistry 2: 651.

- ↑ Buenker, R. J.; Peyerimhoff S. D. (1969). Chemical Physics Letters 3: 37.

- ↑ Schaefer, Henry F. III (1984). Quantum Chemistry. Oxford: Clarendon Press.

- ↑ Streitwieser, A.; Brauman J. I. and Coulson C. A. (1965). Supplementary Tables of Molecular Orbital Calculations. Oxford: Pergamon Press.

- ↑ Pople, John A.; David L. Beveridge (1970). Approximate Molecular Orbital Theory. New York: McGraw Hill.

- ↑ Allinger, Norman (1977). "Conformational analysis. 130. MM2. A hydrocarbon force field utilizing V1 and V2 torsional terms". Journal of the American Chemical Society 99: 8127-8134.

- ↑ Fernbach, Sidney; Taub, Abraham Haskell (1970). Computers and Their Role in the Physical Sciences. Routledge. ISBN 0-677-14030-4.

- ↑ Lipkowitz, Kenny B., ed. (1990-01). Reviews in Computational Chemistry. Reviews in Computational Chemistry (en inglés) 1 (1 edición). Wiley. ISBN 978-0-471-18728-8. doi:10.1002/9780470125786. 

## Bibliografía

- Christopher J. Cramer. Essentials of Computational Chemistry. John Wiley & Sons, 2002.

- T. Clark. A Handbook of Computational Chemistry. Wiley, New York, 1985.

- R. Dronskowski. Computational Chemistry of Solid State Materials. Wiley-VCH, 2005.

- F. Jensen. Introduction to Computational Chemistry. John Wiley & Sons, 1999.

- D. Rogers. Computational Chemistry Using the PC, 3rd Edition. John Wiley & Sons, 2003.

- A. Szabo y N.S. Ostlund. Modern Quantum Chemistry. McGraw-Hill, 1982.

- D. Young. Computational Chemistry: A Practical Guide for Applying Techniques to Real World Problems. John Wiley & Sons, 2001.

- David Young. Introduction to Computational Chemistry. Cytoclonal Pharmaceutics Inc.

## Enlaces externos

- Alternatura - IT, Computing and Sciences Creative Technology - Estudio de propiedades ópticas no lineales aplicando los métodos computacionales de la química cuántica de moléculas.

- NIST Computational Chemistry Comparison and Benchmark DataBase - Contiene un base de datos de miles de resultados computacionales y experimentales de cientos de sistemas (en inglés)

- Computational Chemistry Wiki - Wiki de resultados químicos computacionales (en inglés)
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q369472

-  Multimedia: Computational chemistry / Q369472

-  Recursos didácticos: Química computacional

- Identificadores

- LCCN: sh2020006312

- NDL: 00580704

- NKC: ph534651

- NLI: 987010400176205171

- AAT: 300380501

- Identificadores médicos

- MeSH: D000080486

- UMLS: C0872134

-  Datos: Q369472

-  Multimedia: Computational chemistry / Q369472

-  Recursos didácticos: Química computacional

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.