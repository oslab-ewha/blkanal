class AccScore:
    def __init__(self):
        self.count = 0
        self.n_hits = 0
        self.n_seqs = 0
        self.n_rnds = 0
        self.__merge_weight = 1

    def addScore(self, score):
        self.count += score.count
        self.n_hits += score.n_hits
        self.n_seqs += score.n_seqs
        self.n_rnds += score.n_rnds

    def normalize(self):
        if self.count == 0:
            return
        self.n_hits /= self.count
        self.n_seqs /= self.count
        self.n_rnds /= self.count
        self.count = 1

    def mergeScore(self, score):
        if self.count == 0:
            if score.count == 0:
                return
            self.n_hits = score.n_hits
            self.n_seqs = score.n_seqs
            self.n_rnds = score.n_rnds
            self.count = score.count
            return
        if score.count == 0:
            self.__merge_weight *= 2
            return
        self.n_hits += (self.__merge_weight * score.n_hits)
        self.n_seqs += (self.__merge_weight * score.n_seqs)
        self.n_rnds += (self.__merge_weight * score.n_rnds)
        self.count += (self.__merge_weight * score.count)
        self.__merge_weight = 1

    def getScoreVec(self):
        return [ self.n_hits / self.count, self.n_seqs / self.count, self.n_rnds / self.count ]

    def __str__(self):
        return "hit:{}, seq:{}, rnd:{}".format(self.n_hits, self.n_seqs, self.n_rnds)
