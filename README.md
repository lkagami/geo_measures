# G_measures

The "Geometric Measures" script that was developed to carry out geometric analysis on protein structures.
This script support as input MultiPDB files, and the avaliable analysis are: 
    
    1 - Pincer angle.
                            
    Select the residues that will be used to measure the pincer angle. 
    

                (1)                 (3)
                    \              /
                      \          /
                        \      /
                          \  / 
                          (2)
    
    2 - Dihedral angle.

    Select the residues that will be used to measure the dihedral angle. 
    

                     (1)          (4)
                       |           |
                       |           |
                       |           |
                       |           |
                     (2)----------(3)
        
    3 - Triangle area.

    Select the residues that will be used to measure the triangle area. 
   

                          AC
                  (1)-----------(3)
                    \           /
            AB        \        /     BC
                       \      /
                         \  / 
                          (2)
                            
                           


    4 - PDF (Probability Density Function)
    The Functional Density Function is calculated using different values ​​of mainchain dihedral angles from the considered residue, the mainchain conformation of the equivalent residue between frames.
    
    5 - RMSD

    Compares two protein structures frames (first frame the first frame with the consecutive frames) by computing the root mean square deviation (RMSD).

    6 - RG

    Computes the radius of gyration of the protein and the radii of gyration about the x-, y- and z-axes, as a function of frames.

    7 - FEL
    FEL represents a mapping of all possible conformations a molecule adopted during a simulation, together with their corresponding energy reported as the Gibbs Free Energy. FEL are represented using two variables that reflect specific properties of the system and measure conformational variability. RG measure the torsion angle around a specific bond or the radius of gyration of the protein, and the the RMSD measure the deviation with respective native state (First frame).

Contributors:

Luciano Porto Kagami, Gustavo Machado das Neves, Luís Fernando Saraiva Macedo Timmers, Rafael Andrade Cáceres and Vera Lucia Eifler-Lima

The GROMACS program (http://www.gromacs.org/) is required for the 'Converter' and 'FEL' tools.
The only recognized trajectory file format for G_Measures is multi-PDB.
If the user has only XTC trajectory files, the 'Converter' tool can be used.
Click Browse ..., select the multi-PDB file and follow the steps shown in the status bar.

Thank you for using G_Measures!
G_Measures Team

