from django.shortcuts import render, redirect
from .models import Poll, PollOption, Vote
from .forms import PollForm, PollOptionForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string



@login_required
def create_poll(request):
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        option_forms = []
        i = 0
        while True:
            form = PollOptionForm(request.POST, prefix=f'option_{i}')
            if f'option_{i}-option_text' in request.POST:
                option_forms.append(form)
                i += 1
            else:
                break
        if poll_form.is_valid() and all(f.is_valid() for f in option_forms):
            poll = poll_form.save()
            for f in option_forms:
                f.instance.poll = poll
                f.save()
            return redirect('poll_detail', poll_id=poll.id)
    else:
        poll_form = PollForm()
        option_forms = [PollOptionForm(prefix=f'option_{i}') for i in range(3)]
    return render(request, 'voting/create_poll.html', {
        'poll_form': poll_form,
        'option_forms': option_forms
    })
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


def add_option_form(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':

        next_index = int(request.GET.get('next_index'))
        form = PollOptionForm(prefix=f'option_{next_index}')
        html = render_to_string('voting/option_form_snippet.html', {'form': form})
        return JsonResponse({'form_html': html})

# def ajax_test(request):
#     # Відправка відповіді у форматі JSON
#
#     return JsonResponse({'message': 'ajax working goooooood'})