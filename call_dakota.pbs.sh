#!/usr/bin/env bash
# This PBS submission script runs Dakota on the CSDMS HPCC, beach.
# Call this script with:
#
#  $ qsub call_dakota.pbs.sh

# Add Dakota to PATH and LD_LIBRARY_PATH.
export DAKOTA_DIR=/usr/local/dakota
PATH=$DAKOTA_DIR/bin:$DAKOTA_DIR/test:$PATH
if [ $LD_LIBRARY_PATH ]; then
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DAKOTA_DIR/bin:$DAKOTA_DIR/lib
else
    export LD_LIBRARY_PATH=$DAKOTA_DIR/bin:$DAKOTA_DIR/lib
fi

# Push beach's Anaconda Python distribution to the front of PATH.
PATH=/usr/local/anaconda/bin:$PATH

# Switch to the current working directory and call Dakota.
cd $PBS_O_WORKDIR
dakota -i dakota_analysis.in -o dakota_analysis.out
