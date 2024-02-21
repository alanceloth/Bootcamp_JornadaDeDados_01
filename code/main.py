# 1) Solicita ao usuário que digite seu nome
def recebe_nome():
    """
    This function prompts the user to input their name and returns the input as a string.
    """
    nome = input("Qual seu nome? ")
    return nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
def recebe_salario():
    """
    Function to receive and return the user's salary as a float.
    """
    salario = float(input("Qual seu salário? "))
    return salario

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
def recebe_bonus():
    """
    A function that prompts the user to input the value of a bonus and returns it as a float.
    """
    bonus = float(input("Qual o valor do bônus? "))
    return bonus

# 4) Calcule o valor do bônus final
def calcula_bonus(salario, bonus):
    """
    Calculate the bonus based on the given salary and bonus multiplier.

    Parameters:
    salario (int): The base salary.
    bonus (float): The bonus multiplier.

    Returns:
    int: The calculated bonus.
    """
    return (1000 + salario * bonus)

# 5) Imprima cálculo do KPI para o usuário
def imprime_kpi():
    """
    This function prints the KPI by calling the 'calcula_bonus' function with the results of 'recebe_salario' and 'recebe_bonus' functions as arguments.
    """
    print("KPI: ", calcula_bonus(recebe_salario(), recebe_bonus()))


# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
def imprime_mensagem():
    """
    This function prints a message with the name, bonus, and final bonus amount.
    """
    print("Ola ", recebe_nome(), ", o seu bônus final e: ", calcula_bonus(recebe_salario(), recebe_bonus()))


def main():
    """
    This function calls the imprime_mensagem function.
    """
    imprime_mensagem()


if __name__ == "__main__":
    main()

# Exemplo de uso:
# Qual seu nome? Luciano
# Qual seu salário? 10000
# Qual o valor do bônus? 1.5
# Ola  Luciano , o seu bônus final e:  16000.0
