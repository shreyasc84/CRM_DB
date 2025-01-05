from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import record
from .forms import AddRecordForm

def home(request):
    records = record.objects.all()

    #checking login
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']

        #authentication
        user = authenticate(request, username=_username, password=_password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error Logging in")
    else:
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def customer_record(request, pk):
    if request.user.is_authenticated:
        # look up records
        customer_record = record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to View Record")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to Delete Record")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to Add Record")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None , instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to Update Record")
        return redirect('home')