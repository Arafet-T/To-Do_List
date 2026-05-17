import json
import math
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request


def invalid_response(error, status) :
    request_body = {
        "message": "Failure",
        "error": error
    }
    return request.make_json_response(request_body, status=status)


def valid_response(data, message, status, pagination_infos=None) :
    request_body = {
        "message": message,
        "data": data
    }
    if pagination_infos:
        request_body["pagination_infos"] = pagination_infos
    return request.make_json_response(request_body, status=status)


class TodoTaskApi(http.Controller):

    #Create Task Endpoint
    @http.route("/v1/todo_task", methods=["POST"], type="http", auth="none", csrf=False)
    def post_task(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        if not vals.get("task_name") or not vals.get("estimated_time") or not vals.get("assign_to_id"):
            return invalid_response("Todo Task name, estimated time and assign to id are required", status=400)
        try:
            res = request.env["todo.task"].sudo().create(vals)
            if res:
                return valid_response({
                    "task_id": res.id,
                    "ref": res.ref,
                    "task_name": res.task_name,
                    "assign_to": res.assign_to_id.name
                }, "Task created successfully", status=201)
        except Exception as error:
            return invalid_response(error, status=400)

    #Read One Task Endpoint
    @http.route("/v1/todo_task/<int:task_id>", methods=["GET"], type="http", auth="none", csrf=False)
    def get_task(self, task_id):
        try:
            task_id = request.env["todo.task"].sudo().search([("id", "=", task_id)])
            if not task_id:
                return invalid_response("Task not found", status=404)
            return valid_response({
                "task_id": task_id.id,
                "ref": task_id.ref,
                "task_name": task_id.task_name,
                "description": task_id.description,
                "due_date": task_id.due_date,
                "assign_to": task_id.assign_to_id.name,
                "status": task_id.status,
                "estimated_time": task_id.estimated_time
            }, "Successful", status=200)
        except Exception as error:
            return invalid_response(error, status=400)

    #Update Task Endpoint
    @http.route("/v1/todo_task/<int:task_id>", methods=["PUT"], type="http", auth="none", csrf=False)
    def update_task(self, task_id):
        try:
            task_id = request.env["todo.task"].sudo().search([("id", "=", task_id)])
            if not task_id:
                return invalid_response("Task not found", status=404)
            if task_id.status in ('completed', 'closed'):
                return invalid_response("Task status is completed or closed", status=400)
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            if vals.get("task_name") and len(vals.get("task_name").strip()) < 3:
                return invalid_response("Todo Task name must at list 3 characters", status=400)
            if vals.get("estimated_time") and float(vals.get("estimated_time")) < task_id.total_timesheet_time:
                return invalid_response(f"Total Timesheet time exceeds estimated time! Total Timesheet Time = {task_id.total_timesheet_time}", status=400)
            task_id.write(vals)
            return valid_response({
                "task_id": task_id.id,
                "ref": task_id.ref,
                "task_name": task_id.task_name,
                "assign_to": task_id.assign_to_id.name
            }, "Task updated successfully", status=200)
        except Exception as error:
            return invalid_response(error, status=400)

    #Delete Task Endpoint
    @http.route("/v1/todo_task/<int:task_id>", methods=["DELETE"], type="http", auth="none", csrf=False)
    def delete_task(self, task_id):
        try:
            task_id = request.env["todo.task"].sudo().search([("id", "=", task_id)])
            if not task_id:
                return invalid_response("Task not found", status=404)
            task_id.unlink()
            return valid_response({
                "id": task_id.id,
            }, "Task deleted successfully", status=200)
        except Exception as error:
            return invalid_response(error, status=400)

    #Read All Tasks Endpoint (with Pagination)
    @http.route("/v1/todo_tasks", methods=["GET"], type="http", auth="none", csrf=False)
    def get_all_tasks(self):
        try:
            params = parse_qs(request.httprequest.query_string.decode('utf-8'))
            page = offset = None
            limit = 0
            if params.get('page'):
                page = int(params.get('page')[0])
            if params.get('limit'):
                limit = int(params.get('limit')[0])
            if page:
                offset = (page * limit) - limit
            task_ids = request.env["todo.task"].sudo().search([], offset=offset, limit=limit, order="id DESC")
            task_count = request.env["todo.task"].sudo().search_count([])
            if not task_ids:
                return invalid_response("There is no Task records", status=404)
            return valid_response([{
                "task_id": task.id,
                "ref": task.ref,
                "task_name": task.task_name,
                "description": task.description,
                "due_date": task.due_date,
                "assign_to": task.assign_to_id.name,
                "status": task.status,
                "estimated_time": task.estimated_time
            } for task in task_ids], "Successful", status=200, pagination_infos={
                'page': page if page else 1,
                'limit': limit,
                'pages': math.ceil(task_count / limit) if limit else 1,
                'all_tasks_count': task_count
            })
        except Exception as error:
            return invalid_response(error, status=400)

