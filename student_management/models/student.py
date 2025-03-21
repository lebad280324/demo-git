from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "student.student"
    _description = "Student Management"

    name = fields.Char("Tên sinh viên", required=True)
    student_code = fields.Char("Mã sinh viên", required=True, index=True)
    _sql_constraints = [
        ("unique_student_code", "unique(student_code)", "Mã sinh viên đã tồn tại!"),
    ]
    display_name = fields.Char("Tên hiển thị", compute="_compute_display_name", store=True)
    birth_date = fields.Date("Ngày sinh")
    email = fields.Char("Email")
    phone = fields.Char("Số điện thoại")

    @api.depends("student_code", "name")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.student_code}-{record.name}"

    @api.constrains("student_code")
    def _check_unique_student_code(self):
        for record in self:
            if self.search_count([("student_code", "=", record.student_code), ("id", "!=", record.id)]) > 0:
                raise ValidationError("Mã sinh viên đã tồn tại, vui lòng nhập mã sinh viên khác!")



class ResPartner(models.Model):
    _inherit = "res.partner"

    is_student = fields.Boolean("Là sinh viên")
    student_id = fields.Many2one("student.student", "Sinh viên", domain="[('id', '=', id)]")

    @api.onchange("is_student")
    def _onchange_is_student(self):
        if not self.is_student:
            self.student_id = False



