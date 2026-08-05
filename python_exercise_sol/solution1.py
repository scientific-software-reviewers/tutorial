# String's Vowel and Consonent Counter 

def counter(str):
    vow="aeiou"
    vow_count=0
    conso_count=0
    for char in str.lower().strip():
        if char in vow:
            vow_count+=1
        else:
            conso_count+=1

    return vow_count,conso_count

str=input("Enter your valid string: ")
v,c=counter(str)
print(f"Vowel count is : {v}\nConsonent count is :{c}")