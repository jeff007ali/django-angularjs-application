from .models import *
from django.contrib.auth.models import User

class Project:
    def getProjectsList(self):
        result = {}
        projList = Projects.objects.all()
        tempList = []
        if not projList:
            return {"message":"No projects found!", "code": 404}

        for proj in projList:
            tempDict = proj.__dict__
            del tempDict['_state']
            tempDict['id'] = str(tempDict['id'])
            tempList.append(tempDict)

        result["Projects"] = tempList

        return result

    def getProjectDetail(self, projectId):
        proj = Projects.objects.filter(id=projectId).first()

        if not proj:
            return {"message":"project not found!", "code": 404}

        result = proj.__dict__
        del result['_state']
        result['id'] = str(result['id'])

        return result

    def createProject(self, requestBody):
        name = requestBody.get('name', '')
        description = requestBody.get('description', '')
        duration = int(requestBody.get('duration', '0'))
        avatar = requestBody.get('avatar', '')

        project = Projects(name=name, description= description, duration=duration, avatar=avatar)
        project.save()

        return {"message": 'Project created successfully', "code": 201}

    def updateProject(self, requestBody, projectId):
        name = requestBody.get('name', '')
        description = requestBody.get('description', '')
        duration = int(requestBody.get('duration', '0'))
        avatar = requestBody.get('avatar', '')

        project = Projects.objects.filter(id=projectId)
        if not project:
            return {"message":"Project not found!", "code": 404}

        result = project.update(name=name, description= description, duration=duration, avatar=avatar)
        if result:
            return {"message": 'Project updated successfully', "code": 200}
        return {"message": 'Project not updated successfully', "code": 500}

    def deleteProject(self, projectId):
        x = Projects.objects.filter(id=projectId).delete()
        print(x)

        return {"message": 'Project deleted successfully', "code": 200}


class Task:
    def getTasksList(self, projectId):
        result = {}
        taskList = Tasks.objects.filter(project_id=projectId)
        tempList = []
        if not taskList:
            return {"message":"No tasks found!", "code": 404}

        for task in taskList:
            tempDict = task.__dict__
            del tempDict['_state']
            tempDict['project_id'] = str(tempDict['project_id'])
            tempDict['id'] = str(tempDict['id'])
            tempList.append(tempDict)

        result["Tasks"] = tempList

        return result

    def getTaskDetail(self, projectId, taskId):
        task = Tasks.objects.filter(id=taskId).first()

        if not task:
            return {"message": 'Task not found', "code": 404}

        result = task.__dict__
        del result['_state']
        result['project_id'] = str(result['project_id'])
        result['id'] = str(result['id'])

        return result

    def createTask(self, projectId, requestBody):
        name = requestBody.get('name', '')
        description = requestBody.get('description', '')
        startDate = int(requestBody.get('startDate', '0'))
        endDate = int(requestBody.get('endDate', '0'))
        assignee_id = requestBody.get('assignee_id', '')
        assignee = User.objects.filter(id=assignee_id).first() if assignee_id else None
        project = Projects.objects.filter(id=projectId).first()
        if not project:
            return {"message":"Project not found!", "code": 404}

        task = Tasks(name=name, description= description, startDate=startDate, endDate=endDate, project=project, assignee=assignee)
        task.save()

        return {"message": 'Task created successfully', "code": 201}

    def updateTask(self, projectId, requestBody, taskId):
        name = requestBody.get('name', '')
        description = requestBody.get('description', '')
        startDate = int(requestBody.get('startDate', '0'))
        endDate = int(requestBody.get('endDate', '0'))
        assignee_id = requestBody.get('assignee_id', '')
        assignee = User.objects.filter(id=assignee_id).first() if assignee_id else None
        project = Projects.objects.filter(id=projectId).first()
        if not project:
            return {"message":"Project not found!", "code": 404}

        task = Tasks.objects.filter(id=taskId)
        if not task:
            return {"message":"Task not found!", "code": 404}

        result = task.update(name=name, description= description, startDate=startDate, endDate=endDate, project=project, assignee=assignee)
        if result:
            return {"message": 'Task updated successfully', "code": 200}
        return {"message": 'Task not updated successfully', "code": 500}

    def deleteTask(self, projectId, taskId):
        x = Tasks.objects.filter(id=taskId).delete()
        print(x)

        return {"message": 'Task deleted successfully', "code": 200}


class Subtask:
    def getSubtasksList(self, taskId):
        result = {}
        subtaskList = Subtasks.objects.filter(task_id=taskId)
        tempList = []
        if not subtaskList:
            return {"message":"No subtasks found!", "code": 404}

        for subtask in subtaskList:
            tempDict = subtask.__dict__
            del tempDict['_state']
            tempDict['task_id'] = str(tempDict['task_id'])
            tempDict['id'] = str(tempDict['id'])
            tempList.append(tempDict)

        result["Subtasks"] = tempList

        return result

    def getSubtaskDetail(self, taskId, subtaskId):
        subtask = Subtasks.objects.filter(id=subtaskId).first()

        if not subtask:
            return {"message": 'Subtask not found', "code": 404}

        result = subtask.__dict__
        del result['_state']
        result['task_id'] = str(result['task_id'])
        result['id'] = str(result['id'])

        return result

    def createSubtask(self, taskId, requestBody):
        name = requestBody.get('name', '')
        description = requestBody.get('description', '')
        startDate = int(requestBody.get('startDate', '0'))
        endDate = int(requestBody.get('endDate', '0'))
        task = Tasks.objects.filter(id=taskId).first()
        if not task:
            return {"message":"Task not found!", "code": 404}

        subtask = Subtasks(name=name, description= description, startDate=startDate, endDate=endDate, task=task)
        subtask.save()

        return {"message": 'Subtask created successfully', "code": 201}

    def updateSubtask(self, taskId, requestBody, subtaskId):
        name = requestBody.get('name', '')
        description = requestBody.get('description', '')
        startDate = int(requestBody.get('startDate', '0'))
        endDate = int(requestBody.get('endDate', '0'))
        task = Tasks.objects.filter(id=taskId).first()
        if not task:
            return {"message":"Task not found!", "code": 404}

        subtask = Subtasks.objects.filter(id=subtaskId)
        if not subtask:
            return {"message":"Subtask not found!", "code": 404}

        result = subtask.update(name=name, description= description, startDate=startDate, endDate=endDate, task=task)
        if result:
            return {"message": 'Subtask updated successfully', "code": 200}
        return {"message": 'Subtask not updated successfully', "code": 500}

    def deleteSubtask(self, taskId, subtaskId):
        x = Subtasks.objects.filter(id=subtaskId).delete()
        print(x)

        return {"message": 'Subtask deleted successfully', "code": 200}


class UserUtils:
    def getUsersList(self):
        result = {}
        userList = User.objects.all()
        tempList = []
        if not userList:
            return {"message":"No users found!", "code": 404}

        for user in userList:
            tempDict = {}
            tempDict['id'] = user.id
            tempDict['username'] = user.username
            tempList.append(tempDict)

        result["Users"] = tempList

        return result
