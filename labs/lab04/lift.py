def main():

    # Get user input
    # lift_1_floor, lift_2_floor and lift_3_floor can be either G or 10
    # lift_1_status, lift_2_status and lift_3_status can be moving up, moving down or stopped
    # The strip() method removes spaces or other characters from the start and end of a string. For example:
    # text = "   COMP 1023   "
    # cleaned_text = text.strip()
    # print(cleaned_text)  # Output: "COMP 1023"
    lift_1_floor = input("Current floor of lift 1 (G/10): ").strip()
    lift_1_status = input("Status of lift 1 (moving up/moving down/stopped): ").strip()
    lift_2_floor = input("Current floor of lift 2 (G/10): ").strip()
    lift_2_status = input("Status of lift 2 (moving up/moving down/stopped): ").strip()
    lift_3_floor = input("Current floor of lift 3 (G/10): ").strip()
    lift_3_status = input("Status of lift 3 (moving up/moving down/stopped): ").strip()

    print("Result: ")

    # NOTE: Please do not modify any code above this line.

    # === TODO BELOW ===:
    def time(status, floor):
        match status:
            case "moving up":
                if floor == "G":
                    return 5
                else:
                    return 4
            case "moving down":
                if floor == "G":
                    return 1
                else:
                    return 2
            case "stopped":
                if floor == "G":
                    return 0
                else:
                    return 3
            
    lift_1_time = time(lift_1_status, lift_1_floor)
    lift_2_time = time(lift_2_status, lift_2_floor)
    lift_3_time = time(lift_3_status, lift_3_floor)


    if lift_1_time == 1:
        print("Lift 1 will come to pick you up.")
    
    elif lift_2_time == 1:
        print("Lift 2 will come to pick you up.")
    
    elif lift_3_time == 1:
        print("Lift 3 will come to pick you up.")

    elif lift_1_time == min(lift_1_time, lift_2_time, lift_3_time):
        print("Lift 1 will come to pick you up.")

    elif lift_2_time == min(lift_2_time, lift_3_time):
        print("Lift 2 will come to pick you up.")

    else:
        print("Lift 3 will come to pick you up.")


    # These are the print statements that you will need to use in your solution.
    # The expected output of your program must be exactly the same as these print statements, which is "Lift X will come to pick you up."
    # You can uncomment and then move or copy them to anywhere in your code as you like.

    # print("Lift 1 will come to pick you up.")
    # print("Lift 2 will come to pick you up.")
    # print("Lift 3 will come to pick you up.")

    # === TODO ABOVE ===


if __name__ == "__main__":
    main()

