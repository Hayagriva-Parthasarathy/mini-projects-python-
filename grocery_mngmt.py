product ={"shoe":1000,"socks":200,"kit kat":10,"5 star": 5,"cap":100}
prod=[]
tot_price=0
price=0
product_found = False
iteration=1
#already_found = False
def calc_amt():
    global tot_price
    global product_found
    global iteration
    global prod
    #global already_found
    while True:
        if(iteration ==1):
            cart=input("ADD PRODUCTS TO CART (yes/no):")
            iteration+=1
        else:
           cart = input("ADD ANOTHER PRODUCT TO CART (yes/no):")
        if(cart == "yes"):
            item= input("ENTER THE PRODUCT NAME: ")
            for search_item in product.keys():
                if(search_item == item):
                    product_found = True
            if(product_found):
                qty=int(input("HOW MANY? " ))
                price=product[item]*qty
                tot_price+=price
                prod.append(item)
                prod.append(product[item])
                prod.append(qty)
                prod.append(price)
                product_found=False
            else:
                while True:
                    print("PRODUCT NOT AVAILABLE")
                    item=input("ENTER THE PRODUCT NAME: ")
                    for search_item in product.keys():
                        if(search_item == item):
                            product_found = True
                    if(product_found):
                        qty=int(input("HOW MANY? " ))
                        price=product[item]*qty
                        tot_price+=price
                        product_found=False
                        break
               
        else:
            return tot_price
        
def products_list():
    return prod
    

final_price = calc_amt()
products = products_list()
print("PURCHASED PRODUCTS ARE ",products)
print("FINAL PRICE IS: ")
print(final_price)
