#!/bin/bash
cat DumpBase_C_30 | while read line
do
cut -b -47 |tee hexBaseC_30.csv
done
rm DumpBase_C_30
