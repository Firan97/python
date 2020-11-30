new_list = [4, 3, 1, 3, 1]
while True:
    print(f"Rating: {new_list}")
    number = input("Enter rate number or 100 to finish - ")
    if number.lstrip('-').isdigit() and number !="111":
        number = int(number)
        if new_list.count(number):
            new_list.insert(new_list.index(number) + new_list.count(number), float(number))
        else:
            p=0
            n_p=0
            for n, i in enumerate(new_list):
                if number > i:
                    if p<i:
                        p=i
                        n_p=n
                    else:
                        n_p = n + 1
                        new_list.insert(n_p, n)
                elif not number.isdigit():
                    print("Ent number")
                else:
                    break