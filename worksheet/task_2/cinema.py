#Amritpal Singh
#201965262
"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    conn = sqlite3.connect("tickets.db") 
    cursor = conn.cursor()

    cursor.execute('''select films.title, screenings.screen, tickets.price
                   from screenings join tickets on screenings.screening_id = tickets.screening_id,
                    films on films.film_id = screenings.film_id
                   where tickets.customer_id ?  (customer_id,) 
                   order by films.title asc''') 
    
   
    
    #the query above selected the film title, screen and prices of the tickets
    #joined the tables screenings to films and tickets (as it is the middle table)
    #ordered in alphabetical from a-z
    
    y = cursor.fetchall() #fetch all rows
    return y

def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute('''select screenings.screening_id, films.title, count(tickets.ticket_id) as num_of_tickets
                   from screenings left join films on screenings.film_id = films.film_id, tickets on screenings.screening_id = tickets.screening_id
                   group by screenings.screening_id
                   order by num_of_tickets desc''')

    #query above selects the screening_id, film title and counts tickets sold for that screen
    #do left join to include 0 sales, joins screenings to films and tickets (since it is middle table)
    #order by ticket sales from highest to lowest

    x = cursor.fetchall() #fetch all results
    return x


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("""select customers.customer_name, sum(tickets.price) 
                   from customers join tickets on customers.customer_id = tickets.customer_id
                   group by customers.customer_name
                   order by sum(tickets.price) desc
                   limit ?""", (limit,) ) 
                   
    #query above adds all ticket prices for each customer individually
    #join customers to tickets
    #order by total spent by customer on tickets from highest to lowest
    #set a limit by passsing limit parameter as a tuple 
    #code didn't allow me to rename aggregate to 'total_spent'
    #so not sure if i implemented the num_of_tickets > 0, did it by only join and not left join

    z = cursor.fetchall() #fetch all results
    return z
    