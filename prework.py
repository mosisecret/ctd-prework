
# Recommends which playgrounds parents can visit with their kids on +
# hot days in Durham. Considers what parks are best for +
# learning to ride a bike.

# Playground options to choose from for our recommendation.
rock = "Rockwood Park Playground"
oval = "Oval Park Playground"
burch = "Burch Avenue Playground"

# Playgrounds with shade
shade_trees = burch + " and " + rock

#Playgrounds with bike paths
bike_paths = rock + " and " + oval

# Collect data to inform our recommendation.
temp = int(input("What is today's high temperature? "))
is_biking = input("Do you want to practice bike riding with your kid(s)?"
+" " +"Respond yes or no. ")

# Make a playground recommendation based on temperature and biking preference.

if temp >= 85:
    # On hot days, it's nice to have shade. But not all+
    #shady parks have good
    rec = rock
    if is_biking == "yes":
        print(rec + " has shade trees,"
              + " and there's a nice path to practice biking.")
    if is_biking == "no":
        rec = shade_trees
        print(rec + " both have shade. Have fun!")
 
else:
    #On cooler days
    if is_biking == "yes":
        rec = bike_paths
        print(rec + " have great paths to practice on.")

    else:
        print(rock + " or " + burch + " or " + oval + " will do. Have fun!")


