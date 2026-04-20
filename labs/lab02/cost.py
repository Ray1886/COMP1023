def main():
    # The price of the car parts
    car_door_cost: float = 55.5
    car_wheel_cost: int = 20
    tire_cost: float = 15.3
    set_of_lights_cost: float = 10.16
    engine_cost: int = 150
    steering_wheel_cost: int = 40

    prompt: str = "Enter the number of cars: "

    # Task 1.1 Get the number of cars to produce/manufacture
    # --- TODO below ---
    number = int(input("Enter the number of cars: "))

    # --- TODO above ---

    # Task 1.2 Calculate the total cost
    # --- TODO below ---
    total_cost = (4*(car_door_cost+car_wheel_cost+tire_cost)+2*set_of_lights_cost
    + engine_cost + steering_wheel_cost)*number

    # --- TODO above ---

    # Task 1.3 Print the total cost of car production
    # Feel free to explore different print methods!
    # --- TODO below ---
    print(f"The total cost will be: ${total_cost:.2f}")

    # --- TODO above ---

if __name__ == "__main__":
    main()
