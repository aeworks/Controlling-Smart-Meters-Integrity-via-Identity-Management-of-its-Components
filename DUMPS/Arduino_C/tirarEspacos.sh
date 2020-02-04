#!/bin/bash
cat DumpC_30 | while read line
do
cut -b -47 |tee hexC_30.csv
done
rm DumpC_30
