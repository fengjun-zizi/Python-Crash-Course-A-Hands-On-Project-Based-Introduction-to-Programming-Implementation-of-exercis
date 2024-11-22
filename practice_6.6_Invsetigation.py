favorite_language = {
    'jen' : 'python' ,
    'sarah' : 'C++' , 
    'edward' : 'rust' , 
    'phil' : 'python' 
}

person = { 'jen' , 'steve' ,  'phoil' , 'fengjun' }


print(f"These are the people who should be investigated : {person}")
for persones in person :
    if persones in favorite_language.keys() :
        print(f"Thank you for your cooperation : {persones}")
    else :
        print(f"Please cooperate with us : {persones}")
