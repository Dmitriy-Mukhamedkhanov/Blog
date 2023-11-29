from django.shortcuts import redirect
from django.views import View
from blog.services.comments.add_comment import AddCommentsService
from blog.services.comments.delete_comment import CommentDeleteViewService


class AddComments(View):
    '''Добавление комментариев'''

    def post(self, request, pk):
        outcome = AddCommentsService.execute(
            {
                "text_comment": request.POST["text_comment"],
                "author_comment": request.POST["author_comment"],
                "id": pk
            },
        )
        return redirect('page', pk)

class CommentDeleteView(View):
    def get(self, request, pk):
        outcome = CommentDeleteViewService.execute(
            {
                "id": pk
            },
        )
        return redirect('page', outcome)  # Как остаться на той же странице?









