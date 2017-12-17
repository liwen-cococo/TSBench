import random
from tsbench.algorithms.base import AnomalyDetector

class RandomDetector(AnomalyDetector):
    """
    A simple random detector
    """
    def __init__(self, *args, **kwargs):
        super(RandomDetector, self).__init__(*args, **kwargs)
        self.rate = 0.0
    
    def trainPhase(self, front_values, front_labels):
        self.rate = (front_labels.__len__() + 0.0) / (front_values.__len__() + 0.0)

    def detectPhase(self, latter_values):
        results = []
        c = 0
        for i in latter_values:
            if c % 10 != 0:
                results.append(0)
            else:
                results.append(1)
            c += 1
        return results

if __name__ == '__main__':
    pass
