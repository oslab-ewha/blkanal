class AccScore:
    def __init__(self):
        self.counts = [ 0, 0 ]
        self.n_hits = [ 0, 0 ]
        self.n_seqs = [ 0, 0 ]
        self.n_rnds = [ 0, 0 ]
        self.__merge_weights = [ 1, 1 ]

    def addScore(self, score):
        for i in range(2):
            self.__addScore(score, i)

    def __addScore(self, score, i):
        self.counts[i] += score.counts[i]
        self.n_hits[i] += score.n_hits[i]
        self.n_seqs[i] += score.n_seqs[i]
        self.n_rnds[i] += score.n_rnds[i]

    def mergeScore(self, score):
        for i in range(2):
            self.__mergeScore(score, i)
        
    def __mergeScore(self, score, i):
        if self.counts[i] == 0:
            if score.counts[i] == 0:
                return
            self.n_hits[i] = score.n_hits[i]
            self.n_seqs[i] = score.n_seqs[i]
            self.n_rnds[i] = score.n_rnds[i]
            self.counts[i] = score.counts[i]

        if score.counts[i] == 0:
            self.__merge_weights[i] *= 2
            return
        self.n_hits[i] += (self.__merge_weights[i] * score.n_hits[i])
        self.n_seqs[i] += (self.__merge_weights[i] * score.n_seqs[i])
        self.n_rnds[i] += (self.__merge_weights[i] * score.n_rnds[i])
        self.counts[i] += (self.__merge_weights[i] * score.counts[i])
        self.__merge_weights[i] = 1

    def getScoreVec(self):
        return self.__getScoreVec(0) + self.__getScoreVec(1)

    def __getScoreVec(self, i):
        if self.counts[i] == 0:
            return [ 0, 0, 1]
        return [ self.n_hits[i] / self.counts[i], self.n_seqs[i] / self.counts[i], self.n_rnds[i] / self.counts[i] ]

    def __str__(self):
        return "Read:" + self.__get_str(0) + ", Write:" + self.__get_str(1)

    def __get_str(self, i):
        return "hit:{}, seq:{}, rnd:{}".format(self.n_hits[i], self.n_seqs[i], self.n_rnds[i])
