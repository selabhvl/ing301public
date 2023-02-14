from bikecomputer import BikeComputer, Display
from sensors import GPSSensor, HeightSensor
from datetime import timedelta

# customize this if you want
available_sensors = [GPSSensor(), HeightSensor()]

bc = BikeComputer(available_sensors)

choice = None


def show_display(bc: BikeComputer):
    print(f"Current speed:   {bc.display.speed} km/h")
    print(f"Average speed:   {bc.display.average_speed} km/h")
    print(f"Ride length:     {bc.display.current_distance} km")
    print(f"Total kms:       {bc.display.total_distance} km\n")


def show_all_routes(bc: BikeComputer):
    if len(bc.recorded_routes) == 0:
        print("No routes recoded\n")
    else:
        counter = 1
        for route in bc.recorded_routes:
            print(f"Route #{counter}: {route.first.timestamp} until {route.last.timestamp}, {len(route)} Points")
            counter += 1
        print("")


def show_one_route(bc: BikeComputer):
    print("Enter Route id:")
    id = int(input())
    route = bc.recorded_routes[id - 1]
    route.calculateStatistic()

    print(f"\nDisplaying Rout #{id}")
    print(f"Total length:    {route.totalLength} km")
    print(f"Total height:    {route.totalHeight} m")
    print(f"Average speed:   {route.averageSpeed} km/h")
    print(f"Max speed:       {route.maxSpeed} km/h\n")

    print("Do you want to save this route as well?")
    answer = bool(input())
    if answer:
        route.persist_alternative(f"data/route{id}.pickle")



def simulate_ride(bc: BikeComputer):
    print("Starting simulation... Please choose duration:")
    print("Hours (h):")
    h = int(input())
    print("Minutes (m)")
    m = int(input())
    print("Seconds (s)")
    s = int(input())
    ts = int(timedelta(hours=h, minutes=m, seconds=s).total_seconds())
    print("...simulating...")
    bc.simulate_ride(ride_duration_seconds=ts)
    print("...done\n")

while choice != 5:
    print("Bike Computer Main Menu:")
    print("(1) Show Display")
    print("(2) Show All Routes")
    print("(3) Show Specific Route")
    print("(4) Simulate Ride")
    print("(5) Quit \n")
    user_in = input()
    if user_in.isdigit():
        choice = int(user_in)
    else:
        print(f"Invalid input: {user_in}")
    if choice == 1:
        show_display(bc)
    elif choice == 2:
        show_all_routes(bc)
    elif choice == 3:
        show_one_route(bc)
    elif choice == 4:
        simulate_ride(bc)

