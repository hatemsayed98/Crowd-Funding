from Project import Project
from User import User
from Authentication import Authentication
from datetime import date


def inputProject(msg):
    d, m, y = [int(x) for x in input(msg).split('/')]
    b = date(y, m, d)
    return b


if __name__ == '__main__':

    # Login with the auth class
    auth = None
    while auth is None:
        choice = str(input("1- Register\n2- Login\n3- Exit\n"))
        if choice == '3':
            break
        if choice == '1':
            print(Authentication.register())
            continue

        if choice == '2':
            email = input("Enter Your email: ")
            password = input("Enter Your password: ")
            try:
                auth = Authentication.login(email, password)
                print(auth.__dict__)
                print(f"Hello {auth.fname}")

            except Exception as e:
                print(e)
                auth = None
                continue
            # Logged in user action
            user_choice = '0'
            while user_choice != '6':
                user_choice = str(input("1- Create a project\n2- View my projects\n3- View all projects\n"
                                        "4- Edit your project\n5- Delete your project\n6- Logout\n"))
                # Add project
                if user_choice == '1':

                    title = input("Enter title: ")
                    while len(title) < 1 or not title.isalpha():
                        title = input("Enter title: ")
                    target = input("Enter target: ")
                    while len(target) < 1 or not target.isdigit():
                        target = input("Enter target: ")

                    details = input("Enter details: ")
                    start_date, end_date = '', ''
                    while True:
                        try:
                            start_date = inputProject("Enter start date person's date(DD/MM/YYYY) : ")
                            end_date = inputProject("Enter End date person's date(DD/MM/YYYY) : ")
                            if start_date >= end_date:
                                raise Exception("End date must be before start date")
                            break
                        except Exception as e:
                            print(e)
                            continue

                    project = Project(email=auth.email, title=title, target=target, details=details,
                                      start_date=start_date, end_date=end_date)
                    try:
                        auth.add_project(project)
                    except Exception as e:
                        print(e)
                # Show my projects
                if user_choice == '2':
                    projects = auth.get_my_projects()
                    for p in projects:
                        print(p)
                # Show all projects in Crowd Fund
                if user_choice == '3':
                    projects = User.get_all_projects()
                    for p in projects:
                        print(p)
                # Edit my project
                if user_choice == '4':
                    projects = auth.get_my_projects()
                    if len(projects) < 1:
                        print('No projects to edit!\n')
                        continue

                    while True:
                        for i in range(0, len(projects)):
                            print(f"{i + 1}{projects[i]}")
                        try:
                            projectIndex = int(input(f'0- Exit\nChoose projects 1 : {len(projects)}  '))
                            if projectIndex == 0:
                                break
                            projectIndex -= 1
                            if projectIndex in range(0, len(projects)):

                                print(f"{projectIndex + 1}{projects[projectIndex]}")
                                old_project = projects[projectIndex]

                                title = input(f"Title {old_project.title} : ")
                                while len(title) < 1 or not title.isalpha():
                                    title = input(f"Title {old_project.title} : ")
                                target = input(f"Target {old_project.target} : ")
                                while len(target) < 1 or not target.isdigit():
                                    target = input(f"Target {old_project.target} : ")

                                details = input(f"Details {old_project.details} : ")
                                start_date, end_date = '', ''
                                while True:
                                    try:
                                        start_date = inputProject(f"Start date {old_project.start_date} start date "
                                                                  f"date(DD/MM/YYYY):")
                                        end_date = inputProject(f"End date {old_project.end_date} End date "
                                                                f"date(DD/MM/YYYY):")
                                        if start_date >= end_date:
                                            raise Exception("End date must be before start date")
                                        break
                                    except Exception as e:
                                        print(e)
                                        continue

                                project = Project(email=auth.email, title=title, target=target, details=details,
                                                  start_date=start_date, end_date=end_date)
                                auth.edit_project(old_project.title, project)

                                break
                        except Exception as e:
                            print(e)
                            continue
                # Delete a project
                if user_choice == '5':
                    projects = auth.get_my_projects()
                    if len(projects) < 1:
                        print('No projects to delete!\n')
                        continue
                    deleted = False
                    while not deleted:
                        for i in range(0, len(projects)):
                            print(f"{i + 1}{projects[i]}")
                        try:
                            projectIndex = int(input(f'0- Exit\nChoose projects 1 : {len(projects)}  '))
                            if projectIndex == 0:
                                deleted = True

                            projectIndex -= 1
                            if projectIndex in range(0, len(projects)):
                                old_project = projects[projectIndex]
                                auth.delete_project(old_project.title)
                                deleted = True

                        except Exception as e:
                            print(e)
                            continue

                if user_choice == '6':
                    auth = None
                    continue
                else:
                    continue
        else:
            continue
