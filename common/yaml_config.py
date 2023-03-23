# file = open("../config/environment.yaml", encoding="utf-8")
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()

# with open("../config/environment.yaml", "r", encoding="utf-8") as file:
#     # a = file.read()
#     for i in file.readlines():
#         print("===========")
#         print(i)
# ceshi

import yaml
from common.tools import get_project_path, sep


class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_username_password(self):
        return self.env["username"], self.env["password"]


if __name__ == '__main__':
    print(GetConf().get_username_password())
