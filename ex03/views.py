from django.shortcuts import render

NB_SHADES = 50
COLUMNS = ['noir', 'rouge', 'bleu', 'vert']


def _shade(column, i):
    """Return a hex colour for the given column and shade index (0..49)."""
    v = 255 - i * 5  # 255 (light) down to 10 (dark), all distinct
    if column == 'noir':
        r, g, b = v, v, v
    elif column == 'rouge':
        r, g, b = 255, v, v
    elif column == 'bleu':
        r, g, b = v, v, 255
    else:  # vert
        r, g, b = v, 255, v
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def index(request):
    rows = []
    for i in range(NB_SHADES):
        rows.append([_shade(column, i) for column in COLUMNS])
    return render(request, 'ex03/index.html',
                  {'names': COLUMNS, 'rows': rows})
