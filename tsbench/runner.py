import os
import helper
import scoring
from tsbench.algorithms.random.random_detector import RandomDetector as selectedDetector
try:
  import simplejson as json
except ImportError:
  import json


class Runner(object):
    def __init__(self, algorithm, proportion):
        self.algorithm = algorithm       # str
        self.proportion = proportion     # float
        self.values = helper.getData()   # dict
        self.labels = helper.getLabels() # dict
        self.anomaly_results = self.detect()
    
    def detect(self):
        results = {}
        for k in self.values:
            sd = selectedDetector(self.values[k], self.labels[k], self.proportion)
            results[k] = sd.run() # return index of detected abnormal point 
        return results

    def detectResultToFile(self):
        result_dir = './results/' + self.algorithm + '/'
        if not os.path.exists(result_dir):
            os.mkdir(result_dir)
        json_path = result_dir + 'anomaly.json'

        with open(json_path, 'w') as f:
            json.dump(self.anomaly_results, f, indent=4)

    def scoreTraditional(self):
        scores = {}
        for d in self.labels:
            front_length = int(self.values[d].__len__() * self.proportion)
            latter_length = self.values[d].__len__() - front_length
            (TP, TN, FP, FN, Precision, Recall, FScore) = scoring.sTraditional(self.labels[d], self.anomaly_results[d], front_length, latter_length)
            scores[d] = (TP, TN, FP, FN, Precision, Recall, FScore)
        
        json_path = './results/' + self.algorithm + '/' + 'scoreTraditional.json'
        with open(json_path, 'w') as f:
            json.dump(scores, f, indent=4)
    
    def scoreMrPei(self):
        # to be done
        pass
    
    def scoreSelfDefined(self):
        # to be done
        pass 
    
    def execute(self):
        # to be done
        self.detectResultToFile()
        self.scoreTraditional()
