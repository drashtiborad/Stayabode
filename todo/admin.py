import csv

from django.contrib import admin
from django.http.response import HttpResponse

from .models import TodoList


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'todo_time', 'created_at', 'updated_at', 'deleted_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'todo_time', 'created_at')

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


admin.site.register(TodoList, ToDoAdmin)
