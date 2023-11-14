from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Projects.models import Project
from U_Auth.models import User
from django.contrib import messages

# Create your views here.

#----------------------------------- MANAGE PROJECTS -----------------------------------#

@login_required
def projects(request):
    if request.user.is_superuser:
        projects = Project.objects.all().order_by('-id')
    elif request.user.Job_Role == 'Department Manager':
        projects = Project.objects.filter(Department_Managers__in=[request.user])
    elif request.user.Job_Role == 'Project Engineer':
        projects = Project.objects.filter(Project_Engineers__in=[request.user])
    elif request.user.Job_Role == 'Purchase Manager':
        projects = Project.objects.filter(Purchase_Managers__in=[request.user])

    context = {
        'projects' : projects
    }
    return render(request,'Dashboard/Projects/projects.html',context)

#----------------------------------- CREATE PROJECT -----------------------------------#

@login_required
def create_project(request):
    last_project = Project.objects.last()
    department_managers = User.objects.filter(Job_Role='Department Manager')

    if last_project:
        reference = f'PROJECT-00{last_project.id+1}'
    else:
        reference = f'PROJECT-001'
    
    ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        descriprion = request.POST.get('description')

        client_name = request.POST.get('client_name')
        client_mobile = request.POST.get('client_mobile')
        client_email = request.POST.get('client_email')
        client_address = request.POST.get('client_address')
        contact_name = request.POST.get('contact_name')
        contact_mobile = request.POST.get('contact_mobile')
        department_managers = request.POST.getlist('department_managers')
        expected_date = request.POST.get('expected_date') or None
        expected_amount = request.POST.get('expected_amount') or None

        try:
            project = Project.objects.create(Added_By=request.user,Added_IP=ip,Project_Name=project_name,project_Description=descriprion,
                                Client_Name=client_name,Client_Mobile=client_mobile,Client_Email=client_email,Client_Address=client_address,
                                Contact_Name=contact_name,Contact_Number=contact_mobile,Expected_Starting_Date=expected_date,
                                Expected_Amount=expected_amount,Reference=reference)
            
            project.Department_Managers.set(department_managers)
            project.save()

            messages.success(request,'new project created successfully ... !')
            return redirect('projects')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('create-project')

    context = {
        'reference' : reference,
        'department_managers' : department_managers
    }

    return render(request,'Dashboard/Projects/project-create.html',context)

#----------------------------------- PROJECT DETAILS -----------------------------------#

@login_required
def project_details(request,project_id):
    project = Project.objects.get(Reference=project_id)
    project_engineers = User.objects.filter(Job_Role='Project Engineer')

    d_m = project.Department_Managers.all()
    p_e = project.Project_Engineers.all()
    p_m = project.Purchase_Managers.all()
    s_e = project.Site_Engineers.all()

    staffs = list(d_m) + list(p_e) + list(p_m) + list(s_e)

    context = {
        'project' : project,
        'project_engineers' : project_engineers,
        'staffs' : staffs
    }
    return render(request,'Dashboard/Projects/project-details.html',context)


#----------------------------------- EDIT PROJECT -----------------------------------#

@login_required
def edit_project(request,project_id):
    project = Project.objects.get(Reference=project_id)
    department_managers = User.objects.filter(Job_Role='Department Manager')

    if request.method == 'POST':
        project.Project_Name = request.POST.get('project_name')
        project.project_Description = request.POST.get('description')

        project.Client_Name = request.POST.get('client_name')
        project.Client_Mobile = request.POST.get('client_mobile')
        project.Client_Email = request.POST.get('client_email')
        project.Client_Address = request.POST.get('client_address')
        project.Contact_Name = request.POST.get('contact_name')
        project.Contact_Number = request.POST.get('contact_mobile')
        department_managers = request.POST.getlist('department_managers')
        project.Department_Managers.set(department_managers)
        project.Expected_Starting_Date = request.POST.get('expected_date') or None
        project.Expected_Amount = request.POST.get('expected_amount') or None

        try:
            project.save()
            messages.success(request,'Project details edited successfully ... !')
            return redirect('projects')

        except Exception as exceprion:
            messages.warning(request,exceprion)
            return redirect('edit-project' , project_id=project.Reference)

    context = {
        'project' : project,
        'department_managers' : department_managers
    }
    return render(request,'Dashboard/Projects/project-edit.html',context)

#----------------------------------- ASSIGN PROJECT ENGINEER -----------------------------------#

@login_required
def assign_pe(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        project = Project.objects.get(id=project_id)
        pes = request.POST.getlist('project_engineers')

        try:
            project.Project_Engineers.set(pes)
            messages.success(request,'Successfully assigned project to project engineer ... !')
            return redirect('project-details',project_id=project.Reference)
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('project-details',project_id=project.Reference)