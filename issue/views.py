from dataclasses import dataclass

from django.http import JsonResponse

@dataclass(frozen=True)
class User:
    id: int
    name: str

@dataclass(frozen=True)
class UserMeta:
    id: int
    user_id: int
    age: int



user_data = [
    User(id=1, name="Alex"),
    User(id=2, name="Bob"),
    User(id=3, name="Jack"),
]

user_meta_data = [
    UserMeta(id=1, user_id=1, age=1),
    UserMeta(id=2, user_id=2, age=2)
]


def get_users(request):
    result = []
    for user in user_data:
        for user_meta in user_meta_data:
            if user.id == user_meta.user_id:
                result.append({"id": user.id, "name": user.name, "age": user_meta.age})
    return JsonResponse(data=result, safe=False)
