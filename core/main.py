"""
app entrypoint
"""

from flet import(
    Page, Checkbox,
    Column, Row, icons,
    FloatingActionButton,
    TextField, UserControl,
    Tabs, Tab, Text, OutlinedButton
)

from core import Task


class TodoApp(UserControl):

    def build(self):
        self.new_task = TextField(
            hint_text="Qu'est-ce qui doit être fait ?",
            autofocus=True, expand=True
        )
        self.tasks = Column()

        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                Tab(text="all"),
                Tab(text="active"),
                Tab(text="completed")
            ]
        )

        self.items_left = Text("0 items left")

        return Column(
            width=600,
            controls=[
                Row(
                    [Text(value="Todos", style="headlineMedium")],
                    alignment="center"
                ),
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(
                            icon=icons.ADD,
                            on_click=self.add_clicked
                        )
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="Clear completed",
                                    on_click=self.clear_clicked
                                )
                            ]
                        )
                    ]
                )
            ],
        )

    def add_clicked(self, e):
        task = Task(
            self.new_task.value,
            self.task_status_change,
            self.task_delete
        )
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def task_status_change(self, task):
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"
        super().update()

    def tabs_changed(self, e):
        self.update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)


def mainApp(page: Page):
    page.title = "Todo App"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.pwa
    page.update()

    """
    create application instance
    and add application's root control to the page
    """
    todo = TodoApp()
    page.add(todo)
