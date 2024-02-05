from django.shortcuts import redirect
from django.views import View
from blog.models import Likes


class AddLike(View):
    def get(self, request, pk):
        obj_like = Likes.objects.filter(pos_id=pk, user_id=request.user.id)

        if not obj_like.exists():
            Likes.objects.create(
                pos_id=pk,
                user_id=request.user.id,
            )
            return redirect('page', pk)

        obj_like = obj_like.first()
        obj_like.boolean_value = True
        obj_like.save()
        return redirect('page', pk)


class DeleteLike(View):
    def get(self, request, pk):
        obj_like = Likes.objects.filter(pos_id=pk, user_id=request.user.id)

        if not obj_like.exists():
            return redirect('page', pk)

        obj_like = obj_like.first()
        obj_like.boolean_value = False
        obj_like.save()
        return redirect('page', pk)
