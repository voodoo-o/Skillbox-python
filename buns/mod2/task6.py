domain = input("Введите домен: ")
current_domain = ""
i = len(domain) - 1

while i >= 0:
    char = domain[i]
    if char == '.':
        if current_domain:
            print(current_domain)
        current_domain = ""
    else:
        current_domain = char + current_domain
    i -= 1
if current_domain:
    print(current_domain)
        

        
    
