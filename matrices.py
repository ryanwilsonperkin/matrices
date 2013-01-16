import sys

class MatrixError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def blankMatrix(rows=1, cols=1):
    A = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(None)
        A.append(temp)
    return A

def identityMatrix(degree):
    A = []
    for i in range(degree):
        row = []
        for j in range(degree):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        A.append(row)
    return A

def validateMatrix(A):
    if len(A) == 0:
        raise MatrixError("Cannot have 0 rows")
    rowLength = len(A[0])
    if rowLength == 0:
        raise matrixError("Cannot have 0 length row")
    for row in A:
        if len(row) != rowLength:
            raise MatrixError("Row lengths do not match")

def printMatrix(A,column_separator="\t",line_separator="\n\n"):
    validateMatrix(A)
    rows = len(A)
    try:
        cols = len(A[0])
    except IndexError as e:
        raise MatrixError("Cannot have 0 rows or columns")

    for i in range(rows):
        for j in range(cols):
            sys.stdout.write(str(A[i][j]))
            if j != (cols - 1):
                sys.stdout.write(column_separator)
        if i != (rows - 1):
            sys.stdout.write(line_separator)
    sys.stdout.write("\n")

def addMatrices(A,B,show=False):
    validateMatrix(A)
    validateMatrix(B)
    A_rows = len(A)
    A_cols = len(A[0])
    B_rows = len(B)
    B_cols = len(B[0])
    if A_rows != B_rows or A_cols != B_cols:
        raise MatrixError("Matrices are not the same dimension")
    
    C = blankMatrix(A_rows, A_cols)
    C_explained = blankMatrix(A_rows, A_cols)

    for i in range(A_rows):
        for j in range(A_cols):
            C[i][j] = A[i][j] + B[i][j]
            C_explained[i][j] = "((" + str(A[i][j]) + ")+(" + str(B[i][j]) + "))"

    if show:
        printMatrix(C_explained)

    return C

def subtractMatrices(A,B,show=False):
    validateMatrix(A)
    validateMatrix(B)
    A_rows = len(A)
    A_cols = len(A[0])
    B_rows = len(B)
    B_cols = len(B[0])
    if A_rows != B_rows or A_cols != B_cols:
        raise MatrixError("Matrices are not the same dimension")
    
    C = blankMatrix(A_rows, A_cols)
    C_explained = blankMatrix(A_rows, A_cols)
    
    for i in range(A_rows):
        for j in range(A_cols):
            C[i][j] = A[i][j] - B[i][j]
            C_explained[i][j] = "((" + str(A[i][j]) + ")-(" + str(B[i][j]) + "))"
    
    if show:
        printMatrix(C_explained)
    
    return C

def multiplyMatrices(A,B,show=False):
    validateMatrix(A)
    validateMatrix(B)
    A_rows = len(A)
    A_cols = len(A[0])
    B_rows = len(B)
    B_cols = len(B[0])
    if A_cols != B_rows:
        raise MatrixError("Matrix row and column numbers do not match")

    C = blankMatrix(A_rows, B_cols)
    C_explained = blankMatrix(A_rows, B_cols)

    for i in range(A_rows):
        for j in range(B_cols):
            C[i][j] = 0
            C_explained[i][j] = "("
            for k in range(B_rows):
                C[i][j] += A[i][k] * B[k][j]
                C_explained[i][j] += "(" + str(A[i][k]) + ")*(" + str(B[k][j]) + ")"
                if k != (B_rows - 1):
                    C_explained[i][j] += "+"
            C_explained[i][j] += ")"

    if show:
        printMatrix(C_explained)

    return C

def transposeMatrix(A):
    validateMatrix(A)
    A_rows = len(A)
    A_cols = len(A[0])
    C = blankMatrix(A_cols, A_rows)
    for i in range(A_rows):
        for j in range(A_cols):
            C[j][i] = A[i][j]
    return C
