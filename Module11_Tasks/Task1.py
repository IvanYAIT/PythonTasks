EURO_TO_DOLLAR_EXCHAGE_RATE = 1.25
DOLLAR_TO_RUBLE_EXCHAGE_RATE = 60.87

while True:
    try:
        product_cost_euro = int(input("Стоимость покупки в евро: "))

        if(product_cost_euro > 0):
            break
        
        print("Цена должна быть больше 0")
    except:
        print("Это не число")

product_cost_ruble = (product_cost_euro * EURO_TO_DOLLAR_EXCHAGE_RATE) * DOLLAR_TO_RUBLE_EXCHAGE_RATE
print(f"Стоимость в рублях: {product_cost_ruble}")