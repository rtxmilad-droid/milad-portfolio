from django.shortcuts import render, get_object_or_404, redirect

from .models import Project, ContactMessage


def home(request):

    projects = Project.objects.all()

    return render(request, "home.html", {
        "projects": projects
    })



def project_detail(request, id):

    project = get_object_or_404(Project, id=id)

    return render(request, "project_detail.html", {
        "project": project
    })



def resume(request):

    return render(request, "resume.html")



def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")


        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )


        return redirect("/contact/")


    return render(request, "contact.html")