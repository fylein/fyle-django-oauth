# fyle-django-oauth
Fyle Django project with OAuth

fyle-Django-oauth is an OAuth2 template to show how to implement OAuth2 in your Django application to access fyle APIs .

## FyleSDK :
FyleSDK is a Python SDK for accessing Fyle APIs.
Read more about FyleSDK from [this](https://www.fylehq.com/help/en/articles/3045584-python-sdk-for-fyle-apis ) .

## Dependencies
You can install all the dependencies using :
```
$pip install -r requirements.txt

```
## Run fyle-django-oauth Application

1. Install all the dependencies if you haven't done yet.
2. Set Environment variables for  CLIENT_ID,CLIENT_SECRET,BASE_URL using :
```
export CLIENT_ID='<Your Client id>'
export CLIENT_SECRET='<Your Client Secret>'
export BASE_URL='<Your BASE URL>'
export SECRET_KEY='<Your Secret key for Django app>'

```
3. Here redirect_uri is http://localhost:8000/profile .You can change it if you want.
4. Run the application using :
```
python manage.py runserver

```
5. Visit http://localhost:8000/  to login .