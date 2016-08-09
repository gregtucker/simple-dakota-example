# Simple Dakota Example

A simple example of using [Dakota](https://dakota.sandia.gov/)
iterative systems analysis toolkit
to perform a parameter study.

## Running this example on your computer

To run this example,
you'll need

1. Dakota,
1. Python, and, optionally,
1. Git

installed on on your computer.

Follow the instructions on the Dakota website
for [downloading](https://dakota.sandia.gov/download.html) and
[installing](https://dakota.sandia.gov/content/install-linux-macosx)
a precompiled Dakota binary for your system.

Macs and Linux distributions come with a Python distribution;
however, we recommend using the
[Anaconda](https://www.continuum.io/downloads)
Python distribution
because it's easy to install on Mac, Linux, and Windows,
and it doesn't interefere with any other Python distributions.
If you don't want to use it, you can delete it without harm.

Likewise, Macs and Linux distributions come with
[Git](https://git-scm.com/).
If you're not comfortable using Git,
try the [GitHub Desktop](https://desktop.github.com/) application,
which is available for Mac and Windows.

To download this example,
you can use Git:

    git clone https://github.com/mdpiper/simple-dakota-example

Or you can download a
[zip file](https://github.com/mdpiper/simple-dakota-example/archive/master.zip)
and unpack it.

Change into the **simple-dakota-example** directory
and run the example with:

	cd simple-dakota-example
	dakota -i dakota_analysis.in -o dakota_run.out &> run.log

When the example completes,
view the output in **run.log**.


## Running this example on beach

[CSDMS](https://csdms.colorado.edu)
manages an experimental high-performance computing cluster (HPCC),
***beach***.
Using an HPCC is different than using a personal computer
in that work must be submitted through a job scheduler.
Dakota, Python, and Git are already installed on ***beach***.

Download this example with:

    git clone https://github.com/mdpiper/simple-dakota-example

Change into the **simple-dakota-example** directory
and submit the run to the job scheduler with:

	cd simple-dakota-example
	qsub call_dakota.pbs.in

When the example completes,
view the output in the scheduler output file,
which will have a name like
**call_dakota.pbs.sh.o[run_id]**,
where `[run_id]` is the identifier for a run;
e.g., **call_dakota.pbs.sh.o226983**.
