class AccScore:
    def __init__(self):
        self.count = 0
        self.n_hits = 0
        self.n_seqs = 0
        self.n_rnds = 0

    def addScore(self, score):
        self.count += score.count
        self.n_hits += score.n_hits
        self.n_seqs += score.n_seqs
        self.n_rnds += score.n_rnds

    def getScoreVec(self):
        return [ self.n_hits / self.count, self.n_seqs / self.count, self.n_rnds / self.count ]

    def __str__(self):
        return "hit:{}, seq:{}, rnd:{}".format(self.n_hits, self.n_seqs, self.n_rnds)
