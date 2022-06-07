# flask-chatterbot

#### A web implementation of [ChatterBot](https://github.com/gunthercox/ChatterBot) using Flask.

## Local Setup:
 1. Ensure that Python, Flask, SQLAlchemy, and ChatterBot are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *app.py* with `python app.py`.
 3. The demo will be live at [http://localhost:5000/](http://localhost:5000/)

### Note for Python 3.10 Users, you might see the following errors while setup:
 1. [AttributeError: module 'time' has no attribute 'clock'](https://stackoverflow.com/questions/58569361/attributeerror-module-time-has-no-attribute-clock-in-python-3-8)
 2. [attributeerror module 'collections' has no attribute 'hashable'](https://docs.python.org/3/whatsnew/3.10.html#removed). Quick fix is to import Hashable from typing for Python\lib\site-packages\yaml\constructor.py and modifying the collections.hashable to just Hashable, this is not advisable if you don't know the side effects.

## How do I deploy this to a web server?
If you do not have a dedicated server, I highly recommend using [PythonAnywhere](https://www.pythonanywhere.com/), [AWS](https://aws.amazon.com/getting-started/projects/deploy-python-application/) or [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) to host your application.

### Deploying on Heroku
If you are deploying on Heroku, you will have to change the database adapter from `chatterbot.storage.SQLStorageAdapter` to `chatterbot.storage.MongoDatabaseAdapter` since SQLite3 isn't supported. To do this simply change the following line:

`english_bot = ChatBot("English Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")`

... to use the MongoDB adapter:

```
english_bot = ChatBot("English Bot", 
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = mongodb_name,
                     database_uri = mongodb_uri)
```
... where `mongodb_name` is the name of the database you wish to connect to and `mongodb_uri` is the URI of a remote instance of MongoDB.

## License
This source is free to use, but ChatterBot does have a license which still applies and can be found on the [LICENSE](https://github.com/gunthercox/ChatterBot/blob/master/LICENSE) page.
