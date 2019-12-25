
# RBSA



# Dependencies

If using nucleic acid sequences,third-party software mummer is needed.If you use CDS sequences,McScan is needed.

# Installation

git clone https://github.com/likui345/rbsa.git

python setup.py install

# usage

usage: 
    RBSA2.py  --type nucmer --ref REF --scf SCF
    
    or RBSA2.py  --type mcscan --A_bed A_BED --B_bed B_BED --anchor ANCHOR --scf SCF
    


Using reference genomes or mcscan anchor files to anchor scaffolds


optional arguments:

  -h, --help            show this help message and exit
  
  --type {nucmer,mcscan}
                        nucmer or mcscan anchor
                        
  --ref REF             This is reference genome sequences which has anchored
                        to the chromosomal level
                        
  --scf SCF             This is the scaffold sequences
  
  --A_bed A_BED         species_a bed file
  
  --B_bed B_BED         species_b bed file
  
  --anchor ANCHOR       anchor files of species_a and species_b
  

