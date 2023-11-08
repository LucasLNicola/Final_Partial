https://replit.com/join/qlsiiyymzd-lucasleite32

calling_a = input().lower()
print()
words = calling_a.split()

alexa_count = words.count("alexa")

if alexa_count == 1:
    print("Tell me, how can I help you?")
   
elif alexa_count > 1:
    print("Hey, just say my name once")

else:
    print("No one answers for this name")
