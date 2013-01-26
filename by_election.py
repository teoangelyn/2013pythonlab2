# by_election.py

# 50 spaces in 1 row

import datetime



try:
    time = "TIME: HH:MM AM"
    date = datetime.date.today()
    time = datetime.datetime.now()
    
    
    # open votes file to read
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

    total = papcount + wpcount + sdacount + rpcount + spoiltvotes
    pappercentage = papcount / total * 100
    wppercentage = wpcount / total * 100
    sdapercentage = sdacount / total * 100
    rppercentage = rpcount / total * 100
    spoiltpercentage = spoiltvotes / total * 100


    votes = []
    votes.append(papcount)
    votes.append(wpcount)
    votes.append(sdacount)
    votes.append(rpcount)

    parties = ['PAP', 'WP', 'SDA', 'RP']

    for i in range(0, len(votes)):
        highest = 0
        if votes[i] > highest:
            highest = votes[i]
            winner = parties[i]
        i = i + 1

except IOError:
    print("Cannot read from VOTES.DAT")

    
    # open file to write to
try: 
    outfile = open("RESULTS.TXT", "w")
    
    outfile.write("DATE: " + date.strftime("%d/%m/%Y"))
    outfile.write("{0:>34}".format(time.strftime("%H:%M %p") +"\n"))
    outfile.write("RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION" + "\n")
    outfile.write("WARD                PARTY      #VOTES    %VOTES" + "\n")
    outfile.write('--------------------------------------------------' + "\n")
    outfile.write("PUNGGOL EAST SMC")
    outfile.write("    PAP        " + str(papcount) + "    " + "{0:>4.2f}".format(pappercentage) + "\n")
    outfile.write("                    RP         " + "{0:>5s}".format(str(rpcount)) + "    " + "{0:>4.2f}".format(rppercentage) + "\n")
    outfile.write("                    SDA        " + "{0:>5s}".format(str(sdacount)) + "    " + "{0:>4.2f}".format(sdapercentage) + "\n")
    outfile.write("                    WP         " + "{0:>5s}".format(str(wpcount)) + "    " + "{0:>4.2f}".format(wppercentage) + "\n")

    outfile.write('--------------------------------------------------' + "\n")
    outfile.write('WINNER: ' + winner + "\n")
    outfile.write('TOTAL VOTES: ' + str(total) + "\n")
    outfile.write('#SPOILTVOTES: ' + str(spoiltvotes) + "\n")
    outfile.write('%SPOILTVOTES: ' + "{0:.2f}".format(spoiltpercentage) + "\n")

  
    outfile.close()


    

except IOError:
    print("Cannot write to RESULTS.TXT")
