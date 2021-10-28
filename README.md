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

Once the server has been started, you can open the web url `<ip address>:<port>/HelloWorld.html` to connect to a default demo page using your browser of choice. If you provide a non-existent html file instead of `HelloWorld.html`, it will instead return a plaintext 404 error page.

## CLI Client

Alternatively you can open another seperate terminal and run `python client.py <ip address> <port> <html file>`, which will respond with the header and html file contents being printed to the terminal.
