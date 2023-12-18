import pandas as pd

merged_df = pd.read_csv("../data/csv/merged/merged.csv")

# Index(['nmdept', 'nmprogram', 'nmgiat', 'nmoutput', 'nmsuboutput',
#        'nmtipe_peng', 'pagu_rev', 'rupiah', 'tahun', 'kddept', 'kdunit',
#        'kdprogram', 'kdgiat', 'kdfungsi', 'kdsfung', 'kdoutput', 'tipe_peng',
#        'kdakun', 'nmunit', 'nmfungsi', 'nmsfung', 'nmakun', 'type', 'kdsatker',
#        'kdlokasi', 'kdkabkota', 'iddekon', 'kddekon', 'kdsektor', 'kdsdana',
#        'nmlokasi', 'nmkabkota', 'nmdekon', 'nmsatker', 'nmsdana', 'nmsektor',
#        'pagu_diawal', 'kdtipe_peng'],
#       dtype='object')

merged_df.drop(['kdtipe_peng', 'nmsuboutput', 'type', 'pagu_diawal', 'pagu_rev'], axis=1, inplace=True)

merged_df.to_csv('../data/csv/cleaned/cleaned_merged.csv', index=False)
