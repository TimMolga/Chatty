# Chatty (Work In Progress)
An instant messaging application utilizing Flask and Socket.IO

### Project Requirements:

Display Name: When a user visits your web application for the first time, they should be prompted to type in a display name that will eventually be associated with every message the user sends. If a user closes the page and returns to your app later, the display name should still be remembered.

Channel Creation: Any user should be able to create a new channel, so long as its name doesn’t conflict with the name of an existing channel.

Channel List: Users should be able to see a list of all current channels, and selecting one should allow the user to view the channel. We leave it to you to decide how to display such a list

Messages View: Once a channel is selected, the user should see any messages that have already been sent in that channel, up to a maximum of 100 messages. Your app should only store the 100 most recent messages per channel in server-side memory.

Sending Messages: Once in a channel, users should be able to send text messages to others the channel. When a user sends a message, their display name and the timestamp of the message should be associated with the message. All users in the channel should then see the new message (with display name and timestamp) appear on their channel page. Sending and receiving messages should NOT require reloading the page.

Remembering the Channel: If a user is on a channel page, closes the web browser window, and goes back to your web application, your application should remember what channel the user was on previously and take the user back to that channel.

### TO DO:
##### 1: Implement Handlebars
##### 2: Separate JavaScript
##### 3: Separate Styles
##### 4: Add Documentation

### To Run the App:

You will need a Python virtual environment to be set up (Tutorial here: https://flask.palletsprojects.com/en/1.1.x/installation/#install-virtualenv)

After this has been completed, you will need to install Flask (https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)

Once the environment is setup, you may run the application with ```flask run```.
