<td class="text-end">
    <button class="btn btn-warning" style="cursor: pointer;"
        data-bs-toggle="modal" data-bs-target="#editProdutoModal"
        hx-get="{% url 'produto:edit_produto' produto.id %}" 
        hx-target="#editProdutoForm">Editar</button>
    <button class="btn btn-danger" style="cursor: pointer;"
        hx-delete="{% url 'produto:delete_produto' produto.id %}"
        hx-trigger="click"
        hx-target="#list-produto">Excluir</button>
</td>



<!-- produto/partials/htmx_componentes/edit_produto_row.html -->
{% load custom_filters %}
<tr hx-trigger='cancel' class='editing' hx-get="{% url 'produto:edit_produto' produto.id %}">
    <td><input name='nome_produto' value='{{ form.instance.nome_produto }}' class="form-control"></td>
    <td><input name='venda' value="{{ form.instance.venda|stringformat:"f"|floatformat:2|replace_comma }}" type="number" step="0.01" class="form-control"></td>
    <td><input name='codigo' value='{{ form.instance.codigo }}' class="form-control"></td>
    <td><input name='estoque' value='{{ form.instance.estoque }}' type="number" class="form-control"></td>
