from random import randint
array=[randint(-100,100) for i in range(30)]
print(array)
number=array[0]
position=0
for i in range(1, len(array)):
 if array[i]>number:
  number=array[i]
  position=i
print("Mаксимальний елемент списку:", number)
print("Його порядковий номер:", position)
print("Пари від’ємних чисел, що стоять поруч:")
for i in range(len(array)-1):
  print(array[i],array[i+1]) if array[i]<0 and array[i+1]<0 else None