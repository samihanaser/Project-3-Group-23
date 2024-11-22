import calendar
import random
import tkinter as tk
from tkinter import ttk

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

    def generate_schedule(self, year, month):
        # Define shifts
        shifts = ["7:00AM - 1:00PM", "1:00PM - 7:00PM"]

        # Get the number of days in the specified month
        num_days = calendar.monthrange(year, month)[1]
        
        # Randomly assign people to shifts for each day of the month
        self.schedule = {}

        for day in range(1, num_days + 1):
            self.schedule[day] = {
                shifts[0]: random.choice(self.people),  # Assign someone to the morning shift
                shifts[1]: random.choice(self.people)   # Assign someone to the afternoon shift
            }

        return self.schedule

    def display_schedule_as_html(self, schedule, year, month):
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
        html_schedule += "</table></body></html>"
        return html_schedule

    # Sample list of people to assign
    people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]

    # Get user input for the year and month
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

#function to open popout window
def show_html_window(root, html_content):
    popout = tk.Toplevel(root)
    popout.title("Schedule HTML View")
    popout.geometry("800x600")

    text_widget = tk.Text(popout, wrap="word")
    text_widget.insert("1.0", html_content)
    text_widget.config(state="disabled")  # Make the content read-only
    text_widget.pack(expand=True, fill="both")

    #print(f"HTML work schedule for {calendar.month_name[calendar.month]} , {calendar.year} generated successfully!")

    def calculate_payroll(self):
        payroll = {}
        for person in self.person:
            payroll[person.name] = person.calculate_pay()
        return payroll

def main():
    root = tk.Tk()
    root.title("Schedule Manager")

    manager = ManageSchedule()

# Add caregivers
    manager.add_person(Manager("Alice", "123-456", "alice@example.com", 20, True))
    manager.add_person(Manager("Bob", "789-012", "bob@example.com", 18, True))
    manager.add_person(Manager("Charlie", "345-678", "charlie@example.com", 22, True))

    # Update availability
    manager.person[0].set_availability(0, 0, 'preferred')  # Monday AM
    manager.person[1].set_availability(2, 1, 'unavailable')  # Wednesday PM

    # Generate and display the schedule
    year, month = 11, 2024
    schedule = manager.generate_schedule(year, month)
    html_content = manager.display_schedule_as_html(year, month)

    #button to display html in popout window
    display_button = ttk.Button(root, text="Show HTML Schedule", command=lambda: show_html_window(root, html_content))
    display_button.pack(pady=20)

    # Calculate and display payroll
    payroll = manager.calculate_payroll()
    for name, pay in payroll.items():
        print(f"{name}: ${pay:.2f}") 

    print(f"HTML work schedule for {calendar.month_name[calendar.month]} , {calendar.year} generated successfully!")
    root.mainloop()

if __name__ == "__main__":
    main()