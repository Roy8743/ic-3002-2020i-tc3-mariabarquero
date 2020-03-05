def sumatoria_cubica(n):
    """
       Entrada: Numero maximo de iteraciones de la serie a calcular con complejidad cuadratica
       Salida: Resultado de la sumatoria segun un n dado 
    """

    resultado = 0
    
    i=1
    while i <= n:  
        j = 1                                    
        while j <= i:
            k = j
            while k <= i+j:
                resultado = resultado + 1
                k +=1
            j +=1
        i += 1
                                               
                                                         
    return resultado
    raise NotImplementedError()

def sumatoria_constante(n):
    """
       Entrada: Numero maximo de iteraciones de la serie a calcular con complejidad cuadratica
       Salida: Resultado de la sumatoria segun un n dado 
    """
    resultado = 0

    resultado = (n*(n+1)*(n+2))/3

    return resultado
    raise NotImplementedError()

