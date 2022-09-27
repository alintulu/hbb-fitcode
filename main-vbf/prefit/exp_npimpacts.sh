#!/bin/bash                                                                                                                                   

# Arguments
year=""
if [[ "$PWD" == *"2016APV"* ]]; then
    year="_2016APV"
elif [[ "$PWD" == *"2016"* ]]; then
    year="_2016"
elif [[ "$PWD" == *"2017"* ]]; then
    year="_2017"
elif [[ "$PWD" == *"2018"* ]]; then
    year="_2018"
fi

modelfile=output/testModel${year}/model_combined.root

# Do initial fit
combineTool.py -M Impacts -d $modelfile -m 125 --robustFit 1 --doInitialFit --setParameters rZbb=1,rVBF=1,rggF=1 --cminDefaultMinimizerStrategy 0 -t -1

combineTool.py -M Impacts -d $modelfile -m 125 --robustFit 1 --doFits --setParameters rZbb=1,rVBF=1,rggF=1 --job-mode condor --sub-opts='+JobFlavour="nextweek"' --exclude 'rgx{qcdparams*}' --cminDefaultMinimizerStrategy 0 -t -1
