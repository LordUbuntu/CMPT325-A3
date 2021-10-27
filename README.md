# CMPT325-A3

This is an HTTP web server written in Python.

## Description

As an exercise to learn socket programming for a networking course, we were tasked with developing a web server that can handle single HTTP requests at a time. We were then also tasked with writing a web client that could send requests to the web server and display the server response.

## Participants

- Jacobus Burger
- Jun Park
- Jared Klassen

## Usage

To start the server, open a terminal and run `python server.py` in the repository directory.

## Browser Client

Once the server has been started, you can open the web url `127.0.0.1:8182/` on the same device using your browser of choice, which will return a 404 webpage by default (along with any requests for a non-existent html file).

If you include an existing html file with a url like `127.0.0.1:8182/HelloWorld.html` then you should see a proper html page rendered in instead.

## CLI Client

Alternatively you can open another seperate terminal and run `python client.py`, then provide a url like `127.0.0.1:8182/HelloWorld.html` and receive the server response as text in kind!
