from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy

from .forms import ConfirmDeleteForm, NodeForm

from .models import Node

"""def show_nodes(request):  
    context = Node.objects.all()  
    return render(request, 'nodes/nodes.html', {'nodes': context})"""

class DeleteNode(DeleteView):
    model = Node
    success_url = reverse_lazy('nodes:node_list')

    def get_context_data(self, **kwargs):
        """
        Overridden to add a confirmation form to the context.
        """
        context = super().get_context_data(**kwargs)

        if 'form' not in kwargs:
            context['form'] = ConfirmDeleteForm()

        return context

    def post(self, request, *args, **kwargs):
        """
        Overridden to process the confirmation form before deleting
        the object.
        """
        self.object = self.get_object()
        form = ConfirmDeleteForm(request.POST, instance=self.object)

        if form.is_valid():
            return self.delete(request, *args, **kwargs)
        else:
            return self.render_to_response(
                self.get_context_data(form=form),
            )

class UpdateNode(UpdateView):
    model = Node
    success_url = reverse_lazy('nodes:node_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in kwargs:
            context['form'] = NodeForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        """
        Overridden to process the confirmation form before deleting
        the object.
        """
        self.object = self.get_object()
        form = NodeForm(request.POST, instance=self.object)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
