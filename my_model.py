# This file is both a "driver" that is run automatically by Dakota, and a "model".
# One could separate the two, by having the driver run the model.
#
# In this example, the model is very simple: it is a function y = a x^1/2, which is 
# evaluated on a set of x values 1, 2, 3, ... 10.
#
# We are pretending we also have some data values for x (the same as above) and y. 
# Actually, we make the data to fit the function perfectly when a=10.4. So when we run
# a parameter search and evaluate the goodness of fit, we should find that the value of
# the coefficient (a) closest to 10.4 generates the best fit.
#
# (written by G. Tucker, for Modeling class, March 2016)

from __future__ import print_function

from builtins import str
import sys
from subprocess import call
import numpy as np


# Set the file names to use for the input file and template input file. The template
# input file is a text file we create that contains the string "{coefficient}". The
# actual input file, 'my_inputs.txt', will be created automatically by Dakota, which will
# replace "{coefficient}" with a number.
input_file_template = 'my_inputs_template.txt'
input_file = 'my_inputs.txt'

# Run Dakota's "dprepro" (preprocessor) program. This will make a new copy of
# 'my_inputs_template.txt' but replace the string that reads "{coefficient}" with an
# actual numerical value (or rather, a string representing a numeric value). It will then
# save the file with the name 'my_inputs.txt'. The actual value will be obtained from
# a third, Dakota-created file called 'params.in' (this same name is also passed in as
# an argument, and because it is the first argument, it is in sys.argv[1])
call(['dprepro', sys.argv[1], input_file_template, input_file])

# Get the input value for the model
infile = open(input_file)
coef = float( infile.readline() )
infile.close()
print('Running with coefficient value', coef)

# The model has a domain of "x" values that range from 1 to 10
x = np.arange(1.0, 11.0)

# Let's say we have some data (here completely made up: we "know" that the actual 
# correct coefficient value is 10.4)
y_data = 10.4 * np.sqrt(x)

# Now run the model, which in this case is simple: y = coef sqrt(x)
y_model = coef * np.sqrt(x)

# Find the root-mean-square misfit between model and data
rms_error = np.sqrt( np.sum( (y_model - y_data)**2 ) )
print('RMS error with coef', coef, 'is', rms_error)

# Write the RMS error to a file
outfile = open(sys.argv[2], 'w')
outfile.write(str(rms_error))
outfile.close()
