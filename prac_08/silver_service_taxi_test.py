from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Real-Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("${:.2f}".format(taxi.get_fare()))



main()