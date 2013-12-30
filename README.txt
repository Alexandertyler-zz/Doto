Creator - 
	Alex Tyler

Purpose - 
	The purpose of this project is to analyze DoTA 2 replays and present
	statistics and information on the matches in a clear and informational
	format.

How to Use - 
	Right now, the program begins in a runtime loop that parses commands
	I have designated. The majority of the analysis is done through a class
	called Replay that handles initialization, local variables, and the
	majority of functions that will do data analysis.
	
	In order to make testing easy, I have been using a simple function
	called test() that does a series of calls to Replay(). This is set up to 
	only be run once per program. 

	Other commands include q to quit, h for help, and some others that
	should be ignored for now.

Things to Work On - 
    Fix and finish statistical analysis of certain data.
    Learn and fix heatmaps and other plotting ethods.
    Implement command line variables to allow for script calling.
    Develop an interactive web interface.
    Optimize for single walkthrough based on called commands {
        Essentially, set te program up to do 3 main loops, pregame,
        game, postgame. Then have it run any number of commands for 
        analysis during the one loop. Ie. if key, then function()}


