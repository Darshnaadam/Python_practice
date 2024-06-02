# Problem_7: Customize a coffee order: "small", "medium", "large" 
# with an option of "extra shot" of espresso

order = input("How do you want your coffee: small, medium or large ?: ")
es = input("Do you want an extra shot of espresso? (Yes/No): ")

if order == 'Small'.lower() and es == 'Yes'.lower():
    print("Your order:", order, "Coffee with extra shot of espresso")
elif order == 'Small'.lower() and es == 'No'.lower():
    print("Your order:", order, "Coffee")
elif order == 'Medium'.lower() and es == 'Yes'.lower():
    print("Your order:", order, "Coffee with extra shot of espresso")
elif order == 'Medium'.lower() and es == 'No'.lower():
    print("Your order:", order, "Coffee")
elif order == 'Large'.lower() and es == 'Yes'.lower():
    print("Your order:", order, "Coffee with extra shot of espresso")
elif order == 'Large'.lower() and es == 'No'.lower():
    print("Your order:", order, "Coffee")
else: 
    print("Invalid order. Please try again.")
