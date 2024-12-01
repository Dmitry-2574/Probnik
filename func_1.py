def fuc(name, city, age=35):
    if not isinstance(name, str):
      raise TypeError('Имя должно быть строкой')
    if  not isinstance(city, str):
      raise TypeError('Город должно быть строкой')
    if not isinstance(age, int):
      raise TypeError('Возраст должен быть числом')
    if age >=18:
      city += "(Человек совершолетний)"
    if age<18:
      city += "(Человек не соверщолетний)"
    
    name = name.capitalize()
    city = city.lower()
    return f'Твое имя {name}\nГород: {city}'

print(fuc('дмитрий', 'барнаул', 45))
# print(fuc(35, 56, "дмитрий")) 
# 
# 
# 
def main(nuk, name, hop):
  hop_1 = ''
  if not isinstance(nuk, int):
    raise TypeError('Нужно ввести число')
  if not isinstance(name, str):
    raise TypeError('Должно быть строкой')
  if not isinstance(hop, str):
    raise TypeError('Должно быть строкой')
  
  if nuk>100:
    hop_1 += (f'{name} из города {hop} У тебя доостаточно средств: {nuk}')
  if nuk<100:
    hop_1 += (f'{name} из города {hop} у тебе не хватает, внеси еще')
  return hop_1
f = main(700, 'дмитрий', 'барнаул')
print(f)
  