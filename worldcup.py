winner = "Argentina"

print(" FIFA World Cup 2026 Prediction ")
print("Predict the country that will win the World Cup 2026.")

while True:
    country = input("Enter your prediction: ")

    if country.strip() == "":
        print("Please enter a country name.\n")
        continue

    if country.lower() == "quit":
        print("Thank you for using the prediction program.")
        break

   
    if country.lower() not in [
        "argentina", "brazil", "france", "england", "spain"
    ]:
        pass
        print("That country is not in the list of top competitors.\n")
        continue

   
    if country.lower() == winner.lower():
        print("Excellent prediction! Argentina wins the World Cup 2026!")
        break
    else:
        print("Good guess, but try again.\n")