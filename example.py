from modeller import *
from modeller.automodel import *

env = Environ()
env.io.atom_files_directory = ['.']
a = AutoModel(env, alnfile='aln.fasta', knowns=('1CTP', '3J4Q', '4AE6', '6F14', '6Y05'), sequence='seq')

a.starting_model = 1
a.ending_model = 2
a.make()
a.write("model.pdb")

