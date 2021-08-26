from .tools import CeleryTask

#########################################
# celelry application : dont change or delete

celery_app = CeleryTask('Task-Scheduler')

#########################################


##### define proxy tasks for you tasks below #######


@celery_app.add_task(plug_to='schedule-tasks-from-DB')
# @celery_app.block_exc
def proxy_task1(*arg, **kw):
    from flaskapp.core.ivr_core import profile_detail
    profile_detail()