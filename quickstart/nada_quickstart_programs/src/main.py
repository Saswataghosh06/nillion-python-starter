from nada_dsl import *

def nada_main():
    # Define two parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Input secret integers from Party1 and Party2
    x = SecretInteger(Input(name="X", party=party1))
    y = SecretInteger(Input(name="Y", party=party2))

    # Perform the computation: subtraction of the two secret integers
    result = x - y

    # Output the result to Party2
    return [Output(result, "my_output", party2)]
