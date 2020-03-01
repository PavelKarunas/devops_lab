#!/bin/bash

sudo yum -y install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel

pyenv install 3.7.6
pyenv install 2.7.17

pyenv virtualenv 3.7.6 python_3.7
pyenv virtualenv 2.7.17 python_2.7
