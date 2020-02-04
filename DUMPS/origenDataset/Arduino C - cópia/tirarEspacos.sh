#!/bin/bash
cat DumpA_1Cop | while read line
do
cut -b -47 |tee hexCop1.csv
done
