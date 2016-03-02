@task
def collectstatic(*args):
	cmd = 'bower install'
	local(cmd)

