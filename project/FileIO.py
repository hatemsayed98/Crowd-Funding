from Project import Project
import os


class FileIO:
    @staticmethod
    def create_dir():
        path = "projects"
        is_exist = os.path.exists(path)
        if not is_exist:
            os.makedirs(path)

    @staticmethod
    def save_projects(projects, email):
        FileIO.create_dir()
        filepath = f"projects/{email}_projects.txt"
        if len(projects) > 0:
            with open(filepath, 'w') as file:
                for p in projects:
                    file.write(f"{p.email};{p.title};{p.details};"
                               f"{p.target};{p.end_date};{p.start_date}\n")
        else:
            file = open(filepath, 'w')
            file.close()

    @staticmethod
    def load_projects(email):
        projects = []
        try:
            filepath = f"projects/{email}_projects.txt"
            file = open(filepath, 'r')
            file_parse = file.read()
            file.close()
            for line in file_parse.split("\n"):
                if line:
                    split = line.split(';')
                    usr = Project(email=split[0], title=split[1],
                                  details=split[2], target=split[3], end_date=split[4], start_date=split[5])
                    projects.append(usr)
        except Exception as e:
            pass

        return projects

    @staticmethod
    def getAllProjects():
        path = "projects"
        FileIO.create_dir()
        dir_list = os.listdir(path)
        all_projects = []
        for file in dir_list:
            filepath = f"projects/{file}"
            file = open(filepath, 'r')
            file_parse = file.read()
            file.close()
            for line in file_parse.split("\n"):
                if line:
                    split = line.split(';')
                    proj = Project(email=split[0], title=split[1],
                                   details=split[2], target=split[3], end_date=split[4], start_date=split[5])
                    all_projects.append(proj)
        return all_projects
