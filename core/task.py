from flet import(
    Checkbox, Column, Row, icons,
    TextField, UserControl, IconButton,
    colors
)


class Task(UserControl):

    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_delete = task_delete
        self.task_status_change = task_status_change

    def build(self):
        self.display_task = Checkbox(
            value=False, label=self.task_name,
            on_change=self.status_changed
        )
        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit task",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icon=icons.DELETE_OUTLINE,
                            tooltip="Delete task",
                            on_click=self.delete_clicked
                        )
                    ]
                )
            ]
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update task",
                    on_click=self.save_clicked
                )
            ]
        )

        return Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)

    def delete_clicked(self, e):
        self.task_delete(self)
