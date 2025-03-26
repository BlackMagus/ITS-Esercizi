#def convert_temperature(c:float, f2:bool = None) -> float:
#    if f2 == False:
#        c2 = ((c-32)/9)*5
#        return c2
#   else:
#      f = (c*9)/5 + 32
#      return f

#def check_access(username: str, password: str, is_active: bool):
#    if username == "admin":
#        if password == "12345":
#            if is_active == True:
#                print("Accesso consentito")
#            else:
#                print("Accesso negato")
#        else:
#            print("Accesso negato")
#    else:
#        print("Accesso negato")
        

#def count_isolated(numbers:list) -> int:
#    c = 0
#    x = 10000000
#    for i in range (len(numbers)):
#        j = i + 1
#        if i != 0:
#            x = i - 1
#            if len(numbers) > j:
#                if numbers[i] != numbers[j]:
#                    if numbers[i] != numbers[x]:
#                        c = c + 1
#                        x = x + 1
#    return c


#def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
#    new_set = original_set.copy()
#    new_set = new_set - set(elements_to_remove) 
#    return new_set


            
