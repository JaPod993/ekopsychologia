__author__ = 'jmk'
# -*- encoding: utf-8 -*-
from fabric.api import run, local
from fabric.api import env
from fabric.api import roles
path = '/home/services/python/ekopsychologia2'
venv_path = '/virtuals/ekopsychologia'
env.shell = '/bin/bash -l -c'
sock_path = '/virtuals/ekopsychologia/ekopsychologia.sock'
SETTINGS = 'settings.development'

env.roledefs = {
    'production': ['jmk@delta.silvercube.pl:1923']
}


def host_type():
    run('uname -s')


@roles('production')
def deploy():
    host_type()
    # local('git push')
    gitup()
    run('%s/bin/pip install -r %s/requirements.txt' % (venv_path, path))
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py migrate' % (SETTINGS, venv_path, path))
    # run('SETTINGS=%s %s/bin/python %s/manage.py calculate' % (SETTINGS,venv_path, path))
    reload_app()
    collect_static()

@roles('production')
def quickdeploy():
    host_type()
    # local('git push')
    gitup()
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py migrate' % (SETTINGS, venv_path, path))
    # run('SETTINGS=%s %s/bin/python %s/manage.py calculate' % (SETTINGS,venv_path, path))
    reload_app()
    collect_static()

@roles('production')
def makemigrations():
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py makemigrations' % (SETTINGS, venv_path, path))

@roles('production')
def gitstash():
    run('cd %s; git stash' % path)

@roles('production')
def clean_cache():
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py thumbnail clear' % (SETTINGS, venv_path, path))


@roles('production')
def rebuild_tree():
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py rebuild_tree' % (SETTINGS, venv_path, path))


@roles('production')
def gitup():
    run('cd %s; git pull' % path)


@roles('production')
def reload_app():
    run('source %s/bin/activate' % venv_path)
    run('bash %s/run-sc.sh' % path)

@roles('production')
def pip_install():
    gitup()
    run('%s/bin/pip install -r %s/requirements.txt' % (venv_path, path))


@roles('production')
def collect_static():
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py collectstatic  --noinput' % (SETTINGS, venv_path, path))
    reload_app()

@roles('production')
def clean_cache():
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py thumbnail clear' % (SETTINGS, venv_path, path))

@roles('production')
def quick_test():
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py quick_test' % (SETTINGS, venv_path, path))


@roles('production')
def createsuperuser():
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py createsuperuser' % (SETTINGS, venv_path, path))

@roles('production')
def init_website():
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py init_website' % (SETTINGS, venv_path, path))

@roles('production')
def fixmigrate():
    run('SETTINGS=%s %s/bin/python %s/ekopsychologia/manage.py migrate --fake' % (SETTINGS, venv_path, path))
