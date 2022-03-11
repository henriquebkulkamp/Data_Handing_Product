# The functions to Data Handing here

def FunctionVariation(column):
    columnVariation = [0]
    for i in range(1, len(column)):
        currentValue = column[i]
        oldValue = column[i - 1]

        absoluteVariation = (-(oldValue - currentValue)) / oldValue
        if absoluteVariation != 0:
            percentageVariation = f'{absoluteVariation * 100}%'
        else:
            percentageVariation = '0%'
        columnVariation.append(percentageVariation)

    return columnVariation