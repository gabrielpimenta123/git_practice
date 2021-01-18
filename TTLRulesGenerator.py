import json
import numpy as np

# !!! interessante produzir uma forma de criar estes vetores automaticamente !!! (boto3?)

rule_id = ["bra_jec_fl_fn/influxdb/", "bra_bhz_la_qt/influxdb/", "bra_jec_ac_sp_qa/influxdb/", "bra_jec_qt/influxdb/", "bra_jec_rm_qa/influxdb/", "bra_jec_rm_therma/influxdb/", "bra_jec_rm/influxdb/", "test_aws/influxdb/"]
prefix = ["raw/shalyn-backup/bra_jec_fl_fn/influxdb/", "raw/shalyn-backup/bra_bhz_la_qt/influxdb/", "raw/shalyn-backup/bra_jec_ac_sp_qa/influxdb/", "raw/shalyn-backup/bra_jec_qt/influxdb/", "raw/shalyn-backup/bra_jec_rm_qa/influxdb/", "raw/shalyn-backup/bra_jec_rm_therma/influxdb/", "raw/shalyn-backup/bra_jec_rm/influxdb/", "raw/shalyn-backup/test_aws/influxdb/"]
template_file = ["bra_jec_fl_fn-influxdb.json", "bra_bhz_la_qt-influxdb.json", "bra_jec_ac_sp_qa-influxdb.json", "bra_jec_qt-influxdb.json", "bra_jec_rm_qa-influxdb.json", "bra_jec_rm_therma-influxdb.json", "bra_jec_rm-influxdb.json", "test_aws-influxdb.json"]

for x in range (np.shape(rule_id)[0]): 
    with open("/media/sf_Pasta_Compartilhada/template.json", 'r') as fp: #abrindo o arquivo na variável fp
        template = json.loads(fp.read()) #lendo o arquivo no type dict (json.loads)
    template['Rules'][0]['ID'] = rule_id[x]#alterando valores de ID em formato dict 
    template['Rules'][0]['Filter']['And']['Prefix'] = prefix[x]
    target_file = template_file[x]
    adr='/media/sf_Pasta_Compartilhada/'+str(target_file)
    with open(adr, 'w') as fp: 
        fp.write(json.dumps(template)) #lendo template em dict para string, lendo a string para arquivo .json 


























'''
#utilizando string type str (f.read somente)
#for x in pathid: 

f = open("/media/sf_Pasta_Compartilhada/template.json", "r") #loop com tamanho path.lenght que executa o .replace dos termos pathid e path e gera arquivos com nomes(x)
aux = f.read() #estava antes aux.json.load(f) 
f.close()
aux=aux.replace("pathid","abobora")
print(aux)   

            
#depois tenho que gerar o arquivo 

        
f.replace("path",path(x))
print (f.read())
f.close()
'''

