import pymysql
import re
from datetime import datetime

# Connect to database
def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Blaze2020@",
        database="travel_management"
    )

# email validation
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# phone validation
def is_valid_phone(phone_number):
    pattern = r'^\+?\d{1,3}?[-.\s]??\(?\d{1,4}?\)?[-.\s]??\d{1,4}[-.\s]??\d{1,4}[-.\s]??\d{1,9}$'
    return re.match(pattern, phone_number) is not None

# date validation
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# view all reviews
def view_reviews():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM reviews")
        users = cursor.fetchall()
        print("Reviews}:")
        for user in users:
            print(user)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# view all payments
def view_payments():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM payments")
        users = cursor.fetchall()
        print("Payments}:")
        for user in users:
            print(user)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# view all bookings
def view_bookings():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM booking")
        users = cursor.fetchall()
        print("Bookings:")
        for user in users:
            print(user)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

 # view all users
def view_users():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM app_user")
        users = cursor.fetchall()
        print("Users:")
        for user in users:
            print(user)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# view all activities
def view_activities():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM activities")
        destinations = cursor.fetchall()
        print("Activities:")
        for dest in destinations:
            print(dest)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# view all accommodations
def view_accommodation():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM accommodation")
        destinations = cursor.fetchall()
        print("Accommodations:")
        for dest in destinations:
            print(dest)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# view all destinations
def view_destinations():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM destination")
        destinations = cursor.fetchall()
        print("Destinations:")
        for dest in destinations:
            print(dest)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# view all transportations
def view_transportations():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM transportation")
        destinations = cursor.fetchall()
        print("Transportations:")
        for dest in destinations:
            print(dest)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# view all trips
def view_trips():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM trip")
        destinations = cursor.fetchall()
        print("Trips:")
        for dest in destinations:
            print(dest)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


# create or update accommodation
def create_or_update_accommodation(action, cursor, connection):
    if action == "create":
        accommodation_name = input("Enter Accommodation Name: ")
        accommodation_type = input("Enter Accommodation Type: ")

        price_per_night = input("Enter Price Per Night: ")
        while not price_per_night.isdigit() or int(price_per_night) <= 0:
            print("Invalid price. Please enter a positive integer for Price Per Night.")
            price_per_night = input("Enter Price Per Night: ")

        capacity = input("Enter Capacity: ")
        while not capacity.isdigit() or int(capacity) <= 0:
            print("Invalid capacity. Please enter a positive integer for Capacity.")
            capacity = input("Enter Capacity: ")

        rating = input("Enter Rating (1-5): ")
        while not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
            print("Invalid rating. Please enter an integer between 1 and 5.")
            rating = input("Enter Rating (1-5): ")

        view_destinations()
        destination_id = input("Enter Destination ID: ")

        try:
            cursor.execute(
                """
                INSERT INTO accommodation (accommodation_name, accommodation_type, price_per_night, 
                capacity, rating, destination_id)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (accommodation_name, accommodation_type, price_per_night, capacity, rating, destination_id)
            )
            connection.commit()
            print("Accommodation created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

    elif action == "update":
        view_accommodation()

        accommodation_id = input("Enter Accommodation ID to update: ")

        cursor.execute("SELECT * FROM accommodation WHERE accommodation_id = %s", (accommodation_id,))
        accommodation = cursor.fetchone()
        if accommodation:
            print(f"Current accommodation data: {accommodation}")
            accommodation_name = input(f"Enter Accommodation Name (current: {accommodation[1]}): ") or accommodation[1]
            accommodation_type = input(f"Enter Accommodation Type (current: {accommodation[2]}): ") or accommodation[2]

            price_per_night = input(f"Enter Price Per Night (current: {accommodation[3]}): ") or accommodation[3]
            while price_per_night and (not price_per_night.isdigit() or int(price_per_night) <= 0):
                print("Invalid price. Please enter a positive integer for Price Per Night.")
                price_per_night = input(f"Enter Price Per Night (current: {accommodation[3]}): ") or accommodation[3]

            capacity = input(f"Enter Capacity (current: {accommodation[4]}): ") or accommodation[4]
            while capacity and (not capacity.isdigit() or int(capacity) <= 0):
                print("Invalid capacity. Please enter a positive integer for Capacity.")
                capacity = input(f"Enter Capacity (current: {accommodation[4]}): ") or accommodation[4]

            rating = input(f"Enter Rating (current: {accommodation[5]}): ") or accommodation[5]
            while rating and (not rating.isdigit() or int(rating) < 1 or int(rating) > 5):
                print("Invalid rating. Please enter an integer between 1 and 5.")
                rating = input(f"Enter Rating (current: {accommodation[5]}): ") or accommodation[5]

            view_destinations()
            destination_id = input(f"Enter Destination ID (current: {accommodation[6]}): ") or accommodation[6]

            try:
                cursor.execute(
                    """
                    UPDATE accommodation 
                    SET accommodation_name = %s, accommodation_type = %s, price_per_night = %s, 
                        capacity = %s, rating = %s, destination_id = %s
                    WHERE accommodation_id = %s
                    """,
                    (accommodation_name, accommodation_type, price_per_night, capacity, rating, destination_id, accommodation_id)
                )
                connection.commit()
                print("Accommodation updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            print("Accommodation ID not found.")

# create or update transportation
def create_or_update_transportation(action, cursor, connection):
    if action == "create":
        transportation_type = input("Enter Transportation Type: ")
        company = input("Enter Company: ")
        departure_date = input("Enter Departure Date (YYYY-MM-DD): ")
        while not is_valid_date(departure_date):
            print("Invalid date format. Please try again.")
            departure_date = input("Enter Departure Date (YYYY-MM-DD): ")

        arrival_date = input("Enter Arrival Date (YYYY-MM-DD): ")
        while not is_valid_date(arrival_date):
            print("Invalid date format. Please try again.")
            arrival_date = input("Enter Arrival Date (YYYY-MM-DD): ")

        departure_location = input("Enter Departure Location: ")
        arrival_location = input("Enter Arrival Location: ")
        trip_id = input("Enter Trip ID: ")

        try:
            cursor.execute(
                """
                INSERT INTO transportation (transportation_type, company, departure_date, arrival_date, 
                departure_location, arrival_location, trip_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (transportation_type, company, departure_date, arrival_date, departure_location,
                 arrival_location, trip_id)
            )
            connection.commit()
            print("Transportation created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

    elif action == "update":
        view_transportations()
        transportation_id = input("Enter Transportation ID to update: ")

        cursor.execute("SELECT * FROM transportation WHERE transportation_id = %s", (transportation_id,))
        transportation = cursor.fetchone()
        if transportation:
            print(f"Current transportation data: {transportation}")
            transportation_type = input(f"Enter Transportation Type (current: {transportation[1]}): ") or \
                                  transportation[1]
            company = input(f"Enter Company (current: {transportation[2]}): ") or transportation[2]
            departure_date = input(f"Enter Departure Date (current: {transportation[3]}): ") or transportation[
                3]
            while departure_date and not is_valid_date(departure_date):
                print("Invalid date format. Please try again.")
                departure_date = input("Enter Departure Date (YYYY-MM-DD): ") or transportation[3]

            arrival_date = input(f"Enter Arrival Date (current: {transportation[4]}): ") or transportation[4]
            while arrival_date and not is_valid_date(arrival_date):
                print("Invalid date format. Please try again.")
                arrival_date = input("Enter Arrival Date (YYYY-MM-DD): ") or transportation[4]

            departure_location = input(f"Enter Departure Location (current: {transportation[5]}): ") or \
                                 transportation[5]
            arrival_location = input(f"Enter Arrival Location (current: {transportation[6]}): ") or \
                               transportation[6]
            trip_id = input(f"Enter Trip ID (current: {transportation[7]}): ") or transportation[7]

            try:
                cursor.execute(
                    """
                    UPDATE transportation 
                    SET transportation_type = %s, company = %s, departure_date = %s, arrival_date = %s, 
                    departure_location = %s, arrival_location = %s, trip_id = %s
                    WHERE transportation_id = %s
                    """,
                    (transportation_type, company, departure_date, arrival_date, departure_location,
                     arrival_location, trip_id, transportation_id)
                )
                connection.commit()
                print("Transportation updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            print("Transportation ID not found.")

# create or update user
def create_or_update_user(action, cursor, connection):
    if action == "create":
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        while not is_valid_email(email):
            print("Invalid email format. Please try again.")
            email = input("Enter Email: ")

        phone_number = input("Enter Phone Number: ")
        while not is_valid_phone(phone_number):
            print("Invalid phone number format. Please try again.")
            phone_number = input("Enter Phone Number: ")

        street_num = input("Enter Street Number: ")
        street_name = input("Enter Street Name: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter Zip Code: ")
        registration_date = input("Enter Registration Date (YYYY-MM-DD): ")
        while not is_valid_date(registration_date):
            print("Invalid date format. Please try again.")
            registration_date = input("Enter Registration Date (YYYY-MM-DD): ")

        try:
            cursor.execute(
                """
                INSERT INTO app_user (first_name, last_name, email, phone_number, street_num, 
                street_name, city, state, zip_code, registration_date) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (first_name, last_name, email, phone_number, street_num, street_name, city, state, zip_code,
                 registration_date)
            )
            connection.commit()
            print("User created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

    elif action == "update":
        view_users()
        user_id = input("Enter User ID to update: ")

        cursor.execute("SELECT * FROM app_user WHERE user_id = %s", (user_id,))
        user = cursor.fetchone()
        if user:
            print(f"Current user data: {user}")
            first_name = input(f"Enter First Name (current: {user[1]}): ") or user[1]
            last_name = input(f"Enter Last Name (current: {user[2]}): ") or user[2]
            email = input(f"Enter Email (current: {user[3]}): ") or user[3]
            while email and not is_valid_email(email):
                print("Invalid email format. Please try again.")
                email = input("Enter Email: ") or user[3]

            phone_number = input(f"Enter Phone Number (current: {user[4]}): ") or user[4]
            while phone_number and not is_valid_phone(phone_number):
                print("Invalid phone number format. Please try again.")
                phone_number = input("Enter Phone Number: ") or user[4]

            street_num = input(f"Enter Street Number (current: {user[5]}): ") or user[5]
            street_name = input(f"Enter Street Name (current: {user[6]}): ") or user[6]
            city = input(f"Enter City (current: {user[7]}): ") or user[7]
            state = input(f"Enter State (current: {user[8]}): ") or user[8]
            zip_code = input(f"Enter Zip Code (current: {user[9]}): ") or user[9]
            registration_date = input(f"Enter Registration Date (current: {user[10]}): ") or user[10]
            while registration_date and not is_valid_date(registration_date):
                print("Invalid date format. Please try again.")
                registration_date = input("Enter Registration Date (YYYY-MM-DD): ") or user[10]

            try:
                cursor.execute(
                    """
                    UPDATE app_user 
                    SET first_name = %s, last_name = %s, email = %s, phone_number = %s, 
                    street_num = %s, street_name = %s, city = %s, state = %s, 
                    zip_code = %s, registration_date = %s
                    WHERE user_id = %s
                    """,
                    (first_name, last_name, email, phone_number, street_num, street_name, city, state, zip_code, registration_date, user_id)
                )
                connection.commit()
                print("User updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            print("User ID not found.")

# create or update destination
def create_or_update_destination(action, cursor, connection):
    if action == "create":
        location_name = input("Enter Location Name: ")
        country = input("Enter Country: ")
        average_rating = input("Enter Average Rating: ")

        try:
            cursor.execute(
                """
                INSERT INTO destination (location_name, country, average_rating) 
                VALUES (%s, %s, %s)
                """,
                (location_name, country, average_rating)
            )
            connection.commit()
            print("Destination created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

    elif action == "update":
        view_destinations()
        destination_id = input("Enter Destination ID to update: ")

        cursor.execute("SELECT * FROM destination WHERE destination_id = %s", (destination_id,))
        destination = cursor.fetchone()
        if destination:
            print(f"Current destination data: {destination}")
            location_name = input(f"Enter Location Name (current: {destination[1]}): ") or destination[1]
            country = input(f"Enter Country (current: {destination[2]}): ") or destination[2]
            average_rating = input(f"Enter Average Rating (current: {destination[3]}): ") or destination[3]

            try:
                cursor.execute(
                    """
                    UPDATE destination 
                    SET location_name = %s, country = %s, average_rating = %s
                    WHERE destination_id = %s
                    """,
                    (location_name, country, average_rating, destination_id)
                )
                connection.commit()
                print("Destination updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            print("Destination ID not found.")

# create or update trip
def create_or_update_trip(action, cursor, connection):
    if action == "create":
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        while not is_valid_date(start_date):
            print("Invalid date format. Please try again.")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")

        end_date = input("Enter End Date (YYYY-MM-DD): ")
        while not is_valid_date(end_date):
            print("Invalid date format. Please try again.")
            end_date = input("Enter End Date (YYYY-MM-DD): ")

        trip_type = input("Enter Trip Type (e.g., Vacation, Business): ")

        view_destinations()
        destination_id = input("Enter Destination ID: ")

        try:
            cursor.execute(
                """
                INSERT INTO trip (start_date, end_date, trip_type, destination_id)
                VALUES (%s, %s, %s, %s)
                """,
                (start_date, end_date, trip_type, destination_id)
            )
            connection.commit()
            print("Trip created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

    elif action == "update":
        view_trips()
        trip_id = input("Enter Trip ID to update: ")

        cursor.execute("SELECT * FROM trip WHERE trip_id = %s", (trip_id,))
        trip = cursor.fetchone()
        if trip:
            print(f"Current trip data: {trip}")
            start_date = input(f"Enter Start Date (current: {trip[1]}): ") or trip[1]
            while start_date and not is_valid_date(start_date):
                print("Invalid date format. Please try again.")
                start_date = input("Enter Start Date (YYYY-MM-DD): ") or trip[1]

            end_date = input(f"Enter End Date (current: {trip[2]}): ") or trip[2]
            while end_date and not is_valid_date(end_date):
                print("Invalid date format. Please try again.")
                end_date = input("Enter End Date (YYYY-MM-DD): ") or trip[2]

            trip_type = input(f"Enter Trip Type (current: {trip[3]}): ") or trip[3]

            view_destinations()
            destination_id = input(f"Enter Destination ID (current: {trip[4]}): ") or trip[4]

            try:
                cursor.execute(
                    """
                    UPDATE trip 
                    SET start_date = %s, end_date = %s, trip_type = %s, destination_id = %s
                    WHERE trip_id = %s
                    """,
                    (start_date, end_date, trip_type, destination_id, trip_id)
                )
                connection.commit()
                print("Trip updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            print("Trip ID not found.")

# create or update activity
def create_or_update_activity(action, cursor, connection):
    if action == "create":
        activity_name = input("Enter Activity Name: ")
        activity_description = input("Enter Activity Description: ")

        activity_date = input("Enter Activity Date (YYYY-MM-DD): ")
        while not is_valid_date(activity_date):
            print("Invalid date format. Please try again.")
            activity_date = input("Enter Activity Date (YYYY-MM-DD): ")

        location = input("Enter Location: ")

        view_trips()
        trip_id = input("Enter Trip ID: ")

        try:
            cursor.execute(
                """
                INSERT INTO activities (activity_name, activity_description, activity_date, location, trip_id) 
                VALUES (%s, %s, %s, %s, %s)
                """,
                (activity_name, activity_description, activity_date, location, trip_id)
            )
            connection.commit()
            print("Activity created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

    elif action == "update":
        view_activities()

        activity_id = input("Enter Activity ID to update: ")

        cursor.execute("SELECT * FROM activities WHERE activity_id = %s", (activity_id,))
        activity = cursor.fetchone()
        if activity:
            print(f"Current activity data: {activity}")
            activity_name = input(f"Enter Activity Name (current: {activity[1]}): ") or activity[1]
            activity_description = input(f"Enter Activity Description (current: {activity[2]}): ") or activity[2]

            activity_date = input(f"Enter Activity Date (current: {activity[3]}): ") or activity[3]
            while activity_date and not is_valid_date(activity_date):
                print("Invalid date format. Please try again.")
                activity_date = input("Enter Activity Date (YYYY-MM-DD): ") or activity[3]

            location = input(f"Enter Location (current: {activity[4]}): ") or activity[4]

            view_trips()
            trip_id = input(f"Enter Trip ID (current: {activity[5]}): ") or activity[5]

            try:
                cursor.execute(
                    """
                    UPDATE activities 
                    SET activity_name = %s, activity_description = %s, activity_date = %s, 
                        location = %s, trip_id = %s
                    WHERE activity_id = %s
                    """,
                    (activity_name, activity_description, activity_date, location, trip_id, activity_id)
                )
                connection.commit()
                print("Activity updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            print("Activity ID not found.")

# create or update payment
def create_or_update_payment(action, cursor, connection):
    if action == "create":
        payment_date = input("Enter Payment Date (YYYY-MM-DD): ")
        while not is_valid_date(payment_date):
            print("Invalid date format. Please try again.")
            payment_date = input("Enter Payment Date (YYYY-MM-DD): ")

        amount = input("Enter Amount: ")
        while not amount.isdigit() or int(amount) <= 0:
            print("Invalid amount. Please enter a positive integer for Amount.")
            amount = input("Enter Amount: ")

        payment_method = input("Enter Payment Method (e.g., Credit Card, PayPal): ")

        payment_status = input("Enter Payment Status (e.g., Completed, Pending, Failed): ")

        try:
            cursor.execute(
                """
                INSERT INTO payment (payment_date, amount, payment_method, payment_status)
                VALUES (%s, %s, %s, %s)
                """,
                (payment_date, amount, payment_method, payment_status)
            )
            connection.commit()
            print("Payment created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

    elif action == "update":
        view_payments()

        payment_id = input("Enter Payment ID to update: ")

        cursor.execute("SELECT * FROM payment WHERE payment_id = %s", (payment_id,))
        payment = cursor.fetchone()
        if payment:
            print(f"Current payment data: {payment}")
            payment_date = input(f"Enter Payment Date (current: {payment[1]}): ") or payment[1]
            while payment_date and not is_valid_date(payment_date):
                print("Invalid date format. Please try again.")
                payment_date = input("Enter Payment Date (YYYY-MM-DD): ") or payment[1]

            amount = input(f"Enter Amount (current: {payment[2]}): ") or payment[2]
            while amount and (not amount.isdigit() or int(amount) <= 0):
                print("Invalid amount. Please enter a positive integer for Amount.")
                amount = input(f"Enter Amount (current: {payment[2]}): ") or payment[2]

            payment_method = input(f"Enter Payment Method (current: {payment[3]}): ") or payment[3]

            payment_status = input(f"Enter Payment Status (current: {payment[4]}): ") or payment[4]

            try:
                cursor.execute(
                    """
                    UPDATE payment 
                    SET payment_date = %s, amount = %s, payment_method = %s, payment_status = %s
                    WHERE payment_id = %s
                    """,
                    (payment_date, amount, payment_method, payment_status, payment_id)
                )
                connection.commit()
                print("Payment updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            print("Payment ID not found.")

# create or update booking
def create_or_update_booking(action, cursor, connection):
    if action == "create":
        check_in_date = input("Enter Check-in Date (YYYY-MM-DD): ")
        while not is_valid_date(check_in_date):
            print("Invalid date format. Please try again.")
            check_in_date = input("Enter Check-in Date (YYYY-MM-DD): ")

        check_out_date = input("Enter Check-out Date (YYYY-MM-DD): ")
        while not is_valid_date(check_out_date):
            print("Invalid date format. Please try again.")
            check_out_date = input("Enter Check-out Date (YYYY-MM-DD): ")

        total_cost = input("Enter Total Cost: ")
        while not total_cost.isdigit() or int(total_cost) <= 0:
            print("Invalid total cost. Please enter a positive integer.")
            total_cost = input("Enter Total Cost: ")

        booking_status = input("Enter Booking Status (e.g., Confirmed, Pending, Canceled): ")

        view_trips()
        trip_id = input("Enter Trip ID: ")
        while not trip_id.isdigit() or int(trip_id) <= 0:
            print("Invalid Trip ID. Please enter a valid positive integer.")
            trip_id = input("Enter Trip ID: ")

        view_accommodation()
        accommodation_id = input("Enter Accommodation ID: ")
        while not accommodation_id.isdigit() or int(accommodation_id) <= 0:
            print("Invalid Accommodation ID. Please enter a valid positive integer.")
            accommodation_id = input("Enter Accommodation ID: ")

        try:
            cursor.execute(
                """
                INSERT INTO booking (check_in_date, check_out_date, total_cost, booking_status, trip_id, accommodation_id)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (check_in_date, check_out_date, total_cost, booking_status, trip_id, accommodation_id)
            )
            connection.commit()
            print("Booking created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

    elif action == "update":
        view_bookings()

        booking_id = input("Enter Booking ID to update: ")

        cursor.execute("SELECT * FROM booking WHERE booking_id = %s", (booking_id,))
        booking = cursor.fetchone()
        if booking:
            print(f"Current booking data: {booking}")
            check_in_date = input(f"Enter Check-in Date (current: {booking[1]}): ") or booking[1]
            while check_in_date and not is_valid_date(check_in_date):
                print("Invalid date format. Please try again.")
                check_in_date = input("Enter Check-in Date (YYYY-MM-DD): ") or booking[1]

            check_out_date = input(f"Enter Check-out Date (current: {booking[2]}): ") or booking[2]
            while check_out_date and not is_valid_date(check_out_date):
                print("Invalid date format. Please try again.")
                check_out_date = input("Enter Check-out Date (YYYY-MM-DD): ") or booking[2]

            total_cost = input(f"Enter Total Cost (current: {booking[3]}): ") or booking[3]
            while total_cost and (not total_cost.isdigit() or int(total_cost) <= 0):
                print("Invalid total cost. Please enter a positive integer.")
                total_cost = input(f"Enter Total Cost (current: {booking[3]}): ") or booking[3]

            booking_status = input(f"Enter Booking Status (current: {booking[4]}): ") or booking[4]

            view_trips()
            trip_id = input(f"Enter Trip ID (current: {booking[5]}): ") or booking[5]
            while trip_id and (not trip_id.isdigit() or int(trip_id) <= 0):
                print("Invalid Trip ID. Please enter a valid positive integer.")
                trip_id = input(f"Enter Trip ID (current: {booking[5]}): ") or booking[5]

            view_accommodation()
            accommodation_id = input(f"Enter Accommodation ID (current: {booking[6]}): ") or booking[6]
            while accommodation_id and (not accommodation_id.isdigit() or int(accommodation_id) <= 0):
                print("Invalid Accommodation ID. Please enter a valid positive integer.")
                accommodation_id = input(f"Enter Accommodation ID (current: {booking[6]}): ") or booking[6]

            try:
                cursor.execute(
                    """
                    UPDATE booking 
                    SET check_in_date = %s, check_out_date = %s, total_cost = %s, booking_status = %s, 
                        trip_id = %s, accommodation_id = %s
                    WHERE booking_id = %s
                    """,
                    (check_in_date, check_out_date, total_cost, booking_status, trip_id, accommodation_id, booking_id)
                )
                connection.commit()
                print("Booking updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            print("Booking ID not found.")

# create or update review
def create_or_update_review(action, cursor, connection):
    if action == "create":
        rating = input("Enter Rating (1-5): ")
        while not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
            print("Invalid rating. Please enter a number between 1 and 5.")
            rating = input("Enter Rating (1-5): ")

        review_text = input("Enter Review Text: ")

        review_date = input("Enter Review Date (YYYY-MM-DD): ")
        while not is_valid_date(review_date):
            print("Invalid date format. Please try again.")
            review_date = input("Enter Review Date (YYYY-MM-DD): ")

        view_users()
        user_id = input("Enter User ID: ")

        view_accommodation()
        accommodation_id = input("Enter Accommodation ID: ")

        try:
            cursor.execute(
                """
                INSERT INTO reviews (rating, review_text, review_date, user_id, accommodation_id)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (rating, review_text, review_date, user_id, accommodation_id)
            )
            connection.commit()
            print("Review created successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()

    elif action == "update":
        view_reviews()

        review_id = input("Enter Review ID to update: ")

        cursor.execute("SELECT * FROM reviews WHERE review_id = %s", (review_id,))
        review = cursor.fetchone()
        if review:
            print(f"Current review data: {review}")
            rating = input(f"Enter Rating (current: {review[1]}): ") or review[1]
            while rating and (not rating.isdigit() or int(rating) < 1 or int(rating) > 5):
                print("Invalid rating. Please enter a number between 1 and 5.")
                rating = input(f"Enter Rating (current: {review[1]}): ") or review[1]

            review_text = input(f"Enter Review Text (current: {review[2]}): ") or review[2]

            review_date = input(f"Enter Review Date (current: {review[3]}): ") or review[3]
            while review_date and not is_valid_date(review_date):
                print("Invalid date format. Please try again.")
                review_date = input(f"Enter Review Date (current: {review[3]}): ") or review[3]

            user_id = input(f"Enter User ID (current: {review[4]}): ") or review[4]
            accommodation_id = input(f"Enter Accommodation ID (current: {review[5]}): ") or review[5]

            try:
                cursor.execute(
                    """
                    UPDATE reviews 
                    SET rating = %s, review_text = %s, review_date = %s, user_id = %s, accommodation_id = %s
                    WHERE review_id = %s
                    """,
                    (rating, review_text, review_date, user_id, accommodation_id, review_id)
                )
                connection.commit()
                print("Review updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            print("Review ID not found.")


# delete a trip
def delete_trip():
    connection = connect_db()
    cursor = connection.cursor()

    view_trips()

    trip_id = input("Enter Trip ID to delete: ")

    try:
        cursor.execute("DELETE FROM trip WHERE trip_id = %s", (trip_id,))
        connection.commit()
        print("Trip deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# delete a destination
def delete_destination():
    connection = connect_db()
    cursor = connection.cursor()

    view_destinations()

    destination_id = input("Enter Destination ID to delete: ")

    try:
        cursor.execute("DELETE FROM destination WHERE destination_id = %s", (destination_id,))
        connection.commit()
        print("Destination deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# delete a user
def delete_user():
    connection = connect_db()
    cursor = connection.cursor()

    view_users()

    user_id = input("Enter User ID to delete: ")

    try:
        cursor.execute("DELETE FROM app_user WHERE user_id = %s", (user_id,))
        connection.commit()
        print("User deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# delete a activity
def delete_activity():
    connection = connect_db()
    cursor = connection.cursor()

    view_activities()

    activity_id = input("Enter User ID to delete: ")

    try:
        cursor.execute("DELETE FROM activities WHERE activity_id = %s", (activity_id,))
        connection.commit()
        print("Activity deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# delete a transportation
def delete_transportation():
    connection = connect_db()
    cursor = connection.cursor()

    view_transportations()

    transportation_id = input("Enter Transportation ID to delete: ")

    try:
        cursor.execute("DELETE FROM transportation WHERE transportation_id = %s", (transportation_id,))
        connection.commit()
        print("Transportation deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# delete a accommodations
def delete_accommodation():
    connection = connect_db()
    cursor = connection.cursor()

    view_accommodation()

    transportation_id = input("Enter Accommodation ID to delete: ")

    try:
        cursor.execute("DELETE FROM accommodation WHERE accommodation_id = %s", (transportation_id,))
        connection.commit()
        print("Accommodation deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# delete a booking
def delete_bookings():
    connection = connect_db()
    cursor = connection.cursor()

    view_bookings()

    booking_id = input("Enter Booking ID to delete: ")

    try:
        cursor.execute("DELETE FROM booking WHERE booking_id = %s", (booking_id,))
        connection.commit()
        print("Booking deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# delete a payment
def delete_payments():
    connection = connect_db()
    cursor = connection.cursor()

    view_payments()

    payment_id = input("Enter Payment ID to delete: ")

    try:
        cursor.execute("DELETE FROM booking WHERE booking_id = %s", (payment_id,))
        connection.commit()
        print("Payment deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# delete a review
def delete_reviews():
    connection = connect_db()
    cursor = connection.cursor()

    view_payments()

    review_id = input("Enter Payment ID to delete: ")

    try:
        cursor.execute("DELETE FROM review WHERE review_id = %s", (review_id,))
        connection.commit()
        print("Review deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def main_menu():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        while True:
            print("\nTravel Management System")
            print("-----------------")
            print("Tables:")
            tables = [
                "Users",
                "Destinations",
                "Trips",
                "Transportations",
                "Activities",
                "Accommodations",
                "Bookings",
                "Payments",
                "Reviews"
            ]

            for i, table in enumerate(tables, 1):
                print(f"{i}. {table}")

            print("0. Exit")

            table_choice = input("Select a table to manage (0-9): ")

            if table_choice == "0":
                break

            try:
                table_index = int(table_choice) - 1
                selected_table = tables[table_index]
            except (ValueError, IndexError):
                print("Invalid table selection.")
                continue

            while True:
                print(f"\nManaging {selected_table}")
                print("1. View")
                print("2. Create")
                print("3. Update")
                print("4. Delete")
                print("0. Back to Main Menu")

                crud_choice = input("Select an operation (0-4): ")

                view_funcs = {
                    "Users": view_users,
                    "Destinations": view_destinations,
                    "Trips": view_trips,
                    "Transportations": view_transportations,
                    "Activities": view_activities,
                    "Accommodations": view_accommodation,
                    "Bookings": view_bookings,
                    "Payments": view_payments,
                    "Reviews": view_reviews
                }

                create_update_funcs = {
                    "Users": create_or_update_user,
                    "Destinations": create_or_update_destination,
                    "Trips": create_or_update_trip,
                    "Transportations": create_or_update_transportation,
                    "Bookings": create_or_update_booking,
                    "Payments": create_or_update_payment,
                    "Reviews": create_or_update_review,
                    "Activities": create_or_update_activity,
                    "Accommodations": create_or_update_accommodation,
                }

                delete_funcs = {
                    "Users": delete_user,
                    "Destinations": delete_destination,
                    "Trips": delete_trip,
                    "Transportations": delete_transportation,
                    "Bookings": delete_bookings,
                    "Payments": delete_payments,
                    "Reviews": delete_reviews,
                    "Activities": delete_activity,
                    "Accommodations": delete_accommodation,
                }

                if crud_choice == "1":
                    view_funcs.get(selected_table)()
                elif crud_choice == "2":
                    create_update_funcs.get(selected_table)(
                        "create", cursor, connection
                    )
                elif crud_choice == "3":
                    create_update_funcs.get(selected_table)(
                        "update", cursor, connection
                    )
                elif crud_choice == "4":
                    delete_funcs.get(selected_table)()
                elif crud_choice == "0":
                    break
                else:
                    print("Invalid operation.")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main_menu()