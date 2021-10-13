from django.db import models

# Create your models here.

# 名前とメールアドレスだけを持ったUser
class User(models.Model):
  name = models.CharField(max_length=32)
  mail = models.EmailField()

# ブログの記事を表すEntry
class Entry(models.Model):
  STATUS_DRAFT = "draft"
  STATUS_PUBLIC = "public"
  STATUS_SET = (
    (STATUS_DRAFT, "下書き"), (STATUS_PUBLIC, "公開中"),
  )
  title = models.CharField(max_length=128)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.TextField()
  status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
  # Entryからブログの書いた人の情報としてForeignKeyでUserを参照
  # related_nameを付けるだけで逆参照も行える
  author = models.ForeignKey(User, related_name='entries',on_delete=models.CASCADE)

