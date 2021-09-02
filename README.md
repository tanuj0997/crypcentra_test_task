# crypcentra application.

## Steps to install and run server

### Create and Activate Virtual Environment
* Run `$ python3 -m venv env` command to create virtual environment
* Run `$ source env/bin/activate` command to activate virtual environment

### Install requirements
* Run `$ pip3 install -r requirements.txt` command to Install project requirement

### Migrate and Run Server
* Run `$ cd crypcentra` command for move into the project directory
* Run `$ python manage.py migrate` command to apply migrations on your local.
* Run `$ python manage.py runserver 8000` command to run project on your local machine

### Run tests.
* Run `$ python manage.py test`

###  Setup celery
* Run `celery -A crypcentra worker -l INFO`

### Create coin by using django admin panel.
* Run ` python manage.py createsuperuser`  create superuser to login admin panel.
* `http://127.0.0.1:8000/admin/`



### Cerate bid  
* Run `api/bid/`
* Params `{
		'user_id':1,
		'number_of_tokens':2
		'bidding_price':2000
		'coin_id':1
    }   `


### Assumption
- If bid tokens is greater than remaining tokens, In that case we are not assigning partial token to bid.
- We are also assuming for each trading, User will add a coin entry from the admin section, we are not going to use the same coin.
- If we want to re-use the same coins then in that case I will take the status field for (Pending, Successful, Failed) bids. So after end time we will set success for assigned bids and rest will go into failed.
  


