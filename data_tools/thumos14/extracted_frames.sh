#! /usr/bin/bash env

cd ../

# `--flow_type tvl1` is removed for speed
python build_rawframes.py ../data/thumos14/videos_val/ ../data/thumos14/rawframes/ --level 1 --ext mp4
echo "Raw frames (RGB and tv-l1) Generated for val set"

python build_rawframes.py ../data/thumos14/videos_test/ ../data/thumos14/rawframes/ --level 1 --ext mp4
echo "Raw frames (RGB and tv-l1) Generated for test set"

cd thumos14/
