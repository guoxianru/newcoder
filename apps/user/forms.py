from django import forms


# 注册验证
class SignupForm(forms.Form):
    username = forms.CharField(max_length=16, min_length=6,
                               error_messages={'required': '用户名不能为空', 'min_length': '用户名长度至少6位'})
    nickname = forms.CharField(max_length=16, min_length=2,
                               error_messages={'required': '昵称不能为空', 'min_length': '用户名长度至少2位'})
    password = forms.CharField(max_length=64, min_length=6,
                               error_messages={'required': '密码不能为空', 'min_length': '密码长度至少6位'})
    photo = forms.ImageField(error_messages={'required': '没有选择图片'})


# 登陆验证
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3,
                               error_messages={'required': '用户名不能为空', 'min_length': '用户名长度至少3位'})
    password = forms.CharField(max_length=64, min_length=6,
                               error_messages={'required': '密码不能为空', 'min_length': '密码长度至少6位'})
