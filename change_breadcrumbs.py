# 1、后端方法返回context字典中加入：title、has_view_permission、opts
context = {
            'title': title,
            'has_view_permission': self.has_view_permission(request),
            'opts': self.opts
        }
return render(request, 'admin/xxx/xxx/xxx.html', context=context)

#2、中间页重写breadcrumbs：
{% extends 'admin/base_site.html' %}
{% load i18n admin_urls static admin_list %}

{% block breadcrumbs %}
    <div class="breadcrumbs">
        <a href="{% url 'admin:index' %}">{% trans 'Home' %}</a> &rsaquo;
        <a href="{% url 'admin:app_list' app_label=opts.app_label %}">
            {{ opts.app_config.verbose_name }}
        </a> &rsaquo;
        {% if has_view_permission %}
            <a href="{% url opts|admin_urlname:'changelist' %}">{{ opts.verbose_name_plural|capfirst }}</a>
        {% else %}{{ opts.verbose_name_plural|capfirst }}
        {% endif %}
        {% if title %} &rsaquo; {{ title }}{% endif %}
    </div>
{% endblock %}
