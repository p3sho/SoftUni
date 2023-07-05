price_per_night = 20
transport = 1.6
ticket_for_museum = 6

num_of_people = int(input())
num_of_days = int(input())
num_of_cards_for_transport = int(input())
num_of_tickets = int(input())

total_price_per_day = price_per_night * num_of_days
total_price_for_cards = num_of_cards_for_transport * transport
total_price_of_tickets = num_of_tickets * ticket_for_museum

total_price_per_person = total_price_per_day + total_price_for_cards + total_price_of_tickets
total_price = total_price_per_person * num_of_people

total_price = total_price + total_price * 0.25

print(f"{total_price :.2f}")