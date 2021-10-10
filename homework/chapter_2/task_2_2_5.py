def product(a, b):
    if a < 0:
        a *= -1
    elif b < 0:
        b *= -1
    result = a * b
    print("Product of", a, "and", b, "equals", result)
    return result
def pre_product(a, b):
    product_result = product(a,b)
    if a < 0 and b < 0:
      product_result *= -1
    return product_result
