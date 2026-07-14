from django.shortcuts import render, get_object_or_404

from .models import Project, ContactMessage





def home(request):

    projects = Project.objects.all()

    return render(request, "home.html", {

        "projects": projects

    })







def project_detail(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )


    return render(request, "project_detail.html", {

        "project": project

    })







def resume(request):

    return render(request, "resume.html")







def contact(request):


    if request.method == "POST":


        name = request.POST["name"]

        email = request.POST["email"]

        message = request.POST["message"]



        ContactMessage.objects.create(

            name=name,

            email=email,

            message=message

        )



    return render(request, "contact.html")