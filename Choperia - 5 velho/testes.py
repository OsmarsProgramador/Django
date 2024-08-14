<!-- mesa/templates/mesa/abrir_mesa.html -->
{% extends "core/base.html" %}

{% load static %}

{% block content %}
    <nav class="navbar navbar-expand-md" style="width: 65%; margin: 0 auto;">
        <div class="ms-auto d-flex justify-content-center">
            <button type="button" class="btn btn-primary rounded-pill btn-custom" data-bs-toggle="modal" data-bs-target="#mesaModal"> 
                <i class='bx bx-plus-circle'></i> 
                <span class="text">Add Produto</span> 
            </button>
        </div>
    </nav>
    <!-- Div que exibe a mesa aberta -->
    <div id="mesa-aberta">
        {% include 'mesa/partials/htmx_componentes/uma_mesa_aberta.html' %}
    </div>

    <!-- Modal para adicionar produto a mesa -->
    <div class="modal fade" id="mesaModal" tabindex="-1" aria-labelledby="mesaModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="mesaModalLabel">Adicionar Produto</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <ul class="nav nav-tabs" id="myTab" role="tablist">
                        <li class="nav-item" role="presentation">
                            <button class="nav-link active" id="table-tab" data-bs-toggle="tab" data-bs-target="#table" type="button" role="tab" aria-controls="table" aria-selected="true">Tabela</button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" id="grid-tab" data-bs-toggle="tab" data-bs-target="#grid" type="button" role="tab" aria-controls="grid" aria-selected="false">Grade</button>
                        </li>
                    </ul>
                    <div class="tab-content" id="myTabContent">
                        <div class="tab-pane fade show active" id="table" role="tabpanel" aria-labelledby="table-tab">
                            <!-- Conteúdo da Tabela -->
                            <table class="table mt-3">
                                <thead>
                                    <tr>
                                        <th>Nome</th>
                                        <th>Categoria</th>
                                        <th>Preço</th>
                                        <th>Ação</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for produto in produtos %}
                                    <tr>
                                        <td>{{ produto.nome_produto }}</td>
                                        <td>{{ produto.categoria.nome }}</td>
                                        <td>{{ produto.venda }}</td>
                                        <td>
                                            <form class="add-produto-form" 
                                                method="post"
                                                hx-post="{% url 'mesa:adicionar_item_mesa' mesa.id produto.id %}" 
                                                hx-target="#item-list" 
                                                hx-swap="innerHTML">
                                                
                                                {% csrf_token %}
                                                <input type="number" name="quantidade" value="1" min="1" class="form-control mb-2">
                                                <button type="submit" class="btn btn-success">Adicionar</button>
                                            </form>
                                        </td>
                                    </tr>
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                        <div class="tab-pane fade" id="grid" role="tabpanel" aria-labelledby="grid-tab">
                            <!-- Conteúdo da Grade -->
                            <div class="row mt-3">
                                {% for produto in produtos %}
                                <div class="col-md-4">
                                    <div class="card mb-3">
                                        {% if produto.imagem %}
                                            <img src="{{ produto.imagem.url }}" class="card-img-top" alt="{{ produto.nome_produto }}">
                                        {% else %}
                                            <img src="{% static 'img/default.png' %}" class="card-img-top" alt="Imagem não disponível">
                                        {% endif %}

                                        <div class="card-body">
                                            <h5 class="card-title">{{ produto.nome_produto }}</h5>
                                            <p class="card-text">{{ produto.categoria.nome }}</p>
                                            <p class="card-text">R${{ produto.venda }}</p>
                                            <form class="add-produto-form" 
                                                method="post" 
                                                hx-post="{% url 'mesa:adicionar_item_mesa' mesa.id produto.id %}" 
                                                hx-target="#item-list" 
                                                hx-swap="innerHTML">

                                                {% csrf_token %}
                                                <input type="number" name="quantidade" value="1" min="1" class="form-control mb-2">
                                                <button type="submit" class="btn btn-success">Adicionar</button>
                                            </form>
                                            
                                        </div>
                                    </div>
                                </div>
                                {% endfor %}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <!-- Modal de confirmação para excluir item -->
    <div class="modal fade" id="excluirItemModal" tabindex="-1" aria-labelledby="excluirItemModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <form method="post" action="{% url 'mesa:excluir_item' mesa.id %}">
                    {% csrf_token %}
                    <div class="modal-header">
                        <h5 class="modal-title" id="excluirItemModalLabel">Excluir Item</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <p>Você tem certeza que deseja excluir este item?</p>
                        <div class="form-group">
                            <label for="quantidade">Quantidade:</label>
                            <input type="number" name="quantidade" id="quantidade" class="form-control" value="1" min="1">
                        </div>
                        <input type="hidden" name="item_codigo" id="itemCodigo">
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="submit" class="btn btn-danger">Excluir</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            var excluirItemModal = document.getElementById('excluirItemModal');
            excluirItemModal.addEventListener('show.bs.modal', function (event) {
                var button = event.relatedTarget;
                var itemCodigo = button.getAttribute('data-item-codigo');
                var inputItemCodigo = excluirItemModal.querySelector('#itemCodigo');
                inputItemCodigo.value = itemCodigo;
            });
        });


    </script>

{% endblock %}


<!-- mesa/templates/mesa/mesa_form.html -->
{% extends "core/base.html" %}

{% block content %}
<div class="container mt-5">
    <h2>Cadastro de Nova Mesa</h2>
    <form class="add-produto-form" 
        method="post" 
        hx-post="{% url 'mesa:adicionar_item_mesa' mesa.id produto.id %}" 
        hx-target="#item-list" 
        hx-swap="innerHTML"
    >
        {% csrf_token %}
        <input type="number" name="quantidade" value="1" min="1" class="form-control" style="width: 60px; display: inline-block;">
        <button type="submit" class="btn btn-success">Adicionar</button>
    </form>    
</div>
{% endblock %}


<!-- mesa/templates/mesa/partials/htmx_componentes/uma_mesa_aberta.html -->
<div class="container-fluid mt-0 pt-0">
    <div class="row" style="height: 80vh;">
        <!-- Informações da mesae do atendente -->
        <div class="col-md-4" style="height: 100%;">
            <div class="card border-light mb-3 h-100">
                <div class="card-header">
                    <div class="card-header" style="margin-right: 5px;">
                        <span style="color: green; font-weight: bold;">Mesa: {{ mesa.nome }}</span>
                    </div>
                </div>
                <div class="card-body">
                    <h5 class="card-title">
                        <div class="card-body" style="display: flex; align-items: center; height: 5vh;">
                            <ul class="list-group list-group-flush" style="display: flex; align-items: center; list-style: none; padding: 0; margin: 0;">
                                <li class="list-group-item" style="color: green; font-weight: bold; margin-right: 5px;">{{ mesa.nome }}</li>
                            </ul>
                            <ul class="list-group list-group-flush" style="display: flex; align-items: center; list-style: none; padding: 0; margin: 0;">
                                <li class="list-group-item" style="color: black; font-weight: bold; margin-right: 5px;">Pedido: {{ mesa.pedido }}</li>
                            </ul>
                            <ul class="list-group list-group-flush" style="display: flex; align-items: center; list-style: none; padding: 0; margin: 0;">
                                <li class="list-group-item" style="background-color: green; color: white; font-weight: bold;">Em aberto</li>
                            </ul>
                        </div>
                    </h5>
                    <p class="card-text">
                        <div class="col-md">
                            <hr>
                            <form method="post" action="{% url 'mesa:update_user' mesa.id %}">
                                {% csrf_token %}
                                <div class="form-group mx-2">
                                    <label for="usuario">Atendente:</label>
                                    <select id="usuario" name="usuario" class="form-control">
                                        {% for user in usuarios %}
                                            <option value="{{ user.id }}" {% if user.id == mesa.usuario.id %}selected{% endif %}>
                                                {{ user.username }}
                                            </option>
                                        {% endfor %}
                                    </select>
                                </div>
                                <button type="submit" class="btn btn-primary mt-3 mx-2">Atualizar Usuário</button>
                            </form>
                        </div>
                    </p>
                </div>
            </div> 
        </div>

        <!-- Informações da Comanda de pedido -->
        <div class="col-md-6" style="height: 100%;">
            <div class="card border-light mb-3 h-100">
                {% if mesa.itens %}
                    <h2 class="mt-3 px-2">Comanda de pedido: {{ mesa.pedido }}</h2>
                    <ul id="item-list">
                        {% include 'mesa/partials/item_list.html' %}
                    </ul>
                    <a href="{% url 'mesa:gerar_comanda_pdf' mesa.id %}" class="btn btn-secondary mt-3">Imprimir Comanda</a>
                {% else %}
                    <h>Nenhum produto na comanda</h>
                {% endif %}
            </div>
        </div>
        
    </div>
</div>



