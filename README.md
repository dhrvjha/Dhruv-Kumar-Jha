"# Tech-Adrista-Hackathon" 
<32>--<I Voted!>

Project Overview
What problem did the team try to solve?
Security Of Online Voting Platform.

What is the proposed solution?
Two step verification

Solution Description

We will send one time link on the registered college E-mail id. Link will have time boundation .i.e it can be accessed in a given time frame.
When the link open it demands for the acmera access. Cmera will capture the photo of voter for the authenticity.
If there is any discrepancy his/her vote will be declined by the admin. We have ensured the voter's anonymity to the admin.

Architecture Diagram

<Collect candidate details and Voters email> --> <Mail all voters with unique URLS to direct to voting page> --> 
<Once directed voters agree to vote redirect them to next page> --> <Take pictures using webcam> -->
<POST request all collected data back to server> --> <if photo do not match ID discard the vote> -->
<Publish the result once the voting time is over>

Technical Description
 
 Language/Package/Module used:
 Python 3.8.1
 pip 20.2.4
 virtualenv 20.2.1
 asgiref==3.3.1
 Django==3.1.3
 django-crispy-forms==1.10.0
 gunicorn==20.0.4
 pytz==2020.4
 sqlparse==0.4.1

  Setup instructions:
  Download python 3.8.1 for your OS : https://www.python.org/downloads/
    pip will also download as a package but if not then,
  download pip from https://pip.pypa.io/en/stable/reference/pip_download/
  Add python .bin folder to the path in environment variable
  run following commands
   pip install virtualenv
   virtualenv venv
   cd venv/Scripts
   activate
   cd ../..
   git clone https://github.com/rapjack/Dhruv-Kumar-Jha
   pip install requirements.txt
   
  These installations will be sufficient to run the program.
  
 To RUN the program:
   open terminal from project root directory
   run 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
   now visit 
   http://127.0.0.1:8000/
   to organise vote visit http://127.0.0.1:8000/conduct/
   voting link will be sent to email provided.

Screenshots:
![Mail from mail-service](/I_Voted/screenshots/mail.jpg?raw=true "Mail from mail-service")
![Conduct](/I_Voted/screenshots/conduct.jpg?raw=true "Conduct")

Team Members

  |Dhruv Kumar Jha    | dhruv_201800528@smit.smu.edu.in | django, url-service, database|
  |Ayush              | ayush_201800221@smit.smu.edu.in | mail-service, UI(html,css)   |


References

wwww.freecodecamp.org
www.geeksforgeeks.org
https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
https://developer.mozilla.org/
https://stackoverflow.com/
https://docs.python.org/
https://docs.djangoproject.com/
