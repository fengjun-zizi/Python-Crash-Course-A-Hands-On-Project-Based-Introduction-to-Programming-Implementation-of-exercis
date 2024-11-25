sandwich_orders = [
    "Classic Club Delight",  # 经典俱乐部三明治
    "Spicy Buffalo Crunch",  # 辣味水牛城酥脆三明治
    "Mediterranean Bliss",   # 地中海风味三明治
    "Veggie Garden Feast",   # 蔬菜花园盛宴三明治
    'pastrami' ,              #五香烟熏牛肉
    "Smoky BBQ Pulled Pork", # 烟熏烧烤猪肉三明治
    "Avocado Turkey Fusion", # 牛油果火鸡融合三明治
    "Cheesy Tuna Melt",      # 芝士金枪鱼融化三明治
    'pastrami'  ,             #五香烟熏牛肉
    "Honey Mustard Chicken Supreme", # 蜂蜜芥末鸡肉至尊三明治
    "Egg & Bacon Sunrise",   # 蛋培根日出三明治
    "Italian Caprese Twist"  # 意式卡普雷塞风味三明治
    'pastrami'   ,            #五香烟熏牛肉
]

finished_sandwiches = []
print('I heard that the deli has sold out of the five-spice smoked beef.')

while 'pastrami' in sandwich_orders :
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders :
    finished = sandwich_orders.pop()

    print(f"I made your sandwiches : {finished}")
    finished_sandwiches.append(finished)
