from django import forms

from django.core.exceptions import ValidationError

from app01 import models


class EmpForm(forms.Form):
    name = forms.CharField(min_length=4,label="姓名",error_messages={"min_length":"你太短了","required":"该字段不能为空"})
    age = forms.IntegerField(label="年龄")
    salary = forms.DecimalField(label="工资",decimal_places=2,max_digits=5)
    re_salary=forms.DecimalField(label="在输入工资",decimal_places=2,max_digits=5)

    def clean_name(self):
        val=self.cleaned_data.get("name")

        if val.isdigit():
            raise ValidationError("姓名不能为纯数字")