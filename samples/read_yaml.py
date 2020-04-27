import os
import yaml

current_path=os.path.dirname(__file__)
yaml_path=os.path.join(current_path,'../element_data_infos/login_element_infos.yml')

f=open(yaml_path,'r',encoding='utf-8')
cfg=f.read()
d=yaml.load(cfg)
print(d)
print(type(d))


