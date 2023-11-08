https://replit.com/join/vekimajcgw-lucasleite32

n_events = int(input("How many events does the Quidditch match have? "))
print()
Gryffindor_score = 0
Slytherin_score = 0

for i in range(n_events):
    event = input("Enter an event (goal/snitch/foul): ")
    print()

    if event == "goal":
        team = input("Which team scored (Gryffindor or Slytherin): ")
        print()
      
        if team == "Gryffindor":
            Gryffindor_score += 10
        elif team == "Slytherin":
            Slytherin_score += 10

    elif event == "snitch":
        team = input("Which team caught the Snitch (Gryffindor or Slytherin): ")
        print()
      
        if team == "Gryffindor":
            Gryffindor_score += 150
        elif team == "Slytherin":
            Slytherin_score += 150

    elif event == "foul":
        team = input("Which team committed a foul (Gryffindor or Slytherin): ")
        print()
      
        if team == "Gryffindor":
            Gryffindor_score -= 30
        elif team == "Slytherin":
            Slytherin_score -= 30

print()
print("The Gryffindor team scored", Gryffindor_score, "points.")
print()
print("The Slytherin team scored", Slytherin_score, "points")
print()

if Gryffindor_score > Slytherin_score:
    print("The Gryffindor team wins")
  
elif Gryffindor_score < Slytherin_score:
    print("The Slytherin team wins")
  
else:
    print("It's a tie!")
