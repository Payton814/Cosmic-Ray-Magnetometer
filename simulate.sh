#!/usr/bin/env bash

#SBATCH -A PAS2277

#SBATCH -t 00:10:00
#SBATCH --nodes 1
#SBATCH --ntasks-per-node 10
#SBATCH --cpus-per-task 1
#SBATCH --mem=32000MB

TASK="$SLURM_ARRAY_TASK_ID"
echo "Starting task $TASK"

base_dir="./simulation_data"
prefix="sim"
width=5

# Make sure base directory exists
mkdir -p "$base_dir"

# Find last existing index

# Start near the current max, but let mkdir decide
last=$(ls -d "$base_dir"/${prefix}[0-9]* 2>/dev/null \
       | sed "s#.*/${prefix}##" \
       | sort -n \
       | tail -1)

i=${last:- -1}

while true; do
    ((i++))
    dirname=$(printf "%s%0*d" "$prefix" "$width" "$i")
    fullpath="$base_dir/$dirname"

    if mkdir "$fullpath" 2>/dev/null; then
        echo "Created $fullpath"
        break
    fi
done

NTHROW=10000000
NRUN=10


# Create Run folders inside it
for ((run=1; run<=NRUN; run++)); do
    mkdir -p "$fullpath/Run$run"
done

SAVEEVENTS=1

for RUN in $(seq 1 $NRUN); do
    python3 computeAcceptance.py $NTHROW $RUN "$fullpath/Run$RUN" $SAVEEVENTS &
done

wait
