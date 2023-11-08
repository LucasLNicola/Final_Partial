https://replit.com/join/cnrpbykzow-lucasleite32

temperature_read = int(input("How many temperature readings do you have? "))
print()
temperature = []
wrong = 0

if temperature_read > 0:
  for i in range(temperature_read):
    temperatures = float(input("Temperature " + str(i+1) + ": "))
    print()
    temperature.append(temperatures)
  
    if temperatures < 10 or temperatures > 40:
      wrong += 1

error_rate = float(wrong / temperature_read * 100)

print(f"The sensor went wrong {wrong} times")
print()
print(f"The sensor error rate is {error_rate}")
