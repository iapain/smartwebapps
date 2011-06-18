import operator
import re
import math

POSITIVE = "H" #Happy
NEGATIVE = "S" #Sad
NEUTRAL  = "N" #Neutral


class BayesianClassifier(object):

  POSITIVE = POSITIVE
  NEGATIVE = NEGATIVE
  NEUTRAL  = NEUTRAL

  THRESHHOLD = 0.05
  guesser = None

  def __init__(self):
    self.guesser = Bayes()
    self.guesser.train(POSITIVE, "cool")
    self.guesser.train(POSITIVE, "Woo")
    self.guesser.train(POSITIVE, "quite amazing")
    self.guesser.train(POSITIVE, "thks")
    self.guesser.train(POSITIVE, "looking forward to")
    self.guesser.train(POSITIVE, "damn good")
    self.guesser.train(POSITIVE, "frickin ruled")
    self.guesser.train(POSITIVE, "frickin rules")
    self.guesser.train(POSITIVE, "Way to go")
    self.guesser.train(POSITIVE, "cute")
    self.guesser.train(POSITIVE, "comeback")
    self.guesser.train(POSITIVE, "not suck")
    self.guesser.train(POSITIVE, "prop")
    self.guesser.train(POSITIVE, "kinda impressed")
    self.guesser.train(POSITIVE, "props")
    self.guesser.train(POSITIVE, "come on")
    self.guesser.train(POSITIVE, "congratulation")
    self.guesser.train(POSITIVE, "gtd")
    self.guesser.train(POSITIVE, "proud")
    self.guesser.train(POSITIVE, "thanks")
    self.guesser.train(POSITIVE, "can help")
    self.guesser.train(POSITIVE, "thanks!")
    self.guesser.train(POSITIVE, "pumped")
    self.guesser.train(POSITIVE, "integrate")
    self.guesser.train(POSITIVE, "really like")
    self.guesser.train(POSITIVE, "loves it")
    self.guesser.train(POSITIVE, "yay")
    self.guesser.train(POSITIVE, "amazing")
    self.guesser.train(POSITIVE, "epic flail")
    self.guesser.train(POSITIVE, "flail")
    self.guesser.train(POSITIVE, "good luck")
    self.guesser.train(POSITIVE, "fail")
    self.guesser.train(POSITIVE, "life saver")
    self.guesser.train(POSITIVE, "piece of cake")
    self.guesser.train(POSITIVE, "good thing")
    self.guesser.train(POSITIVE, "hawt")
    self.guesser.train(POSITIVE, "hawtness")
    self.guesser.train(POSITIVE, "highly positive")
    self.guesser.train(POSITIVE, "my hero")
    self.guesser.train(POSITIVE, "yummy")
    self.guesser.train(POSITIVE, "awesome")
    self.guesser.train(POSITIVE, "congrats")
    self.guesser.train(POSITIVE, "would recommend")
    self.guesser.train(POSITIVE, "intellectual vigor")
    self.guesser.train(POSITIVE, "really neat")
    self.guesser.train(POSITIVE, "yay")
    self.guesser.train(POSITIVE, "ftw")
    self.guesser.train(POSITIVE, "I want")
    self.guesser.train(POSITIVE, "best looking")
    self.guesser.train(POSITIVE, "imrpessive")
    self.guesser.train(POSITIVE, "positive")
    self.guesser.train(POSITIVE, "thx")
    self.guesser.train(POSITIVE, "thanks")
    self.guesser.train(POSITIVE, "thank you")
    self.guesser.train(POSITIVE, "endorse")
    self.guesser.train(POSITIVE, "clearly superior")
    self.guesser.train(POSITIVE, "superior")
    self.guesser.train(POSITIVE, "really love")
    self.guesser.train(POSITIVE, "woot")
    self.guesser.train(POSITIVE, "w00t")
    self.guesser.train(POSITIVE, "super")
    self.guesser.train(POSITIVE, "wonderful")
    self.guesser.train(POSITIVE, "leaning towards")
    self.guesser.train(POSITIVE, "rally")
    self.guesser.train(POSITIVE, "incredible")
    self.guesser.train(POSITIVE, "the best")
    self.guesser.train(POSITIVE, "is the best")
    self.guesser.train(POSITIVE, "strong")
    self.guesser.train(POSITIVE, "would love")
    self.guesser.train(POSITIVE, "rally")
    self.guesser.train(POSITIVE, "very quickly")
    self.guesser.train(POSITIVE, "very cool")
    self.guesser.train(POSITIVE, "absolutely love")
    self.guesser.train(POSITIVE, "very exceptional")
    self.guesser.train(POSITIVE, "so proud")
    self.guesser.train(POSITIVE, "funny")
    self.guesser.train(POSITIVE, "recommend")
    self.guesser.train(POSITIVE, "so proud")
    self.guesser.train(POSITIVE, "so great")
    self.guesser.train(POSITIVE, "so cool")
    self.guesser.train(POSITIVE, "cool")
    self.guesser.train(POSITIVE, "wowsers")
    self.guesser.train(POSITIVE, "plus")
    self.guesser.train(POSITIVE, "liked it")
    self.guesser.train(POSITIVE, "make a difference")
    self.guesser.train(POSITIVE, "moves me")
    self.guesser.train(POSITIVE, "inspired")
    self.guesser.train(POSITIVE, "OK")
    self.guesser.train(POSITIVE, "love it")
    self.guesser.train(POSITIVE, "LOL")
    self.guesser.train(POSITIVE, ":)")
    self.guesser.train(POSITIVE, ";)")
    self.guesser.train(POSITIVE, ":-)")
    self.guesser.train(POSITIVE, ";-)")
    self.guesser.train(POSITIVE, ":D")
    self.guesser.train(POSITIVE, ";]")
    self.guesser.train(POSITIVE, ":]")
    self.guesser.train(POSITIVE, ":p")
    self.guesser.train(POSITIVE, ";p")
    self.guesser.train(POSITIVE, "voting for")
    self.guesser.train(POSITIVE, "great")
    self.guesser.train(POSITIVE, "agreeable")
    self.guesser.train(POSITIVE, "amused")
    self.guesser.train(POSITIVE, "brave")
    self.guesser.train(POSITIVE, "calm")
    self.guesser.train(POSITIVE, "charming")
    self.guesser.train(POSITIVE, "cheerful")
    self.guesser.train(POSITIVE, "comfortable")
    self.guesser.train(POSITIVE, "cooperative")
    self.guesser.train(POSITIVE, "courageous")
    self.guesser.train(POSITIVE, "delightful")
    self.guesser.train(POSITIVE, "determined")
    self.guesser.train(POSITIVE, "eager")
    self.guesser.train(POSITIVE, "elated")
    self.guesser.train(POSITIVE, "enchanting")
    self.guesser.train(POSITIVE, "encouraging")
    self.guesser.train(POSITIVE, "energetic")
    self.guesser.train(POSITIVE, "enthusiastic")
    self.guesser.train(POSITIVE, "excited")
    self.guesser.train(POSITIVE, "exuberant")
    self.guesser.train(POSITIVE, "excellent")
    self.guesser.train(POSITIVE, "I like")
    self.guesser.train(POSITIVE, "fine")
    self.guesser.train(POSITIVE, "fair")
    self.guesser.train(POSITIVE, "faithful")
    self.guesser.train(POSITIVE, "fantastic")
    self.guesser.train(POSITIVE, "fine")
    self.guesser.train(POSITIVE, "friendly")
    self.guesser.train(POSITIVE, "fun ")
    self.guesser.train(POSITIVE, "funny")
    self.guesser.train(POSITIVE, "gentle")
    self.guesser.train(POSITIVE, "glorious")
    self.guesser.train(POSITIVE, "good")
    self.guesser.train(POSITIVE, "pretty good")
    self.guesser.train(POSITIVE, "happy")
    self.guesser.train(POSITIVE, "healthy")
    self.guesser.train(POSITIVE, "helpful")
    self.guesser.train(POSITIVE, "high")
    self.guesser.train(POSITIVE, "agile")
    self.guesser.train(POSITIVE, "responsive")
    self.guesser.train(POSITIVE, "hilarious")
    self.guesser.train(POSITIVE, "jolly")
    self.guesser.train(POSITIVE, "joyous")
    self.guesser.train(POSITIVE, "kind")
    self.guesser.train(POSITIVE, "lively")
    self.guesser.train(POSITIVE, "lovely")
    self.guesser.train(POSITIVE, "lucky")
    self.guesser.train(POSITIVE, "nice")
    self.guesser.train(POSITIVE, "nicely")
    self.guesser.train(POSITIVE, "obedient")
    self.guesser.train(POSITIVE, "perfect")
    self.guesser.train(POSITIVE, "pleasant")
    self.guesser.train(POSITIVE, "proud")
    self.guesser.train(POSITIVE, "relieved")
    self.guesser.train(POSITIVE, "silly")
    self.guesser.train(POSITIVE, "smiling")
    self.guesser.train(POSITIVE, "splendid")
    self.guesser.train(POSITIVE, "successful")
    self.guesser.train(POSITIVE, "thankful")
    self.guesser.train(POSITIVE, "thoughtful")
    self.guesser.train(POSITIVE, "victorious")
    self.guesser.train(POSITIVE, "vivacious")
    self.guesser.train(POSITIVE, "witty")
    self.guesser.train(POSITIVE, "wonderful")
    self.guesser.train(POSITIVE, "zealous")
    self.guesser.train(POSITIVE, "zany")
    self.guesser.train(POSITIVE, "rocks")
    self.guesser.train(POSITIVE, "comeback")
    self.guesser.train(POSITIVE, "pleasantly surprised")
    self.guesser.train(POSITIVE, "pleasantly")
    self.guesser.train(POSITIVE, "surprised")
    self.guesser.train(POSITIVE, "love")
    self.guesser.train(POSITIVE, "glad")
    self.guesser.train(POSITIVE, "yum")
    self.guesser.train(POSITIVE, "interesting")



    self.guesser.train(NEGATIVE, "FTL")
    self.guesser.train(NEGATIVE, "irritating")
    self.guesser.train(NEGATIVE, "not that good")
    self.guesser.train(NEGATIVE, "suck")
    self.guesser.train(NEGATIVE, "lying")
    self.guesser.train(NEGATIVE, "duplicity")
    self.guesser.train(NEGATIVE, "angered")
    self.guesser.train(NEGATIVE, "dumbfounding")
    self.guesser.train(NEGATIVE, "dumbifying")
    self.guesser.train(NEGATIVE, "not as good")
    self.guesser.train(NEGATIVE, "not impressed")
    self.guesser.train(NEGATIVE, "stomach it")
    self.guesser.train(NEGATIVE, "pw")
    self.guesser.train(NEGATIVE, "pwns")
    self.guesser.train(NEGATIVE, "pwnd")
    self.guesser.train(NEGATIVE, "pwning")
    self.guesser.train(NEGATIVE, "in a bad way")
    self.guesser.train(NEGATIVE, "horrifying")
    self.guesser.train(NEGATIVE, "wrong")
    self.guesser.train(NEGATIVE, "flailing")
    self.guesser.train(NEGATIVE, "failing")
    self.guesser.train(NEGATIVE, "fallen way behind")
    self.guesser.train(NEGATIVE, "fallen behind")
    self.guesser.train(NEGATIVE, "lose")
    self.guesser.train(NEGATIVE, "fallen")
    self.guesser.train(NEGATIVE, "self-deprecating")
    self.guesser.train(NEGATIVE, "hunker down")
    self.guesser.train(NEGATIVE, "duh")
    self.guesser.train(NEGATIVE, "get killed by")
    self.guesser.train(NEGATIVE, "got killed by")
    self.guesser.train(NEGATIVE, "hated us")
    self.guesser.train(NEGATIVE, "only works in safari")
    self.guesser.train(NEGATIVE, "must have ie")
    self.guesser.train(NEGATIVE, "fuming and frothing")
    self.guesser.train(NEGATIVE, "heavy")
    self.guesser.train(NEGATIVE, "buggy")
    self.guesser.train(NEGATIVE, "unusable")
    self.guesser.train(NEGATIVE, "nothing is")
    self.guesser.train(NEGATIVE, "is great until")
    self.guesser.train(NEGATIVE, "don't support")
    self.guesser.train(NEGATIVE, "despise")
    self.guesser.train(NEGATIVE, "pos")
    self.guesser.train(NEGATIVE, "hindrance")
    self.guesser.train(NEGATIVE, "sucks")
    self.guesser.train(NEGATIVE, "problems")
    self.guesser.train(NEGATIVE, "not working")
    self.guesser.train(NEGATIVE, "fuming")
    self.guesser.train(NEGATIVE, "annoying")
    self.guesser.train(NEGATIVE, "frothing")
    self.guesser.train(NEGATIVE, "poorly")
    self.guesser.train(NEGATIVE, "headache")
    self.guesser.train(NEGATIVE, "completely wrong")
    self.guesser.train(NEGATIVE, "sad news")
    self.guesser.train(NEGATIVE, "didn't last")
    self.guesser.train(NEGATIVE, "lame")
    self.guesser.train(NEGATIVE, "pet peeves")
    self.guesser.train(NEGATIVE, "pet peeve")
    self.guesser.train(NEGATIVE, "can't send")
    self.guesser.train(NEGATIVE, "bullshit")
    self.guesser.train(NEGATIVE, "fail")
    self.guesser.train(NEGATIVE, "so terrible")
    self.guesser.train(NEGATIVE, "negative")
    self.guesser.train(NEGATIVE, "anooying")
    self.guesser.train(NEGATIVE, "an issue")
    self.guesser.train(NEGATIVE, "drop dead")
    self.guesser.train(NEGATIVE, "trouble")
    self.guesser.train(NEGATIVE, "brainwashed")
    self.guesser.train(NEGATIVE, "smear")
    self.guesser.train(NEGATIVE, "commie")
    self.guesser.train(NEGATIVE, "communist")
    self.guesser.train(NEGATIVE, "anti-women")
    self.guesser.train(NEGATIVE, "WTF")
    self.guesser.train(NEGATIVE, "anxiety")
    self.guesser.train(NEGATIVE, "STING")
    self.guesser.train(NEGATIVE, "nobody spoke")
    self.guesser.train(NEGATIVE, "yell")
    self.guesser.train(NEGATIVE, "Damn")
    self.guesser.train(NEGATIVE, "aren't")
    self.guesser.train(NEGATIVE, "anti")
    self.guesser.train(NEGATIVE, "i hate")
    self.guesser.train(NEGATIVE, "hate")
    self.guesser.train(NEGATIVE, "dissapointing")
    self.guesser.train(NEGATIVE, "doesn't recommend")
    self.guesser.train(NEGATIVE, "the worst")
    self.guesser.train(NEGATIVE, "worst")
    self.guesser.train(NEGATIVE, "expensive")
    self.guesser.train(NEGATIVE, "crap")
    self.guesser.train(NEGATIVE, "socialist")
    self.guesser.train(NEGATIVE, "won't")
    self.guesser.train(NEGATIVE, "wont")
    self.guesser.train(NEGATIVE, ":(")
    self.guesser.train(NEGATIVE, ":-(")
    self.guesser.train(NEGATIVE, "Thanks")
    self.guesser.train(NEGATIVE, "smartass")
    self.guesser.train(NEGATIVE, "don't like")
    self.guesser.train(NEGATIVE, "too bad")
    self.guesser.train(NEGATIVE, "frickin")
    self.guesser.train(NEGATIVE, "snooty")
    self.guesser.train(NEGATIVE, "knee jerk")
    self.guesser.train(NEGATIVE, "jerk")
    self.guesser.train(NEGATIVE, "reactionist")
    self.guesser.train(NEGATIVE, "MUST DIE")
    self.guesser.train(NEGATIVE, "no more")
    self.guesser.train(NEGATIVE, "hypocrisy")
    self.guesser.train(NEGATIVE, "ugly")
    self.guesser.train(NEGATIVE, "too slow")
    self.guesser.train(NEGATIVE, "not reliable")
    self.guesser.train(NEGATIVE, "noise")
    self.guesser.train(NEGATIVE, "crappy")
    self.guesser.train(NEGATIVE, "horrible")
    self.guesser.train(NEGATIVE, "bad quality")
    self.guesser.train(NEGATIVE, "angry")
    self.guesser.train(NEGATIVE, "annoyed")
    self.guesser.train(NEGATIVE, "anxious")
    self.guesser.train(NEGATIVE, "arrogant")
    self.guesser.train(NEGATIVE, "ashamed")
    self.guesser.train(NEGATIVE, "awful")
    self.guesser.train(NEGATIVE, "bad")
    self.guesser.train(NEGATIVE, "bewildered")
    self.guesser.train(NEGATIVE, "blues")
    self.guesser.train(NEGATIVE, "bored")
    self.guesser.train(NEGATIVE, "clumsy")
    self.guesser.train(NEGATIVE, "combative")
    self.guesser.train(NEGATIVE, "condemned")
    self.guesser.train(NEGATIVE, "confused")
    self.guesser.train(NEGATIVE, "crazy")
    self.guesser.train(NEGATIVE, "flipped-out")
    self.guesser.train(NEGATIVE, "creepy")
    self.guesser.train(NEGATIVE, "cruel")
    self.guesser.train(NEGATIVE, "dangerous")
    self.guesser.train(NEGATIVE, "defeated")
    self.guesser.train(NEGATIVE, "defiant")
    self.guesser.train(NEGATIVE, "depressed")
    self.guesser.train(NEGATIVE, "disgusted")
    self.guesser.train(NEGATIVE, "disturbed")
    self.guesser.train(NEGATIVE, "dizzy")
    self.guesser.train(NEGATIVE, "dull")
    self.guesser.train(NEGATIVE, "embarrassed")
    self.guesser.train(NEGATIVE, "envious")
    self.guesser.train(NEGATIVE, "evil")
    self.guesser.train(NEGATIVE, "fierce")
    self.guesser.train(NEGATIVE, "foolish")
    self.guesser.train(NEGATIVE, "frantic")
    self.guesser.train(NEGATIVE, "frightened")
    self.guesser.train(NEGATIVE, "grieving")
    self.guesser.train(NEGATIVE, "grumpy")
    self.guesser.train(NEGATIVE, "helpless")
    self.guesser.train(NEGATIVE, "homeless")
    self.guesser.train(NEGATIVE, "hungry")
    self.guesser.train(NEGATIVE, "hurt")
    self.guesser.train(NEGATIVE, "ill")
    self.guesser.train(NEGATIVE, "itchy")
    self.guesser.train(NEGATIVE, "jealous")
    self.guesser.train(NEGATIVE, "jittery")
    self.guesser.train(NEGATIVE, "lazy")
    self.guesser.train(NEGATIVE, "lonely")
    self.guesser.train(NEGATIVE, "mysterious")
    self.guesser.train(NEGATIVE, "nasty")
    self.guesser.train(NEGATIVE, "rape")
    self.guesser.train(NEGATIVE, "naughty")
    self.guesser.train(NEGATIVE, "nervous")
    self.guesser.train(NEGATIVE, "nutty")
    self.guesser.train(NEGATIVE, "obnoxious")
    self.guesser.train(NEGATIVE, "outrageous")
    self.guesser.train(NEGATIVE, "panicky")
    self.guesser.train(NEGATIVE, "fucking up")
    self.guesser.train(NEGATIVE, "repulsive")
    self.guesser.train(NEGATIVE, "scary")
    self.guesser.train(NEGATIVE, "selfish")
    self.guesser.train(NEGATIVE, "sore")
    self.guesser.train(NEGATIVE, "tense")
    self.guesser.train(NEGATIVE, "terrible")
    self.guesser.train(NEGATIVE, "testy")
    self.guesser.train(NEGATIVE, "thoughtless")
    self.guesser.train(NEGATIVE, "tired")
    self.guesser.train(NEGATIVE, "troubled")
    self.guesser.train(NEGATIVE, "upset")
    self.guesser.train(NEGATIVE, "uptight")
    self.guesser.train(NEGATIVE, "weary")
    self.guesser.train(NEGATIVE, "wicked")
    self.guesser.train(NEGATIVE, "worried")
    self.guesser.train(NEGATIVE, "is a fool")
    self.guesser.train(NEGATIVE, "painful")
    self.guesser.train(NEGATIVE, "pain")
    self.guesser.train(NEGATIVE, "gross") 


  def classify(self, sentence):
    guess = self.guesser.guess(sentence)
    if len(guess) == 0:
      return NEUTRAL

    if len(guess) == 1:
      (sentiment, probabitily) = guess[0]
      return sentiment

    (max_sentiment, max_value) = guess[0]
    (min_sentiment, min_value) = guess[1]
    if max_value - min_value > self.THRESHHOLD:
      return max_sentiment


    return NEUTRAL



class BayesData(dict):

    def __init__(self, name='', pool=None):
        self.name = name
        self.training = []
        self.pool = pool
        self.tokenCount = 0
        self.trainCount = 0

    def trainedOn(self, item):
        return item in self.training

    def __repr__(self):
        return '<BayesDict: %s, %s tokens>' % (self.name, self.tokenCount)

class Bayes(object):

    def __init__(self, tokenizer=None, combiner=None, dataClass=None):
        if dataClass is None:
            self.dataClass = BayesData
        else:
            self.dataClass = dataClass
        self.corpus = self.dataClass('__Corpus__')
        self.pools = {}
        self.pools['__Corpus__'] = self.corpus
        self.trainCount = 0
        self.dirty = True
        # The tokenizer takes an object and returns
        # a list of strings
        if tokenizer is None:
            self._tokenizer = Tokenizer()
        else:
            self._tokenizer = tokenizer
        # The combiner combines probabilities
        if combiner is None:
            self.combiner = self.robinson
        else:
            self.combiner = combiner

    def commit(self):
        self.save()

    def newPool(self, poolName):
        """Create a new pool, without actually doing any
        training.
        """
        self.dirty = True # not always true, but it's simple
        return self.pools.setdefault(poolName, self.dataClass(poolName))

    def removePool(self, poolName):
        del(self.pools[poolName])
        self.dirty = True

    def renamePool(self, poolName, newName):
        self.pools[newName] = self.pools[poolName]
        self.pools[newName].name = newName
        self.removePool(poolName)
        self.dirty = True

    def mergePools(self, destPool, sourcePool):
        """Merge an existing pool into another.
        The data from sourcePool is merged into destPool.
        The arguments are the names of the pools to be merged.
        The pool named sourcePool is left in tact and you may
        want to call removePool() to get rid of it.
        """
        sp = self.pools[sourcePool]
        dp = self.pools[destPool]
        for tok, count in sp.items():
            if dp.get(tok):
                dp[tok] += count
            else:
                dp[tok] = count
                dp.tokenCount += 1
        self.dirty = True

    def poolData(self, poolName):
        """Return a list of the (token, count) tuples.
        """
        return self.pools[poolName].items()

    def poolTokens(self, poolName):
        """Return a list of the tokens in this pool.
        """
        return [tok for tok, count in self.poolData(poolName)]

    def save(self, fname='bayesdata.dat'):
        from cPickle import dump
        fp = open(fname, 'wb')
        dump(self.pools, fp)
        fp.close()

    def load(self, fname='bayesdata.dat'):
        from cPickle import load
        fp = open(fname, 'rb')
        self.pools = load(fp)
        fp.close()
        self.corpus = self.pools['__Corpus__']
        self.dirty = True

    def poolNames(self):
        """Return a sorted list of Pool names.
        Does not include the system pool '__Corpus__'.
        """
        pools = self.pools.keys()
        pools.remove('__Corpus__')
        pools = [pool for pool in pools]
        pools.sort()
        return pools

    def buildCache(self):
        """ merges corpora and computes probabilities
        """
        self.cache = {}
        for pname, pool in self.pools.items():
            # skip our special pool
            if pname == '__Corpus__':
                continue

            poolCount = pool.tokenCount
            themCount = max(self.corpus.tokenCount - poolCount, 1)
            cacheDict = self.cache.setdefault(pname, self.dataClass(pname))

            for word, totCount in self.corpus.items():
                # for every word in the copus
                # check to see if this pool contains this word
                thisCount = float(pool.get(word, 0.0))
                if (thisCount == 0.0):
                  continue
                otherCount = float(totCount) - thisCount

                if not poolCount:
                    goodMetric = 1.0
                else:
                    goodMetric = min(1.0, otherCount/poolCount)
                badMetric = min(1.0, thisCount/themCount)
                f = badMetric / (goodMetric + badMetric)

                # PROBABILITY_THRESHOLD
                if abs(f-0.5) >= 0.1 :
                    # GOOD_PROB, BAD_PROB
                    cacheDict[word] = max(0.0001, min(0.9999, f))

    def poolProbs(self):
        if self.dirty:
            self.buildCache()
            self.dirty = False
        return self.cache

    def getTokens(self, obj):
        """By default, we expect obj to be a screen and split
        it on whitespace.

        Note that this does not change the case.
        In some applications you may want to lowecase everthing
        so that "king" and "King" generate the same token.

        Override this in your subclass for objects other
        than text.

        Alternatively, you can pass in a tokenizer as part of
        instance creation.
        """
        return self._tokenizer.tokenize(obj)

    def getProbs(self, pool, words):
        """ extracts the probabilities of tokens in a message
        """
        probs = [(word, pool[word]) for word in words if word in pool]
        probs.sort(lambda x,y: cmp(y[1],x[1]))
        return probs[:2048]

    def train(self, pool, item, uid=None):
        """Train Bayes by telling him that item belongs
        in pool. uid is optional and may be used to uniquely
        identify the item that is being trained on.
        """
        tokens = self.getTokens(item)
        pool = self.pools.setdefault(pool, self.dataClass(pool))
        self._train(pool, tokens)
        self.corpus.trainCount += 1
        pool.trainCount += 1
        if uid:
            pool.training.append(uid)
        self.dirty = True

    def untrain(self, pool, item, uid=None):
        tokens = self.getTokens(item)
        pool = self.pools.get(pool, None)
        if not pool:
            return
        self._untrain(pool, tokens)
        # I guess we want to count this as additional training?
        self.corpus.trainCount += 1
        pool.trainCount += 1
        if uid:
            pool.training.remove(uid)
        self.dirty = True


    def _train(self, pool, tokens):
        wc = 0
        for token in tokens:
            count = pool.get(token, 0)
            pool[token] =  count + 1
            count = self.corpus.get(token, 0)
            self.corpus[token] =  count + 1
            wc += 1
        pool.tokenCount += wc
        self.corpus.tokenCount += wc

    def _untrain(self, pool, tokens):
        for token in tokens:
            count = pool.get(token, 0)
            if count:
                if count == 1:
                    del(pool[token])
                else:
                    pool[token] =  count - 1
                pool.tokenCount -= 1

            count = self.corpus.get(token, 0)
            if count:
                if count == 1:
                    del(self.corpus[token])
                else:
                    self.corpus[token] =  count - 1
                self.corpus.tokenCount -= 1

    def trainedOn(self, msg):
        for p in self.cache.values():
            if msg in p.training:
                return True
        return False

    def guess(self, msg):
        tokens = set(self.getTokens(msg))
        pools = self.poolProbs()

        res = {}
        for pname, pprobs in pools.items():
            p = self.getProbs(pprobs, tokens)
            if len(p) != 0:
                res[pname]=self.combiner(p, pname)
        res = res.items()
        res.sort(lambda x,y: cmp(y[1], x[1]))
        return res

    def robinson(self, probs, ignore):
        """ computes the probability of a message being spam (Robinson's method)
            P = 1 - prod(1-p)^(1/n)
            Q = 1 - prod(p)^(1/n)
            S = (1 + (P-Q)/(P+Q)) / 2
            Courtesy of http://christophe.delord.free.fr/en/index.html
        """

        nth = 1./len(probs)
        P = 1.0 - reduce(operator.mul, map(lambda p: 1.0-p[1], probs), 1.0) ** nth
        Q = 1.0 - reduce(operator.mul, map(lambda p: p[1], probs)) ** nth
        S = (P - Q) / (P + Q)
        return (1 + S) / 2


    def robinsonFisher(self, probs, ignore):
        """ computes the probability of a message being spam (Robinson-Fisher method)
            H = C-1( -2.ln(prod(p)), 2*n )
            S = C-1( -2.ln(prod(1-p)), 2*n )
            I = (1 + H - S) / 2
            Courtesy of http://christophe.delord.free.fr/en/index.html
        """
        n = len(probs)
        try: H = chi2P(-2.0 * math.log(reduce(operator.mul, map(lambda p: p[1], probs), 1.0)), 2*n)
        except OverflowError: H = 0.0
        try: S = chi2P(-2.0 * math.log(reduce(operator.mul, map(lambda p: 1.0-p[1], probs), 1.0)), 2*n)
        except OverflowError: S = 0.0
        return (1 + H - S) / 2

    def __repr__(self):
        return '<Bayes: %s>' % [self.pools[p] for p in self.poolNames()]

    def __len__(self):
        return len(self.corpus)

class Tokenizer:
    """A simple regex-based whitespace tokenizer.
    It expects a string and can return all tokens lower-cased
    or in their existing case.
    """

    WORD_RE = re.compile('\\w+', re.U)

    def __init__(self, lower=False):
        self.lower = lower

    def tokenize(self, obj):
        for match in self.WORD_RE.finditer(obj):
            if self.lower:
                yield match.group().lower()
            else:
                yield match.group()

def chi2P(chi, df):
    """ return P(chisq >= chi, with df degree of freedom)

    df must be even
    """
    assert df & 1 == 0
    m = chi / 2.0
    sum = term = math.exp(-m)
    for i in range(1, df/2):
        term *= m/i
        sum += term
    return min(sum, 1.0)

