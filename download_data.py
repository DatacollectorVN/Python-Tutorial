import urllib
import requests
import argparse
import os

class Cfg(object):
    def __init__(self):
        super(Cfg, self).__init__()
        self.model_url = ["https://github.com/DatacollectorVN/Releases-Models/releases/download/data/sample_data_s5.zip"]
    
    def down_model(self, destination):
        model_url = self.model_url[0]
        print ('Start to download, this process take a few minutes')
        urllib.request.urlretrieve(model_url, destination)
        print("Downloaded data- {} to-'{}'".format(model_url, destination))


def main(directory):
    cfg = Cfg()
    os.makedirs(directory, exist_ok = True)
    cfg.down_model(destination = os.path.join(directory, "sample_data_s5.zip"))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help = 'Destination to save model', type = str,
                        default = 'data')

    args = parser.parse_args()
    main(directory = args.dir)