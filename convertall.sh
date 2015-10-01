#!/bin/bash

for f in `ls *.ipynb`
do
  ipython nbconvert --to html --ExecutePreprocessors.enabled=True --template=template.tpl $f
done