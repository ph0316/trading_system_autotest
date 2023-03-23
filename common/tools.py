import datetime
import os.path


def get_now_time():
    return datetime.datetime.now()


def get_project_path():
    # 获取项目绝对路径
    project_name = "trading_system_autotest"
    file_path = os.path.dirname(__file__)
    # print(file_path)
    # print(file_path.find(project_name))
    # print(file_path[:file_path.find(project_name) + len(project_name)])
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    all_path = os.sep.join(path)
    # print(all_path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    # print(all_path)
    return all_path


if __name__ == '__main__':
    print(get_now_time())
    print(get_project_path())
    sep(["config", "environment.yml"], add_sep_before=True, add_sep_after=True)
