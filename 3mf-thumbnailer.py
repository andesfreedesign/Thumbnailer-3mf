#!/usr/bin/python3

import sys
import zipfile
import getopt

opt, par = getopt.getopt(sys.argv[1:], '-s:')
input_file = par[0]
output_file = par[1]

# Read compressed file
zfile = zipfile.ZipFile(input_file)
files = zfile.namelist()

# Read thumbnail from file
image = "Metadata/thumbnail.png"
if image in files:
    image = zfile.read(image)

# Write icon to output_file
thumb = open(output_file, "wb")
thumb.write(image)
thumb.close()
