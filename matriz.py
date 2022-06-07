def  print_matrix(matrix):
    #print (matrix)
    for row in matrix:
        temp = "["
        for item in row:
            temp+=str(item) + ","
        print(temp[:-1] + "]") 
            
def create_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range (size):
            # Para poner en 1 la diagonal de arriba hacia abajo partiendo desde la izquierda
            if (i==j):
                row.append(1)
            # Para poner en 1 la diagonal de arriba hacia abajo pero partiendo desde la derecha
            elif i+j==size-1:
                row.append(1)
            else:
                row.append(0)
            
        matrix.append(row)
    print_matrix(matrix)

def main():
    size = input("Ingrese el numero: ")
    create_matrix(int(size))

if __name__ == "__main__":
    main()
        
