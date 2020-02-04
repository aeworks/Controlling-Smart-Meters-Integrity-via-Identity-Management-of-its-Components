#!/bin/bash
cat DumpA_30 | while read line
do
cut -b -47 |tee hexA_30.csv
done
rm DumpA_30
