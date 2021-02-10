# telegram-bot

This is a bot for the messaging app Telegram. I don't have a server active to run this bot, so if you would like to test it, see [Setup](https://github.com/RD1K/python-telegram-bot#Setup).


## Example
[Click to see a screen recording of the bot in action.](https://i.imgur.com/8M6p0q6.mp4)

## Usage
It is able to do a few different things, as stated in the help message:

```I create memes based on templates and text provided to me by you. These are the available templates right now:
 - Dominoes, accepts 2 arguments (/domino)
Also, the /rate command allows you to rate something out of 100% and accepts 2 arguments (person, topic).
The /chance command allows you to rate the chance of an event, with 1 argument, being the event.
The /say command echoes what the user says.
```

I will go more in depth about each of these commands here.

The /domino command can be used with this syntax: `/hs 1,2`

The /rate command can be used with this syntax: `/rate John,happy` to output, for example, `John is 78 percent happy.`

The /chance command can be used with this syntax: `/chance tomorrow is a snow day` to output, for example, `There is a 37 percent chance that tomorrow is a snow day.`

The /say command has no particular syntax. For example, if you send `/say Hi!` the bot will reply `Hi!`

The bot is somewhat aggressive, so make sure to put the appropriate number of arguments.

## Setup
To run this bot, the `python-telegram-bot` and `Pillow` libraries have to be installed. You can install them via PIP.

After that, you need to generate a token for the bot. Install Telegram on your phone if you don't already have it, and then direct message @BotFather `\newbot`. Follow the prompts. Then, copy and paste the token into the `TOKEN` variable in main.py, in quotes. In the same file, add the directory to your home folder (or wherever you `git clone` this repository to), in quotes. Don't include a slash at the end. Do this in pythonimaging.py as well. Then, run main.py, and now you can message the bot to try it out.

If you would like to add additional meme templates to the bot, download the image to a directory of your choice and add it to the bottom of the pythonimaging.py file in the syntax `[variable name of your choice] = Template("/directory/to/the/image",[(x1,y1),(x2,y2)])`, replacing x1 and y1 with the coordinates on the image of where you want the first piece of text to go, and x2 and y2 for the second piece of text. You don't need to have 2 coordinate pairs though, and you can have more if you want to. If you want to find these coordinates easily, you can download software such as GIMP, load the image into it, and hover over the desired place to see its coordinates. 

Then, go to main.py. Near line 29, add this code:

```
elif template == 2:
    pythonimaging.[variable name you chose].make_meme(userInput)
```

If you did this before, add the next whole number instead of 2. Then, go to line 40 and add the command to the help message if you want to. This doesn't really change anything aside from the help message, so it isn't necessary. 

Then, below the `domino` function around line 43, add an identical function but replace domino with the name you want for your template. Also, replace 1 with the number you put in the `elif` statement before.

Then, go just above the last line of code, and add an identical line of code to one of the handlers, replacing the first argument with the command you want to be used (in quotes), and replacing the second argument with the function name.

Now, if you send the bot the command you chose, preceded by "/" and followed by the appropriate number of arguments separated by a comma, it will use your template.
