from django.shortcuts import render
from .models import Maize_cluster
from django.db.models import Q
from django.contrib import messages
from django.http import *

# Create your views here.
def home(request):


    return render(request,'search/home.html')
def results(request):

    urlx=[]
    global mylist

    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Maize_cluster.objects.filter(Q(gene_id__icontains=srch))
            if match:
                for k in match:
                    url = "https://plants.ensembl.org/Zea_mays/Location/View?db=core;g={0};r={1}:{2};t={3};mr={1}:{4}-{4}".format(k.gene_id,k.chromosome,k.transcript_code,k.transcript_id,k.pac)
                    urlx.append(url)
                mylist = zip(match,urlx)


                return render(request, 'search/results.html',{'sr':mylist})
            else:
                return render(request, 'search/results.html')
        else:
            return HttpResponseRedirect('/result/')


    return render(request,'search/results.html')
def contact(request):
    return render(request,'search/contact.html')
def detailed(request,id):
    if request.method == 'POST':
        q= request.POST['q']
        if q:
            query =  Maize_cluster.objects.filter(Q(id__iexact=q[0]))
            for a in query:
                b = a.gene_id

            querye = Maize_cluster.objects.filter(Q(gene_id__iexact= b))

            if query:
                return render(request, "search/Detailed.html",{'sr':query ,'ab':querye})
            else:
                return render(request, "search/Detailed.html")
        else:
            return render(request, "search/Detailed.html")

    return render(request,"search/Detailed.html")