from django.shortcuts import render

# Create your views here.
def landing(request):
    classifications = ["Inf.02", "Inf.03", "Ele.02", "Ele.03", "SPC.02", "SPC.03", "ROL.02", "ROL.03"]
    context = {"classifications": classifications}
    return render(request, "landing.html", context)

def exam(request):
    examCode = request.GET.get("code")
    return render(request,'exam.html',{"code": examCode})
    pass