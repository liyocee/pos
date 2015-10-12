"""
    Fab Tasks for deployment.
    Delegates to ansible for doing actual deployment
"""
import os
from fabric.api import local, lcd
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def rm_frontend_folder(folder):
    try:
        local("rm {}".format(folder))
    except:
        pass


def deploy_frontend():
    zip_folder = "frontend.zip"
    with lcd(os.path.join(BASE_DIR, "ui")):
        rm_frontend_folder(zip_folder)
        local("grunt build")
        local("grunt compile")
        local("zip -r {} bin".format(zip_folder))

    with lcd(os.path.join(BASE_DIR, "deployment/playbooks")):
        tags = "--tags 'beyonic_frontend'"
        tags = ''
        task = " --start-at-task 'remove any existing installations' "
        local(
            "ansible-playbook -vv -s {} {} {}".format(
                'ui_servers.yml', tags, task))

    with lcd(os.path.join(BASE_DIR, "ui")):
        rm_frontend_folder(zip_folder)


def deploy_backend():
    with lcd(os.path.join(BASE_DIR, "deployment/playbooks")):
        # tags = '--tags django.docs_user'
        tags = ''
        task = "--start-at-task 'Run Background tasks'"
        task = ''
        local(
            "ansible-playbook -vv -s {}  {} {}".format(
                'webservers.yml', tags, task))


def deploy():
    deploy_frontend()
    deploy_backend()
