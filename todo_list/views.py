from django.shortcuts import render, redirect
from .models import TodoList, Category


def index(request):
    todo_items = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        if 'add_task' in request.POST:
            title = request.POST['title']
            date = str(request.POST["date"])
            category = request.POST["selected_category"]
            content = "{} // {} -- {}".format(date, title, category)
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/")
        if "delete_task" in request.POST:
            checked_todo_list = request.POST['checkedbox']
            for todo_id in checked_todo_list:
                todo_to_delete = TodoList.objects.get(id=int(todo_id))
                todo_to_delete.delete()
    context_output = {"todo_items": todo_items,
                      "categories": categories}
    return render(request, "index.html", context_output)
