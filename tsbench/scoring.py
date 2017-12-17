try:
  import simplejson as json
except ImportError:
  import json
import os

def sTraditional(t_labels, detected, f_length, l_length):
    """
    @param t_labels (dict) true anomaly-index labels
    @param detected (dict) detected labels by specific algorithm
    @param f_length (int)  traing data length
    @param l_length (int)  test data length
    """
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    a_length = f_length + l_length
    for id in xrange(f_length, a_length):
        x1 = id in t_labels
        x2 = id in detected
        if x1 and x2:
            TP += 1
        elif not x1 and x2:
            FP += 1
        elif x1 and not x2:
            FN += 1
        else:
            TN += 1
    
    Precision = (TP + 0.0) / (TP + FP +0.0)
    Recall = (TP + 0.0) / (TP + FN +0.0)
    FScore = 2 * Precision * Recall / (Precision + Recall)

    return (TP, TN, FP, FN, Precision, Recall, FScore)


def addTogether(score_json_path):
    source_data = {}
    with open(score_json_path) as f:
        source_data = json.load(f)
    
    results = {}
    results['total'] = [0, 0, 0, 0, 0, 0, 0]
    # accumulate TP, TN, FP, FN
    for key in source_data:
        csv_file_name_len = key.split('/')[-1].__len__()
        x = key[:0 - csv_file_name_len]
        if x not in results:
            results[x] = [0, 0, 0, 0, 0, 0, 0] # TP, TN, FP, FN, Precision, Recall, FScore
        for ii in xrange(4): # accumulate TP, TN, FP, FN
            results[x][ii] = results[x][ii] + source_data[key][ii]
            results['total'][ii] = results['total'][ii] + source_data[key][ii]
    
    # calculate Precision, Recall and F-Score
    for r in results:
        results[r][4] = (results[r][0] + 0.0) / (results[r][0] + results[r][2] + 0.0)  # Precision = TP/(TP + FP)
        results[r][5] = (results[r][0] + 0.0) / (results[r][0] + results[r][3] + 0.0)  # Recall = TP/(TP + FN)
        results[r][6] = round(2 * results[r][4] * results[r][5] / (results[r][4] + results[r][5]), 4)
        results[r][4] = round(results[r][4], 4)
        results[r][5] = round(results[r][5], 4)
        
    return results


if __name__ == '__main__':
    r = addTogether('./results/random/scoreTraditional.json')
    for k in r:
        print k, r[k]
        print ''


