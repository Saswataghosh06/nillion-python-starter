from nada_dsl import *

def nada_main():
    # Define two parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Input secret integers for the coordinates of two points from Party1 and Party2
    x1 = SecretInteger(Input(name="X1", party=party1))
    y1 = SecretInteger(Input(name="Y1", party=party1))
    x2 = SecretInteger(Input(name="X2", party=party2))
    y2 = SecretInteger(Input(name="Y2", party=party2))

    # Calculate the Euclidean distance between the points (x1, y1) and (x2, y2)
    # Distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    dx = x2 - x1
    dy = y2 - y1
    distance_squared = dx * dx + dy * dy
    distance = Sqrt(distance_squared)

    # Output the result to Party2
    return [Output(distance, "euclidean_distance", party2)]

