# Arguments
year="2018"

echo "Zjetsbb SIGNIFICANCE"
combine -M Significance -m 125 --signif output/testModel_${year}/model_combined.root --redefineSignalPOI rZbb  --verbose 9 --setParameters rZbb=1
#combine -M Significance -m 125 --signif output/testModel_${year}/model_combined.root --redefineSignalPOI rZbb  --verbose 9 --setParameters rZbb=1,rggF=1 --freezeParameters rggF

