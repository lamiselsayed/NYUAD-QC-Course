def linear_evolve(operator, currentState):
    newState = []
    for i in range(len(operator)):          # for each row in the operator
        newState.append(0)
        for j in range(len(currentState)):  # for each element in state
            newState[i] += (operator[i][j] * currentState[j])

    return newState
