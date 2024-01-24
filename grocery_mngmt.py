product ={"shoe":1000,"socks":200,"kit kat":10,"5 star": 5,"cap":100}
prod=[]
tot_price=0
price=0
product_found = False
def calc_amt():
    global tot_price
    global product_found
    while True:
        cart=input("Do you want to add to cart: ")
        if(cart == "yes"):
            item= input("Enter the product name: ")
            for search_item in product.keys():
                if(search_item == item):
                    product_found = True
            if(product_found):
                qty=int(input("How many? " ))
                price=product[item]*qty
                tot_price+=price
                product_found=False
            else:
                while True:
                    print("Product not available")
                    item=input("Enter the product name: ")
                    for search_item in product.keys():
                        if(search_item == item):
                            product_found = True
                    if(product_found):
                        qty=int(input("How many? " ))
                        price=product[item]*qty
                        tot_price+=price
                        product_found=False
                        break
               
        else:
            return tot_price
           
final_price = calc_amt()
print("Final price is: ")
print(final_price)
