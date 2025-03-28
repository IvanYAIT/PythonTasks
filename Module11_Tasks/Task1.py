EURO_TO_DOLLAR_EXCHAGE_RATE = 1.25
DOLLAR_TO_RUBLE_EXCHAGE_RATE = 60.87

while True:
    try:
        productCostEuro = int(input("Стоимость покупки в евро: "))

        if(productCostEuro > 0):
            break
        
        print("Цена должна быть больше 0")
    except:
        print("Это не число")

productCostRuble = (productCostEuro * EURO_TO_DOLLAR_EXCHAGE_RATE) * DOLLAR_TO_RUBLE_EXCHAGE_RATE
print(f"Стоимость в рублях: {productCostRuble}")