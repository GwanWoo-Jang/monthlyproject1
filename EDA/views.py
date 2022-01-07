from django.shortcuts import render

import plotly.express as px
import plotly.graph_objects as go


# Create your views here.

def eda_views(request):


    return render(request, 'index.html', {})
