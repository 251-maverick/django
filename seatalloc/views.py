from django.shortcuts import render,redirect
from seatalloc.forms import CandidateForm, PreferenceForm
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from seatalloc.models import Candidate, Preference

def add_candidate(request):
    if request.method == 'POST':
        form= CandidateForm(request.POST)
        if form.is_valid():
            # Save the new candidate to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CandidateForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'seatalloc/detail.html', {'form':form})

def add_preference(request, candidate_roll):
    try:
        cat = Candidate.objects.get(roll=candidate_roll)
        print ("try")
    except Candidate.DoesNotExist:
        print("except")
        cat = None
    print ("m mad")
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            print ("valid form")
            if cat:
                print ("cat not none, saved")
                preference = form.save(commit=False)
                preference.candidate = cat
                preference.save()
                return candidate(request, "a")
                # probably better to use a redirect here.
                #return HttpResponseRedirect("/detail/")
        else:
            print ("nt valid")
            print (form.errors)
    else:
        print ("req.nt ppst")
        form = PreferenceForm()

    context_dict = {'form':form, 'candidate': cat}
    return render(request, 'seatalloc/add_preference.html', context_dict)
    #return redirect('candidate',candidate_roll)
    #return HttpResponseRedirect("/detail/candidate_roll")
        
# def add_preference(request, candidate_roll):
    try:
        cat = Candidate.objects.get(roll=candidate_roll)
    except Candidate.DoesNotExist:
        cat = None
        if request.method == 'POST':
            form = PreferenceForm(request.POST)
            if form.is_valid():
                 if cat:
                     preference = form.save(commit=False)
                     preference.candidate = cat
                     preference.save()
                # probably better to use a redirect here.
                     return candidate(request, candidate_roll)
                 else:
                     print (form.errors)
            else:
                form = PreferenceForm()

        context_dict = {'form':form, 'candidate': cat}
        return render(request, 'seatalloc/add_preference.html', context_dict)
  
  

def candidate(request, candidate_roll):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a candidate name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        candidate = Candidate.objects.get(roll=candidate_roll)
        context_dict['candidate_roll'] = candidate.roll

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        preference = Preference.objects.filter(candidate=candidate)

        # Adds our results list to the template context under name pages.
        context_dict['preference'] = preference
        # We also add the candidate object from the database to the context dictionary.
        # We'll use this in the template to verify that the candidate exists.
        context_dict['candidate'] = candidate
    except Candidate.DoesNotExist:
        # We get here if we didn't find the specified candidate.
        # Don't do anything - the template displays the "no candidate" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'seatalloc/candidate.html', context_dict)      
        
def index(request):
    context_dict = {'boldmessage' : "dictionary"}
    return render(request, 'seatalloc/index.html',context_dict)


