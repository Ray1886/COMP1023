def main():
    # The time taken to assemble of the car parts
    car_door_time: int = 8
    car_wheel_time: float = 5.8
    tire_time: int = 5
    set_of_lights_time: float = 10.5
    engine_time: int = 20
    steering_wheel_time: float = 12.7

    prompt: str = "Enter the number of cars: "

    # Task 2.1 Get the number of cars to produce/manufacture
    # --- TODO below ---
    number = int(input("Enter the number of cars: "))

    # --- TODO above ---

    # Task 2.2 Calculate the total time
    # --- TODO below ---
    total_time = (4*(car_door_time+car_wheel_time+tire_time)+2*set_of_lights_time
    + engine_time + steering_wheel_time+30)*number

    # --- TODO above ---

    # Task 2.3 Print the total time of car production
    # Feel free to explore different print methods!
    # --- TODO below ---
    print(f"The total time taken will be: {total_time:.2f} second(s)")

    # --- TODO above ---

if __name__ == "__main__":
    main()
