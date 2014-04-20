import re
import random

from hamper.interfaces import ChatPlugin


class NumberWang(ChatPlugin):
    name = 'numberwang'

    def setup(self, *args, **kwargs):
        super(NumberWang, self).setup(*args, **kwargs)
        self.numberwang = []
        self.more_numberwangs()

    def more_numberwangs(self, goal=0.9):
        again = random.random()

        while again < goal:
            another = round(abs(random.gauss(0, 100)))
            self.numberwang.append(another)
            print 'New numberwang is %d' % another
            again = random.random()
            goal **= 2

    def message(self, bot, comm):
        numbers = [int(d) for d in re.findall(r'\d+', comm['message'])]

        for d in numbers:
            if d in self.numberwang:
                bot.reply(comm, self.success(d))
                self.numberwang = []
                self.more_numberwangs()
                break

        self.more_numberwangs(0.9 if numbers else 0.1)

    def success(self, num):
        return random.choice(
            ["That's numberwang!"] * 5 +
            ["THAT'S NUMBERWANG!"] * 3 +
            ["That's wanganum!"] * 3 +
            ["Did someone say %d? That's numberwang!" % num] * 2 +
            ["That's numberwank!"] +
            ["Love those decimals. Numberwang!"]
        )


numberwang = NumberWang()
