[toc]

# Django ModelMultipleChoiceField

**ModelMultipleChoiceField**는 Django 폼에서 **다중 선택**(Multiple Choice)이 필요할 때, 특히 **ManyToMany 관계**나 외부 모델을 선택해야 하는 상황에서 사용되는 **폼 필드**

**Model**에서 생성된 쿼리셋(`QuerySet`)을 사용하여, 사용자가 여러 개의 항목을 체크하거나 선택할 수 있게 함



---



## 1. 개념

- **ModelMultipleChoiceField**: Django의 `forms` 모듈에서 제공하는 폼 필드로, **Model**에 대한 쿼리셋을 기반으로 **여러 개의 선택**이 가능하도록 구성
- **HTML 표현**: `<select multiple>`가 기본이나, `CheckboxSelectMultiple` 등의 위젯을 통해 **체크박스** 형태로도 사용할 수 있음
- **ManyToManyField**와 주로 사용: DB에서 다대다(ManyToMany) 구조를 모델로 표현할 때, 폼에서는 여러 항목을 동시에 선택하기 위해 ModelMultipleChoiceField를 사용하는 경우가 일반적



---



## 2. 기본 사용 예시

```python
# forms.py
from django import forms
from .models import Tag, Article

class ArticleForm(forms.ModelForm):
    # ManyToManyField인 tags 필드에 대한 폼 구현
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),         # 1
        widget=forms.CheckboxSelectMultiple # 2
    )

    class Meta:
        model = Article
        fields = ['title', 'content', 'tags']
```

1. **`queryset=Tag.objects.all()`**: 이 폼 필드는 Tag 모델의 모든 레코드를 선택지로 보여줌
2. **`widget=forms.CheckboxSelectMultiple`**: HTML에서 체크박스 그룹으로 표시

> **주의**: `Article` 모델에서 `tags`라는 ManyToManyField를 정의해두었고, 폼에서는 `tags` 항목을 다중 선택할 수 있도록 ModelMultipleChoiceField를 사용.



---



## 3. `queryset` 인자

**`queryset`**는 ModelMultipleChoiceField가 제공할 **선택지의 집합**을 결정하는 핵심 인자

### 3.1 기본 설정

```python
tags = forms.ModelMultipleChoiceField(
    queryset=Tag.objects.all()
)
```
- `Tag` 모델에 있는 모든 객체가 선택지로 나온다.  
- 폼이 렌더링될 때 이 쿼리셋을 기준으로 `<option>` 또는 체크박스 항목이 생성된다.



---



## 4. 뷰 및 템플릿에서의 처리

```python
# views.py
def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()  # ManyToMany 관계가 자동 처리
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})
```

- **`form.save()`** 사용 시, `tags`와 같은 다대다 관계도 Django가 자동으로 처리
- 템플릿에서 **`{{ form.tags }}`**를 렌더링하면, `<select multiple>` 또는 체크박스 그룹이 표시



---



## 5. 실제 DB 저장 동작

- **ModelMultipleChoiceField**에 의해 선택된 객체들은 **cleaned_data**에서 **쿼리셋** 리스트로 반환
  - 예: `[<Tag: Python>, <Tag: Django>]`
- ModelForm의 **`form.save()`**는 이 리스트를 **ManyToManyField**에 자동으로 반영

> **커스텀 폼**을 쓴다면, `form.cleaned_data['tags']`를 직접 처리하여 `article_instance.tags.set(...)` 같은 식으로 저장 가능



