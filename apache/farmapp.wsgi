import os
import sys
import site
import time, signal
sys.stdout = sys.stderr

new_path = '/var/www/farmapp/farmenv/lib/python3.4/site-packages'

prev_sys_path = list(sys.path)
# add the site-packages of our virtualenv as a site dir
site.addsitedir(new_path)
# add the app's directory to the PYTHONPATH
sys.path.append('/var/www/farmapp/farmapp')
sys.path.append('/var/www/farmapp')

# reorder sys.path so new directories from the addsitedir show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path


os.environ['DJANGO_SETTINGS_MODULE'] = 'farmapp.settings'

from django.core.wsgi import get_wsgi_application


try:
    application = get_wsgi_application()
except Exception:
    time.sleep(0.25)
    os.kill(os.getpid(), signal.SIGINT)
application = get_wsgi_application()
