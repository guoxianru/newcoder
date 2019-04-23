from django import forms


# 添加文章验证
class AddarticleForm(forms.Form):
    title = forms.CharField()
    type = forms.CharField()
    pic = forms.ImageField()
    content = forms.CharField()
