#! /usr/bin/bash env

# please make sure unrar has been installed
# sudo apt-get install unrar

DATA_DIR="../../data/hmdb51/"

if [[ ! -d "${DATA_DIR}" ]]; then
  echo "${DATA_DIR} does not exist. Creating";
  mkdir -p ${DATA_DIR}
fi

cd ${DATA_DIR}

mkdir -p ./videos
cd ./videos

wget http://serre-lab.clps.brown.edu/wp-content/uploads/2013/10/hmdb51_org.rar

unrar x ./hmdb51_org.rar
rm ./hmdb51_org.rar

# extract all rar files with full path
for file in *.rar; do unrar x $file; done

rm ./*.rar
cd "../../../data_tools/hmdb51"
