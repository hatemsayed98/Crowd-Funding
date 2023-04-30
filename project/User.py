from FileIO import FileIO


class User:
    def __init__(self, fname, lname, email, password, phone):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.phone = phone
        self.projects = []

    def get_my_projects(self):
        self.projects = FileIO.load_projects(self.email)
        return self.projects

    @staticmethod
    def get_all_projects():
        return FileIO.getAllProjects()

    def add_project(self, myproject):
        for p in self.projects:
            if p.title == myproject.title:
                raise Exception("Project Already exists!")
        self.projects.append(myproject)
        FileIO.save_projects(self.projects, self.email)

    def edit_project(self, oldTitle, project):# old => iti   project.title =>>> alx
        for p in self.projects:
            if p.title == oldTitle:
                self.projects.remove(p)
                self.projects.append(project)
                break
        FileIO.save_projects(self.projects, self.email)

    def delete_project(self, ptitle):
        for p in self.projects:
            if p.title == ptitle:
                self.projects.remove(p)
                FileIO.save_projects(self.projects, self.email)
                break

    @staticmethod
    def fund_project(project):
        projects = FileIO.load_projects(project.email)
        for p in projects:
            if p.email == project.email:
                p.target = project.target
        FileIO.save_projects(projects, project.email)
