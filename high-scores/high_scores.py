class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def highest(self):
        return max(self.scores)

    def top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        if self.latest() == self.highest():
            return "Your latest score was {}. That's your personal best!".format(self.latest())
        else:
            return "Your latest score was {}. That's {} short of your personal best!".format(self.latest(), self.highest() - self.latest())
