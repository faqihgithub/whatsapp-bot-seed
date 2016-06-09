from utils.media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random


class SuperViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            ("^/help", self.help),
            ("^/about", self.about),
            ("^/roll", self.roll),
            ("/(?P<evenOrOdd>even|odd)$", self.even_or_odd),
            ("/(?P<s0rp0rs>stone|paper|scissor)$", self.sps),
        ]

    def about(self, message=None, match=None, to=None):
        self.url_print_sender.send_by_url(message.getFrom(), "https://github.com/joaoricardo000/whatsapp-bot-seed", ABOUT_TEXT)

    def roll(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("[%d]" % random.randint(1, 6), to=message.getFrom())

    def even_or_odd(self, message=None, match=None, to=None):
        is_odd = len(match.group("evenOrOdd")) % 2
        num = random.randint(1, 10)
        if (is_odd and num % 2) or (not is_odd and not num % 2):
            return TextMessageProtocolEntity("[%d]\nYou win." % num, to=message.getFrom())
        else:
            return TextMessageProtocolEntity("[%d]\nYou lose!" % num, to=message.getFrom())
    
    def sps(self, message=None, match=None, to=None): 
	list= ['stone','paper','scissor'] #Created a list for random.
	txt = random.choice(list)
	is_choice = match.group("s0rp0rs")
	if (list.index(txt) + 1 == list.index(is_choice)) or (list.index(txt) -2 == list.index(is_choice)) : # Index of your choice is more than auto generated choice, hence You win. Exception: Stone-Scissor case.
		return TextMessageProtocolEntity("Bot: %s\nYou: %s\nYou won!." % (txt, is_choice), to=message.getFrom())
	elif (list.index(txt) == list.index(is_choice) + 1) or (list.index(txt) == list.index(is_choice) - 2): # Index of your choice is less than auto generated choice, hence You lose. Exception: Stone-Scissor case.
		return TextMessageProtocolEntity("BOT: %s\nYou: %s\nYou lost ." % (txt, is_choice), to=message.getFrom())
	else:
		return TextMessageProtocolEntity("BOT: %s\nYou: %s\nIt's a tie." % (txt, is_choice), to=message.getFrom())


HELP_TEXT = """ [HELP]
- Commands
/help - Show this message.
/about - About
/search - I'm lucky!
/image - I'm lucky with image!
/tts - Text to speech.
/even or /odd - Amazing game.
/ping - Pong.
/echo - Echo.
/roll - Roll a dice.
/stone or /paper or /scissor - Play Stone Paper Scissor
Automatic: 
    - Url (http://...) print screen.
    - Image (jpeg, gif, png) download.
    - Videos (mp4, webm) downloads.
    - Youtube videos.
"""

ABOUT_TEXT = """ [Whatsapp Bot Seed]
A small open source python framework to create a whatsapp bot, with regex-callback message routing.
https://github.com/joaoricardo000/whatsapp-bot-seed
"""
