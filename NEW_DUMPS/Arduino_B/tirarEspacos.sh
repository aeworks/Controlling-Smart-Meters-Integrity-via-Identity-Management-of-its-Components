#!/bin/bash
cat DumpBase_B_30 | while read line
do
cut -b -47 |tee hexBaseB_30.csv
done
rm DumpBase_B_30
