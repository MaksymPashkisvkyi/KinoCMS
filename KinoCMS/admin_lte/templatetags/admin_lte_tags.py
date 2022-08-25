from django import template

register = template.Library()


@register.inclusion_tag('admin_lte/base/table_buttons.html')
def table_buttons():
    buttons = [
        {
            'class': 'edit fa fa-edit text-decoration-none text-reset',
            'title': 'Edit'
        },
        {
            'class': 'delete fa fa-trash text-decoration-none text-reset',
            'title': 'Delete'
        }
    ]
    return {'buttons': buttons}


@register.inclusion_tag('admin_lte/base/sidebar_menu.html')
def show_side_menu():
    menu = [
        {'title': "Статистика", 'url': "admin_statistic"},
        {'title': "Баннера/Слайдеры", 'url': "admin_banner"},
        {'title': "Фильмы", 'url': "admin_film"},
        {'title': "Кинотеатры", 'url': "admin_cinema"},
        {'title': "Новости#", 'url': "admin_statistic"},
        {'title': "Акции#", 'url': "admin_statistic"},
        {'title': "Страницы#", 'url': "admin_statistic"},
        {'title': "Пользователи", 'url': "admin_user"},
        {'title': "Рассылка#", 'url': "admin_statistic"}
    ]
    return {'menu': menu}
