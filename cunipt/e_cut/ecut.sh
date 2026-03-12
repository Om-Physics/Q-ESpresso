#!/bin/sh

NAME="ecut"
 
for CUTOFF in  10 15 20 25 30 35 40
do
cat > ${NAME}_${CUTOFF}.in << EOF
&control
    calculation = 'scf'
    prefix = 'cunipt'
    pseudo_dir = './.'
    outdir = "./."
/

&system
    ibrav = 2,
    celldm(1) = 10.89,
    nat = 3,
    ntyp = 3,
    ecutwfc = $CUTOFF
    occupations = 'smearing'
     smearing = 'gaussian',
    degauss = 0.01
/

&electrons
    mixing_beta = 0.6
    
/
ATOMIC_SPECIES
Cu 63.546 Cu.upf
 Ni 58.693 Ni.upf
 Pt 195.08 Pt.upf

ATOMIC_POSITIONS {alat}
 Cu 0.0 0.0 0.0
 Ni 0.5 0.5 0.5
 Pt 0.25 0.25 0.25

K_POINTS (automatic) 
 6 6 6 1 1 1    
EOF

pw.x < ${NAME}_${CUTOFF}.in> ${NAME}_${CUTOFF}.out
echo ${NAME}_${CUTOFF}.out
grep ! ${NAME}_${CUTOFF}.out
done

 awk '/kinetic-energy/{ecut=$4}/^!.*total/{print ecut, $5}' *out > etot_v_ecut.dat
