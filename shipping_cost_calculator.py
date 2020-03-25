def cost_of_ground_shipping(weight):
    if weight <= 2.00:
        cost = 20 + weight * 1.50
    elif weight > 2.00 and weight <= 6.00:
        cost = 20 + weight * 3.00
    elif weight > 6.00 and weight <= 10.00:
        cost = 20 + weight * 4.00
    else:  # Weight over 10 lbs
        cost = 20 + weight * 4.75
        # Flat charge 125 if premium ground
    return cost

def cost_of_drone_shipping(weight):
    if weight <= 2.00:
        cost = weight * 4.50
    elif weight > 2.00 and weight <= 6.00:
        cost = weight * 9.00
    elif weight > 6.00 and weight <= 10.00:
        cost = weight * 12.00
    else:  # Weight over 10 lbs
        cost = weight * 14.25
    return cost

def cheapest_shipping(weight):
    ground = cost_of_ground_shipping(weight)
    premium = flat_premium
    drone = cost_of_drone_shipping(weight)

    if ground < premium and ground < drone:
        return "Cheapest Option: Regular Ground Shipping $" + str(cost_of_ground_shipping(weight))
    elif drone < ground and drone < premium:
        return "Cheapest Option: Regular Drone Shipping $" + str(cost_of_drone_shipping(weight))
    elif premium < ground and premium < drone:
        return "Cheapest Option: Premium Ground Shipping $" + str(premium)
    else:
        return "Error"

flat_premium = 125.00

weight = float(input("Weight:"))

print ("Cost of regular ground shipping: $" + str(cost_of_ground_shipping(weight)))
print ("Cost of premium ground shipping: $125.00")
print ("Cost of regular drone shipping: $" + str(cost_of_drone_shipping(weight)))
print (cheapest_shipping(weight))



