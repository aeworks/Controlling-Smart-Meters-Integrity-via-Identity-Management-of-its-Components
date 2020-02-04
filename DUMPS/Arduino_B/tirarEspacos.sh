#!/bin/bash
cat DumpB_30 | while read line
do
cut -b -47 |tee hexB_30.csv
done
rm DumpB_30