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
            if (i + j)%2 ==0:
                col="B"
            else:
                col ="W"
            row.append(col)
        matrix.append(row)
    print_matrix(matrix)

def main():
    size = input("Ingrese el numero: ")
    create_matrix(int(size))

if __name__ == "__main__":
    main()
        
