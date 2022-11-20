def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name+" "+l_name


name = input("Enter your name: ")
split_name = name.split(" ")
f_name = split_name[0]
l_name = split_name[1]

print(format_name(f_name, l_name))
