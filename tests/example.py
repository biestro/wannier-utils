import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.core import Spin
import os

from wannier_utils import get_kticks

if __name__=="__main__":
    cwd = os.path.dirname(__file__)
    vr = Vasprun(cwd+"/vasprun.xml")
    bands = vr.get_band_structure(line_mode=True)

    kticks, klabels = get_kticks(bands)
    fig, ax = plt.subplots()
    ax.plot(bands.distance, bands.bands[Spin.up][34:].T - bands.efermi,)
    ax.set_xlim(kticks[0], kticks[-1])
    ax.set_xticks(kticks)
    [ax.axvline(k, lw=0.5, color='gray', zorder=0) for k in kticks]
    ax.set_xticklabels(klabels)
    plt.show()