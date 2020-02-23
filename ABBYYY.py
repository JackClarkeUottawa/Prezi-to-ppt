#!/usr/bin/python

import os
import time
from Functions.ABBYYY.process import *
from Functions.ABBYYY.AbbyyOnlineSdk import *

def processtopdf(input,outputname):
    global processor
    processor = AbbyyOnlineSdk()

    setup_processor()

    args = create_parser().parse_args()

    source_file = input
    target_file = outputname
    output_format = "pdf"
    language = "English"

    if os.path.isfile(source_file):
        recognize_file(source_file, target_file, language, output_format)
    else:
        print("No such file: {}".format(source_file))




