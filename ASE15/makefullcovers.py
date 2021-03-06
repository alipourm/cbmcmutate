import sys
import glob

mutant_base = sys.argv[1]
maxcov = sys.argv[2]

for infile in glob.glob("mutant*_" + mutant_base):

    outfile = "FULLCOV_" + infile

    outf = open(outfile,'w')

    outf.write ("int mutant_covered = 0;\n\n")
    outf.write ("int total_covered = 0;\n\n")
    outf.write ("int covered[" + maxcov + "];\n\n")

    cnum = 0
    
    for l in open(infile):
        if "/*" in l:
            inComment = True
        if not inComment:
            if "MUTANT" in l:
                sp = "";
                for c in l:
                    if c == " ":
                        sp += " "
                    else:
                        break
                outf.write(sp + "mutant_covered = 1;\n")
            inCode = ((l[0] == " " or l[0] == "\t") and not (l.split()[0] == "else"))
            if inCode:
                sp = "";
                for c in l:
                    if c == " ":
                        sp += " "
                    elif c == "\t":
                        sp += "\t"
                    else:
                        break            
                outf.write(sp + "__CPROVER_atomic_begin(); if (!covered[" + str(cnum) + "]) {covered[" + str(cnum) + "] = 1; total_covered += 1;} __CPROVER_atomic_end(); \n")
                cnum += 1
        if "*/" in l:
            inComment = False
        outf.write(l)

    outf.close()
