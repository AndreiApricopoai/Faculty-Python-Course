# Laboratory 4

# Ex1 - Write a Python class that simulates a Stack.
# The class should implement methods like push, pop, peek
# (the last two methods should return None if no element is present in the stack).
class Stack:
    MAX_SIZE = 100

    def __init__(self):
        self.elements: list = []

    def push(self, element):
        if self.is_full():
            print("Stack overflow")
        else:
            self.elements.append(element)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.elements.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.elements[-1]

    def is_full(self) -> bool:
        return len(self.elements) == Stack.MAX_SIZE

    def is_empty(self) -> bool:
        return len(self.elements) == 0

    def __str__(self):
        return str(self.elements)


my_stack = Stack()
print("Is the stack empty?", my_stack.is_empty())
my_stack.push('apple')
my_stack.push('banana')
my_stack.push('cherry')
print(my_stack)
print("Top element is:", my_stack.peek())
print("Is the stack full?", my_stack.is_full())
print("Popped element:", my_stack.pop())
print("Popped element:", my_stack.pop())
print("Is the stack empty?", my_stack.is_empty())
print("Top element is:", my_stack.peek())
for i in range(Stack.MAX_SIZE):
    my_stack.push(f"element-{i}")

print("Is the stack full?", my_stack.is_full())
my_stack.push('overflow')
print('\n\n\n')


# Ex2 - Write a Python class that simulates a Queue. The class should implement
# methods like push, pop, peek (the last two methods should return None if
# no element is present in the queue).
class Queue:
    MAX_SIZE = 100

    def __init__(self):
        self.elements: list = []

    def push(self, element):
        if self.is_full():
            print("Queue overflow")
        else:
            self.elements.append(element)

    def pop(self):
        if len(self.elements) == 0:
            return None
        else:
            return self.elements.pop(0)

    def peek(self):
        if len(self.elements) == 0:
            return None
        else:
            return self.elements[0]

    def is_full(self) -> bool:
        return len(self.elements) == Queue.MAX_SIZE

    def is_empty(self) -> bool:
        return len(self.elements) == 0

    def __str__(self):
        return str(self.elements)


my_queue = Queue()
print("Is the queue empty?", my_queue.is_empty())
my_queue.push('apple')
my_queue.push('banana')
my_queue.push('cherry')
print(my_queue)
print("Front element is:", my_queue.peek())
print("Removed element:", my_queue.pop())
print("Is the queue full?", my_queue.is_full())
print("Removed element:", my_queue.pop())
print("Removed element:", my_queue.pop())
print("Is the queue empty?", my_queue.is_empty())
print("Removed element:", my_queue.pop())
for i in range(Queue.MAX_SIZE):
    my_queue.push(f"element-{i}")

print("Is the queue full?", my_queue.is_full())
my_queue.push('overflow')


# Ex3 - Write a Python class that simulates a matrix of size NxM, with N and M
# provided at initialization. The class should provide methods to access elements
# (get and set methods) and some mathematical functions such as transpose, matrix
# multiplication and a method that allows iterating through all elements form a matrix
# and apply a transformation over them (via a lambda function).
class Matrix:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mat = []

        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            self.mat.append(row)

    def __str__(self):
        result = ""
        for i in range(self.n):
            for j in range(self.m):
                result += str(self.mat[i][j]) + " "
            result += "\n"
        return result

    def get(self, row, column):
        if row >= 0 and row < self.n and column >= 0 and column < self.m:
            return self.mat[row][column]
        else:
            print(f"Cant get element from row {row} and column {column}")

    def set(self, row, column, value):
        if row >= 0 and row < self.n and column >= 0 and column < self.m:
            self.mat[row][column] = value
        else:
            print(f"Cant set element from row {row} and column {column}")

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.m != other.n:
            print("Matrix dimensions do not match for multiplication")

        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                element_sum = 0
                for k in range(self.m):
                    element_sum += self.mat[i][k] * other.mat[k][j]
                result.mat[i][j] = element_sum
        return result

    def apply(self, transform):
        for i in range(self.n):
            for j in range(self.m):
                self.mat[i][j] = transform(self.mat[i][j])


matrix1 = Matrix(2, 3)
matrix2 = Matrix(3, 2)

matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(0, 2, 3)
matrix1.set(1, 0, 4)
matrix1.set(1, 1, 5)
matrix1.set(1, 2, 6)

matrix2.set(0, 0, 7)
matrix2.set(0, 1, 8)
matrix2.set(1, 0, 9)
matrix2.set(1, 1, 10)
matrix2.set(2, 0, 11)
matrix2.set(2, 1, 12)

print(matrix1)
print(matrix2)

result_matrix = matrix1.multiply(matrix2)
print(result_matrix)
result_matrix.apply(lambda x: x + 1)
print(result_matrix)
transposed_matrix = result_matrix.transpose()
print(transposed_matrix)

