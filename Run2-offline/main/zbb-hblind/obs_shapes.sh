year="_2018"

combine -M FitDiagnostics -m 125 output/testModel${year}/model_combined.root --saveShapes --saveWithUncertainties --robustFit=1 --robustHesse=1 --cminDefaultMinimizerStrategy=0 --setParameters rZbb=1,rggF=1 --freezeParameters rggF --verbose 9

