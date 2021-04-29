                                            AUTO SEARCH API 
                                           
 Our tool is AutoSearch for errors in the python program.This a simple parser program where main.py files executes the test.py file and shows its errors and automatically opens related stack overflow similar error solution pages in the default browser.
Make sure both test.py and main.py are in the same file location.

If no errors are seen then it prints no errors.    
The exe_rtn method takes the command that has to be executed.  
We have splitted the command for the subprocess method.  
Through the communicate method we fetch the output and error.  
Through the main method the error is extracted.  
The make_rqst method takes the error and makes a request for the Stackexchange API.  
We imported a request module to make the requests.  
To extract the urls we created the fetch_urls method.  
We imported browser module so that links can open in the default browser in the pc.  
Once link get fetched it open automatically open webpages in the browser.  

CONTRIBUTIONS: we both discussed and wrote this code through a google meet.  
