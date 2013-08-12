#!/bin/bash
for i in {19..19}
do
   ./cbhvset.py $i $@ &
done
echo "All jobs started, wait for output! Stop with 'killall cbhvset.py'"
