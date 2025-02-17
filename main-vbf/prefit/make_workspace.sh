year=""

if [[ "$PWD" == *"2016"* ]]; then
    year="_2016"
elif [[ "$PWD" == *"2017"* ]]; then
year="_2017"
elif [[ "$PWD" == *"2018"* ]]; then
    year="_2018"
fi

cd output/testModel${year}/

. build.sh

text2workspace.py model_combined.txt -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=.*/ggF:rggF[1,-9,10]' --PO verbose --PO 'map=.*/VBF:rVBF[1,-9,10]' --PO 'map=.*/Zjetsbb:rZbb[1,-5,6]'

