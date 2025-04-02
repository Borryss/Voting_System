from django.shortcuts import render, redirect
from .models import Poll, PollOption, Vote
from .forms import PollForm, PollOptionForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def create_poll(request):
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        option_forms = [PollOptionForm(request.POST, prefix=f'option_{i}') for i in range(3)]
        if poll_form.is_valid() and all(option_form.is_valid() for option_form in option_forms):
            poll = poll_form.save()
            for option_form in option_forms:
                option_form.instance.poll = poll
                option_form.save()
            return redirect('poll_detail', poll_id=poll.id)
    else:
        poll_form = PollForm()
        option_forms = [PollOptionForm(prefix=f'option_{i}') for i in range(3)]
    return render(request, 'voting/create_poll.html', {'poll_form': poll_form, 'option_forms': option_forms})

def poll_detail(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        option_id = request.POST.get('option')
        option = PollOption.objects.get(id=option_id)
        if not Vote.objects.filter(user=request.user, poll=poll).exists():
            Vote.objects.create(user=request.user, poll=poll, option=option)
            option.votes += 1
            option.save()
        return redirect('poll_detail', poll_id=poll.id)
    options = poll.options.all()
    return render(request, 'voting/poll_detail.html', {'poll': poll, 'options': options})
