def total (millions, hundreds, thousands):
    return (millions + thousands + hundreds)

money = [2330000, 4000, 203]
money = {"millions":2000000, "thousands":4000, "hundreds":200}
print(total(**money))
"""
    *: unpacking values in list
    **: unpacking values in a dictionary
"""