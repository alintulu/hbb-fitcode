import os
import numpy as np
import json

if __name__ == '__main__':

    year = "2016"
    thisdir = os.getcwd()
    if "2016APV" in thisdir:
        year = "2016APV"
    elif "2017" in thisdir:
        year = "2017"
    elif "2018" in thisdir:
        year = "2018"

    for pt in range(0,1):
        for rho in range(0,3):
            print("pt = "+str(pt)+", rho = "+str(rho))
            # Make the directory and go there
            thedir = "pt"+str(pt)+"rho"+str(rho)
            if not os.path.isdir(thedir):
                os.mkdir(thedir)
                os.chdir(thedir)

            # Link what you need
            os.system("mkdir plots")
            os.system("ln -s ../../../../../main-vbf/zbb-hblind/"+year+"-zbb/signalregion.root .")
            os.system("ln -s ../../../../../main-vbf/zbb-hblind/"+year+"-zbb/muonCR.root .")
            os.system("cp ../../../../../main-vbf/zbb-hblind/"+year+"-zbb/initial_vals_ggf.json .")
            os.system("cp ../../../../../main-vbf/zbb-hblind/"+year+"-zbb/initial_vals_vbf.json .")
            os.system("ln -s ../../../../../main-vbf/lumi.json .")
            os.system("ln -s ../../../../../main-vbf/sf.json .")
            os.system("ln -s ../../make_cards.py .")
            os.system("ln -s ../../make_workspace.sh .")

            # Create your json files of initial values
            if not os.path.isfile("initial_vals_data_ggf.json"):

                initial_vals = (np.full((pt+1,rho+1),1)).tolist()
                thedict = {}
                thedict["initial_vals"] = initial_vals
                        
                with open("initial_vals_data_ggf.json", "w") as outfile:
                    json.dump(thedict,outfile)

            # Create your json files of initial values                                                                           
            if not os.path.isfile("initial_vals_data_vbf.json"):
                initial_vals = (np.full((pt+1,rho+1),1)).tolist()
                thedict = {}
                thedict["initial_vals"] = initial_vals

                with open("initial_vals_data_vbf.json", "w") as outfile:
                    json.dump(thedict,outfile)

            # Make the workspace
            os.system("./make_workspace.sh")

            # Run the first fit
            combine_cmd = "combineTool.py -M MultiDimFit -m 125 -d output/testModel_"+year+"/model_combined.root --saveWorkspace \
            -P rZbb --floatOtherPOIs=0 -n \"Snapshot\" \
            --robustFit=1 --cminDefaultMinimizerStrategy=0 \
            --setParameters rZbb=1 "
            os.system(combine_cmd)

            # Run the goodness of fit
            combine_cmd = "combineTool.py -M GoodnessOfFit -m 125 -d higgsCombineSnapshot.MultiDimFit.mH125.root \
            -n \"Observed\" --snapshotName MultiDimFit --bypassFrequentistFit --algo \"saturated\" \
            --setParameters rZbb=1 "
            os.system(combine_cmd)
                
            os.chdir("../")
