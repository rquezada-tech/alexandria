---
title: "Ecuación de Gibbs-Helmholtz"
domain: manufactura
subtopic: quimica
source: wikipedia
has_images: false
---

Ecuación de Gibbs-Helmholtz
    
    
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
  
  
    
      
        
          
            
              
## Ecuación de Gibbs-Helmholtz

            
            
            
              
                

              

              La ecuación de Gibbs-Helmholtz es una ecuación termodinámica utilizada para calcular los cambios en la energía de Gibbs de un sistema en función de la temperatura.

## Ecuación

La ecuación es:[1]​

  
    
      
        
          
            (
            
              
                
                  ∂
                  (
                  
                    
                      G
                      T
                    
                  
                  )
                
                
                  ∂
                  T
                
              
            
            )
          
          
            p
          
        
        =
        −
        
          
            H
            
              T
              
                2
              
            
          
        
      
    
    {\displaystyle \left({\frac {\partial ({\frac {G}{T}})}{\partial T}}\right)_{p}=-{\frac {H}{T^{2}}}}
  

donde H es la entalpía, T la temperatura absoluta y G la energía libre de Gibbs del sistema, todo a presión constante p. La ecuación establece que el cambio en la relación G/T a presión constante como resultado de un cambio infinitamente pequeño de temperatura es factor de H/T2.

## Reacciones químicas

Las aplicaciones típicas son en las reacciones químicas. La ecuación dice:[2]​

  
    
      
        
          
            (
            
              
                
                  ∂
                  (
                  Δ
                  
                    G
                    
                      ⊖
                    
                  
                  
                    /
                  
                  T
                  )
                
                
                  ∂
                  T
                
              
            
            )
          
          
            p
          
        
        =
        −
        
          
            
              Δ
              H
            
            
              T
              
                2
              
            
          
        
      
    
    {\displaystyle \left({\frac {\partial (\Delta G^{\ominus }/T)}{\partial T}}\right)_{p}=-{\frac {\Delta H}{T^{2}}}}
  

con ΔG como el cambio en la energía de Gibbs y ΔH como el cambio de entalpía (considerado independiente de la temperatura). El exponente o denota presión estándar (1 bar).

Al integrarse con respecto a T (nuevamente p es constante) se convierte en:

  
    
      
        
          
            
              Δ
              
                G
                
                  ⊖
                
              
              (
              
                T
                
                  2
                
              
              )
            
            
              T
              
                2
              
            
          
        
        −
        
          
            
              Δ
              
                G
                
                  ⊖
                
              
              (
              
                T
                
                  1
                
              
              )
            
            
              T
              
                1
              
            
          
        
        =
        Δ
        
          H
          
            ⊖
          
        
        (
        p
        )
        
          (
          
            
              
                1
                
                  T
                  
                    2
                  
                
              
            
            −
            
              
                1
                
                  T
                  
                    1
                  
                
              
            
          
          )
        
      
    
    {\displaystyle {\frac {\Delta G^{\ominus }(T_{2})}{T_{2}}}-{\frac {\Delta G^{\ominus }(T_{1})}{T_{1}}}=\Delta H^{\ominus }(p)\left({\frac {1}{T_{2}}}-{\frac {1}{T_{1}}}\right)}
  

Esta ecuación permite rápidamente el cálculo del cambio de energía libre de Gibbs para una reacción química a cualquier temperatura T2 con el conocimiento de solo el cambio de formación de energía libre estándar de Gibbs y el cambio de formación de entalpía estándar para los componentes individuales.

Además, utilizando la ecuación de reacción isoterma;[3]​

  
    
      
        
          
            
              Δ
              
                G
                
                  ⊖
                
              
            
            T
          
        
        =
        −
        R
        ln
        ⁡
        K
      
    
    {\displaystyle {\frac {\Delta G^{\ominus }}{T}}=-R\ln K}
  

que relaciona la energía de Gibbs con una constante de equilibrio químico, se puede derivar la ecuación de van't Hoff.[2]​

## Derivación

## Antecedentes

Artículos principales: ecuación de definición (química física), entalpía y potencial termodinámico

La definición de la función de Gibbs es

  
    
      
        H
        =
        G
        +
        S
        T
        
        
      
    
    {\displaystyle H=G+ST\,\!}
  

donde H es la entalpía definida por:

  
    
      
        H
        =
        U
        +
        p
        V
        
        
      
    
    {\displaystyle H=U+pV\,\!}
  

Tomando diferenciales de cada definición para encontrar dH y dG, y luego usando la relación termodinámica fundamental (siempre verdadera para procesos reversibles o irreversibles):

  
    
      
        d
        U
        =
        T
        
        d
        S
        −
        p
        
        d
        V
        
        
      
    
    {\displaystyle dU=T\,dS-p\,dV\,\!}
  

donde S es la entropía, V es el volumen (con signo negativo debido a la reversibilidad, en la cual dU = 0: aparte del de la presión-volumen, se puede realizar más trabajo, que será igual a -pV) conduce la forma "invertida" de la relación fundamental inicial a una nueva ecuación maestra:

  
    
      
        d
        G
        =
        −
        S
        
        d
        T
        +
        V
        
        d
        p
        
        
      
    
    {\displaystyle dG=-S\,dT+V\,dp\,\!}
  

Esta es la energía libre de Gibbs para un sistema cerrado. La ecuación de Gibbs-Helmholtz se puede derivar por esta segunda ecuación maestra y la regla de la cadena para derivadas parciales.

Derivación

Partiendo de la ecuación

  
    
      
        d
        G
        =
        −
        S
        
        d
        T
        +
        V
        
        d
        p
        =
        
          
            
              ∂
              G
            
            
              ∂
              T
            
          
        
        
        d
        T
        +
        
          
            
              ∂
              G
            
            
              ∂
              p
            
          
        
        
        d
        p
        
        
      
    
    {\displaystyle dG=-S\,dT+V\,dp={\frac {\partial G}{\partial T}}\,dT+{\frac {\partial G}{\partial p}}\,dp\,\!}
  

a presión constante, es decir dp = 0. Entonces dG se reduce a

  
    
      
        d
        
          G
          
            p
          
        
        =
        −
        S
        
        d
        T
        =
        
          
            (
            
              
                
                  ∂
                  G
                
                
                  ∂
                  T
                
              
            
            )
          
          
            p
          
        
        
        d
        T
        
        →
        
        −
        S
        =
        
          
            (
            
              
                
                  ∂
                  G
                
                
                  ∂
                  T
                
              
            
            )
          
          
            p
          
        
        .
        
        
      
    
    {\displaystyle dG_{p}=-S\,dT=\left({\frac {\partial G}{\partial T}}\right)_{p}\,dT\quad \rightarrow \quad -S=\left({\frac {\partial G}{\partial T}}\right)_{p}.\,\!}
  

La dependencia de la razón G/T respecto a T se encuentra mediante la regla del producto de las derivadas:

  
    
      
        
          
            (
            
              
                
                  ∂
                  (
                  G
                  
                    /
                  
                  T
                  )
                
                
                  ∂
                  T
                
              
            
            )
          
          
            p
          
        
        =
        
          
            1
            T
          
        
        
          
            (
            
              
                
                  ∂
                  G
                
                
                  ∂
                  T
                
              
            
            )
          
          
            p
          
        
        +
        G
        
          
            
              ∂
              (
              
                T
                
                  −
                  1
                
              
              )
            
            
              ∂
              T
            
          
        
        =
        
          
            
              T
              
                
                  (
                  
                    
                      
                        ∂
                        G
                      
                      
                        ∂
                        T
                      
                    
                  
                  )
                
                
                  p
                
              
              −
              G
            
            
              T
              
                2
              
            
          
        
        =
        
          
            
              −
              S
              T
              −
              G
            
            
              T
              
                2
              
            
          
        
        =
        −
        
          
            H
            
              T
              
                2
              
            
          
        
        
        
      
    
    {\displaystyle \left({\frac {\partial (G/T)}{\partial T}}\right)_{p}={\frac {1}{T}}\left({\frac {\partial G}{\partial T}}\right)_{p}+G{\frac {\partial (T^{-1})}{\partial T}}={\frac {T\left({\frac {\partial G}{\partial T}}\right)_{p}-G}{T^{2}}}={\frac {-ST-G}{T^{2}}}=-{\frac {H}{T^{2}}}\,\!}
  

## Referencias

- ↑ Physical chemistry, P. W. Atkins, Oxford University Press, 1978, ISBN 0-19-855148-7

- ↑ a b Chemical Thermodynamics, D.J.G. Ives, University Chemistry, Macdonald Technical and Scientific, 1971, ISBN 0-356-03736-3

- ↑ Chemistry, Matter, and the Universe, R.E. Dickerson, I. Geis, W.A. Benjamin Inc. (USA), 1976, ISBN 0-19-855148-7

## Enlaces externos

- Gibbs–Helmholtz equation
Control de autoridades

- Proyectos Wikimedia

-  Datos: Q900590

- Diccionarios y enciclopedias

- Britannica: url

-  Datos: Q900590

    Este artículo ha sido escrito por Wikipedia. El texto está disponible bajo la licencia Creative Commons Attribution-Share Alike 4.0. Pueden aplicarse cláusulas adicionales a los archivos multimedia.