from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    STATUS_CHOICES = [
        ('none', '아직 작가 활동은 안 해봤어요'),
        ('aspiring', '작가를 준비하고 있어요 (지망생)'),
        ('hobbyist', '취미로 글을 쓰고 있어요'),
        ('semi_pro', '연재 또는 상업 활동 중이에요'),
        ('professional', '전업 작가입니다'),
    ]
    # 프로필 사진
    profile_image = models.ImageField(upload_to='profile_images', blank=True)

    # 전화번호
    phone_number = PhoneNumberField(region='KR')

    # 주력 장르
    genres = models.CharField(
        max_length=100,
        help_text='어떤 장르의 글을 가장 많이 쓰시나요? (최대 3개 선택 가능)',
        blank=True,
        verbose_name='장르',
    )
    
    # 작가 경력
    author_status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        help_text='작가님의 글쓰기 경험을 알려주세요',
        verbose_name='작가 활동 경력',
    )

    def __str__(self):
        return self.username # 04.18. self.name에서 self.username으로 변경

    def get_category_list(self):
        """콤마로 구분된 카테고리 문자열을 리스트로 변환"""
        if not self.genres:
            return []
        return self.genres.split(',')

    def get_category_display_list(self):
        """카테고리 코드에 해당하는 표시 이름 리스트 반환"""
        genres = self.get_category_list()
        genre_dict = dict(
            [
                ('romance', '로맨스'),
                ('fantasy', '판타지'),
                ('sf', 'SF/공상 과학'),
                ('mystery', '미스터리 / 스릴러'),
                ('essay', '에세이'),
                ('poetry', '시'),
            ]
        )
        return [genre_dict.get(cat, cat) for cat in genres]

    def get_category_display(self):  # 원래 choices 필드에서 사용하는 메서드
        """카테고리 이름들을 콤마로 구분하여 반환"""
        return ', '.join(self.get_category_display_list())



"""
User 모델 클래스 : AbstractUser 모델 클래스를 상속받는 커스템 모델 사용
"""

'''
- id
- password
- username
- first_name
- last_name
- email
- 프로필 사진
- 전화번호
- 주력 장르 (다중 선택 필요)
- 작가 여부 (author_status)
'''

