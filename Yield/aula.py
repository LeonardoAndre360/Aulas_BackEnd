def counter_function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5 
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10
    yield 11



contador = counter_function()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
