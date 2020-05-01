from models.group import Group
import random


def test_edit_name_group_by_index(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="NSKjcndk", header="dfde", footer="dddfe"))

    old_groups = db.get_group_list()

    group_by_edit = random.choice(old_groups)
    group = Group(name="new")
    group.id = group_by_edit.id

    app.group.edit_by_id(group_by_edit.id, group)
    new_groups = db.get_group_list()

    assert len(old_groups) == len(new_groups)

    for element in old_groups:
        if element == group_by_edit:
            element.name = group.name

    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(
            app.group.get_group_list(), key=Group.id_or_max)


def test_edit_header_group_by_index(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="NSKjcndk", header="dfde", footer="dddfe"))

    old_groups = db.get_group_list()

    group_by_edit = random.choice(old_groups)
    group = Group(header="new header")
    group.id = group_by_edit.id
    group.name = group_by_edit.name

    app.group.edit_by_id(group_by_edit.id, group)
    new_groups = db.get_group_list()

    for element in old_groups:
        if element == group_by_edit:
            element.header = group.header

    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(
            app.group.get_group_list(), key=Group.id_or_max)
