# global list variable

cart = []
# create a function to add items to the cart
def add_item(item):
    cart.append(item)
    print(f'{item} has been added,')

# removing item
def remove_item(item):
    try:
        cart.remove(item)
        print(f'{item} has been removed.')
    except:
        print("sorry unknown item can't be removed")

# make a funtion to show item in the cart
def show_cart():

    if cart:
        print('Here is your cart: ')
        for item in cart:
            print(f'-{item}')
    else:
        print('Your cart is empty.')

# create a function to clear our cart
def clear_cart():
    cart.clear()
    print('Your cart is empty ')

# a function for our loop
def body():
    done = False
    while not done :
        ans = input('QUIT/ ADD/ REMOVE/ SHOW/ CLEAR:  ').lower()

        if ans == 'quit':
            print('Thanks for using our shopping site')
            show_cart()
            done = True

        elif ans == 'add': #used the add_item function here
            item = input('what would you like to add to your cart?:  ').title()
            add_item(item)

        elif ans == 'remove':
            show_cart()# show_cart function here
            item = input('what would you like to remove?: ').title()
            remove_item(item) # remove_item function here

        elif ans == 'show':
            show_cart() # the show cart function here

        elif ans == 'clear':
            clear_cart() # clear cart function here
        else:
            print('Sorry that was not an option') # when input wrong option
body()# closing of the body function

