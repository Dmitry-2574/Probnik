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