sequences = list(range(1, 10) )
for sequence in sequences :
    if sequence == 1 :
        print(f"{sequence}st")
    elif sequence == 2 :
        print(f"{sequence}nd")
    elif sequence == 3 :
        print(f"{sequence}rd")
    elif sequence != 1 and sequence != 2 and sequence != 3 and sequence in list(range (1,10 ) )  :
        print(f"{sequence}th")
 
