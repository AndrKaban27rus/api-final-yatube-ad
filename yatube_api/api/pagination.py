from rest_framework.pagination import LimitOffsetPagination


class MyPostPagination(LimitOffsetPagination):
    default_limit = None
    max_limit = 100
    offset_query_param = 'offset'
