#!/usr/bin/python
import os, sys
import subprocess
import argparse

# Main method                                                                          
def main():

    year = "postfit"
    yearstr = ""
    thisdir = os.getcwd()
    if "2016" in thisdir:
        year = "2016-postfit"
        yearstr = "_2016"
    elif "2017" in thisdir:
        year = "2017-postfit"
        yearstr = "_2017"
    elif "2018" in thisdir:
        year = "2018-postfit"
        yearstr = "_2018"

    print("Submitting for year " + year)

    loc_base = os.environ['PWD']
    logdir = 'logs'
    locdir = logdir
    os.system('mkdir -p  %s' %locdir)

    outdir = '/store/user/jennetd/fits/'+year+'/'
    os.system('mkdir -p /eos/uscms'+outdir)

    for tag in ['exp_npimpacts']: #contour68','exp_contour95','exp_significance','exp_shapes','exp_mu_zbb','exp_mu_vbf','exp_mu_ggf']:
        
        print('Submitting '+tag)

        condorfilename = "fit.templ.condor"
        if "npimpacts" in tag:
            condorfilename = "parallelfit.templ.condor"

        condor_templ_file = open(condorfilename)
        localcondor = locdir+'/'+tag+".condor"
        condor_file = open(localcondor,"w")
        for line in condor_templ_file:
            line=line.replace('YEAR',yearstr)
            line=line.replace('TAG',tag)
            condor_file.write(line)
        condor_file.close()

        if "shapes" in tag or "contour" in tag or "exp_mu" in tag:
            sh_templ_file    = open(tag+".sh")
            localsh = locdir+'/'+tag+'.sh'
            sh_file = open(localsh,"w")
            for line in sh_templ_file:
                line=line.replace('EOSDIR',outdir)
                sh_file.write(line)
            sh_file.close()
        else:
            os.system("cp "+tag+".sh "+locdir)

        if (os.path.exists('%s.log'  % localcondor)):
            os.system('rm %s.log' % localcondor)
        os.system('condor_submit %s' % localcondor)

    return 

if __name__ == "__main__":
    main()
