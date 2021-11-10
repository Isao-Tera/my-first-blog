from django.shortcuts import render
from django.utils import timezone

# models の前にあるドットは カレントディレクトリ 、もしくは カレントアプリケーション のことです。
from .models import Post

def post_list(request):
    """
    表示したいデータを取り出して、テンプレートファイルに渡す
    request: インターネットを介してユーザから受け取った全ての情報が詰まったもの
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # {}: 指定した情報を、テンプレートが表示してくれます。
    # {} の中に引数を記述する時は、名前と値をセットにしなくてはなりません。
    return render(request, 'blog/post_list.html', {'posts':posts})
    


