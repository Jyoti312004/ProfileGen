import PyPDF2
import re

from django.shortcuts import render ,HttpResponse,redirect
from datetime import datetime
from Home.models import Form,File
# Create your views here.

def index(request):
    context = {
      'variable': 'THIS IS VARIABLE PLACEHOLDER'
    }
    return render(request,'index.html',context)


def about(request):
  return HttpResponse("This is about")


def form(request):
  if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      experience = request.POST.get('experience')
      education = request.POST.get('education')
      skills = request.POST.get('skills')
      projects = request.POST.get('projects')
      linkedin = request.POST.get('linkedin')
      github = request.POST.get('github')
      leetcode = request.POST.get('leetcode')
      varForm = Form(name = name, email= email, phone = phone , education = education, experience=experience,
                  skills=skills,linkedin=linkedin,github=github,leetcode=leetcode, projects=projects)
      varForm.save()
      context = {
        'name' : name,
        'email': email,
        'phone':phone,
        'experience':experience,
        'education':education,
        'skills':skills,
        'projects':projects,
        'linkedin':linkedin,
        'github':github,
        'leetcode':leetcode,
      }
      return render(request,'dashboard.html',context)

  return render(request,'form.html')

def dashboard(request):

  return render(request,'dashboard.html')




def contact(request):
    return render(request,'contact.html')


def file(request):
  if request.method=="POST":
    file = request.FILES['file']
    File.objects.create(file=file)
    # Open the pdf file containing the resume
    #with open('file', 'rb') as resume_pdf:
    # Create a pdf reader object
    pdf_reader = PyPDF2.PdfReader(file)
      # Extract text from all pages in the pdf
    text = ""
    for page in pdf_reader.pages:
        # Extract the text from the page
        text += page.extract_text()

    # Parse the text to extract specific pieces of information
    # such as the candidate's name, contact information, education, and work experience
    
    # Extracting the name
    name = text.split('\n')[0]

    # Extracting the email
    email = re.search("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text).group(0)

    # Extracting the phone number
    phone = re.search(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
    if phone:
      phone = phone.group(0)
    else:
      phone = "Phone number not found"

    linkedin = re.search(r"linkedin.com/in/([a-zA-Z0-9_-]+)", text)
    if linkedin:
        linkedin = linkedin.group(1)
    else:
        linkedin = "LinkedIn username not found"

    # Extracting the LeetCode username
    leetcode = re.search(r"leetcode.com/([a-zA-Z0-9_-]+)", text)
    if leetcode:
        leetcode = leetcode.group(1)
    else:
        leetcode = "LeetCode username not found"

    # Extracting the GitHub username
    github = re.search(r"github.com/([a-zA-Z0-9_-]+)", text)
    if github:
        github = github.group(1)
    else:
        github = "GitHub username not found"

    sections = [ "Experience","Education","Projects", "Skills","Achievements", "Certifications"]
    data = {section: "Not found" for section in sections}

    for i, section in enumerate(sections):
        start = text.find(section)
        if start != -1:
            end = text.find(sections[i + 1]) if i + 1 < len(sections) else len(text)
            data[section] = text[start:end].strip()

    context = {
        'name': name,
        'email': email,
        'phone': phone,
        'work_experience': data["Experience"],
        'education': data["Education"],
        'skills': data["Skills"],
        'projects': data["Projects"],
        'certifications': data["Certifications"],
        'achievements': data["Achievements"],
        'leetcode': leetcode,
        'github': github,
        'linkedin': linkedin,
    }
    return render(request,'file.html',context)




  return render(request,'file.html')

