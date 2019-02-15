#!/bin/bash

URL=https://www.dropbox.com/s//final_N_vgrid3.zip
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/" && pwd )"
cd $DIR

rm -rf *.tar.gz *.zip
echo "Downloading the environment executable..."
wget $URL
echo "Unzipping..."
unzip final_N_vgrid3.zip
mv final_N_vgrid3/* .
rm -rf final_N_vgrid3 __MACOSX .DS_Store
rm -rf *.tar.gz *.zip
echo "Downloading Done."
