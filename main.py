"""
Task 4:
You are hired as a software coder for Movies4Us Pty Ltd located in Melbourne, Australia. 
Your task is to develop a software program that issues 200 movie tickets. Your software 
program is to print “welcome to Movie4Us” to the first 200 users but write “there is no more ticket”
 to the 201th user. The software also needs to display how many tickets are available to each customer.
For example, if Tim is 50th user to buy the movie ticket, your software program should display 
“You are the 50th user. The number of remaining tickets is now 150”. Prepare software code with sufficient 
comments to explain the progress.

@author: Jordan
"""
import random as r #To simulate consumers buying tickets https://www.w3schools.com/python/module_random.asp

class TicketPurchase:
    def __init__(self, username, sessions):
        self.movie_title, self.session_time, self.reserved_tickets, self.total_seats = sessions
        self.available_seats = self.total_seats - self.reserved_tickets
        self.username = username
        self.prompt_spacing = '\n\t\t\t\t\t->'
        self.bold = '\033[4m\033[1m'
        self.unbold = '\033[0m\033[0m'

    def ticketDispenser(self):
        while self.available_seats > 0:  #Loop until all tickets are issued
            user_purchase= int(input(f'\nHow many tickets do you want to purchase? (Enter a number from: 1-{self.available_seats}){self.prompt_spacing}'))
            self.reserved_tickets += user_purchase    #Increment the user count

            if user_purchase <= self.available_seats:  #Check if tickets are available
                self.available_seats = self.available_seats - user_purchase
                print(f"Thankyou for watching with us {self.username}! Your {user_purchase} tickets makes you the {self.reserved_tickets}th viewer!")
                print(f"The number of tickets remaining is now {self.available_seats}.")
            else:
                #If all tickets are issued and loop ends, print the message for the 201st user
                print(f"\n\nThere are not enough tickets left to buy {user_purchase} tickets. There are just {self.available_seats} remaining.\nPlease purchase a lower amount of tickets or sign up to another movie session")  #Print if no more tickets are available
        else:
            print(f"\n{self.bold}All tickets have been issued, the session is full{self.unbold}\nThanks for watching with us {username}.")


def sessions(total_seats):
    movie_times = {
        "Dune: Part Two": ['08:00', '9:00', '11:00', '12:00', '14:00', '16:30', '18:00', '19:00', '20:30'],
        "Kung Fu Panda 4": ['07:00', '8:00', '11:00', '13:00', '14:30', '16:00', '17:00'],
        "Godzilla X Kong: The New Empire": ['10:00', '13:00', '15:00', '17:30', '19:00', '21:00', '22:30'],
        "The First Omen": ['16:00', '19:30', '21:30', '22:30'],
        "Ghostbusters: Frozen Empire": ['12:00', '13:00', '14:30', '15:30', '17:00', '19:30'],
        "Monkey Man": ['18:00', '19:00', '20:30'],
        "Barbie and The Twelve Dancing Princesses": ['10:00', '12:00'],
        "Barbie: Fairytopia": ['1:00']
    }
    bold = '\033[4m\033[1m'
    unbold = '\033[0m\033[0m'
    movie_options = {}
    available_seats = {}
    i = 0
    prompt_spacing = '\n\t\t\t\t\t->'
    print(f"\t\t\t\t\t{bold}Press CTRL-C to quit!{unbold}")
    print(f"{bold}Available sessions information:{unbold}") #Tricker. (2020, June 25). How can i put formated text in python? (Bold, italic, etc.) | Sololearn: Learn to code for FREE! https://www.sololearn.com/en/discuss/2359764/how-can-i-put-formated-text-in-python-bold-italic-etc
    
    error = ''
    while True:
        for session in movie_times:
            if i < len(movie_times):
                i += 1
            else:
                i = 1
            print(f"| Enter: {i} | for: {session}")
            movie_options[i] = session

            for times in movie_times[session]:
                available_seats[f'{session}@{times}'] = r.randint(0,200)
                #^ this dictionary value ^ is set to an arbitrary number to attempt to simulate a real box office scenario by using the randint() method from the 'random' module; source: w3schools. (2024). Python Random randint() Method. https://www.w3schools.com/python/ref_random_randint.asp
        try:
            movie_selection = int(input(f"What Movie do you want to watch? {error}{prompt_spacing}"))
        except ValueError:
            error = bold + 'Error: Input must be a number between 1-' + str(len(movie_times)) + unbold
        else:
            break

    movie_selection = movie_options[movie_selection]

    while True:
        print(f"\nFor {bold}{movie_selection}{unbold} There are {bold}{len(movie_times[movie_selection])} sessions available{unbold}. Please pick your time:")
        
        for times in movie_times[movie_selection]:
            print('|', times, '| Available seats:', total_seats - available_seats[movie_selection+'@'+times]) 
  
        for movie_slots in list(available_seats):
            if movie_selection not in movie_slots:
                available_seats.pop(movie_slots) #Olumide, S. (2023, February 22). Python Remove Key from Dictionary – How to Delete Keys from a Dict. freeCodeCamp.Org. https://www.freecodecamp.org/news/python-remove-key-from-dictionary/

            session_time = input(f"\nPlease enter your chosen time in 24 hour format (HH:00 only){prompt_spacing}")
            if session_time not in movie_times[movie_selection]:
                print(f"\nFor {bold}{movie_selection}{unbold} There are {bold}{len(movie_times[movie_selection])} sessions available{unbold}. Please pick your time:")
                for times in movie_times[movie_selection]:
                    print('|', times, '| Available seats:', total_seats - available_seats[movie_selection+'@'+times]) 
            else:
                break
        if session_time in movie_times[movie_selection]:
            break

    print(f"\nFor {movie_selection}, {available_seats[movie_selection+'@'+session_time]} tickets have been purchased by customers")


    return (movie_selection, session_time, available_seats[movie_selection+'@'+session_time], total_seats)

username = input('\n\nWelcome to Movies4Us, Please enter your username:\n\t\t\t\t\t->')

TicketPurchase(username, sessions(200)).ticketDispenser() #answered by: Flury, T. (2023). How do you pass a tuple to a function in Python? Quora. Retrieved 9 April 2024, from https://www.quora.com/How-do-you-pass-a-tuple-to-a-function-in-Python