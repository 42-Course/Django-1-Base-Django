from django.conf import settings
from django.shortcuts import redirect, render

from .forms import InputForm
from .models import HistoryEntry


def _append_to_log(entry):
    """Append the entry and its timestamp to the log file from settings."""
    with open(settings.EX02_LOG_FILE, 'a') as f:
        f.write('{} : {}\n'.format(
            entry.created.strftime('%Y-%m-%d %H:%M:%S'), entry.text))


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            entry = HistoryEntry.objects.create(
                text=form.cleaned_data['text'])
            _append_to_log(entry)
            return redirect('/ex02')
    else:
        form = InputForm()

    history = HistoryEntry.objects.all()
    return render(request, 'ex02/index.html',
                  {'form': form, 'history': history})
