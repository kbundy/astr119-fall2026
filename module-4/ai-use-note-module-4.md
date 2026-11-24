# AI-use note (about 150 words, submitted with every homework from HW2 on)

Copy this into a text file named `ai-use-note.md` in the module folder, fill it in, and upload it with your code and your exported transcript.

**Assignment:**
    HW4: can you spare a square?

**Prediction, written before I asked for anything** (the page tells you what to predict):
    The figure must contain 5 rings of varying sizes drawn on top of each other, with the center of the smallest ring shaded. The area of each ring should be identical.

**What I asked the agent for** (one line per request):
    I asked it to create the chart specified in my spec.md file.

**What I changed by hand:**
    The functions product_remaining and product_visible

**One "why" I asked, and the answer in my own words:**
    I asked why the agent added line 72, "fracs = np.linspace(0, 1, n + 1)"
    The agent responded by stating that this line is what decides where the lines of the circles go on the chart. For the required 5 rings, I need 6 circles (hence the n+1 term).

**What the agent got wrong, and how I found out** (if nothing, say what check you ran that would have caught it):
    The agent got nothing wrong. I verified that the final ring had the thinnest radius. I also verified that my calculated value of x(2/5) = 2.049 matched the radius of the boundry between rings 2 and 3.
    
**What I still do not understand:**
    Nothing