#Example:
products = [
    ["Cheese",          "Dairy"],
    ["Carrots",         "Produce"],
    ["Potatoes",        "Produce"],
    ["Canned Tuna",     "Pantry"],
    ["Romaine Lettuce", "Produce"],
    ["Chocolate Milk",  "Dairy"],
    ["Flour",           "Pantry"],
    ["Iceberg Lettuce", "Produce"],
    ["Coffee",          "Pantry"],
    ["Pasta",           "Pantry"],
    ["Milk",            "Dairy"],
    ["Blueberries",     "Produce"],
    ["Pasta Sauce",     "Pantry"]
]

list1 = ["Blueberries", "Milk", "Coffee", "Flour", "Cheese", "Carrots"] #=> 2
list2 = ["Blueberries", "Carrots", "Coffee", "Milk", "Flour", "Cheese"] #=> 2
list3 = ["Blueberries", "Carrots", "Romaine Lettuce", "Iceberg Lettuce"] #=> 0
list4 = ["Milk", "Flour", "Chocolate Milk", "Pasta Sauce"] #=> 2
list5 = ["Cheese", "Potatoes", "Blueberries", "Canned Tuna"] #=> 0

"""
#Vueltas sin repetir
Dairy = []
Produce = []
Pantry = []
vr = 0
for producto in products:
    if producto[1] == "Dairy":
        Dairy.append(producto[0])

    elif producto[1] == "Produce":
        Produce.append(producto[0])

    elif producto[1] == "Pantry":
        Pantry.append(producto[0])

Dairy = set(Dairy)
Produce = set(Produce)
Pantry = set(Pantry)
list2 = set(list2)
count = 0
if len(Dairy &list2) > (len(Dairy &list2) == 0):
    count += 1
if len(Produce &list2) > (len(Produce &list2) == 0):
    count += 1
if len(Pantry &list2) > (len(Pantry &list2) == 0):
    count += 1
print(count)
"""
"""
#Vueltas sin repetir
vuelta = 0
for v in products:
    for lis in list1:
        if lis == v[0]:
            vuelta += 1
print(vuelta)
"""
def shopping(products, list):
    #Vueltas sin repetir
    vuelta = 0
    for v in products:
        for lis in list:
            if lis == v[0]:
                vuelta += 1
    Dairy = []
    Produce = []
    Pantry = []
    vr = 0
    for producto in products:
        if producto[1] == "Dairy":
            Dairy.append(producto[0])

        elif producto[1] == "Produce":
            Produce.append(producto[0])

        elif producto[1] == "Pantry":
            Pantry.append(producto[0])

    Dairy = set(Dairy)
    Produce = set(Produce)
    Pantry = set(Pantry)
    list = set(list)
    count = 0
    if len(Dairy &list) > (len(Dairy &list) == 0):
        count += 1
    if len(Produce &list) > (len(Produce &list) == 0):
        count += 1
    if len(Pantry &list) > (len(Pantry &list) == 0):
        count += 1
    print(vuelta-count)
# #All Test Cases:
shopping(products, list1) #=> 2
shopping(products, list2) #=> 2
shopping(products, list3) #=> 0
shopping(products, list4) #=> 2
shopping(products, list5) #=> 0