# Eric Gan
# Babbler. Generates random sentence based off corpus.
# Also known as a Disscociated Press algorithm
#
# Note: This script requires the NLTK package. This can be downloaded from
# www.nltk.org.

import nltk
import sys, os
import random, time

# N_GRAM = 3 takes 22 seconds to train.
# N_GRAM = 4 takes 50 seconds to train.
N_GRAM = 3
SENT_LEN = 100

words = ["The", "In", "O", "My", "When", "If", "Jesus"]

class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

if __name__ == '__main__':
    print "\nSci-Faith Babbler intialized! (powered by Eric Gan)"
    
    devnull = open(os.devnull, 'w')
    inputfd = open("esv.txt", "r")
    corpus = inputfd.read()
    inputfd.close()
    
    print "Training language model...",
    sys.stdout.flush()
    startTime = time.time()
    bibleModel = nltk.model.NgramModel(N_GRAM, nltk.word_tokenize(corpus))
    totalTime = time.time() - startTime
    print "Done!"
    print "Training took %fs." % (totalTime)
    
    
    try: 
        with RedirectStdStreams(stdout=None, stderr=devnull):
            while 1:
                raw_input("Press Enter to generate a string. Press Ctrl+C to exit... ")
                startWord = [ words[random.randint(0,len(words)-1)] ]
                print
                print " ".join(bibleModel.generate(SENT_LEN, startWord))
                print
    except KeyboardInterrupt:
        devnull.close()
        print "\nExiting...\n"

