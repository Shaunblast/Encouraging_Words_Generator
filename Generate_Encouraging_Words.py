L = ["You can do it!", "Keep going!", "Stay strong!", "Storms will happen. Look for the sun!"]
I = ["Chase after your dreams!", "Pursue your dreams relentlessly!", "God has got you!"]
S = ["Be courageous!", "Do it scared!", "Be confident despite other people!"]
T = ["Believe in yourself!", "Be your biggest advocate!", "Never give up on your dreams!"]

encouraging_words = L + I + S + T #Add lists together for their positions

x = len(encouraging_words) #Getting how many total encouraging words I have (automatically changes if add)

encouraging_index = input("Please input a number from 0 to " + str(x-1) + ": ") # x-1 gives index

try: #use try and use except to make sure they put in a number and the number is within our index values
    print(encouraging_words[int(encouraging_index)])
except ValueError:
    print("Please input a number from 0 to " + str(x-1) + " next time.")
except IndexError:
    print("Please input a number from 0 to " + str(x-1) + " next time.")


