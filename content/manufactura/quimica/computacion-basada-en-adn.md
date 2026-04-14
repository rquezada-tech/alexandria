---
title: "Computación basada en ADN"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Computación basada en ADN
    
    
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
  
  
    
      
        
          
            
              
## Computación basada en ADN

            
            
            
              
                

              

              
La computación basada en ADN es una rama emergente de la informática que utiliza el ADN como hardware en vez de los circuitos integrados de silicio empleados por las computadoras tradicionales.

Probablemente la primera vez que fue mencionada la computación sub-microscópica fue en la charla Hay Espacio de sobra allí abajo, por el físico Richard Feynman.

## Historia

Leonard Adleman, de la Universidad del Sur de California inició el estudio en este campo, en 1994.[1]​

Adleman probó la utilidad, al menos teórica, del uso del ADN para resolver problemas. En particular, logró resolver el Problema del camino Hamiltoniano de 7 nodos. 
Desde los primeros experimentos de Adleman, se han realizado numerosos avances, y se ha demostrado que se pueden construir varias Máquinas de Turing.[2]​
[3]​

Esta es una tecnología todavía en etapas bastante tempranas, por lo cual su uso existe más que nada como una opción teórica. Todavía usar computación convencional es una opción más eficiente que usar este método.

## Modelo de Stickers

Consideremos por ejemplo un modelo de computación con ADN conocido como sticker model. Este modelo usa dos tipos básicos 
de hebras simples de ADN, llamadas hebras memoria y hebras sticker. Una hebra memoria tiene n bases de largo y contiene k
sub-hebras no superpuestas, cada una de largo m. Así que, 
  
    
      
        n
        ≥
        m
        k
      
    
    {\displaystyle n\geq mk}
  
. Aunque no es necesario, se supondrá para la explicación, que
cada sub-hebra sigue otra consecutiva (sin ninguna otra base entre medio). Cada sub-hebra representa exactamente una variable 
booleana, un  bit. Las subhebras deben ser suficientemente diferentes unas de otras. Cada sticker es de largo m y complementario a una y solo una sub-hebra.

Una sub-hebra está prendida o apagada, dependiendo de si tiene unido su sticker o no. Si tiene su sticker pegado, está prendida (es verdadera o 1), en el otro caso está apagada (falso o 0).

Es importante crear las hebras memoria de tal forma que un sticker no pueda pegarse entre dos sub-hebras. Hay que considerar también que no todas las cadenas son posibles, por lo que al hacer un experimento real hay que buscar un óptimo.

Tanto en el experimento de Adleman, como en la solución de Richard J. Lipton del problema de satifacibilidad, no hay una hebra larga de la cual partir, sino que hebras cortas que se van uniendo paso a paso, dejando un sobrante para que se pueda pegar otra hebra en cada paso. La densidad de información en ambos casos (con hebras largas o cortas), es básicamente la misma 
  
    
      
        
          
            1
            m
          
        
      
    
    {\displaystyle {\frac {1}{m}}}
  
 bits por base. Aunque el máximo teórico es dos bits por base, una densidad tan alta deja cualquier computador molecular basado en separación peligrosamente propenso a errores.

## Operaciones

El elemento básico es un tubo test, o simplemente tubo, el cual es un multiconjunto de hebras memorias. Las operaciones válidas son: merge (combinar), separate (separar), set (encender), y clear (apagar).

- La operación merge es mezclar 2 tubos en uno. Así las memorias de dos tubos de entrada con sus stickers pegados sin perturbaciones se combinan para formar el multiconjunto unión de ambos.

- La operación separate produce, dado un tubo de entrada N, y un entero i,  
  
    
      
        1
        ≤
        i
        ≤
        k
      
    
    {\displaystyle 1\leq i\leq k}
  
, dos tubos nuevos, +(N,i) y -(N,i). El tubo +(N,i) (respectivamente -(N,i)) consiste en todos las hebras memoria en el tubo original N, donde la i-ésima sub-hebra está prendida (respectivamente apagada).

- Para un tubo dado N y un entero i, 
  
    
      
        1
        ≤
        i
        ≤
        k
      
    
    {\displaystyle 1\leq i\leq k}
  
, la operación set produce un nuevo tubo test set(N,i), donde la i-ésima sub-hebra de cada hebra memoria está encendida. (Esto es, se le adhiere el sticker apropiado si la i-ésima subhebra estaba apagada, y se deja sin cambios si ya tenía uno).

- Finalmente para un tubo dado N y un entero i, 
  
    
      
        1
        ≤
        i
        ≤
        k
      
    
    {\displaystyle 1\leq i\leq k}
  
, la operación clear produce un nuevo tubo test clear(N,i), donde la i-ésima sub-hebra de cada hebra memoria está apagada, es decir, un eventual sticker fue removido de ella.
La computación consiste en una secuencia de operaciones merge, separate, set y clear. Las entradas y salidas (Input, Output) son tubos test. Para leer la salida, una hebra memoria debe ser aislada del tubo y determinar que stickers tiene adheridos o sino, determinar si el tubo de salida no tiene hebras memoria.

La entrada inicial (tubo) será una biblioteca de hebras memoria. En particular una biblioteca (k,l), 
  
    
      
        1
        ≤
        l
        ≤
        k
      
    
    {\displaystyle 1\leq l\leq k}
  
 consiste en memorias con k sub-hebras, de las cuales las últimas k-l están apagadas, mientras las primeras l están prendidas o apagadas en todas las combinaciones posibles. En binario sería 
  
    
      
        w
        
          0
          
            k
            −
            l
          
        
      
    
    {\displaystyle w0^{k-l}}
  
, con w una cadena binaria arbitraria de tamaño l. En el tubo inicial, las primeras l hebras de la memoria representan la entrada, y el resto se para uso intermedio y salida.

El paradigma computacional asociado con el modelo sticker es resolver problemas difíciles buscando exhaustivamente en todas las combinaciones posibles de largo l. Todos las 
  
    
      
        
          2
          
            l
          
        
      
    
    {\displaystyle 2^{l}}
  
 posibles entradas son analizadas en paralelo. Este paradigma es la esencia de la computación de ADN en general.

## Aplicaciones

El 2002, investigadores del Instituto Weizmann de Ciencias en Rehovot, Israel, crearon un computador programable, compuesta de enzimas y moléculas de ADN.[4]​  El 28 de abril de 2004, Ehud Shapiro, Yaakov Benenson, Binyamin Gil, Uri Ben-Dor, y Rivka Adar del Instituto Weizman anunciaron en la revista Nature que habían construido un computador basado en ADN.[5]​ Aunque era solo un autómata finito determinista, de dos estados, al unirlo con un módulo de entrada y salida, fue capaz de diagnosticar actividad cancerígena y liberar drogas para su tratamiento.

## Ejemplo de Aplicación

Se muestran a continuación los pasos seguidos por Adleman para resolver el problema del camino Hamiltoniano.

Se tiene un grafo direccionado G con n vértices vi. Existen aristas conectando algunos vértices. Se denota la arista que conecta al vértice vi con vj como ei→j.

Para simplificar el ejemplo, y sin pérdida de generalidad, se considera que se comienza en el vértice v1 y se termina en el vértice vn.

Los pasos son:

- Generar caminos aleatorios.

- Seleccionar aquellos que comiencen con v1 y terminen con vn.

- Seleccionar solo aquellos caminos que cuenten con exactamente n vértices.

- Seleccionar solo aquellos caminos que tengan cada vértice una sola vez.

- Si queda algún camino en la muestra, responder SI, de otra forma responder NO.
La forma en que Adleman lo solucionó usando ADN se muestra a continuación.

A cada vértice vi del grafo se le asigna un oligonucleótido si de un largo de 20 pares base. Estos se generan al azar, cuidando de que ninguno sea idéntico a otro.

A su vez, a cada arista ei→j se le asigna un oligo Ei→j, compuesto de una forma particular; se forma un segundo oligo tomando la segunda mitad del vértice de partida y la primera mitad del vértice de llegada. El oligo que se le asigna a la arista es el complemento de esta hebra.

El primer paso se lleva a cabo mezclando muestras de grandes cantidades de oligos representando vértices y aristas, y se agrega una solución de ADN ligasa para generar una gran cantidad de caminos aleatorios. Gracias a la composición de los oligos, se asegura que se respete la estructura del grafo, y gracias al tamaño de la muestra es probable que el camino Hamiltoniano buscado esté presente.

Para ejecutar el segundo paso, se lleva a cabo un proceso de RCP usando como cebadores los oligos correspondientes a sn y el complemento de s0. Notar que estos dos cebadores representan los complementos de los extremos de las cadenas que interesan, que son las que comienzan con s0 y comienzan con sn. Así se asegura la replicación de los caminos válidos para el siguiente paso solamente.

El tercer paso se efectúa usando electroforesis. Este proceso separa las moléculas en función de su tamaño, dejando las más cortas a un lado y las más largas al otro lado de la matriz. Se seleccionan solo las moléculas presentes en el rango de largo apropiado para el próximo paso.

El cuarto paso se lleva a cabo mediante un proceso de purificación de proteínas. Se separan las hebras de los caminos, como también las hebras para cada vértice. Se asocian las hebras simples de los vértices con partículas magnéticas. Luego se asocia cada hebra simple de los caminos del paso cuatro con estas partículas, mientras que los caminos que no se logran asociar, por la ausencia de algún vértice, son removidos junto con la solución. Se efectúa este proceso para cada vértice en el camino.

Con las muestras restantes se efectúa un proceso de RCP, al igual que el descrito anteriormente, para luego aplicar electroforesis. Se analiza la matriz para ver si quedan o no muestras, y se responde si el camino fue encontrado o no.

## Véase también

- Computación cuántica

- Nanotecnología

- Chip de ADN

- MAYA II

- Computación paralela

## Enlaces externos

- Método para resolver el problema del camino Hamiltoniano (inglés)

- Dirk de Pol: DNS – Ein neuer Supercomputer?. In: Die Neue Gesellschaft / Frankfurter Hefte  ISSN 0177-6738, Heft 2/96, Februar 1996, S. 170–172  (alemán e inglés)

## Referencias

- ↑ Leonard M. Adleman (1994-11-11). «Molecular Computation Of Solutions To Combinatorial Problems». Science (journal) 266 (11): 1021-1024. Archivado desde el original el 6 de febrero de 2005. 
La primera publicación de computación basada en ADN. Describe una solución realizada en Problema del camino Hamiltoniano dirigido.

- ↑ Dan Boneh, Christopher Dunworth, Richard J. Lipton, and Jiri Sgall (1996). «On the Computational Power of DNA». DAMATH: Discrete Applied Mathematics and Combinatorial Operations Research and Computer Science 71.  — Describe una solución al Problema de satisfacibilidad booleana.

- ↑ Lila Kari, Greg Gloor, Sheng Yu (enero de 2000). «Using DNA to solve the Bounded Post Correspondence Problem». Theoretical Computer Science 231 (2): 192-203. Archivado desde el original el 18 de abril de 2008. Consultado el 24 de junio de 2008.  — describe una solución al Problema de satisfacibilidad booleana ligado, un problema duro en promedio, NP-completo.

- ↑ Computer Made from DNA and Enzymes

- ↑ 
Yaakov Benenson1, Binyamin Gil, Uri Ben-Dor, Rivka Adar, Ehud Shapiro (2004-04-28). «An autonomous molecular computer for logical control of gene expression». Nature (journal) 429: 423-429. 

Control de autoridades

- Proyectos Wikimedia

-  Datos: Q177126

- Identificadores

- LCCN: sh96004522

- NLI: 987007551662305171

- Diccionarios y enciclopedias

- Britannica: url

-  Datos: Q177126

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.