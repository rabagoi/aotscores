'''
This Python script writes an HTML file to display
the scores for Astronomy on Tap. The number of
questions per round can be adjusted.

During the event, each team gets its own array in the
scores variable. Once the scores are filled in, the
script fills in the appropriate HTML table, which can
be displayed with a web browser.
'''

'''
---------------------------------------------------------------------
TO DO:
| | Allow the number of entries in the team arrays to be any size, while
adjusting the number of rounds, i.e. separate the round and team counters
| | Use a file input instead of opening the code?
---------------------------------------------------------------------
'''

N = 2                       # Number of questions in a round
roundlength = 2*(N+1)       # Length of a round, including labels
indent = ' '*2              # Size of the indent
finale = True               # If True, the Final Scores row will be colored.

# Team names and scores. Fill in with teams and scores from each event.
# <sub>, <sup>, &Greek;
scores= [
        ["Spacegoats",
            30, 50, 50, 0, 0, 0],

        ["Captain's Log is Orbiting Uranus",
            10, 40, 50, 0, 0, 0],

        ["Black Hole - A Movie Date Night",
            20, 30, 50, 0, 0, 0],

        ["Sun Dogs",
            40, 40, 40, 0, 0, 0],

        ["Comet me, bro",
            40, 40, 50, 0, 0, 0],

        ["Plutocracy",
            10, 50, 40, 0, 0, 0],

        ["Shooting Stars",
            10, 20, 50, 0, 0, 0],

        ["Gibbeous Liberty or Gibbeous Death!",
            30, 40, 50, 0, 0, 0],
        
        ["Carry a Towel",
            30, 50, 50, 0, 0, 0],

        ["The Black Hole of Knowledge",
            30, 50, 50, 0, 0, 0],

        ["Higgs Bosom (.Y.)",
            40, 40, 40, 0, 0, 0],

        ["Boobquest",
            30, 20, 50, 0, 0, 0],

        ["Cassini deserved better",
            10, 0, 50, 0, 0, 0],

        ]


# Add the HTML header.
def Header():
    data.write("<!DOCTYPE html>\n")
    data.write("<html>\n")
    data.write("<head>\n")
    data.write(indent+"<meta charset=\"utf-8\" />\n")
    data.write(indent+"<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
    data.write(indent+"<title>Astronomy on Tap Scoreboard</title>\n")
    data.write(indent+"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n")
    data.write(indent+"<link rel=\"stylesheet\" type=\"text/css\" media=\"screen\" href=\"main.css\" />\n")
    data.write(indent+"<script src=\"main.js\"></script>\n")
    data.write("</head>\n")


# Write the scores for individual rounds
def WriteScores(scores):
    for i in range(len(scores[0])+3):

        # Strings for the opening tags, table row, and closing tags.
        ot = 2*indent+"<tr>\n"
        row = 3*indent
        ct = '\n'+2*indent+"</tr>\n"

        # Cell opening and closing tags
        cell_ot = "<td>" if i!=0 else "<th>"
        cell_ct = "</td>" if i!=0 else "</th>"

        # Variable to set the question number, set to i%(1+N_questions).
        # Change this if the number of questions per round is different.
        qnum = i-i//(N+1)
        qlabel = "Round"+(' '+str(qnum) if i!=0 else '')

        # Add special labels for the halftime and final questions.
        if i == roundlength/2:
            qlabel = "Halftime"
            ot = ot.replace("<tr>", "<tr class=\"bigquestion\">")
        elif i == roundlength:
            qlabel = "Final"
            ot = ot.replace("<tr>", "<tr class=\"bigquestion\">")
        elif i == roundlength+1:
            qlabel = "Halftime Totals"
            ot = ot.replace("<tr>", "<tr class=\"summary\">")
            ot = 2*indent+"<tr><td><br></td></tr>\n" + ot
        elif i == roundlength+2:
            qlabel = "Pre-Final Scores"
            ot = ot.replace("tr", "tr class=\"summary\"")
        elif i == roundlength+3:
            qlabel = "Final Scores"
            ot = ot.replace("tr", "tr class=\"final summary\"")

        # Add question number
        ot += 3*indent+cell_ot+qlabel+cell_ct+"\n"
        
        # Write the scores for each round.
        for j in range(len(scores)):
            # Halftime Scores
            if i == roundlength+1:
                row += cell_ot+str(sum(scores[j][1:N+2]))+cell_ct
            # Prefinal Scores
            elif i == roundlength+2:
                row += cell_ot+str(sum(scores[j][1:-1]))+cell_ct
            # Final Scores
            elif i == roundlength+3:
                fscore = sum(scores[j][1:])
                # Color the final scores for the finale.
                if (finale):
                    cell_ot = Podium(scores, fscore)
                row += cell_ot+str(fscore)+cell_ct
            # Scores for round i
            else:
                row += cell_ot+str(scores[j][i])+cell_ct

        data.write(ot+row+ct)

# Write only the summary scores, Round 1 total, Round 2 total, etc.
# Might not need this?
def RoundScores(scores):
    # Calculate total scores for each round.
    totals = [
    ["Teams"]+[scores[i][0] for i in range(len(scores))],
    ["Round 1"]+[sum(scores[i][1:N+1]) for i in range(len(scores))],
    ["Halftime"]+[sum(scores[i][1:N+2]) for i in range(len(scores))],
    ["Round 2"]+[sum(scores[i][N+2:-1]) for i in range(len(scores))],
    ["Pre-Final"]+[sum(scores[i][1:-1]) for i in range(len(scores))],
    ["Final"]+[sum(scores[i][1:]) for i in range(len(scores))],
    ]

    # Write total scores
    for i in range(len(totals)):
        print(totals[i])

        # Strings for the opening tags, table row, and closing tags.
        ot = 2*indent+"<tr>\n"
        row = 3*indent
        ct = '\n'+2*indent+"</tr>\n"

        # Cell opening and closing tags
        cell_ot = "<td>" if i!=0 else "<th>"
        cell_ct = "</td>" if i!=0 else "</th>"

        # Write each row of the cell.
        for j in range(len(totals[0])):
            row += cell_ot+str(totals[i][j])+cell_ct

        # Write data to file
        data.write(ot+row+ct)


# Colors the final scores for 1st, 2nd, and 3rd place.
def Podium(scores, x):
    finals = [sum(scores[k][1:]) for k in range(len(scores))]
    finals.sort()   # Sort scores. Easy way out for now.

    # Change color for 1st, 2nd, 3rd, and other.
    if (x == finals[-1]):
        return "<td style=\"color:gold\">"
    elif (x == finals[-2]):
        return "<td style=\"color:silver\">"
    elif (x == finals[-3]):
        return "<td style=\"color:chocolate\">"
    else:
        return "<td style=\"color:#fff8e7\">"


#------------------------------------------------------------------------
# Write the HTML script.
with open("index.html", 'w') as data:
    Header()

    #Set background and text colors, font
    data.write("<body>\n")
    # data.write(indent+"<img src=\"AoTLogo.png\">\n")
    data.write(indent+"<h1 style=\"font-size:60px; text-align:center\">Astronomy on Tap Scoreboard</h1>\n")
    data.write(indent+"<hr>\n")
    data.write(indent+"<table>\n")

    #Fill in the data cells of the table
    WriteScores(scores)

    data.write(indent+"</table>\n")
    data.write("</body>\n")
    data.write("</html>")