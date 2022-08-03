<h1>How run ?</h1>
<h2>Download project</h2>
<code>git clone https://github.com/parhamkmp1386/django-blog</code>
<h2>Run project</h2>
<code>mkdir django-blog</code>
<code>sudo mv env django-blog</code>
<code>sudo mv project django-blog</code>
<br>
<code>source env/bin/activate</code>
<br>
<code>cd project</code>
<br>
<code>pip3 install -r requirements.txt</code>
<br>
<h5><b>(django must installed)</b></h5>
<h5>install django: </h5> <code>pip3 install django</code>
<h2>Runserver and save data to database</h2>
<h5>Save data to database:</h5>
<code>python3.9 manage.py migrate</code>
<h5>Runserver (Default port: 8000):</h5>
<code>python3.9 manage.py runserver</code>
<p>if you want run on other port:</p>
<code>python3.9 manage.py runserver [your post exam: 5000]</code>
