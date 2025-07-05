#iteration is support in tuple
choclate_bag1=("Kitkat", "DairyMilk")
choclate_bag2=("perk","5star")
choclate_box=(choclate_bag1,choclate_bag2)
print(choclate_box)
for bag in choclate_box:
    for choc in bag:
        print(choc)