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

NTHROW=10000000
NRUN=10


# Create Run folders inside it
for ((run=1; run<=NRUN; run++)); do
    mkdir -p "$fullpath/Run$run"
done

SAVEEVENTS=1

for RUN in $(seq 1 $NRUN); do
    python3 computeAcceptance.py $NTHROW $RUN "$fullpath/Run$RUN" $SAVEEVENTS&
done

wait