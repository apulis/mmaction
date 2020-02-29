#! /usr/bin/bash env

# please make sure unrar has been installed
# sudo apt-get install unrar

DATA_DIR="../../data/ucf101/"

if [[ ! -d "${DATA_DIR}" ]]; then
  echo "${DATA_DIR} does not exist. Creating";
  mkdir -p ${DATA_DIR}
fi

cd ${DATA_DIR}

wget https://www.crcv.ucf.edu/data/UCF101/UCF101.rar
unrar x UCF101.rar
mv ./UCF-101 ./videos

cd "../../data_tools/ucf101"
