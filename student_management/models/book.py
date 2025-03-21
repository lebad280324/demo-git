from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    book_code = fields.Char("Mã sách", required=True, copy=False, readonly=True, default=lambda self: self.env["ir.sequence"].next_by_code("library.book") or "TV00001")
    name = fields.Char("Tên sách", required=True)
    publish_year = fields.Char("Thời gian xuất bản")
    author = fields.Char("Tác giả")
    student_id = fields.Many2one("student.student", "Sinh viên")

    @api.model
    def create(self, vals):
        vals["book_code"] = self.env["ir.sequence"].next_by_code("library.book") or "TV00001"
        return super().create(vals)
