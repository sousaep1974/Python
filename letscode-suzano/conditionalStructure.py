ticket_price = 4.60
""" trip_value = input("Qual valor da viagem de uber? ")
if float(trip_value) <= ticket_price * 5:
    print("Pague a viagem")
if float(trip_value) > ticket_price * 5:
    print("Pegue o ônibus") """

trip_value = input("Qual valor da viagem de uber? ")
if float(trip_value) <= ticket_price * 5:
    print("Pague a viagem")
elif float(trip_value) <= ticket_price * 6:
        print("Espere um pouco o valor pode baixar")
else:
        print("Pegue o ônibus")