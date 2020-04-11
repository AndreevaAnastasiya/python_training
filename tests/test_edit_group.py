from models.group import Group
from random import randrange


def test_edit_name_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NSKjcndk", header="dfde", footer="dddfe"))

    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))
    group = Group(name="new")
    group.id = old_groups[index].id

    app.group.edit_by_index(index, group)
    new_groups = app.group.get_group_list()

    assert len(old_groups) == len(new_groups)

    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)


def test_edit_header_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NSKjcndk", header="dfde", footer="dddfe"))

    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))
    group = Group(header="new header")
    group.id = old_groups[index].id
    group.name = old_groups[index].name

    app.group.edit_by_index(index, group)
    new_groups = app.group.get_group_list()

    assert len(old_groups) == len(new_groups)

    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)
