---
title: "Base de datos química"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Base de datos química
    
    
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
  
  
    
      
        
          
            
              
## Base de datos química

            
            
            
              
                

              

              Una base de datos química es una base de datos específicamente diseñada para almacenar información química. Esta información puede incluir fórmulas, estructuras químicas y cristalinas, espectros, reacciones químicas, síntesis químicas, y datos termodinámicos.

## Tipos de bases de datos químicas

## Estructuras químicas

Las estructuras químicas se representan tradicionalmente usando líneas que indican los enlaces químicos entre los átomos y dibujadas sobre papel (fórmula estructural 2D. Mientras que éstas son representaciones visuales ideales para el químico, no son válidas para uso computacional ni especialmente para algoritmo de búsqueda y almacenamiento informático. Las moléculas pequeñas (también llamadas ligandos en aplicaciones de diseño de fármacos), se representan usualmente usando listas de átomos y sus conexiones. Las moléculas grandes como proteínas se representan de un modo más compacto usando secuencias de aminoácidos, sus bloques de construcción. 
Las grandes bases de datos químicas para estructuras son capaces de gestionar el almacenamiento y búsqueda de información sobre millones de moléculas, ocupando terabytes de memoria física de ordenador. 

## Bases de datos de literatura científica

Las bases de datos de literatura científica relacionan las estructuras y otra información química con referencias importantes como artículos pedagógicos o patentes. Entre estas bases de datos se incluyen Chemical Abstracts Service STN y SciFinder o EBSCOhost. Los enlaces a cada publicación científica se incluyen en muchas bases de datos que se centran en las características químicas de cada sustancia.

## Bases de datos cristalográficos

Las bases de datos cristalográficos almacenan datos de difracción de estructuras cristalinas con rayos-X. Algunos ejemplos de estas bases son Protein Data Bank and Cambridge Structural Database.

## Bases de datos de espectros de RMN

Las bases de datos de espectros de RMN relacionan estructuras químicas con datos de RMN. Estas bases de datos incluyen a veces otras características como datos de espectroscopia infrarroja de transformada de Fourier y de espectros de masas.

## Base de datos de reacciones

La mayoría de las bases de datos químicas almacenan información sobre moléculas estables pero en las bases de datos de reacciones también se recogen compuestos intermedios y moléculas inestables de corta vida. Estas bases contienen información sobre productos, eductos y mecanismos de reacción.

## Bases de datos termofísicos y termodinámicos

Los datos termofísicos más importantes se refieren a

- Equilibrio de fases incluyendo equilibrio líquido-vapor, solubilidad de gases en líquidos, y de líquidos en sólidos, calores de disolución, de vaporización, y de fusión.

- Datos caloríficos como calor específico, calor de formación y de combustión,

- Propiedades de transporte como viscosidad y conductividad térmica

## Bases de datos de representación de estructuras químicas

Hay dos técnicas principales para representar estructuras químicas en bases de datos digitales:

- Como tablas de conexión / matrices de adyacencia / listas con información adicional sobre enlaces (ejes) y los átomos entre ellos (nodos). Por ejemplo:
MDL Molfile, Protein Data Bank, Chemical Markup Language

- Como una notación de cuerdas lineales basada en distintos algoritmos de búsqueda. Por ejemplo:
SMILES/SMARTS, SLN, Wiswesser Line Notation, International Chemical Identifier (InChI)
Estos enfoques se han mejorado para permitir la representación de diferencias estereoquímicas y especies químicas con carga eléctrica así como tipos especiales de enlace como los que aparecen en compuestos organometálicos. La principal ventaja de una representación informática es la posibilidad del almacenamiento elevado y las búsquedas flexibles y rápidas.

## Búsqueda

## Por subestructuras

Los químicos pueden buscar en bases de datos usando partes de estructuras, partes de sus nombres según la IUPAC y también basándose en limitaciones de sus propiedades. Las bases de datos químicas son particularmente diferentes de las bases de datos de propósito general en su soporte a la búsqueda por subestructuras. Esta clase de búsqueda se consigue buscando isomorfismo de subestructuras (a veces también llamado monomorfismo) que es una aplicación muy estudiada de la teoría de grafos. Los algoritmos de búsqueda requieren mucha potencia de computación[1]​). Se consigue mejor eficacia en la búsqueda con el mecanismo de amortización de tiempo, es decir, algunas tareas de búsqueda son guardadas para así usar información preprocesada por el ordenador. Buscando los fragmentos presentes en una búsqueda de estructura es posible eliminar las comparaciones con moléculas que no poseen los fragmentos presentes en la estructura de búsqueda. Esta eliminación se llama screening o rastreo (no confundir con los procedimientos de screening usados en el descubrimiento de fármacos).[2]​

## Por conformación

Las búsquedas por emparejamiento con la conformación 3D de moléculas o especificando limitaciones espaciales es otra característica especialmente útil en el diseño de fármacos. Estas búsquedas consumen mucho tiempo de cálculo.[3]​[4]​[5]​[6]​[7]​

## Por descriptores

Todas las propiedades de las moléculas aparte de su estructura pueden clasificarse en atributos físico-químicos o farmacológicos, también llamados descriptores. Por encima de eso, hay varios sistemas de nombres artificiales y más o menos estandarizados para moléculas que facilitan nombres más o menos ambiguos y sinónimos. El nombre IUPAC es habitualmente una buena elección para representar una estructura de molécula que sea inteligible a la vez para el humano y el ordenador aunque se hace pesado y difícil de manejar para moléculas grandes. Los nombres tradicionales por otra parte poseen abundantes homónimos y sinónimos y son por tanto una mala elección como clave primaria de indexación. Mientras que los descriptores físico-químicos como la masa molecular, la (carga parcial), solubilidad, etc. pueden ser directamente computados en la mayoría de los casos, los descriptores farmacológicos pueden derivarse solo indirectamente usando estadística multivariante o resultados experimentales (screening, bioensayos). Todos esos descriptores suelen almacenarse junto a la representación de la molécula por cuestiones de esfuerzo computacional.

## Por semejanza química

No hay una definición simple de la semejanza molecular, pero el concepto puede definirse según la aplicación y a menudo se describe como el inverso de una distancia en el espacio descriptor. Dos moléculas podrían considerarse más semejantes por ejemplo si su diferencia en masa molecular es menor que cuando se la compara con otras. Varias medidas pueden combinarse para producir una medida de la distancia multivariable. Las medidas de distancia se clasifican a menudo en medidas euclídeas y no euclídeas. La búsqueda de subestructuras basada en el máximo común subgrafo[8]​ (semejanza o medida de distancia) es también muy común. Este método también se emplea para discriminar fármacos, marcando moléculas, que comparten un subgrafo o subestructura común.[9]​ 

Los compuestos químicos en estas bases de datos pueden ser agrupados en grupos de moléculas semejantes que comparten algunas similitudes. Existen dos enfoques de agrupamiento jerárquico y no-jerárquico que pueden aplicarse a entidades químicas con atributos múltiplos. Estos atributos o propiedades moleculares pueden determinarse empíricamente o derivarse computacionalmente. Uno de los enfoques de agrupamiento más populares es el algoritmo de Jarvis-Patrick.[10]​

## Sistemas de registro

Son sistemas de bases de datos que mantienen registros únicos de cada compuesto químico. Son frecuentemente usados para indexación de compuestos, sistemas de patentes y bases de datos industriales.

Los sistemas de registro fuerzan la unicidad de cada compuesto representado en la base de datos mediante el uso de representaciones únicas. Aplicando reglas de precedencia para la generación de notaciones lineales, se pueden obtener representaciones lineales únicas/'canónicas' tales como las de SMILES'. Algunos sistemas de registro como el CAS (Chemical Abstract Service) pueden usar algoritmos para generar un código hash único y consiguen el mismo objetivo.

Una diferencia clave entre un sistema de registro y una base de datos química simple es la cualidad de representar con precisión lo que es conocido, desconocido o parcialmente conocido. Por ejemplo, una base de datos química podría almacenar una molécula con una estereoquímica no especificada, mientras que un sistema de registro químico requiere que elregistrador especifique si la configuración spacial es desconocida, una mezcla específica (conocida), o un racémico. Cada una de esas posibilidades sería considerada un registro diferente en la base de datos.

Los sistemas de registro también preprocesan las moléculas para evitar considerar diferencias triviales tales como las diferencias en los iones halógenos en los compuestos.

Un ejemplo es el sistema de registro Chemical Abstracts Service[1], por medio de números de registro CAS.

## Herramientas

Las representaciones computacionales habitualmente se hacen transparentes para los químicos mediante el uso de diagramas gráficos de los datos. La entrada de datos también se simplifica mediante el uso de editores de estructura química. Estos editores convierten internamente los datos gráficos en representaciones computacionales.

También hay numerosos algoritmos para la interconversión de los variados formatos de representación. Una utilidad de conversión, de acceso libre, es OpenBabel. Estos algoritmos de búsqueda y conversión se implementan bien dentro del propio sistema de la base de datos o, como viene siendo ahora habitual, como componentes externos que se mantienen en sistemas de bases de datos relacionales. Tanto los sistemas basados en Oracle como en PostgreSQL hacen uso de la tecnología de cartucho que permiten tipos de datos definidos por el usuario. Estos permiten al usuario hacer peticiones en SQL con las condiciones de búsqueda química (Por ejemplo una petición para buscar registros que tengan un anillo fenilo en su estructura se representa como un diagrama lineal SMILES que podría ser 

 SELECT * FROM CHEMTABLE WHERE SMILESCOL.CONTAINS('c1ccccc1')

Los algoritmos para la conversión de nombres IUPAC a representaciones de la estructura y viceversa se usan también para extraer información estructural del texto (minería de textos). Sin embargo hay dificultades debido a la existencia de múltiples dialectos de la IUPAC. Se está trabajando para establecer un único estándar de la IUPAC (Ver International Chemical Identifier o InChI).

## Véase también

- ChemSpider

- DrugBank

- PubChem

## Referencias

- ↑ S. A. Rahman, M. Bashton, G. L. Holliday, R. Schrader and J. M. Thornton (2009) Small Molecule Subgraph Detector (SMSD) toolkit, Journal of Cheminformatics, 1:12. DOI:10.1186/1758-2946-1-12

- ↑ Cummings, Maxwell D.; Maxwell, Alan C.; DesJarlais, Renee L. (2007) Processing of Small Molecule Databases for Automated Docking. Medicinal Chemistry 3(1):107-113

- ↑ Pearlman, R.S. and Smith, K.M., Metric Validation and the Receptor-Relevant Subspace Concept, J. Chem. Inf. Comput. Sci., 1999, 39:28-35

- ↑  LIN Jr-Hung ; CLARK Timothy (2005) An analytical, variable resolution, complete description of static molecules and their intermolecular binding properties. JCIM Vol. 45, no4, pp. 1010-1016

- ↑  Meek P. J., Liu, Z., Tian, L., Wang C. J, Welsh W. J, Zauhar, R. J (2006) Shape Signatures: speeding up computer aided drug discovery. DDT 2006 Vol (19-20):895-904

- ↑  Grant, J. A, Gallardo, M. A., Pickup B. T. (1996) A fast method of molecular shape comparison: A simple application of a Gaussian description of molecular shape. JCIC Vol 17, No. 14, pp 1653-1666

- ↑ Ballester, P. J. & W. G. Richards (2007) Ultrafast shape recognition for similarity search in molecular databases. Proc R Soc A, 463:1307-1321

- ↑ S. A. Rahman, M. Bashton, G. L. Holliday, R. Schrader and J. M. Thornton, Small Molecule Subgraph Detector (SMSD) toolkit, Journal of Cheminformatics 2009, 1:12. DOI:10.1186/1758-2946-1-12

- ↑ «SMSD::Home Page». Archivado desde el original el 28 de enero de 2020. Consultado el 2009. 

- ↑ Butina, Darko (1999) Unsupervised Data Base Clustering Based on Daylight’s Fingerprint and Tanimoto Similarity: A Fast and Automated Way To Cluster Small and Large Data Sets. Chem. Inf. Comput. Sci. 39:747-750

## Enlaces externos

## Bases de datos y software de registro

- CDK es una biblioteca Java de acceso libre para el manejo dedatos químicos

- JChem Base Archivado el 19 de octubre de 2009 en Wayback Machine. and JChem Cartridge Gestión de bases de datos en Java y .NET y herramientas de búsqueda de ChemAxon

- Instant JChem Gestión de base de datos de escritorio y aplicación de búsqueda de ChemAxon. Edición gratuita para uso personal.

- SMSD (Detector de diagramas de moléculas pequeñas) Archivado el 28 de enero de 2020 en Wayback Machine. es una biblioteca de software basado en Java para calcular Diagramas máximos comunes ovMaximum Common Subgraph (MCS) entre moléculas pequeñas.

- JOELib, una biblioteca java de gestión para el manejo de datos químicos.

- 'Chemical Structure Lookup Service' y 'NCI Enhanced Database Browser', servicios web del grupo CADD del National Cancer Institute (NCI)

## Bases de datos de estructuras químicas

- Base de datos de referencias de síntesis

- eChemPortal, un portal global para información sobre substancias químicas

- NLM ChemIDplus, compuestos biomédicos accesibles por nombre y estructura.

- OBase de datos de síntesis orgánicas

- ZINC, una base de datos libre para rastreo virtual

- JCHEM.INFO, Base de datos libre de compuestos orgánicos e inorgánicos, y datos físicos de esos compuestos.

- ChemSpider, Acceso libre a más de 20 millones de estructuras químicas, datos de propiedades físicas e identificadores sistemáticos

- MMsINC, una base de datos de acceso libre vía web de compuestos disponibles comercialmente para rastreo virtual y aplicaciones quimioinformáticas

- ChemIndustry Archivado el 22 de julio de 2009 en Wayback Machine. una base de datos libre derivada de los datos de PubChem

- [2] Archivado el 22 de julio de 2011 en Wayback Machine., OpenCDLig: una aplicación web libre para complejos huésped-anfitrión

- NCI/CADD Servicio de búsqueda de estructuras químicas, busca en qué bases de datos se presenta una estructura (actualmente indexa más de 70 millones de estructuras químicas)

## Bases de datos de nombres químicos

- Base de datos de sustancias químicas, una base de datos de nombres químicos, de acceso libre, usada principalmente para traducción de nombres entre inglés y japonés. dispone de más de 37,000 entradas.

- ChemSub Online, portal químico libre con más de 237.000 sustancias, nombradas en 8 idiomas.

- Base de datos EuroChem Online, una base de datos química gratuita.
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q2881060

- Identificadores médicos

- MeSH: D062126

-  Datos: Q2881060

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.