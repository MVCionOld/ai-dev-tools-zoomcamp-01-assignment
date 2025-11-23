from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Todo

# Create your views here.

def index(request):
    """Render the main TODO page"""
    return render(request, 'todos/index.html')

@csrf_exempt
@require_http_methods(["GET"])
def todo_list(request):
    """API endpoint to get all todos"""
    todos = Todo.objects.all()
    data = [{
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'due_date': todo.due_date.isoformat() if todo.due_date else None,
        'is_resolved': todo.is_resolved,
        'created_at': todo.created_at.isoformat(),
        'updated_at': todo.updated_at.isoformat(),
    } for todo in todos]
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def todo_create(request):
    """API endpoint to create a new todo"""
    try:
        data = json.loads(request.body)
        
        # Handle empty string for due_date
        due_date = data.get('due_date')
        if due_date == '':
            due_date = None
            
        todo = Todo.objects.create(
            title=data.get('title'),
            description=data.get('description', ''),
            due_date=due_date,
            is_resolved=data.get('is_resolved', False)
        )
        return JsonResponse({
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'due_date': todo.due_date.isoformat() if todo.due_date else None,
            'is_resolved': todo.is_resolved,
            'created_at': todo.created_at.isoformat(),
            'updated_at': todo.updated_at.isoformat(),
        }, status=201)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["PUT"])
def todo_update(request, todo_id):
    """API endpoint to update a todo"""
    try:
        todo = get_object_or_404(Todo, id=todo_id)
        data = json.loads(request.body)
        
        if 'title' in data:
            todo.title = data['title']
        if 'description' in data:
            todo.description = data['description']
        if 'due_date' in data:
            due_date = data['due_date']
            todo.due_date = due_date if due_date and due_date != '' else None
        if 'is_resolved' in data:
            todo.is_resolved = data['is_resolved']
        
        todo.save()
        
        return JsonResponse({
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'due_date': todo.due_date.isoformat() if todo.due_date else None,
            'is_resolved': todo.is_resolved,
            'created_at': todo.created_at.isoformat(),
            'updated_at': todo.updated_at.isoformat(),
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def todo_delete(request, todo_id):
    """API endpoint to delete a todo"""
    try:
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return JsonResponse({'message': 'Todo deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

