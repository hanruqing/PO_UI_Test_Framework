import os
import yaml

current_path = os.path.dirname(__file__)
yaml_path = os.path.join(current_path, '../element_data_infos/login_element_infos.yml')
yaml_path1 = os.path.join(current_path, '../element_data_infos/myzone_elem_infos.yml')



class ElementdataUtilsYaml:
    def __init__(self, element_path=yaml_path):
        self.element_path = element_path

    def get_element_info_by_yaml(self):
        file = open(self.element_path, 'r', encoding='utf-8')
        cfg = file.read()
        dict_data=yaml.load(cfg,Loader=yaml.FullLoader)
        return dict_data




if __name__ == '__main__':
    elements = ElementdataUtilsYaml().get_element_info_by_yaml()
    print(elements)
    element=elements['username_inputbox']
    print(element)