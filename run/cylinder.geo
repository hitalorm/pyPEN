
A solid cylinder. Note that we need two limiting planes.

0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   1)   Plane Z=0.00
INDICES=( 0, 0, 0, 1, 0)
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   2)   Plane Z=2.00
INDICES=( 0, 0, 0, 1, 0)
Z-SHIFT=(+1.000000000000000E+00,   0)
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   3)   Cylinder R=10.00 cm
INDICES=( 1, 1, 0, 0,-1)
X-SCALE=(+1.000000000000000E+01,   0)
Y-SCALE=(+1.000000000000000E+01,   0)
0000000000000000000000000000000000000000000000000000000000000000
MODULE  (   1)   Solid cylinder
MATERIAL(   1)
SURFACE (   1), SIDE POINTER=(+1)
SURFACE (   2), SIDE POINTER=(-1)
SURFACE (   3), SIDE POINTER=(-1)
0000000000000000000000000000000000000000000000000000000000000000
END      0000000000000000000000000000000000000000000000000000000