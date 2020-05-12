# Python_Webinar_10May
This is a basic introduction to flask framework along with a basic API implementation done during the python webinar session on 10 May 2020.


Steps to run this application:

1. Have Python installed on your system and ensure its path is set in the environment variables
2. Open command prompt and clone this Repository
3. run pip install -r requirements.txt
4. python wsgi.py (run in the command propmt)
5. Open http://127.0.0.1:5000 in your browser

Steps for Deployment on heroku:

1. Create a heroku account
2. Download and install heroku cli & git (Ensure that the path is set in environment variables)
3. Restart your cmd and goto to your project directory
Run Below commands only if you make any changes
4. git add -A
5. git commit -m "Your Commit message"
6. heroku login
7. heroku create "sitename" (Instead of "sitename" mentione the name of what you want the website to be named as)
    Ex: heroku create flasksimple
8. heroku git:remote -a "sitename"
    Ex: heroku git:remote -a flasksimple
9. git push heroku master
10. On success you can open the web application using www.sitename.herokuapp.com in your browser.
