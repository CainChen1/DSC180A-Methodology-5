import subprocess
import sys

def main():
    subprocess.run('~/.local/bin/kaggle datasets download -p /home/xic023/DSC180A-Methodology-5/data/raw ankurzing/sentiment-analysis-for-financial-news', shell = True, stdout = subprocess.PIPE)
    subprocess.run('~/.local/bin/kaggle datasets download -p /home/xic023/DSC180A-Methodology-5/data/raw yash612/stockmarket-sentiment-dataset', shell = True, stdout = subprocess.PIPE)
    subprocess.run('unzip /home/xic023/DSC180A-Methodology-5/data/raw/\*.zip -d /home/xic023/DSC180A-Methodology-5/data/raw', shell = True, stdout = subprocess.PIPE)
    
if __name__ == '__main__':
    main()
