from rest_framework.pagination import PageNumberPagination


class CoursesPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "per_page"
    max_page_size = 10
