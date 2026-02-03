#! /bin/bash

base_dir="./simulation_data"
prefix="sim"
width=5

# Make sure base directory exists
mkdir -p "$base_dir"

# Find last existing index
last=$(ls -d "$base_dir"/${prefix}[0-9]* 2>/dev/null \
       | sed "s#.*/${prefix}##" \
       | sort -n \
       | tail -1)

if [[ -z "$last" ]]; then
    next=0
else
    next=$((10#$last + 1))
fi

dirname=$(printf "%s%0*d" "$prefix" "$width" "$next")
fullpath="$base_dir/$dirname"

mkdir "$fullpath"


NTHROW=100000
NRUN=5

for RUN in {1..5}; do
    echo $RUN
    python3 computeAcceptance.py $NTHROW $RUN $fullpath
done

