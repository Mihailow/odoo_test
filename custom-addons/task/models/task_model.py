from odoo import models, fields


class TaskModel(models.Model):
    _name = "task.model"
    _description = "Task"

    name = fields.Char(string="Name", required=True)
    production_date = fields.Date(string="Production Date", required=True)
    color = fields.Selection(
        [
            ('red', 'red'),
            ('blue', 'blue'),
            ('green', 'green'),
            ('black', 'black'),
            ('white', 'white')
        ],
        string="Color", required=True
    )
    weight = fields.Float(string="Weight", required=True)

    color_badge = fields.Html(
        string="Color",
        compute="_compute_color_badge",
        sanitize=False,
        sanitize_tags=False,
        sanitize_attributes=False,
    )

    def _compute_color_badge(self):
        for rec in self:
            if rec.color:
                rec.color_badge = f"""
                    <div style="
                        background-color:{rec.color};
                        width: 100%;
                        height: 30px;
                        border-radius: 4px;">
                    </div>
                """
            else:
                rec.color_badge = ""

    def button_register(self):
        return True