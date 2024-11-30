def make_shirt ( size = None , display = None ) :
    if size == None :
        size = input ('You need give me your size : ')
    if display == None :
        display = input ('What is you need display : ')
    
    print ( f" This is your size {size} , and it is your display {display}  ")
    
make_shirt()
make_shirt(size = 'XXXL' , display = 'I love python ' )
make_shirt( size = 'XXL' , display = 'I love python ')
make_shirt( size = 'L' , display = 'I love python ')
