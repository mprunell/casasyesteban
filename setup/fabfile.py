from fabric.api import env, settings, local, put, cd, sudo, run
from fabric.contrib.files import exists

env.user = 'root'


def new_user(username, password):
    group = 'cye'
    put('cye_pass', '/tmp')
    with settings(warn_only=True):
        output = sudo('getent group {group}'.format(group=group))
        if output.return_code != 0:
            sudo('addgroup {group}'.format(group=group))
        output = sudo('useradd -g users -G {group} -d /home/{username} -m {username}'.format(username=username, group=group))
        sudo('chpasswd < /tmp/cye_pass')
        sudo('rm /tmp/cye_pass')        


def configure_supervisor():
    sudo('apt-get install supervisor')
    put('casasyesteban_site.conf', '/etc/supervisor/conf.d')
    sudo('supervisorctl reread')
    sudo('supervisorctl update')
    

def configure_nginx():
    sudo('apt-get install nginx')
    put('casasyesteban_site_nginx.conf', '/etc/nginx/conf.d/casasyesteban_site.conf')
    sudo('service nginx start')


def configure_uwsgi():
    sudo('apt-get install build-essential python')
    sudo('apt-get install python-dev')
    sudo('pip install uwsgi')


def provision():
    sudo('apt-get update && apt-get upgrade')
    sudo('apt-get install python-virtualenv')
    if not exists('/home/cye', use_sudo=True):
        new_user('cye', 'cye')
    with settings(user='cye'):
        if not exists('/home/cye/.ssh'):
            run('ssh-keygen -t rsa -C "webmaster@casasyesteban.com"')
    put('requirements.txt', '/home/cye')
    with settings(user='cye'):
        path = '/home/cye/webapp'
        if not exists(path, use_sudo=False):
            run('mkdir ' + path)
            path = '/home/cye/venv'
            if not exists(path, use_sudo=False):
                run('mkdir ' + path)
            path = '/home/cye/venv/bin'
            if not exists(path, use_sudo=False):
                run('virtualenv /home/cye/venv')
        run('source /home/cye/venv/bin/activate')
        run('/home/cye/venv/bin/pip install -r requirements.txt')
        with cd('/home/cye/webapp'):
            if not exists('casasyesteban'):
                run('git clone https://github.com/mprunell/casasyesteban.git')
    path = '/home/cye/webapp/log'
    if not exists(path):
        with settings(user='cye'):
            run('mkdir ' + path)
    configure_uwsgi()
    configure_supervisor()
    configure_nginx()
    deploy()


def deploy():
        with cd('/home/cye/webapp/casasyesteban/app'):
            with settings(user='cye'):
                run('git pull origin master') 
                run('/home/cye/venv/bin/python manage.py collectstatic --noinput')
                run('/home/cye/venv/bin/python manage.py syncdb')
                run('/home/cye/venv/bin/python manage.py migrate')
            
        sudo('supervisorctl restart casasyesteban_site')
            
            