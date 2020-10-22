from logpy import run, var, fact
import logpy.assoccomm as la


#operaciones logicas
add = 'addition'
mul = 'miltiplication'


#declaramos que estas operaciones son conmutativas
fact(la.commutative, mul)
fact(la.commutative, add)
fact(la.associative, mul)
fact(la.associative, add)

#Definimos variables 
a, b, c, = var('a'), var('b'), var('c')


#Expresión original = 3 x (-2) + (1 + 2 x 3)x (-1)
expression_orig = (add, (mul, 3, -2), (mul, (add, 1, (mul, 2, 3)), -1))
#Esta se puede transformar  en las siguientes expresiones equivalentes
#expression1 = (1 + 2 x a) x b + 3 x c
expression1 = (add, (mul, (add, 1, (mul, 2, a)), b), (mul, 3, c))
#expression2 = c x 3 + b x (2 x a + 1)
expression2 = (add, (mul, c, 3), (mul, b, (add, (mul, 2, a), 1)))
#expression3 = (((2 x a) x b) + b) + 3 x c
expression3 = (add, (add, (mul, (mul, 2, a), b), b),(mul, 3, c))

# Compare expressions
print(run(0, (a, b, c), la.eq_assoccomm(expression1, expression_orig)))
print(run(0, (a, b, c), la.eq_assoccomm(expression2, expression_orig)))
print(run(0, (a, b, c), la.eq_assoccomm(expression3, expression_orig)))











