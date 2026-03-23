# This helps divide hours based on how hard a subject is

print("--- WELCOME TO MY STUDY PLANNER ---")

# Getting inputs
# I'm just putting everything in a list of dicts
all_subs = []
num = int(input("How many subjects you got? "))

# Using a simple for loop
for i in range(num):
    print("\nSetting up subject " + str(i+1))
    n = input("Name of subject: ")
    d = int(input("Difficulty (1 to 5): ")) # 5 is hardest
    
    # s for subject, diff for difficulty
    temp = {"s": n, "diff": d}
    all_subs.append(temp)

# Totaling up the difficulty points
# This is how we will divide the time
total_d = 0
for x in all_subs:
    total_d = total_d + x["diff"]

# Getting total hours
hrs = float(input("\nHow many hours can you study today? "))

print("\n" + "="*25)
print("   YOUR STUDY PLAN")
print("="*25)

# Calculating and printing at the same time
# (Easier than making another list)
for item in all_subs:
    # Logic: (subject diff / total diff) * total hours
    # This gives more time to hard subjects
    calc = (item["diff"] / total_d) * hrs
    
    # Rounding it to 2 decimal places so it looks clean
    final_time = round(calc, 2)
    
    print(item["s"] + ": " + str(final_time) + " hours")

print("\nGood luck with your studies!")
# TODO: Maybe add a feature to save this to a txt file? 
# No time left now.