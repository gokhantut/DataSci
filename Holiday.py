# Define function for hotel cost
def hotel_cost(num_nights, city):
    # Create dictionary to store hotel prices for different cities
    hotel_prices = {"Istanbul": 200, "Tokyo": 250, "Paris": 150, "London": 120}
    # Retrieve price for chosen city
    if city in hotel_prices:
        price_per_night = hotel_prices[city]
    else:
        return "City not found"
    # Calculate total cost for hotel stay
    total_cost = num_nights * price_per_night
    return total_cost

# Define function for car rental cost
def car_rental(rental_days, city):
    # Create dictionary to store car rental prices for different cities
    rental_prices = {"Istanbul": 50, "Paris": 60, "London": 40, "Tokyo": 80}
    # Retrieve price for chosen city
    if city in rental_prices:
        daily_rental_cost = rental_prices[city]
    else:
        return "City not found"
    # Calculate total cost for car rental
    total_cost = rental_days * daily_rental_cost
    return total_cost

# Define function for plane cost
def plane_cost(city):
    # Create dictionary to store flight prices for different cities
    flight_prices = {"Istanbul": 500, "Paris": 700, "London": 900, "Tokyo": 1200}
    # Retrieve price for chosen city
    if city in flight_prices:
        return flight_prices[city]
    else:
        return "City not found"

# Define function for holiday cost
def holiday_cost(num_nights, rental_days, flight_cost, city):
    # Calculate costs for hotel, and car rental using their respective functions
    hotel_cost_total = hotel_cost(num_nights, city)
    car_rental_total = car_rental(rental_days, city)
    # Calculate total cost for holiday
    total_cost = hotel_cost_total + flight_cost + car_rental_total
    return total_cost

# Get user input for city_flight
print("Enter the city you will be flying to (options: Istanbul, Paris, London, Tokyo):")
city = input()
while city not in ["Istanbul", "Paris", "London", "Tokyo"]:
    print("Invalid city. Please enter a valid city.")
    city = input()

# Call plane_cost function with the chosen city and store the result
flight_cost = plane_cost(city)

# Get user inputs for num_nights and rental_days
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car for: "))

# Call holiday_cost function with user inputs and flight cost, and store the result
total_holiday_cost = holiday_cost(num_nights, rental_days, flight_cost, city)

# Print out details of the holiday and the total cost
print("Holiday Details:")
print("City of Flight: ", city)
print("Flight Cost: £",flight_cost)
print("Hotel Cost per Night: £",hotel_cost(num_nights, city))
print("Car Rental Cost per Day: £",car_rental(rental_days, city))
print("Number of Nights at Hotel: ", num_nights)
print("Number of Days for Car Rental: ", rental_days)
print("Total Cost: £",total_holiday_cost)