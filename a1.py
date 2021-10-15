list1 = []
list1.append((0, 'Tshirt', 500, 'Apparels'))
list1.append((1, 'Trousers', 600, 'Apparels'))
list1.append((2, 'Scarf', 250, 'Apparels'))
list1.append((3, 'Smartphone', 20000, 'Electronics'))
list1.append((4, 'ipad', 30000, 'Electronics'))
list1.append((5, 'Laptop', 50000, 'Electronics'))
list1.append((6, 'Eggs', 5, 'Eatables'))
list1.append((7, 'Chocolate', 10, 'Eatables'))
list1.append((8, 'Juice', 100, 'Eatables'))
list1.append((9, 'Milk', 45, 'Eatables'))

def show_menu():
	print('''=================================================
                   MY BAZAAR
=================================================
Hello! Welcome to my grocery store!
Following are the products available in the shop:

-------------------------------------------------
CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
-------------------------------------------------
  0  | Tshirt      | Apparels     | 500
  1  | Trousers    | Apparels     | 600
  2  | Scarf       | Apparels     | 250
  3  | Smartphone  | Electronics  | 20,000
  4  | iPad        | Electronics  | 30,000
  5  | Laptop      | Electronics  | 50,000
  6  | Eggs        | Eatables     | 5
  7  | Chocolate   | Eatables     | 10
  8  | Juice       | Eatables     | 100
  9  | Milk        | Eatables     | 45
------------------------------------------------
''')

def get_regular_input():
 #takes the input of item codes and stores it as a string
    quantities=[0]*10


    print('''-------------------------------------------------
ENTER ITEMS YOU WISH TO BUY
-------------------------------------------------''')
    y = input('Enter the item codes (space-separated):').split()
    for i in y :
        if int(i)<=9 and int(i)>=0:
            quantities[int(i)]+=1
        else:
            print("Invalid Input.")
            continue


    return quantities

def get_bulk_input():
    print('''-------------------------------------------------
ENTER ITEMS YOU WISH TO BUY
-------------------------------------------------''')
    quantities=[0]*10


    t=True
    while (t):
        z = input("Enter code and quantity (leave blank to stop): ")#takes the input of item codes and stores it as a string
        z=list(map(int,z.split()))
        if (z == []):
            print("Your order has been finalized.")
            break

        if len(z) != 2:
            print("Invalid input.Try again.")
            continue
        else:

            if (z[0]<=9 or z[0]>=0 and z[1]>0):
                quantities[z[0]] += z[1]
                print(f"You added {z[1]} {list1[int(z[0])][1]}")

            elif ((z[0] > 9 or z[0] < 0) and z[1] < 0):
                print("Invalid code and quantity. Try again.")
            elif z[0] > 9 or z[0] < 0:
                print('Invalid code. Try again. ')
            elif z[1] < 0:
                print('Invalid quantity. Try again. ')
            else:
                print("Invalid Input. Try again.")

    return(quantities)
def print_order_details(quantities):
    a=0
    print('''-------------------------------------------------
ORDER DETAILS
-------------------------------------------------''')
    for i in range(len(quantities)):
        if quantities[i]==0:
            continue
        else:
            a+=1
            total=0
            total=quantities[i]*list1[i][2]
            print(f"{[a]} {list1[i][1]} x {quantities[i]} = Rs {list1[i][2]} * {quantities[i]} = Rs {total} ")

def calculate_category_wise_cost(quantities):
    apparels_cost=0
    electronics_cost=0
    eatables_cost=0
    for i in range(len(quantities)):
        if list1[i][3]=='Apparels':
            apparels_cost+=list1[i][2]*quantities[i]
        elif list1[i][3]=='Electronics':
            electronics_cost+=list1[i][2]*quantities[i]
        elif list1[i][3]=='Eatables':
            eatables_cost+=list1[i][2]*quantities[i]
    a=(apparels_cost,electronics_cost,eatables_cost)
    print('''-------------------------------------------------
CATEGORY-WISE COST
-------------------------------------------------''')
    print(f"Apparels = Rs {apparels_cost}")
    print(f"Electronics = Rs {electronics_cost}")
    print(f"Eatables = Rs {eatables_cost}")
    return (a)

def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    discounted_apparels_cost=0
    discounted_electronics_cost=0
    discounted_eatables_cost=0
    total_disc_app=0
    total_disc_elec=0
    total_disc_eat=0
    val_check1=0
    val_check2=0
    val_check3=0
    print('''-------------------------------------------------
DISCOUNTS
-------------------------------------------------''')
    if apparels_cost>=2000:
        discounted_apparels_cost=get_discount(apparels_cost,0.1)
        total_disc_app = apparels_cost - discounted_apparels_cost
        if discounted_apparels_cost != 0:
            val_check1=True
            print(f"[APPARELS] Rs {apparels_cost} - Rs {discounted_apparels_cost} = Rs {total_disc_app}")
    else:
        discounted_apparels_cost=apparels_cost
        total_disc_app=apparels_cost
    if electronics_cost>=25000:
        discounted_electronics_cost=get_discount(electronics_cost,0.1)
        total_disc_elec = electronics_cost - discounted_electronics_cost
        if discounted_electronics_cost != 0:
            val_check2=True
            print(f"[ELECTRONICS] Rs {electronics_cost} - Rs {discounted_electronics_cost} = Rs {total_disc_elec}")
    else :
        discounted_electronics_cost=electronics_cost
        total_disc_elec=electronics_cost
    if eatables_cost>=500:
        discounted_eatables_cost=get_discount(eatables_cost,0.1)
        total_disc_eat = eatables_cost - discounted_eatables_cost
        if discounted_eatables_cost != 0:
            val_check3=True
            print(f"[EATABLES] Rs {eatables_cost} - Rs {discounted_eatables_cost} = Rs {total_disc_eat}")
    else :
        discounted_eatables_cost=eatables_cost
        total_disc_eat=eatables_cost
    total_disc =0
    total_cost=0
    if val_check1==True:
        total_disc+=discounted_apparels_cost

    if val_check2==True:
        total_disc+=discounted_electronics_cost

    if val_check3==True:
        total_disc+=discounted_eatables_cost

    b = (total_disc_app, total_disc_elec, total_disc_eat)
    print('')
    print(f"TOTAL DISCOUNT = Rs {total_disc}")
    print(f"TOTAL COST = Rs {total_disc_app+total_disc_elec+total_disc_eat}")
    print('')
    return b


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):

    app_tax=0
    elec_tax=0
    eat_tax=0
    total_tax=0
    total_cost_including_tax=0
    app_tax=get_tax(apparels_cost,0.10)
    elec_tax=get_tax(electronics_cost,0.15)
    eat_tax=get_tax(eatables_cost,0.05)
    total_tax=app_tax+elec_tax+eat_tax
    total_cost_including_tax=apparels_cost+electronics_cost+eatables_cost+total_tax
    print('''-------------------------------------------------
TAX
-------------------------------------------------''')
    b= (total_cost_including_tax,total_tax)
    if apparels_cost!=0:
        print(f"[APPARELS] Rs {apparels_cost} * 0.10 = Rs {app_tax}")
    if electronics_cost!=0:
        print(f"[ELECTRONICS] Rs {electronics_cost} * 0.15 = Rs{elec_tax}")
    if eatables_cost!=0:
        print(f"[EATABLES] Rs {eatables_cost} * 0.05 = Rs {eat_tax}")
    print('')
    print(f"TOTAL TAX = Rs {total_tax}")
    print(f"TOTAL COST = Rs {total_cost_including_tax}")
    return b

def apply_coupon_code(total_cost):
    a=0

    t=True
    total_cost_after_coupon_discount=0
    total_coupon_discount=0
    while t:
        c_code=input('''-------------------------------------------------
COUPON CODE
-------------------------------------------------
Enter coupon code (else leave blank):''')
        if c_code=='':
            print("No coupon code applied.")
            t=False
        elif c_code=='HELL25' or c_code=='CHILL50':
            if c_code=='HELL25':
                if total_cost>=25000:
                    a=total_cost*0.75
                    if a>5000:
                        a=5000
                    print(f"[HELL25] min({a}, Rs {total_cost} * 0.25) = Rs {a}")
                    break
                else :
                    print("Total amount must be greater than Rs 25000 to avail this coupon code. ")
                    continue

            elif c_code=='CHILL50':
                if total_cost>=50000:
                    a=total_cost*0.5
                    if a>10000:
                        a=10000
                    print(f"[CHILL50] min({a}, Rs {total_cost} * 0.50) = Rs {a}")
                    break
                else :
                    print("Total amount must be greater than Rs 50000 to avail this coupon code. ")
                    continue

    total_coupon_discount=a
    total_cost_after_coupon_discount=total_cost-total_coupon_discount
    b=(total_cost_after_coupon_discount,total_coupon_discount)
    print("")
    print(f"TOTAL COUPON DISCOUNT = Rs {total_coupon_discount}")
    print(f"TOTAL COST = Rs {total_cost_after_coupon_discount}")
    return b




def main():
    show_menu()
    global a

    while True:
        x = input("Would you like to buy in bulk? (y or Y / n or N): ")
        if x=='y' or x=='Y' :
            a=get_bulk_input()
            break
        elif x=='n' or x=='N':
            a=get_regular_input()
            break
        else:
            print('Invalid Input. Please Try again')
    print_order_details(a)
    cost = calculate_category_wise_cost(a)
    disc_price = calculate_discounted_prices(cost[0], cost[1], cost[2])
    tax = calculate_tax(disc_price[0], disc_price[1], disc_price[2])
    total_money=apply_coupon_code(tax[0])
    print('')
    print(f"You have to pay a total amount of Rs {total_money[0]}")
    print('Thank You For Visiting!')

if __name__ == '__main__':
	main()


