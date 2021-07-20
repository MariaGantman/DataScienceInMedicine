a = input("Введите время в секундах")
hours=(int(a)//3600)
minutes=(int(a)%3600)//60
seconds=(int(a)%3600)%60
simple_str=f"{hours}:{minutes}:{seconds}"
print(simple_str)


