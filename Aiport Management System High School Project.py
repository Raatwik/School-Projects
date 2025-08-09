import mysql.connector
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="sathvik", 
        database="airport_management"
    )
def insert_flight(flight_no, flight_name, departure_time, arrival_time):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO flights (flight_no, flight_name, departure_time, arrival_time) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (flight_no, flight_name, departure_time, arrival_time))
    db.commit()
    cursor.close()
    db.close()
    print(f"Flight '{flight_no}' inserted successfully!")


def insert_passenger(name, age, flight_no):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO passengers (name, age, flight_no) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, flight_no))
    db.commit()
    cursor.close()
    db.close()
    print(f"Passenger '{name}' inserted successfully!")
def update_flight(flight_no, flight_name=None, departure_time=None, arrival_time=None):
    db = connect_db()
    cursor = db.cursor()
    if flight_name:
        cursor.execute("UPDATE flights SET flight_name = %s WHERE flight_no = %s", (flight_name, flight_no))
    if departure_time:
        cursor.execute("UPDATE flights SET departure_time = %s WHERE flight_no = %s", (departure_time, flight_no))
    if arrival_time:
        cursor.execute("UPDATE flights SET arrival_time = %s WHERE flight_no = %s", (arrival_time, flight_no))
        db.commit()
    cursor.close()
    db.close()
    print(f"Flight '{flight_no}' updated successfully!")
def update_passenger(passenger_id, name=None, age=None, flight_no=None):
    db = connect_db()
    cursor = db.cursor()
    if name:
        cursor.execute("UPDATE passengers SET name = %s WHERE passenger_id = %s", (name, passenger_id))
    if age:
        cursor.execute("UPDATE passengers SET age = %s WHERE passenger_id = %s", (age, passenger_id))
    if flight_no:
        cursor.execute("UPDATE passengers SET flight_no = %s WHERE passenger_id = %s", (flight_no, passenger_id))
        db.commit()
    cursor.close()
    db.close()
    print(f"Passenger ID {passenger_id} updated successfully!")
def delete_flight(flight_no):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM flights WHERE flight_no = %s", (flight_no,))
    db.commit()
    cursor.close()
    db.close()
    print(f"Flight '{flight_no}' deleted successfully!")
def delete_passenger(passenger_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM passengers WHERE passenger_id = %s", (passenger_id,))
    db.commit()
    cursor.close()
    db.close()
    print(f"Passenger ID {passenger_id} deleted successfully!")
def display_flights():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM flights")
    flights = cursor.fetchall()
    print("Available Flights:")
    for flight in flights:
        print(f"Flight No: {flight[0]}, Name: {flight[1]}, Departure: {flight[2]}, Arrival: {flight[3]}")
    cursor.close()
    db.close()
def display_passengers(flight_no):
    db = connect_db()
    cursor = db.cursor()
    query = """
        SELECT passenger_id, name, age 
        FROM passengers 
        WHERE flight_no = %s
    """
    cursor.execute(query, (flight_no,))
    passengers = cursor.fetchall()
    if not passengers:
        print(f"No passengers found for Flight No: {flight_no}")
    else:
        print(f"Passengers for Flight No: {flight_no}:")
        for passenger in passengers:
            print(f"ID: {passenger[0]}, Name: {passenger[1]}, Age: {passenger[2]}")
    cursor.close()
    db.close()
def ticket(passenger_id):
    db = connect_db()
    cursor = db.cursor()
    query = """
        SELECT passenger_id, name, age, passengers.flight_no, flight_name, departure_time, arrival_time
        FROM passengers, flights
        WHERE passenger_id= %s and passengers.flight_no=flights.flight_no;
    """
     
    cursor.execute(query, (passenger_id,))
    passengers = cursor.fetchall()
    for passenger in passengers:
        print("passenger_id \t", "name \t", "age \t", "flight_no \t", "flight_name \t", "deparutre_time \t",
              "arrival_time")
        print('\t',passenger[0],'\t',passenger[1], '\t', passenger[2], '\t', passenger[3], '\t\t', passenger[4], '\t',
              passenger[5], '\t\t', passenger[6])
    cursor.close()
    db.close()
if __name__ == "__main__":
    while True:
        print("\n--- Airport Management Menu ---")
        print("1. Insert Flight")
        print("2. Insert Passenger")
        print("3. Update Flight")
        print("4. Update Passenger")
        print("5. Delete Flight")
        print("6. Delete Passenger")
        print("7. Display Flights")
        print("8. Display Passengers by Flight")
        print("9. Display Ticket")
        print("10. Exit")
        choice = input("Enter your choice: ")
    if choice == "1":
            flight_no = input("Enter flight number: ")
            flight_name = input("Enter flight name: ")
            departure_time = input("Enter departure time (HH:MM:SS): ")
            arrival_time = input("Enter arrival time (HH:MM:SS): ")
            insert_flight(flight_no, flight_name, departure_time, arrival_time)
    elif choice == "2":
            name = input("Enter passenger name: ")
            age = int(input("Enter passenger age: "))
            flight_no = input("Enter flight number (leave blank if none): ")
            insert_passenger(name, age, flight_no)
    elif choice == "3":
            flight_no = input("Enter flight number to update: ")
            flight_name = input("Enter new flight name (leave blank if no change): ")
            departure_time = input("Enter new departure time (HH:MM:SS) (leave blank if no change): ")
            arrival_time = input("Enter new arrival time (HH:MM:SS) (leave blank if no change): ")
            update_flight(flight_no, flight_name if flight_name else None, departure_time if departure_time else None, arrival_time if arrival_time else None)
    elif choice == "4":
            passenger_id = int(input("Enter passenger ID to update: "))
            name = input("Enter new name (leave blank if no change): ")
            age = input("Enter new age (leave blank if no change): ")
            flight_no = input("Enter new flight number (leave blank if no change): ")
            update_passenger(passenger_id, name if name else None, int(age) if age else None, flight_no if flight_no else None)
    elif choice == "5":
            flight_no = input("Enter flight number to delete: ")
            delete_flight(flight_no)
    elif choice == "6":
            passenger_id = int(input("Enter passenger ID to delete: "))
            delete_passenger(passenger_id)
    elif choice == "7":
            display_flights()
    elif choice == "8":
            flight_no = input("Enter flight number: ")
            display_passengers(flight_no)
    elif choice== "9":
            passenger_id= int(input("Enter passenger ID to show ticket"))
            ticket(passenger_id)
    elif choice == "10":
            print("Exiting program.")
            break
    else:
            print("Invalid choice, try again.")
