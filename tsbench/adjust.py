# modify file: ./runner.py
# modify line 4 --- import algorithm
def adjust(algorithm_name):
    with open('runner.py', 'r') as f:
        data = f.readlines()
    data[3] = 'from tsbench.algorithms.'+algorithm_name+'.'+algorithm_name+'_detector import '+ algorithm_name.capitalize()+'Detector as selectedDetector\n'
    with open('runner.py', 'w') as f:
        f.writelines(data)

if __name__ == '__main__':
    adjust('random')