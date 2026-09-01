"""
Plot utilities for kpoints
"""

import numpy as np
from pymatgen.electronic_structure.bandstructure import BandStructure

def get_kticks(bs: BandStructure):
    indices = []
    labels  = []
    [indices.append(branch['start_index']) for branch in bs.branches]
    [labels.append(branch['name'].split('-')[0]) for branch in bs.branches]
    indices.append(bs.branches[-1]['end_index'])
    labels.append(bs.branches[-1]['name'].split('-')[-1])
    xticks = np.array(bs.distance)[indices]
    
    xticklabels = [rf"${lab}$" if 'GAM' not in lab else r"$\Gamma$" for lab in labels]
    return xticks, xticklabels