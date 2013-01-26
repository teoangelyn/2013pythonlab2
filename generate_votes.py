# generate_votes.py

import random

try: 
    count = 0

    outfile = open("VOTES.DAT", "w")

    while count <= 31649:
        num = random.randint(0,1000)
        # generate spoilt vote
        if num <= 20:
            if num <= 8:
                # generate spoilt pap vote
                outfile.write("PAP,0\n")
                count = count + 1

            elif 8 < num <= 15: 
                # generate spoilt wp vote
                outfile.write("WP,0\n")
                count = count + 1

            elif 15 < num <= 18:
                # generate spoilt sda vote
                outfile.write("SDA,0\n")
                count = count + 1
            else: # 18 < num <= 20
                # generate spoilt rp vote
                outfile.write("RP, 0\n")
                count = count + 1
                
        # generate valid vote
        else:
            # generate pap vote
            if 20 < num <= 545:
                outfile.write("PAP,1\n")
                count = count + 1
                
            # generate wp vote
            elif 545 < num <= 933:
                outfile.write("WP,1\n")
                count = count + 1
                
            # generate sda vote
            elif 933 < num <= 962:
                outfile.write("SDA,1\n")
                count = count + 1
                
            # generate rp vote
            else: # 962 < num <= 1000
                outfile.write("RP,1\n")
                count = count + 1

    outfile.close()
    
except IOError:
    print("Cannot write to VOTES.DAT")
    
    
