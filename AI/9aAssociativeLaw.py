def associative_law_addition(a, b, c):
    left_association = (a + b) + c
    right_association = a + (b + c)
    
    return left_association, right_association

def associative_law_multiplication(a, b, c):
    left_association = (a * b) * c
    right_association = a * (b * c)
    
    return left_association, right_association

a, b, c = 2, 3, 4
left_result_addition, right_result_addition = associative_law_addition(a, b, c)
print(f"Addition Associative Law: ({a} + {b}) + {c} = {left_result_addition}")
print(f"Addition Associative Law: {a} + ({b} + {c}) = {right_result_addition}")

a, b, c = 2, 3, 4
left_result_multiplication, right_result_multiplication = associative_law_multiplication(a, b, c)
print(f"Multiplication Associative Law: ({a} * {b}) * {c} = {left_result_multiplication}")
print(f"Multiplication Associative Law: {a} * ({b} * {c}) = {right_result_multiplication}")
