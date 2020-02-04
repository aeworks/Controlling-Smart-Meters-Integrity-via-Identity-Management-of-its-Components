#!/bin/bash
cat DumpBase_A_1 | while read line
do
cut -b -47 |tee hexBaseA_1.csv
done
rm DumpBase_A_1
