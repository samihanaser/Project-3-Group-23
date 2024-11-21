import calendar
import random

#Define caregiver class
class Manager:
    #Initialize variables
    def __init__(self, name, phone, email, payrate, hours, paid = False):
        self.name = name
        self.phone = phone
        self.email = email
        self.payrate = payrate
        self.hours = 0
        self.availability = {day: ['available', 'available'] for day in range(7)}

    def set_availability(self, day, shift, available):
        self.availability[day][shift] = available

    def calculate_pay(self):
        return self.hours * self.payrate if self.paid else 0

class ManageSchedule:
    def __init__(self):
        self.person = []
        self.schedule = {}

    def add_person(self, person):
        self.person.append(person)

    def generate_schedule(people, year, month):
        # Define shifts
        shifts = ["7:00AM - 1:00PM", "1:00PM - 7:00PM"]

        # Get the number of days in the specified month
        num_days = calendar.monthrange(year, month)[1]
        
        # Randomly assign people to shifts for each day of the month
        schedule = {}
        for day in range(1, num_days + 1):
            schedule[day] = {
                shifts[0]: random.choice(people),  # Assign someone to the morning shift
                shifts[1]: random.choice(people)   # Assign someone to the afternoon shift
            }

        return schedule

    def display_schedule_as_html(schedule, year, month):
        # Create the HTML structure
        html_schedule = f"""
        <html>
        <head>
            <title>Work Schedule for {calendar.month_name[month]} {year}</title>
            <style>
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid black;
                    padding: 10px;
                    text-align: center;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                td {{
                    height: 100px;
                    vertical-align: top;
                }}
            </style>
        </head>
        <body>
            <h1>Work Schedule for {calendar.month_name[month]} {year}</h1>
            <table>
                <tr>
                    <th>Mon</th>
                    <th>Tue</th>
                    <th>Wed</th>
                    <th>Thu</th>
                    <th>Fri</th>
                    <th>Sat</th>
                    <th>Sun</th>
                </tr>
        """
        
        # Get the first weekday of the month and the total days
        first_weekday, num_days = calendar.monthrange(year, month)

        # Fill in the days of the month
        current_day = 1
        for week in range((num_days + first_weekday) // 7 + 1):
            html_schedule += "<tr>"
            for day in range(7):
                if (week == 0 and day < first_weekday) or current_day > num_days:
                    html_schedule += "<td></td>"  # Empty cell for days outside the month
                else:
                    # Add the day and the assigned shifts
                    shifts_for_day = schedule.get(current_day, {})
                    morning_shift = shifts_for_day.get("7:00AM - 1:00PM", "N/A")
                    afternoon_shift = shifts_for_day.get("1:00PM - 7:00PM", "N/A")
                    html_schedule += f"<td>{current_day}<br><b>AM:</b> {morning_shift}<br><b>PM:</b> {afternoon_shift}</td>"
                    current_day += 1
            html_schedule += "</tr>"

    # Close the table and HTML
        html_schedule += """
            </table>
        </body>
        </html>
        """
    
    # Write the HTML content to a file
        with open(f"work_schedule_{year}_{month}.html", "w") as file:
            file.write(html_schedule)

        print(f"HTML work schedule for {calendar.month_name[month]} {year} generated successfully!")

    # Sample list of people to assign
    people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]

    # Get user input for the year and month
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    # Generate the work schedule
    schedule = generate_schedule(people, year, month)

    # Display the schedule as an HTML calendar
    display_schedule_as_html(schedule, year, month)

    def calculate_payroll(self):
        payroll = {}
        for person in self.person:
            payroll[person.name] = person.calculate_pay()
        return payroll

def main():
    manager = ManageSchedule()

# Add caregivers
    manager.add_person(Manager("Alice", "123-456", "alice@example.com", 20, True))
    manager.add_person(Manager("Bob", "789-012", "bob@example.com"))
    manager.add_person(Manager("Charlie", "345-678", "charlie@example.com", 20, True))

    # Update availability
    manager.person[0].set_availability(0, 0, 'preferred')  # Monday AM
    manager.person[1].set_availability(2, 1, 'unavailable')  # Wednesday PM

    # Generate and display the schedule
    year = 2024
    month = 11
    manager.generate_schedule(year, month)
    manager.display_schedule_as_html(year, month)

    # Calculate and display payroll
    payroll = manager.calculate_payroll()
    for name, pay in payroll.items():
        print(f"{name}: ${pay:.2f}") 