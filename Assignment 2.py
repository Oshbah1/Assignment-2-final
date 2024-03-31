artwork_dictionary = {"title": [],
                      "artist_name": [],
                      "Date_Of_Creation": [],
                      "history_significance": []}
event_dictinary = {"event_name": [],
                   "start_date_time": [],
                   "end_date_time": [],
                   "venue": []}
price_dictionary = {"Entry_Gate": 63,
                    "event_name_price": {}}


class event:
    global event_dictinary

    def __init__(self, event_name, start_date_time, end_date_time, venue):
        self.event_name = event_name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.venue = venue
        event_name_variable = input("the big event ")

    def event_save(self):
        event_dictinary['event_name'].append(self.event_name)
        event_dictinary['start_date_time'].append(self.start_date_time)
        event_dictinary['end_date_time'].append(self.end_date_time)
        event_dictinary['venue'].append(self.venue)


class artwork:
    global artwork_dictionary

    def __init__(self, title, artist_name, Date_Of_Creation, history_significance):
        self.title = title
        self.artist_name = artist_name
        self.Date_Of_Creation = Date_Of_Creation
        self.history_significance = history_significance

    def artwork_save(self):
        artwork_dictionary['title'].append(self.title)
        artwork_dictionary['artist_name'].append(self.artist_name)
        artwork_dictionary['Date_Of_Creation'].append(self.Date_Of_Creation)
        artwork_dictionary['history_significance'].append(self.history_significance)


class artwork_handler(artwork):
    def __init__(self, title, artist_name, Date_Of_Creation, history_significance):
        self.title = title
        self.artist_name = artist_name
        self.Date_Of_Creation = Date_Of_Creation
        self.history_significance = history_significance

    def verify_confirm_artwork_info(self):
        print("title :", self.title)
        print("artist_name :", self.artist_name)
        print("Date_Of_Creation :", self.Date_Of_Creation)
        print("history_significance :", self.history_significance)

        confirm = input("please confirm (yes/no):")
        if confirm == 'yes':
            artwork.artwork_save(self)
            print('Item info saved')
        else:
            print("discarded")


class event_handler(event):
    global event_dictinary

    def __init__(self, event_name, start_date_time, end_date_time, venue):
        self.event_name = event_name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.venue = venue

    def verify_confirm_event_info(self):
        print("event_name :", self.event_name)
        print("start_date_time :", self.start_date_time)
        print("end_date_time :", self.end_date_time)
        print("venue :", self.venue)

        confirm = input("please confirm (yes/no):")
        if confirm == 'yes':
            event.event_save(self)
            print('price added or modified')
        else:
            print("discarded")


class ticket_purchase:
    # userr will by ticket
    some_global_value = 10

    def __init__(self, visitor):
        print('Entry_Gate :', price_dictionary['Entry_Gate'])
        for k in price_dictionary['event_name_price']:
            print(k, ":", price_dictionary['event_name_price'][k])
        self.visitor = visitor

    def book_ticket(price_value):
        price_value = some_global_value
        ticket_price = 0
        if self.visitor.Entry_gate:
            ticket_price = price_dictionary['Entry_Gate']
            event_name = "Entry_Gate"
        else :
            while True:
                event_name = self.visitor.event_name
                ticket_price = price_dictionary['event_name_price'].get(event_name)
                if ticket_price is not None:
                    break  # Break the loop if the event name exists
                print("No Event with this Name. Please try again.")
                # Optional: Allow the user to try again or exit
                try_again = input("Do you want to try another event name? (yes/no): ")
                if try_again.lower() != 'yes':
                    return 0  # Exit the booking process if the user does not want to try again
                self.visitor.event_name = input("Please enter event Name: ")

        price_dictionary['event_name_price'][event_name_variable] = price_value

        if self.visitor.age >= 18 and self.visitor.age <= 60 and self.visitor.category == 'adult':
            ticket_price = ticket_price + (ticket_price * 0.05)
        if self.visitor.category in ['teacher', 'student', 'senior', 'children'] or \
                self.visitor.age < 18:
            if self.visitor.ID_card == 'yes':
                ticket_price = 0
        if self.visitor.group == True:
            count_group = int(input("Total Person In Group :"))
            ticket_price = (count_group * ticket_price) * 0.5  # 50% discount

        return ticket_price

    def final_ticket(self, names, event_names, prices, visitor_cat):
        print("The final Bill !!!")
        total = 0
        for i in range(len(names)):
            print("Name :", names[i])
            print("categpry :", visitor_cat[i])
            print('event name :', event_names[i])
            print("Ticket Price :", prices[i])
            total += prices[i]

        print("Total Price :", total)


class ticket_manager:
    global price_dictionary

    def __init__(self, Museum_entry=True, event_name=False, price=62):
        '''
        Assuming Museum_entry fees = 62 Base Price , And Price will vary according to different event
        '''
        self.Museum_entry = Museum_entry
        if event_name != False:
            self.event_name = event_name
        self.price = price

    def verify_and_confirm(self):
        if self.Museum_entry == True:
            print("Museum_entry :", "Museum_entry_fee")
        else:
            print("event_name :", self.event_name)
        print("price :", self.price)

        confirm = input("please confirm (yes/no):")
        if confirm == 'yes':
            if self.Museum_entry != True:
                price_dictionary['event_name_price']['event_name'] = self.price
            else:
                price_dictionary['Entry_Gate'] = self.price
            print('price added or modified')
        else:
            print("discarded")


class admin_info_viwer:
    global event_dictinary, artwork_dictionary, price_dictionary

    def event_info(self):
        for i in range(len(event_dictinary['event_name'])):
            print('event_name :', event_dictinary['event_name'][i])
            print('start_date_time :', event_dictinary['start_date_time'][i])
            print('end_date_time :', event_dictinary['end_date_time'][i])
            print('venue :', event_dictinary['venue'][i])
            print()

    def artwork_info(self):
        for i in range(len(artwork_dictionary['title'])):
            print('title :', artwork_dictionary['title'][i])
            print('artist_name :', artwork_dictionary['artist_name'][i])
            print('Date_Of_Creation :', artwork_dictionary['Date_Of_Creation'][i])
            print('history_significance :', artwork_dictionary['history_significance'][i])
            print()

    def price_info(self):
        print('Entry_Gate :', price_dictionary['Entry_Gate'])
        for k in price_dictionary['event_name_price']:
            print(k, ":", price_dictionary['event_name_price'][k])
        print()


class visitor:
    def __init__(self, name, mobile_number, email, Entry_gate='yes', event_name=None, \
                 age=None, category=None, group='no', ID_card='no'):
        self.name = name
        self.mobile_number = mobile_number
        self.email = email
        self.Entry_gate = Entry_gate
        self.event_name = event_name
        self.category = category
        self.group = group
        self.age = age
        self.ID_card = ID_card
        print('Visitor Created!!!')


def final_ticket(names, event_names, prices, visitor_cat):
    print("The final Bill !!!")
    total = 0
    for i in range(len(names)):
        print("Name :", names[i])
        print("categpry :", visitor_cat[i])
        print('event name :', event_names[i])
        print("Ticket Price :", prices[i])
        total += prices[i]

    print("Total Price :", total)


# This block of code is specifically for ticket purchase only by visitor for
# entry gate or any event/exhibition

names = []
event_names = []
prices = []
visitor_cat = []

while True:
    vis = visitor(name="Richard", mobile_number=1234567895, email="abc@xyz.com",
                  Entry_gate='yes', age=25, category='adult')
    obj_ticketpurchase = ticket_purchase(vis)
    ticket_price = price_dictionary['event_name_price'].get("the big event")

    names.append(vis.name)
    event_names.append(vis.event_name)
    prices.append(ticket_price)
    visitor_cat.append(vis.category)
    more_ticket = input('Do you want to purchase more ticket (yes/no) :')
    if more_ticket.lower() == 'yes':
        name = input("Please enter your name :")
        mobile_number = input("please enter your mobile number :")
        email = input("Please enter your email :")
        Entry_gate = input("Do you want Normal Museum Entry ticket (yes/no) :")
        if Entry_gate.lower() == 'no':
            event_name = input("Please enter event Name :")
        else:
            event_name = "the big event"
        age = input("Please enter your age :")
        category = input("Please enter your category (adult/child/student/teacher) :")  # Correct spelling
        group = input("You want Group ticket (yes/no) :")
        Id_Card = input("Do you have Id_card (yes/no) :")
        vis = visitor(name=name, mobile_number=mobile_number, email=email,
                      Entry_gate=Entry_gate, event_name=event_name, age=age, category=category,
                      group=group, ID_card=Id_Card)
        # Presumably, you need to add the newly created visitor to the lists again
        names.append(vis.name)
        event_names.append(vis.event_name)
        # You need to determine the price for the new event_name and append it to prices
        # prices.append(new_ticket_price)  # Replace with actual price calculation
        visitor_cat.append(vis.category)
        # ... Further processing ...
    else:
        print("Thank you for your purchase.")
        break  # Break out of the loop if no more tickets need to be purchased.



# test case 1 : The addition of new art to the museum

# Function to add a new event
def add_new_event():
    event_name = input("Festive gala: ")
    start_date_time = input("2/5/2024 9:00 AM'): ")
    end_date_time = input( "10/5/2024 6:00 PM'): ")
    venue = input("Exhibition Hall 1'): ")
    new_event = event_handler(event_name, start_date_time, end_date_time, venue)
    new_event.verify_confirm_event_info()

# add first artwork
obj_artwork = artwork_handler(title="The Starry Night", artist_name="Paul", \
                              Date_Of_Creation="1/1/1900", history_significance="High")
obj_artwork.verify_confirm_artwork_info()
# add second artwork
obj_artwork = artwork_handler(title="Mona Lisa", artist_name="Leonardo da vinci", \
                              Date_Of_Creation="1/1/1503", history_significance="High")
obj_artwork.verify_confirm_artwork_info()
# visualize your all previosuly stored artwork
obj_viewer = admin_info_viwer()
obj_viewer.artwork_info()

# test case 2 : Create new exhibition or event at museum

# added new event by manager
obj_event_hanlder = event_handler(event_name="spark", start_date_time="2/5/2024 9:00 AM", \
                                  end_date_time="10/5/2024 6:00 PM", venue="exhibition halls")
obj_event_hanlder.verify_confirm_event_info()
# view all previously added event
obj_viewer = admin_info_viwer()
obj_viewer.event_info()

# test case
some_iterable = [1, 2, 3, 4]
for some_variable in some_iterable:
    names = []
    event_names = []
    prices = []
    visitor_cat = []

while True:
    more_ticket = input("Do you want to purchase more ticket (yes/no) :")
    if more_ticket.lower() == 'no':
        print("Thank you for your purchase.")
        break  # This should exit the while loop
    else:
        event_name = None
    age = input("Please enter you age :")
    categpry = input("Please enter your category :")  # adult, children, student, teacher
    group = input("You want Group ticket (yes/no) :")
    Id_Card = input("Do you have Id_card (yes/no) :")
    vis = visitor(name=name, mobile_number=mobile_number, email=email,
                  Entry_gate=Entry_gate, event_name=event_name, age=age, category=categpry,
                  group=group, ID_card=Id_Card)
    obj_ticketpurchase = ticket_purchase(vis)
    ticket_price = obj_ticketpurchase.book_ticket()
    names.append(vis.name)
    event_names.append(vis.event_name)
    prices.append(ticket_price)
    visitor_cat.append(vis.category)
    more_ticket = input('Do you want to purchase more ticket (yes/no) :')
    if more_ticket == 'no':
        break
print("purchase Done!!!!!")
