The program RedditScrape.py should be run in the following format:

python RedditScrape.py RedditLink outputFileName

This program will only accept input in this format. Any other format will result in the program reiterating the correct format.
As stated in the project description, the reddit link should be to a post in a subreddit.

-------------------------------------------------------------------------------------------------------------------------------------

The program ExtractComments.py should be run in the following format:

python ExtractComments.py inputFileName

This program will only accept input in this format. Any other format will result in the program reiterating the correct format.
It will output the comments of the inputted file to a file named "comments.txt", which is included in the GitHub Repository. If not found, the program will create a new "comments.txt".

-------------------------------------------------------------------------------------------------------------------------------------

For Project 3, the File structure is under CS325_p3.


-------------------------------------------------------------------------------------------------------------------------------------

For Project 4, run the program by first running the following command from within the CS325_p3 folder:

python run.py RedditLink outputFileName

Once done, run the API call program with the following command:

python APIrun.py

API sentiments will be found in the folder Data->Sentiments->sentiments.txt

In order for this program to work, you will need access to a BardAPI key.
To access the API key, go to a bard chat and hit f12 or right click and select inspect. From there, copy and paste the value for F12 > Applications > Cookies > bard > __Secure-1PSID into the line os.environ['_BARD_API_KEY']="xxxxxx" in replace of xxxxxx. If this key does not work, logout of bard, log in again, and then repaste the value.
If you encounter the error "Response status code is not 200. Response Status is 429", that means that you have used up your alloted API calls. To fix this, simply wait around 30 minutes, and functionality will return.

-------------------------------------------------------------------------------------------------------------------------------------

Note: for the best results make sure to clear out all .txt files from the Raw, Processed, and Sentiments folders in Data before running the program.

For project 5, the program run.py should be run in the following format:

python run.py urlFileName.txt

where urlFileName.txt is the file containing the list of reddit post urls. The program will output each url into a unique raw output file titled raw_i.txt, where i is the order of the url from the file. It will then be processed into a file titled [posttitle]_comments.txt, where [posttitle] is the title of the reddit post using underscores to replace spacing.

Once done, run the API call program with the following command:

python APIrun.py

To see instructions on how to get API key, see instruction for Project4.

It should be noted that since this program uses a large amount of API calls on a free api key, running into the error "Response status code is not 200. Response Status is 429" can be quite common. To assure that this does not happen, please make sure that you get refresh your cookies (process listed in Project4 Instructions) before running this program. Furthermore, if using a free api key, the response:

"Excluded response with 'Response Error' from being written."

can sometimes be an occuring issue, and might be outputted to the command line. Whenever this response happens, the program will try to retrieve a sentiment from this comment a few more times. Usually, it will fix itself rather quickly.

-------------------------------------------------------------------------------------------------------------------------------------

Note: for the best results make sure to clear out all files from the Plots folder in Data and only have the files you want turned into a plot in the Sentiments folder in Data.

For project 6, the program GraphRun.py should be run in the following format:

python GraphRun.py

This assumes that run.py and APIrun.py have already been run correctly. After this program has run, the graphs will appear in the Data/Plots folder as separate .PNG files
