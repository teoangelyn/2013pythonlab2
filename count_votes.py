# count_votes.py

try: 
    infile = open("VOTES.DAT", "r")

    votes = infile.readlines()
    papcount = 0
    wpcount = 0
    sdacount = 0
    rpcount = 0
    spoiltvotes = 0

    for vote in votes:
        if vote == 'PAP,1\n':
            papcount += 1
        elif vote == 'WP,1\n':
            wpcount += 1
        elif vote == 'SDA,1\n':
            sdacount += 1
        elif vote == 'RP,1\n':
            rpcount += 1
        else:
            spoiltvotes += 1

    infile.close()

except IOError:
    print("Cannot read from VOTES.DAT")

total = papcount + wpcount + sdacount + rpcount + spoiltvotes
pappercentage = papcount / total * 100
wppercentage = wpcount / total * 100
sdapercentage = sdacount / total * 100
rppercentage = rpcount / total * 100
spoiltpercentage = spoiltvotes / total * 100

print("# of PAP votes: " + str(papcount))
print("% of PAP votes: " + "{0:.2f}".format(pappercentage) + "\n")
print("# of WP votes: " + str(wpcount))
print("% of WP votes: " + "{0:.2f}".format(wppercentage) + "\n")

print("# of SDA votes: " + str(sdacount))
print("% of SDA votes: " + "{0:.2f}".format(sdapercentage) + "\n")

print("# of RP votes: " + str(rpcount))
print("% of RP votes: " + "{0:.2f}".format(rppercentage) + "\n")

print("# of spoilt votes: " + str(spoiltvotes))
print("% of spoilt votes: " + "{0:.2f}".format(spoiltpercentage))
