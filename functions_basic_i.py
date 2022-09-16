#1
def number_of_food_groups():  #Result:5
    return 5
print(number_of_food_groups())


#2
def number_of_military_branches(): #Result:5 /La funcion number_of_days_in_a_week_silicon_or_triangle_sides() no esta definida, por ende manda error 
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3
def number_of_books_on_hold():   #Result: 5-10 /Solo devuelve 5
    return 5
    return 10
print(number_of_books_on_hold())


#4
def number_of_fingers():  #result: 10/Solo devuelve 5
    return 5
    print(10)
print(number_of_fingers())


#5
def number_of_great_lakes(): #result: 5-5 /imprime solo un 5 y un none
    print(5)
x = number_of_great_lakes()
print(x)


#6
def add(b,c):  #Resul: 3-5-8/ Imprime solo 3 y 5
    print(b+c)
print(add(1,2) + add(2,3))


#7
def concatenate(b,c):  #Result: "25" /si imprime 25 en string
    return str(b)+str(c)
print(concatenate(2,5))


#8
def number_of_oceans_or_fingers_or_continents(): #Result: 100-10-7-7 /Devuelve solo 100-10  
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c): #Result:  7-14-21/ si da el resultado
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10
def addition(b,c): #Result: 8-10 /Imprime solo 8
    return b+c
    return 10
print(addition(3,5))


#11
b = 500          
print(b)
def foobar():  #Result: 500-300 / Es 500-500-300-500
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12
b = 500
print(b)
def foobar():  #Result: 500-500-300-500-300-500/ no da, solo da 500-500-300-500
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13
b = 500
print(b)
def foobar(): #Result: 500-500-300-500 / nooo daaa, 500-500-300-300
    b= 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14
def foo(): #result: 1-2-3-2/ no, 1-3-2
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15
def foo():  #Result: 1-3-5-10/ si da 
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)