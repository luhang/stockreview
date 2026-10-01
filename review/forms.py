from django import forms
from django.forms.widgets import FileInput
from .models import Review, ReviewImage


class MultipleFileInput(FileInput):
    allow_multiple_selected = True

    def __init__(self, attrs=None):
        super().__init__(attrs={**(attrs or {}), 'multiple': True, 'accept': 'image/*'})


class ReviewForm(forms.ModelForm):
    images = forms.ImageField(
        label='上传图片',
        required=False,
        widget=MultipleFileInput(),
    )

    class Meta:
        model = Review
        fields = ['stock_code', 'trade_date', 'action', 'price', 'note']
        widgets = {
            'trade_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_images(self):
        files = self.files.getlist('images')
        if len(files) > 3:
            raise forms.ValidationError('最多只能上传 3 张图片')
        return files

    def save(self, commit=True):
        instance = super().save(commit)
        if commit:
            for f in self.cleaned_data.get('images', []):
                ReviewImage.objects.create(review=instance, image=f)
        return instance
