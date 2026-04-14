---
title: "Factor de estructura"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Factor de estructura
    
    
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
  
  
    
      
        
          
            
              
## Factor de estructura

            
            
            
              
                

              

              En la física de la materia condensada y la cristalografía, se conoce como factor de estructura o factor de estructura estático a la función que describe la dispersión de un haz incidente de radiación por la materia. El factor de estructura es un concepto que facilita la interpretación de los patrones de interferencia obtenidos en experimentos de difracción de rayos X, de electrones y de neutrones. Cuando es necesario examinar la evolución temporal del sistema estudiado, se utiliza el factor de estructura dinámico.

## Definición matemática

Sea 
  
    
      
        ϕ
        (
        
          r
        
        )
      
    
    {\displaystyle \phi (\mathbf {r} )}
  
 una función escalar definida en un volumen 
  
    
      
        V
      
    
    {\displaystyle V}
  
 que represente la distribución espacial de una propiedad física. Si la función 
  
    
      
        ϕ
        (
        
          r
        
        )
      
    
    {\displaystyle \phi (\mathbf {r} )}
  
 es integrable, se puede definir el factor de estructura como la transformada de Fourier:

  
    
      
        F
        (
        
          q
        
        )
        =
        
          ∫
          
            V
          
        
        ϕ
        (
        
          r
        
        )
         
        
          
            e
          
          
            −
            i
            
              q
            
            
              r
            
          
        
        
          d
        
        
          r
        
      
    
    {\displaystyle F(\mathbf {q} )=\int _{V}\phi (\mathbf {r} )\ \mathrm {e} ^{-i\mathbf {q} \mathbf {r} }\mathrm {d} \mathbf {r} }
  

La expresión de 
  
    
      
        ϕ
      
    
    {\displaystyle \phi }
  
 en el espacio recíproco es muy útil para la interpretación de los experimentos de dispersión y difracción de una onda electromagnética. Se puede demostrar que en la aproximación de Born, aplicable cuando el campo dispersado es mucho más débil que el campo incidente, la amplitud de la onda asociada dispersada es proporcional a 
  
    
      
        
          F
          (
          
            q
          
          )
        
      
    
    {\displaystyle \textstyle F(\mathbf {q} )}
  
, donde 
  
    
      
        
          q
        
      
    
    {\displaystyle \mathbf {q} }
  
 es el vector de transferencia, igual a la diferencia entre los vectores de onda del campo incidente y dispersado.[1]​ A menudo, solo se puede medir la intensidad de la onda dispersada 
  
    
      
        
          I
          (
          
            q
          
          )
        
      
    
    {\displaystyle \textstyle I(\mathbf {q} )}
  
, relacionada con 
  
    
      
        
          F
          (
          
            q
          
          )
        
      
    
    {\displaystyle \textstyle F(\mathbf {q} )}
  
 por la expresión 
  
    
      
        
          I
          (
          
            q
          
          )
          ∼
          
            
              |
              
                F
                (
                
                  q
                
                )
              
              |
            
            
              2
            
          
        
      
    
    {\displaystyle \textstyle I(\mathbf {q} )\sim \left|F(\mathbf {q} )\right|^{2}}
  
.

Cuando el sistema a estudiar está compuesto de un número 
  
    
      
        N
      
    
    {\displaystyle N}
  
 de átomos es conveniente expresar  
  
    
      
        ϕ
      
    
    {\displaystyle \phi }
  
 en función de la morfología o «forma» de las partículas individuales, descrita mediante la función  
  
    
      
        f
        (
        
          r
        
        )
      
    
    {\displaystyle f(\mathbf {r} )}
  
:

  
    
      
        ϕ
        (
        
          r
        
        )
        =
        
          ∑
          
            j
            =
            1
          
          
            N
          
        
        f
        (
        
          r
        
        −
        
          
            R
          
          
            j
          
        
        )
        =
        f
        (
        
          r
        
        )
        ∗
        
          ∑
          
            j
            =
            1
          
          
            N
          
        
        δ
        (
        
          r
        
        −
        
          
            R
          
          
            j
          
        
        )
      
    
    {\displaystyle \phi (\mathbf {r} )=\sum _{j=1}^{N}f(\mathbf {r} -\mathbf {R} _{j})=f(\mathbf {r} )\ast \sum _{j=1}^{N}\delta (\mathbf {r} -\mathbf {R} _{j})}
  

donde 
  
    
      
        
          
            
              R
            
            
              j
            
          
          ,
          j
          =
          1
          ,
          
          …
          ,
          
          N
        
      
    
    {\displaystyle \textstyle \mathbf {R} _{j},j=1,\,\ldots ,\,N}
  
 denota la posición de cada partícula. De esta forma se obtiene una expresión de la intensidad de la onda dispersada como la convolución de la función 
  
    
      
        f
      
    
    {\displaystyle f}
  
, que describe las características de las partículas con la suma de la función delta de Dirac, que describe su posición.[2]​
Dado que la transformada Fourier de una convolución es igual al producto de las transformadas de los dos factores, se obtiene:

  
    
      
        F
        (
        
          q
        
        )
        =
        f
        (
        
          q
        
        )
        
          ∑
          
            j
            =
            1
          
          
            N
          
        
        
          
            e
          
          
            −
            i
            
              q
            
            
              
                R
              
              
                j
              
            
          
        
      
    
    {\displaystyle F(\mathbf {q} )=f(\mathbf {q} )\sum _{j=1}^{N}\mathrm {e} ^{-i\mathbf {q} \mathbf {R} _{j}}}
  

lo que resulta en:

  
    
      
        I
        (
        
          q
        
        )
        ∼
        
          
            |
            
              F
              (
              
                q
              
              )
            
            |
          
          
            2
          
        
        =
        
          
            |
            
              f
              (
              
                q
              
              )
            
            |
          
          
            2
          
        
        ×
        
          (
          
            
              ∑
              
                j
                =
                1
              
              
                N
              
            
            
              
                e
              
              
                −
                i
                
                  q
                
                
                  
                    R
                  
                  
                    j
                  
                
              
            
          
          )
        
        ×
        
          (
          
            
              ∑
              
                k
                =
                1
              
              
                N
              
            
            
              
                e
              
              
                i
                
                  q
                
                
                  
                    R
                  
                  
                    k
                  
                
              
            
          
          )
        
        =
        
          
            |
            
              f
              (
              
                q
              
              )
            
            |
          
          
            2
          
        
        
          ∑
          
            j
            k
          
        
        
          
            e
          
          
            −
            i
            
              q
            
            (
            
              
                R
              
              
                j
              
            
            −
            
              
                R
              
              
                k
              
            
            )
          
        
      
    
    {\displaystyle I(\mathbf {q} )\sim \left|F(\mathbf {q} )\right|^{2}=\left|f(\mathbf {q} )\right|^{2}\times \left(\sum _{j=1}^{N}\mathrm {e} ^{-i\mathbf {q} \mathbf {R} _{j}}\right)\times \left(\sum _{k=1}^{N}\mathrm {e} ^{i\mathbf {q} \mathbf {R} _{k}}\right)=\left|f(\mathbf {q} )\right|^{2}\sum _{jk}\mathrm {e} ^{-i\mathbf {q} (\mathbf {R} _{j}-\mathbf {R} _{k})}}
  

En varias aplicaciones se define el factor de estructura geométrico como el factor que depende exclusivamente de la posición relativa de las partículas 
  
    
      
        S
        (
        
          Q
        
        )
      
    
    {\displaystyle S(\mathbf {Q} )}
  
 como

  
    
      
        S
        (
        
          Q
        
        )
        =
        
          
            1
            N
          
        
        
          
            e
          
          
            −
            i
            
              q
            
            (
            
              
                R
              
              
                j
              
            
            −
            
              
                R
              
              
                k
              
            
            )
          
        
      
    
    {\displaystyle S(\mathbf {Q} )={\frac {1}{N}}\mathrm {e} ^{-i\mathbf {q} (\mathbf {R} _{j}-\mathbf {R} _{k})}}
  

En este, caso, la intensidad dispersada se expresa como:

  
    
      
        I
        (
        
          q
        
        )
        =
        N
        
          
            |
            
              f
              (
              
                q
              
              )
            
            |
          
          
            2
          
        
        S
        (
        
          q
        
        )
      
    
    {\displaystyle I(\mathbf {q} )=N\left|f(\mathbf {q} )\right|^{2}S(\mathbf {q} )}
  

Si se conoce el valor del factor de estructura, se puede obtener información sobre la distribución espacial de las componentes del sistema mediante la transformada de Fourier inversa.

## Factor de estructura cristalino

En un cristal, las partículas constituyentes están dispuestas periódicamente en las tres direcciones espaciales, formando una red. Para describir la difracción por un cristal, se considera que todas las partículas de la red tienen un entorno idéntico, es decir, forman una red de Bravais; Si 
  
    
      
        
          
            R
          
          
            j
          
        
      
    
    {\displaystyle \mathbf {R} _{j}}
  
 son las posiciones de las partículas con respecto a un punto cualquiera de la red y 
  
    
      
        
          
            R
          
          
            n
          
        
      
    
    {\displaystyle \mathbf {R} _{n}}
  
 es un vector de la red, el factor de estructura se denota como:

  
    
      
        F
        (
        
          q
        
        )
        =
        
          ∑
          
            j
            =
            1
          
          
            M
          
        
        f
        (
        
          q
        
        
          )
          
            j
          
        
        
          
            e
          
          
            −
            i
            
              q
            
            
              
                R
              
              
                j
              
            
          
        
        
          ∑
          
            n
            =
            1
          
          
            N
          
        
        
          
            e
          
          
            −
            i
            
              q
            
            
              
                R
              
              
                n
              
            
          
        
      
    
    {\displaystyle F(\mathbf {q} )=\sum _{j=1}^{M}f(\mathbf {q} )_{j}\mathrm {e} ^{-i\mathbf {q} \mathbf {R} _{j}}\sum _{n=1}^{N}\mathrm {e} ^{-i\mathbf {q} \mathbf {R} _{n}}}
  

El primer factor corresponde al factor de estructura de los 
  
    
      
        M
      
    
    {\displaystyle M}
  
 átomos en la celda unidad del cristal, y el segundo, a la suma sobre todos los puntos 
  
    
      
        N
      
    
    {\displaystyle N}
  
 de la red. El vector 
  
    
      
        
          
            R
          
          
            n
          
        
      
    
    {\displaystyle \mathbf {R} _{n}}
  
 se puede expresar como una combinación lineal de los vectores de los vectores base de la red:

  
    
      
        
          
            R
          
          
            n
          
        
        =
        
          n
          
            1
          
        
        
          a
        
        +
        
          n
          
            2
          
        
        
          b
        
        +
        
          n
          
            3
          
        
        
          c
        
      
    
    {\displaystyle \mathbf {R} _{n}=n_{1}\mathbf {a} +n_{2}\mathbf {b} +n_{3}\mathbf {c} }
  

Similarmente, 
  
    
      
        
          q
        
      
    
    {\displaystyle \mathbf {q} }
  
 se puede expresar como una combinación lineal de vectores de la red recíproca calculada como la transformada de Fourier de la red cristalina:

  
    
      
        
          q
        
        =
        h
        
          
            a
          
          
            ∗
          
        
        +
        k
        
          
            b
          
          
            ∗
          
        
        +
        l
        
          
            c
          
          
            ∗
          
        
      
    
    {\displaystyle \mathbf {q} =h\mathbf {a} ^{\ast }+k\mathbf {b} ^{\ast }+l\mathbf {c} ^{\ast }}
  

Puesto que el producto de dos vectores de una red y su correspondiente red recíproca es 
  
    
      
        
          
            R
          
          
            n
          
        
        
          q
        
        =
        2
        π
        (
        
          n
          
            1
          
        
        h
        +
        
          n
          
            2
          
        
        k
        +
        
          n
          
            3
          
        
        l
        )
        =
        2
        π
        n
      
    
    {\displaystyle \mathbf {R} _{n}\mathbf {q} =2\pi (n_{1}h+n_{2}k+n_{3}l)=2\pi n}
  
, donde 
  
    
      
        n
      
    
    {\displaystyle n}
  
 es un número entero, se deduce que se observará difracción cristalina si el vector de transferencia de momento 
  
    
      
        
          q
        
      
    
    {\displaystyle \mathbf {q} }
  
 es un vector de la red recíproca,[3]​ lo que se conoce como «condición de Laue».

## Red unidimensional

En el caso especial de que las partículas o moléculas dispuestas en una línea con un periodo del 
  
    
      
        a
      
    
    {\displaystyle a}
  
 cuyas posiciones vienen dadas por 
  
    
      
        
          R
          
            n
          
        
        =
        a
        (
        j
        −
        (
        N
        −
        1
        )
        
          /
        
        2
        )
      
    
    {\displaystyle R_{n}=a(j-(N-1)/2)}
  
 (para simplificar, consideramos que 
  
    
      
        N
      
    
    {\displaystyle N}
  
 es impar), la suma de los factores de fase es una serie geométrica y el factor de la estructura se convierte en:

  
    
      
        F
        (
        q
        )
        =
        
          
            |
            
              
                
                  1
                  −
                  
                    
                      e
                    
                    
                      −
                      i
                      N
                      q
                      a
                    
                  
                
                
                  1
                  −
                  
                    
                      e
                    
                    
                      −
                      i
                      q
                      a
                    
                  
                
              
            
            |
          
          
            2
          
        
        =
        
          
            [
            
              
                
                  sin
                  ⁡
                  (
                  N
                  q
                  a
                  
                    /
                  
                  2
                  )
                
                
                  sin
                  ⁡
                  (
                  q
                  a
                  
                    /
                  
                  2
                  )
                
              
            
            ]
          
          
            2
          
        
      
    
    {\displaystyle F(q)=\left|{\frac {1-\mathrm {e} ^{-iNqa}}{1-\mathrm {e} ^{-iqa}}}\right|^{2}=\left[{\frac {\sin(Nqa/2)}{\sin(qa/2)}}\right]^{2}}
  

De esta expresión para 
  
    
      
        F
        (
        q
        )
      
    
    {\displaystyle F(q)}
  
 , se obtienen las siguientes conclusiones:

- La red recíproca tiene una separación entre sus puntos igual a 
  
    
      
        2
        π
        
          /
        
        a
      
    
    {\displaystyle 2\pi /a}
  

- la intensidad de los máximos aumenta con el número de partículas, hasta llegar a 
  
    
      
        N
      
    
    {\displaystyle N}
  
 lo que se puede demostrar mediante el cálculo del límite 
  
    
      
        F
        (
        q
        →
        0
        )
      
    
    {\displaystyle F(q\to 0)}
  
 utilizando, por ejemplo, la regla de l'Hôpital; la intensidad en los puntos medios es  
  
    
      
        1
        
          /
        
        N
      
    
    {\displaystyle 1/N}
  
, por evaluación directa y la anchura del pico también disminuye como 
  
    
      
        1
        
          /
        
        N
      
    
    {\displaystyle 1/N}
  
 . Cuando 
  
    
      
        N
      
    
    {\displaystyle N}
  
 tiende a infinito, los picos se convierten en funciones delta de Dirac.

## Casos especiales de redes tridimensionales

La simetría de la red y del cristal resulta en relaciones entre los factores de estructura para diferentes valores de 
  
    
      
        
          q
        
      
    
    {\displaystyle \mathbf {q} }
  
 que son útiles para el análisis de patrones de difracción cristalina; en el caso particular de cristales pertenecientes al sistema cúbico, caracterizado por vectores base de la misma longitud, 
  
    
      
        a
      
    
    {\displaystyle a}
  
 formando ángulos de 90°, se pueden definir varias redes de Bravais y elementos de simetría, como los siguientes:

Estructura cúbica centrada en el cuerpo (bcc)
Por convención, una red de tipo bcc contiene dos puntos, uno en el origen 
  
    
      
        
          
            r
          
          
            0
          
        
        =
        (
        0
        ,
        0
        ,
        0
        )
      
    
    {\displaystyle \mathbf {r} _{0}=(0,0,0)}
  
 y otro en 
  
    
      
        
          
            r
          
          
            1
          
        
        =
        (
        1
        
          /
        
        2
        ,
        1
        
          /
        
        2
        ,
        1
        
          /
        
        2
        )
      
    
    {\displaystyle \mathbf {r} _{1}=(1/2,1/2,1/2)}
  
, es decir, con  coordenadas 
  
    
      
        (
        a
        
          /
        
        2
        )
        (
        
          
            u
          
          
            1
          
        
        +
        
          
            u
          
          
            2
          
        
        +
        
          
            u
          
          
            3
          
        
        )
      
    
    {\displaystyle (a/2)(\mathbf {u} _{1}+\mathbf {u} _{2}+\mathbf {u} _{3})}
  
, donde 
  
    
      
        (
        
          
            u
          
          
            1
          
        
      
    
    {\displaystyle ({u}_{1}}
  
, 
  
    
      
        
          
            u
          
          
            2
          
        
      
    
    {\displaystyle {u}_{2}}
  
 y 
  
    
      
        
          
            u
          
          
            3
          
        
        )
      
    
    {\displaystyle {u}_{3})}
  
 son vectores unitarios. La red recíproca es cúbica, con vectores base de magnitud 
  
    
      
        2
        π
        
          /
        
        a
      
    
    {\displaystyle 2\pi /a}
  
 y los puntos de la red recíproca se pueden expresar como 
  
    
      
        
          q
        
        =
        2
        π
        a
        (
        h
        
          
            u
          
          
            1
          
          
            ∗
          
        
        +
        k
        
          
            u
          
          
            2
          
          
            ∗
          
        
        +
        l
        
          
            u
          
          
            3
          
          
            ∗
          
        
        )
      
    
    {\displaystyle \mathbf {q} =2\pi a(h\mathbf {u} _{1}^{\ast }+k\mathbf {u} _{2}^{\ast }+l\mathbf {u} _{3}^{\ast })}
  

  
    
      
        F
        (
        
          q
        
        )
        =
        f
        (
        
          q
        
        )
        (
        
          
            e
          
          
            0
          
        
        +
        
          
            e
          
          
            −
            i
            2
            π
            (
            h
            a
            
              /
            
            2
            +
            k
            a
            
              /
            
            2
            +
            l
            a
            
              /
            
            2
            )
          
        
        =
        f
        (
        
          q
        
        )
        (
        1
        +
        
          e
          
            −
            i
            π
            (
            h
            +
            k
            +
            l
            )
          
        
        )
      
    
    {\displaystyle F(\mathbf {q} )=f(\mathbf {q} )(\mathrm {e} ^{0}+\mathrm {e} ^{-i2\pi (ha/2+ka/2+la/2)}=f(\mathbf {q} )(1+e^{-i\pi (h+k+l)})}
  

Puesto que 
  
    
      
        
          e
          
            −
            i
            π
            (
            h
            +
            k
            +
            l
            )
          
        
        =
        −
        1
      
    
    {\displaystyle e^{-i\pi (h+k+l)}=-1}
  
 si 
  
    
      
        h
        +
        k
        +
        l
      
    
    {\displaystyle h+k+l}
  
 es un número impar, el factor de estructura será nulo —es decir, no se observará difracción— para los vectores  
  
    
      
        
          q
        
        =
        (
        h
        ,
        k
        ,
        l
        )
      
    
    {\displaystyle \mathbf {q} =(h,k,l)}
  
 que cumplan esa condición; en cambio,  
  
    
      
        
          e
          
            −
            i
            π
            (
            h
            +
            k
            +
            l
            )
          
        
        =
        1
      
    
    {\displaystyle e^{-i\pi (h+k+l)}=1}
  
 cuando 
  
    
      
        h
        +
        k
        +
        l
      
    
    {\displaystyle h+k+l}
  
 sea 0 o un número par y en este caso el factor de estructura será 
  
    
      
        2
        f
        (
        
          q
        
        )
      
    
    {\displaystyle 2f(\mathbf {q} )}
  
.

Estructura cúbica centrada en las caras (fcc)
Las redes fcc cuentan con cuatro puntos, con índices 
  
    
      
        
          
            r
          
          
            0
          
        
        =
        (
        0
        ,
        0
        ,
        0
        )
      
    
    {\displaystyle \mathbf {r} _{0}=(0,0,0)}
  
, 
  
    
      
        
          
            r
          
          
            1
          
        
        =
        (
        1
        
          /
        
        2
        ,
        1
        
          /
        
        2
        ,
        0
        )
      
    
    {\displaystyle \mathbf {r} _{1}=(1/2,1/2,0)}
  
, 
  
    
      
        
          
            r
          
          
            2
          
        
        =
        (
        1
        
          /
        
        2
        ,
        0
        ,
        1
        
          /
        
        2
        )
      
    
    {\displaystyle \mathbf {r} _{2}=(1/2,0,1/2)}
  
 y 
  
    
      
        
          
            r
          
          
            3
          
        
        =
        (
        0
        ,
        1
        
          /
        
        2
        ,
        1
        
          /
        
        2
        )
      
    
    {\displaystyle \mathbf {r} _{3}=(0,1/2,1/2)}
  
. En este caso el factor de estructura es

  
    
      
        F
        (
        
          q
        
        )
        =
        f
        (
        
          q
        
        )
        (
        1
        +
        
          
            (
            −
            1
            )
          
          
            h
            +
            k
          
        
        +
        
          
            (
            −
            1
            )
          
          
            k
            +
            l
          
        
        +
        
          
            (
            −
            1
            )
          
          
            h
            +
            l
          
        
        )
      
    
    {\displaystyle F(\mathbf {q} )=f(\mathbf {q} )(1+\mathrm {(-1)} ^{h+k}+\mathrm {(-1)} ^{k+l}+\mathrm {(-1)} ^{h+l})}
  

Esta expresión es igual a 
  
    
      
        4
        f
        (
        
          q
        
        )
      
    
    {\displaystyle 4f(\mathbf {q} )}
  
 siempre que los índices 
  
    
      
        h
      
    
    {\displaystyle h}
  
,  
  
    
      
        k
      
    
    {\displaystyle k}
  
 y 
  
    
      
        l
      
    
    {\displaystyle l}
  
 sean todos pares o todos impares, y 0 en caso contrario.

Red de diamante
Esta red, así llamada por ser característica de los diamantes, al igual que del silicio y otros semiconductores tiene ocho puntos, con índices

- 
  
    
      
        
          
            r
          
          
            0
          
        
        =
        (
        0
        ,
        0
        ,
        0
        )
      
    
    {\displaystyle \mathbf {r} _{0}=(0,0,0)}
  

- 
  
    
      
        
          
            r
          
          
            1
          
        
        =
        (
        1
        
          /
        
        2
        ,
        1
        
          /
        
        2
        ,
        0
        )
      
    
    {\displaystyle \mathbf {r} _{1}=(1/2,1/2,0)}
  

- 
  
    
      
        
          
            r
          
          
            2
          
        
        =
        (
        1
        
          /
        
        2
        ,
        0
        ,
        1
        
          /
        
        2
        )
      
    
    {\displaystyle \mathbf {r} _{2}=(1/2,0,1/2)}
  

- 
  
    
      
        
          
            r
          
          
            3
          
        
        =
        (
        0
        ,
        1
        
          /
        
        2
        ,
        1
        
          /
        
        2
        )
      
    
    {\displaystyle \mathbf {r} _{3}=(0,1/2,1/2)}
  

- 
  
    
      
        
          
            r
          
          
            4
          
        
        =
        (
        1
        
          /
        
        4
        ,
        1
        
          /
        
        4
        ,
        1
        
          /
        
        4
        )
      
    
    {\displaystyle \mathbf {r} _{4}=(1/4,1/4,1/4)}
  

- 
  
    
      
        
          
            r
          
          
            5
          
        
        =
        (
        3
        
          /
        
        4
        ,
        3
        
          /
        
        4
        ,
        1
        
          /
        
        4
        )
      
    
    {\displaystyle \mathbf {r} _{5}=(3/4,3/4,1/4)}
  

- 
  
    
      
        
          
            r
          
          
            6
          
        
        =
        (
        3
        
          /
        
        4
        ,
        1
        
          /
        
        4
        ,
        3
        
          /
        
        4
        )
      
    
    {\displaystyle \mathbf {r} _{6}=(3/4,1/4,3/4)}
  

- 
  
    
      
        
          
            r
          
          
            7
          
        
        =
        (
        1
        
          /
        
        4
        ,
        3
        
          /
        
        4
        ,
        3
        
          /
        
        4
        )
      
    
    {\displaystyle \mathbf {r} _{7}=(1/4,3/4,3/4)}
  

El factor se estructura es

  
    
      
        F
        (
        
          q
        
        )
        =
        f
        (
        
          q
        
        )
        (
        1
        +
        
          
            (
            −
            1
            )
          
          
            h
            +
            k
          
        
        +
        
          
            (
            −
            1
            )
          
          
            k
            +
            l
          
        
        +
        
          
            (
            −
            1
            )
          
          
            h
            +
            l
          
        
        +
        
          
            i
          
          
            h
            +
            k
            +
            l
          
        
        +
        
          
            i
          
          
            3
            h
            +
            k
            +
            3
            l
          
        
        +
        
          
            i
          
          
            3
            h
            +
            3
            k
            +
            l
          
        
        +
        
          
            i
          
          
            h
            +
            3
            k
            +
            3
            l
          
        
        )
      
    
    {\displaystyle F(\mathbf {q} )=f(\mathbf {q} )(1+\mathrm {(-1)} ^{h+k}+\mathrm {(-1)} ^{k+l}+\mathrm {(-1)} ^{h+l}+\mathrm {i} ^{h+k+l}+\mathrm {i} ^{3h+k+3l}+\mathrm {i} ^{3h+3k+l}+\mathrm {i} ^{h+3k+3l})}
  

Si 
  
    
      
        h
      
    
    {\displaystyle h}
  
,  
  
    
      
        k
      
    
    {\displaystyle k}
  
 y 
  
    
      
        l
      
    
    {\displaystyle l}
  
 son todos pares o impares el factor de estructura toma los siguientes valores:

- si 
  
    
      
        h
        +
        k
        +
        l
      
    
    {\displaystyle h+k+l}
  
 es impar,  
  
    
      
        F
        =
        4
        f
        (
        1
        +
        i
        )
      
    
    {\displaystyle F=4f(1+i)}
  
 o 
  
    
      
        F
        =
        4
        f
        (
        1
        −
        i
        )
      
    
    {\displaystyle F=4f(1-i)}
  

- si 
  
    
      
        h
        +
        k
        +
        l
      
    
    {\displaystyle h+k+l}
  
 es par y 
  
    
      
        h
        +
        k
        +
        l
        =
        4
        n
      
    
    {\displaystyle h+k+l=4n}
  
, 
  
    
      
        F
        =
        8
        f
      
    
    {\displaystyle F=8f}
  

- si 
  
    
      
        h
        +
        k
        +
        l
      
    
    {\displaystyle h+k+l}
  
 es par y 
  
    
      
        h
        +
        k
        +
        l
        ≠
        4
        n
      
    
    {\displaystyle h+k+l\neq 4n}
  
, 
  
    
      
        F
        =
        0
      
    
    {\displaystyle F=0}
  

el factor de estructura es 0 en todos los casos restantes.

## Líquidos

A diferencia de los cristales, la materia en estado líquido no posee orden de alcance largo, por lo que el factor de estructura no exhibe los picos discretos que caracterizan a la difracción por cristales. Sin embargo, los líquidos tienen un cierto grado de orden de corto alcance, que depende de su densidad y la magnitud de la interacción entre sus partículas conformantes. Como los líquidos son isotrópicos, el factor de estructura solo depende del módulo del vector 
  
    
      
        q
        =
        
          |
          
            q
          
          |
        
      
    
    {\displaystyle q=\left|\mathbf {q} \right|}
  
 y no de su dirección.[4]​ Si en la expresión general para el factor de estructura se separan los términos diagonales 
  
    
      
        j
        =
        k
      
    
    {\displaystyle j=k}
  
, cuya fase es 0 y son por tanto iguales a la unidad se obtiene:

  
    
      
        S
        (
        q
        )
        =
        1
        +
        
          
            1
            N
          
        
        
          ∑
          
            j
            ≠
            k
          
        
        
          
            e
          
          
            −
            i
            
              q
            
            (
            
              
                R
              
              
                j
              
            
            −
            
              
                R
              
              
                k
              
            
            )
          
        
      
    
    {\displaystyle S(q)=1+{\frac {1}{N}}\sum _{j\neq k}\mathrm {e} ^{-i\mathbf {q} (\mathbf {R} _{j}-\mathbf {R} _{k})}}
  

## Gas ideal

En el caso extremo de que no exista ninguna interacción entre las partículas, los términos no diagonales 
  
    
      
        j
        ≠
        k
      
    
    {\displaystyle j\neq k}
  
 del factor de estructura para líquidos se anulan, por ser las posiciones 
  
    
      
        
          
            R
          
          
            j
          
        
      
    
    {\displaystyle \mathbf {R} _{j}}
  
 y 
  
    
      
        
          
            R
          
          
            k
          
        
      
    
    {\displaystyle \mathbf {R} _{k}}
  
 totalmente independientes entre sí. Eso conlleva que  
  
    
      
        S
        (
        q
        )
        =
        1
      
    
    {\displaystyle S(q)=1}
  
 y  
  
    
      
        F
        (
        q
        )
      
    
    {\displaystyle F(q)}
  
  es isotrópico y su magnitud depende sólo del tipo de partículas que dispersan la radiación incidente.

## Casos límite

Incluso cuando existe interacción entre las partículas, 
  
    
      
        S
        (
        q
        )
        ≃
        1
      
    
    {\displaystyle S(q)\simeq 1}
  
 para valores altos de 
  
    
      
        q
      
    
    {\displaystyle q}
  
. Cuando 
  
    
      
        q
      
    
    {\displaystyle q}
  
 es pequeño, es decir, se examina el sistema sobre distancias mayores, el factor de estructura está relacionado con la compresibilidad isoterma del líquido 
  
    
      
        
          χ
          
            T
          
        
      
    
    {\displaystyle \chi _{T}}
  
 mediante la ecuación:[5]​

  
    
      
        
          lim
          
            q
            →
            0
          
        
        S
        (
        q
        )
        =
        ρ
        k
        T
        
          χ
          
            T
          
        
        =
        k
        T
        
          (
          
            
              
                ∂
                ρ
              
              
                ∂
                p
              
            
          
          )
        
      
    
    {\displaystyle \lim _{q\rightarrow 0}S(q)=\rho kT\chi _{T}=kT\left({\frac {\partial \rho }{\partial p}}\right)}
  

donde 
  
    
      
        ρ
      
    
    {\displaystyle \rho }
  
 es la densidad del líquido, y 
  
    
      
        p
      
    
    {\displaystyle p}
  
 es la presión.

## Líquidos de esfera dura

En el modelo de esferas duras, las partículas conformantes de un líquido son esferas impenetrables de radio 
  
    
      
        R
      
    
    {\displaystyle R}
  
; por tanto, no experimentan ninguna interacción a distancias 
  
    
      
        r
      
    
    {\displaystyle r}
  
 mayores que 
  
    
      
        2
        R
      
    
    {\displaystyle 2R}
  
. El potencial de interacción se describe matemáticamente así:

  
    
      
        V
        (
        r
        )
        =
        
          {
          
            
              
                
                  ∞
                  
                
                
                  
                    para
                  
                  
                  
                  r
                  <
                  2
                  R
                
              
              
                
                  0
                  
                
                
                  
                    para
                  
                  
                  
                  r
                  ≥
                  2
                  R
                
              
            
          
          
        
      
    
    {\displaystyle V(r)=\left\lbrace {\begin{array}{l l}\infty \,&{\text{para}}\,\,r<2R\\0\,&{\text{para}}\,\,r\geq 2R\\\end{array}}\right.}
  

La aproximación de Percus-Yevick resulta en una solución analítica para este modelo,[6]​  que a pesar de su simplicidad, proporciona una buena descripción de varios sistemas, desde los metales líquidos[7]​ hasta las suspensiones coloidales.[8]​

## Véase también

- Red recíproca

- Cristalografía de rayos X

- Factor de Debye-Waller

## Referencias

- ↑ Born, Max; Wolf, Emil (2002). Principles of Optics: Electromagnetic Theory of Propagation, Interference and Diffraction of Light (en inglés) (7.ª edición). Cambridge University Press. ISBN 9781139643405. 

- ↑ Cusack, 1987, p. 57.

- ↑ Als-Nielsen;McMorrow, 2011, p. 15.

- ↑ Cusack, 1987, p. 60.

- ↑ Cusack, 1987, p. 77.

- ↑ Wertheim, M (1963). «Exact Solution of the Percus-Yevick Integral Equation for Hard Spheres». Physical Review Letters 10 (8): 321-323. doi:10.1103/PhysRevLett.10.321. 

- ↑ Ashcroft, N.; Lekner, J (1966). «Structure and Resistivity of Liquid Metals». Physical Review Letters 145 (1): 83-90. doi:10.1103/PhysRev.145.83. 

- ↑ Pusey, P. N.; Van Megen, W (1986). «Phase behaviour of concentrated suspensions of nearly hard colloidal spheres». Nature 320 (6060): 340-342. doi:10.1038/320340a0. 

## Bibliografía

- Als-Nielsen, Jens; McMorrow, Des (2011). Elements of Modern X-ray Physics (en inglés) (2ª edición). John Wiley & Sons. ISBN 978-0-470-97395-0. 

- 

- Cusack,  N.E. (1987). The Physics of Structurally Disordered Matter — An Introduction (en inglés). Adam Hilger. ISBN 0-85274-591-5,0-85274-829-9 |isbn= incorrecto (ayuda). 

## Enlaces externos

- Kevin Cowtan. «Tutorial interactivo sobre el factor de estructura cristalino» (en inglés). Universidad de York. Archivado desde el original el 15 de abril de 2015. Consultado el 13 de marzo de 2014. 

- «El factor de estructura cristalino». CSIC. 

- «Cristalografía para todos». CSIC. 
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q900684

-  Multimedia: Structure factor / Q900684

- Identificadores

- GND: 4183800-2

-  Datos: Q900684

-  Multimedia: Structure factor / Q900684

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.