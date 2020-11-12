month = int(input("Месяц от 1 до 12: "))
m_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "Novermber", 12: "December"}
m_list = ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
if month in m_dict:
    print(f"{month} -й месяц года - это {m_dict[month]}")
    print(f"{month} -й месяц года - это {m_list[month - 1]}")
else:
    print("Wrong number")