from django import forms

from .models import Node

class ConfirmDeleteForm(forms.ModelForm):
	name = forms.CharField(label="confirm object's name", max_length=100)

	class Meta:
		model = Node
		fields = ['name']

	def clean_name(self):
		name = super().clean().get('name')

		if self.instance.name.lower() != name.lower():
			raise forms.ValidationError('Confirmation incorrect')
		return name

class NodeForm(forms.ModelForm):
	class Meta:
		model = Node
		fields = ['name', 'parent']

	def clean_parent(self):
		name = self.cleaned_data['name']
		parent = self.cleaned_data['parent']

		if name.lower() == parent.name.lower():
			raise forms.ValidationError('A object may not be made a child of itself.')
		return parent
			

