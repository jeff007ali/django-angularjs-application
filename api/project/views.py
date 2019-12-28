import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .utils import Project, Task, Subtask, UserUtils

# Projects related views
class ProjectsListView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """
    def get(self, request, *args, **kwargs):
        payload = Project().getProjectsList()

        return HttpResponse(json.dumps(payload), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class ProjectDetailView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """
    def get(self, request, *args, **kwargs):

        projectId = kwargs["projectId"]
        payload = Project().getProjectDetail(projectId)

        return HttpResponse(json.dumps(payload), content_type='application/json')
    
    def put(self, request, *args, **kwargs):

        projectId = kwargs["projectId"]
        requestBody = json.loads(request.body)
        payload = Project().updateProject(requestBody, projectId)

        return HttpResponse(json.dumps(payload), content_type='application/json')

    def delete(self, request, *args, **kwargs):

        projectId = kwargs["projectId"]
        payload = Project().deleteProject(projectId)

        return HttpResponse(json.dumps(payload), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class CreateProjectView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """        

    def post(self, request, *args, **kwargs):
        requestBody = json.loads(request.body)
        payload = Project().createProject(requestBody)

        return HttpResponse(json.dumps(payload), content_type='application/json')


#Tasks related views
class TasksListView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """
    def get(self, request, *args, **kwargs):
        projectId = kwargs["projectId"]
        payload = Task().getTasksList(projectId)

        return HttpResponse(json.dumps(payload), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class TaskDetailView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """
    def get(self, request, *args, **kwargs):
        projectId = kwargs["projectId"]
        taskId = kwargs["taskId"]
        payload = Task().getTaskDetail(projectId, taskId)

        return HttpResponse(json.dumps(payload), content_type='application/json')
    
    def put(self, request, *args, **kwargs):
        projectId = kwargs["projectId"]
        taskId = kwargs["taskId"]
        requestBody = json.loads(request.body)
        payload = Task().updateTask(projectId, requestBody, taskId)

        return HttpResponse(json.dumps(payload), content_type='application/json')

    def delete(self, request, *args, **kwargs):
        projectId = kwargs["projectId"]
        taskId = kwargs["taskId"]
        payload = Task().deleteTask(projectId, taskId)

        return HttpResponse(json.dumps(payload), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class CreateTaskView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """        

    def post(self, request, *args, **kwargs):
        projectId = kwargs["projectId"]
        requestBody = json.loads(request.body)
        payload = Task().createTask(projectId, requestBody)

        return HttpResponse(json.dumps(payload), content_type='application/json')


#Subtasks related views
class SubtasksListView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """
    def get(self, request, *args, **kwargs):
        taskId = kwargs["taskId"]
        payload = Subtask().getSubtasksList(taskId)

        return HttpResponse(json.dumps(payload), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class SubtaskDetailView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """
    def get(self, request, *args, **kwargs):
        taskId = kwargs["taskId"]
        subtaskId = kwargs["subtaskId"]
        payload = Subtask().getSubtaskDetail(taskId, subtaskId)

        return HttpResponse(json.dumps(payload), content_type='application/json')
    
    def put(self, request, *args, **kwargs):
        taskId = kwargs["taskId"]
        subtaskId = kwargs["subtaskId"]
        requestBody = json.loads(request.body)
        payload = Subtask().updateSubtask(taskId, requestBody, subtaskId)

        return HttpResponse(json.dumps(payload), content_type='application/json')

    def delete(self, request, *args, **kwargs):
        taskId = kwargs["taskId"]
        subtaskId = kwargs["subtaskId"]
        payload = Subtask().deleteSubtask(taskId, subtaskId)

        return HttpResponse(json.dumps(payload), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class CreateSubtaskView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """        

    def post(self, request, *args, **kwargs):
        taskId = kwargs["taskId"]
        requestBody = json.loads(request.body)
        payload = Subtask().createSubtask(taskId, requestBody)

        return HttpResponse(json.dumps(payload), content_type='application/json')


#Users related view
class UsersListView(View):
    """Get information regrading properties
    Args:
        IntegrationBaseClass (class) -- extend base class
    """        

    def get(self, request, *args, **kwargs):
        payload = UserUtils().getUsersList()

        return HttpResponse(json.dumps(payload), content_type='application/json')
