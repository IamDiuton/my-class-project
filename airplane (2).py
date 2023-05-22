# no error handling
import random
import pandas as pd

cols = ['first name', 'Last name', 'gender', 'age']
df = pd.read_csv(r'C:\Users\HOME\Documents\Passengers.txt',
                 header=None, delimiter="\s+", names=cols)
print(df)
unoccupied_seats=[10, 24, 33, 15, 18, 45, 26, 30]
file_path = r'C:\Users\HOME\Documents\bookingcodesfile.txt'

file = open(file_path, 'w')

for i in range(12):
    booking = random.randint(10, 99)
    first_in = df.iloc[i, 0]
    second_in = df.iloc[i, 1]
    str_booking = str(booking)
    booking_code = "DA" + str_booking + first_in + second_in
    # print(booking_code)
    file.write(booking_code + '\n')
file.close()
# Assign seats to 8 out of 12 passengers
assigned_seats = {}
for i in range(8):
    passenger_name = df.iloc[i]['first name'] + ' ' + df.iloc[i]['Last name']
    available_seats = set(unoccupied_seats) - set(assigned_seats.values())

    if not available_seats:
        print(f"No seats available for passenger {passenger_name}")
        break

    while True:
        chosen_seat = int(input(f"Passenger {passenger_name}, choose a seat from {available_seats}: "))
        if chosen_seat in available_seats:
            assigned_seats[passenger_name] = chosen_seat
            break
        else:
            print("Invalid seat choice. Please choose from the available seats.")

# Generate a text file of all booking IDs
with open('BookingIDs.txt', 'w') as file:
    for booking_id in booking_code:
        file.write(booking_id + '\n')

# Generate a text file of the names, booking IDs, and seat numbers for the successful passengers
with open('BookedPassengers.txt', 'w') as file:
    for passenger_name, seat_number in assigned_seats.items():
        booking_id = next((booking_id for booking_id in booking_code if passenger_name in booking_id), None)
        file.write(f"Passenger Name: {passenger_name}, Booking ID: {booking_id}, Seat Number: {seat_number}\n")
