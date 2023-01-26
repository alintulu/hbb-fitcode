# Arguments
year="_2018"
poi="rZbb"
frozen="rgx{CMS_.*},rgx{QCDscale_.*},rgx{UEPS_.*},rgx{pdf_.*},rgx{.*mcstat},rgx{qcd.*}"

npoints=100

combine -M MultiDimFit -m 125 output/testModel${year}/model_combined.root --setParameters rggF=1,rZbb=1 --cminDefaultMinimizerStrategy 0 --algo grid --points ${npoints} --redefineSignalPOI ${poi} --saveWorkspace -n ${poi} --freezeParameters rggF

combine -M MultiDimFit -m 125 --setParameters rggF=1,rZbb=1 --cminDefaultMinimizerStrategy 0 --algo grid --points ${npoints} --redefineSignalPOI ${poi} --saveWorkspace -n ${poi}StatOnly -d higgsCombine${poi}.MultiDimFit.mH125.root -w w --snapshotName "MultiDimFit" --freezeParameters rggF,${frozen}
