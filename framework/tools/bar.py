#!/usr/bin/python
# -*- coding: utf-8 -*-

## Copyright (C) 2010 - 2011, University of New Orleans
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#
# --
#
# Bar chart generator.
#

import pylab

import rdp

def generate(sample_sequence_tuples, save_path = None):
    samples = [x[0] for x in sample_sequence_tuples]
    number_of_sequences = [x[1] for x in sample_sequence_tuples]

    pos = pylab.arange(len(number_of_sequences))+.5

    width = len(samples) / 5
    if width < 5:
        width = 5

    if width > 15:
        width = 15

    fig = pylab.figure(figsize=(width, 4))

    pylab.rcParams.update({'axes.linewidth' : 0, 'axes.axisbelow': False})
    pylab.rc('grid', color='0.80', linestyle='-', linewidth=0.1)
    pylab.grid(True)
    pylab.bar(pos, number_of_sequences, align='center', color='#EFADAD', linewidth=0.1)
    pylab.xticks(pos, samples, rotation=90, size='xx-small')
    pylab.xlim(xmax=len(samples))
    pylab.yticks(size='xx-small')
    pylab.ylabel('Number of sequences (%d samples)' % len(samples), size="small")

    if save_path:
        pylab.savefig(save_path)
    else:
        pylab.show()

if __name__ == '__main__':
    sample_sequence_tuples = [('4002', 3448148), ('4003', 898692), ('4004', 9381260), ('4005', 6412960), ('4006', 6495321), ('4007', 6688560), ('4008', 3951180), ('4009', 3274087), ('4010', 6898681), ('4011', 5985175), ('4012', 13243550), ('4013', 2259064), ('4014', 5191440), ('4016', 48220793), ('4017', 1553203), ('4018', 7374300), ('4019', 9274300), ('4020', 7910898), ('4021', 5094387), ('4022', 1816354), ('4023', 794727), ('4024', 3166415), ('4025', 4417170), ('4026', 3610642), ('4027', 4270995), ('4030', 7703843), ('4031', 5646226), ('4032', 1971628), ('4034', 805139), ('4035', 9266441), ('4037', 6567388), ('4038', 1664804), ('4040', 358930), ('4041', 2696350)]
    generate(sample_sequence_tuples)

