# AoTScores
Scoreboard for Astronomy on Tap Las Vegas.

## Basic Usage

This is a Github Pages website that displays the scoreboard for Astronomy on Tap Las Vegas.  The scoreboard uses two files, `scores.txt` and `AoT_ScoreKeeping.py`, to update the site as the event progresses.

`scores.txt`

This file contains a list of the team names (separated by '*****'), and six numerical score values separated by spaces (R1,R2,HT,R3,R4,Final).  A default version of the file, `scores_default.txt`, is also available for clearing the board.

`AoT_ScoreKeeping.py`

This is a Python script that parses `scores.txt` and creates the HTML page for the scoreboard.  The teams are sorted in order of decreasing score and the top 3 scores are highlighted with special formatting.

To update the scoreboard:

- Update `scores.txt` with the new scores
- Run `AoT_ScoreKeeping.py`
- Commit and push the updated files to the live page.
