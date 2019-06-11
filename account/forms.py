from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
    
    email = forms.EmailField(required=True) # 이메일 필드 추가
    nickname = forms.CharField(required=True) # nickname 필드 추가

    class Meta:
        model = User # django에 내장되어있는 User 모델 불러오기
        fields = ("username", "email","nickname", "password1", "password2") # User 모델에서 사용할 필드 불러오기

    def save(self, commit=True): # 저장하는 부분 오버라이딩
        user = super(CreateUserForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
        user.nickname = self.cleaned_data["nickname"] # user.nickname user모델에 nickname 을 추가해주기
        user.email = self.cleaned_data["email"] # user.email 변수에 user모델에 있는 email 추가해주기
        if commit:
            user.save()  # user모델에 저장하기
        return user
