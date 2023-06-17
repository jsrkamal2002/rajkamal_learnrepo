# Assignment 3

To Create a Flask api that serve two endpoints

## Question

```bash
Deploy the previous two assignments on a flask api and we should be able to run this by calling.
/api/printHello
/api/modifyRecepie
```

## How i'm implemented it

- Created a virtual environment

```bash
python -m venv <folder_name>
```

- Installed flask

```bash
pip install flask
```

- Created a flask_app.py file
- Created second_assignment.py file to do the second assignment functions
- Imported the second_assignment.py file to flask_app.py
- Created two routes in flask_app.py file

# Demo

## Check it out

- [Print "Hello World!!"](https://flask.jsrkamal.in/api/printHello)
- [Original Recipe](https://flask.jsrkamal.in/api/originalRecepie)
- [Modify Recipe](https://flask.jsrkamal.in/api/modifiedRecepie)

## How i deployed it

- I have a domain name [jsrkamal.in](https://jsrkamal.in)
- I have a personal home lab server
- I created a subdomain [flask.jsrkamal.in](https://flask.jsrkamal.in) and pointed it to my home lab server
- I have a HTTPD reverse proxy server running on my home lab server
- I have created a docker container of the assignment 3
- I have a docker container running on my home lab server
