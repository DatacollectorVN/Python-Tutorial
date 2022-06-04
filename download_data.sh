echo 'This script for downloading data'
python download_data.py --dir data
unzip data/sample_data_s5.zip -d data  
rm -rf data/__MACOSX
rm data/sample_data_s5.zip