class Material:
    def __init__(self,type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.value = 0

        if (self.type == "Pawn"):
            self.value = 1
        elif (self.type == "Knight" or self.type == "Bishop"):
            self.value = 3
        elif (self.type == "Rook"):
            self.value = 5
        elif (self.type == "Queen"):
            self.value = 9
        elif (self.type == "King"):
            self.value = 15
        
            

def evaluate(white, black):
    evaluate_value = 0
    white_val = 0
    black_val = 0

    for material in white:
        white_val += material.value

    for material in black:
        black_val += material.value

    evaluate_value = white_val - black_val

    if evaluate_value > 0:
        print("(" + str(evaluate_value) + ") The evaluation suggests that white is winning.")
    elif evaluate_value < 0:
        print("(" + str(evaluate_value) + ") The evaluation suggests that black is winning.")
    else:
        print("(" + str(evaluate_value) + ") The position is equal")
