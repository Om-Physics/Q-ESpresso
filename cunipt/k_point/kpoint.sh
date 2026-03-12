#!/bin/sh
NAME="kpt"
 
for nk in  02 04 06 08 10 
do
cat > ${NAME}_${nk}.in << EOF
 &control
    calculation = 'scf',
    prefix = 'cunipt'
    outdir = './.'
    pseudo_dir = './.'
 /
 &system
    ibrav =  2,
    celldm(1) = 10.89,
    nat =  3,
    ntyp = 3,
    ecutwfc = 60.0
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
 
 K_POINTS automatic 
$nk $nk $nk 1 1 1
EOF
 
pw.x < ${NAME}_${nk}.in > ${NAME}_${nk}.out
echo ${NAME}_${nk}
grep ! ${NAME}_${nk}.out  
done
awk '/number of k points=/{kpt=$5}
     /^!.*total/{print kpt, $5}' *out > etot_v_kp.dat
