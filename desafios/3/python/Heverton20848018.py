def eh_palindromo(num: int) -> bool:
    return str(num) == str(num)[::-1]

def listar_palindromos(inicio: int, fim: int):
    resultados = []
    for n in range(inicio, fim + 1):
        if eh_palindromo(n):
            resultados.append(n)
    return resultados

if __name__ == "__main__":
    # Exemplos de teste
    print(listar_palindromos(1, 20))      # [1,2,3,4,5,6,7,8,9,11]
    print(listar_palindromos(3000, 3010)) # [3003]
    print(listar_palindromos(101, 121))   # [101,111,121]
