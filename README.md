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

python run.py RedditLink outputFileName.txt

Once done, run the API call program with the following command:

python APIrun.py

API sentiments will be found in the folder Data->Sentiments->sentiments.txt

In order for this program to work, you will need access to a BardAPI key.
To access the API key, go to a bard chat and hit f12 or right click and select inspect. From there, copy and paste the value for F12 > Applications > Cookies > bard > __Secure-1PSID into the line os.environ['_BARD_API_KEY']="xxxxxx" in replace of xxxxxx. If this key does not work, logout of bard, log in again, and then repaste the value.
If you encounter the error "Response status code is not 200. Response Status is 429", that means that you have used up your alloted API calls. To fix this, simply wait around 30 minutes, and functionality will return.