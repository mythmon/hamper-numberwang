import re
import random

from hamper.interfaces import ChatPlugin


class NumberWang(ChatPlugin):
    name = 'numberwang'

    def setup(self, *args, **kwargs):
        super(NumberWang, self).setup(*args, **kwargs)
        self.next_numberwang()

    def next_numberwang(self):
        self.numberwang = round(abs(random.gauss(0, 500)))
        print 'New numberwang is %d' % self.numberwang

    def message(self, bot, comm):
        numbers = re.findall(r'\d+', comm['message'])
        if any(int(d) == self.numberwang for d in numbers):
            bot.reply(comm, "That's numberwang!")
            self.next_numberwang()
        if random.random() > 0.9:
            self.next_numberwang()


numberwang = NumberWang()
