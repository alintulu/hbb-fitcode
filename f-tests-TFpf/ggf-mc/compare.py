import os
import numpy as np
import ROOT
import argparse

def GoF(infile, ntoys, seed=123456):

    combine_cmd = "combine -M GoodnessOfFit -m 125 -d "+infile+" -n Toys -t " + str(ntoys) + " --algo saturated --seed " + str(seed)
    os.system(combine_cmd)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='F-test')
    parser.add_argument('-p','--pt',nargs='+',help='pt of baseline')
    parser.add_argument('-r','--rho',nargs='+',help='rho of baseline')
    parser.add_argument('-n','--ntoys',nargs='+',help='number of toys')
    parser.add_argument('-i','--index',nargs='+',help='index for random seed')
    args = parser.parse_args()

    pt = int(args.pt[0])
    rho = int(args.rho[0])
    ntoys = int(args.ntoys[0])
    seed = 123456+int(args.index[0])*100+31
    
    baseline = "pt"+str(pt)+"rho"+str(rho)
    alternatives = []
    pvalues = []

    alternatives += ["pt"+str(pt+1)+"rho"+str(rho)]
    alternatives += ["pt"+str(pt)+"rho"+str(rho+1)]

    for i,alt in enumerate(alternatives):

        pt_alt = int(alt.split("rho")[0].split("pt")[1])
        rho_alt = int(alt.split("rho")[1])
        print(pt_alt, rho_alt)
        
        print(alt)
        thedir = baseline+"_vs_"+alt

        os.mkdir(thedir)
        os.chdir(thedir)

        # Copy what we need
        os.system("cp ../"+baseline+"/output/testModel_*/model_combined.root baseline.root")
        os.system("cp ../"+alt+"/output/testModel_*/model_combined.root alternative.root")

        # run baseline gof
        GoF("baseline.root",ntoys,seed=seed)
        os.system('mv higgsCombineToys.GoodnessOfFit.mH125.'+str(seed)+'.root higgsCombineToys.baseline.GoodnessOfFit.mH125.'+str(seed)+'.root')

        # run alternative gof
        GoF("alternative.root",ntoys,seed=seed)    
        os.system('mv higgsCombineToys.GoodnessOfFit.mH125.'+str(seed)+'.root higgsCombineToys.alternative.GoodnessOfFit.mH125.'+str(seed)+'.root')

        os.chdir('../')

