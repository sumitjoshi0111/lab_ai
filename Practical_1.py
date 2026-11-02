
# Simple Reflex Vacuum Cleaner Agent

def vacuum_agent(location, status):
    if status == "DIRTY":
        return "SUCK"
    elif location == "A":
        return "RIGHT"
    else:
        return "LEFT"


def main():
    environment = {"A": "DIRTY", "B": "DIRTY"}
    location = "A"

    while True:
        # Stop when both rooms are clean
        if environment["A"] == "CLEAN" and environment["B"] == "CLEAN":
            print("Both rooms are clean. STOP")
            break

        status = environment[location]
        action = vacuum_agent(location, status)

        print("Location:", location, "Action:", action)

        if action == "SUCK":
            environment[location] = "CLEAN"
        elif action == "RIGHT":
            location = "B"
        else:
            location = "A"

    print("Final Environment:", environment)


if __name__ == "__main__":
    main()
