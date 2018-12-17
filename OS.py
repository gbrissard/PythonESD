import os # pour importer module entier
# OU
from time import sleep # pour ne prendre que certaines commandes

cmd = raw_input("Commande ? ")

print os.system(cmd)