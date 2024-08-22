# mesa/views.py
import os
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render
from .models import Mesa
from produto.models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from usuario.models import Usuario
from django.http import HttpResponse
from django.utils import timezone

# pip install reportlab - para imprimir comanda
# from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.units import mm

# mesa/views.py
from django.conf import settings
from empresa.models import Empresa

def get_empresa_padrao():
    return Empresa.objects.get(cnpj=settings.DEFAULT_EMPRESA_CNPJ)

""" 
Resumo Visual do Passo a Passo
Template URL Tag: {% url 'mesa:list_mesa' %}
Resolução da URL: Encontrar a URL correspondente em urls.py
Mapeamento para View: views.MesaListView.as_view()
Chamada de as_view: Criação da função de view
Método dispatch: Determinar o método HTTP e chamar get
Método get: Chamar get_context_data
Método get_context_data: Adicionar dados ao contexto
Renderização: Renderizar o template com o contexto
Isso mostra como Django sabe como chegar ao método get_context_data quando você clica no link "Listar mesas".
"""
"""O uso do LoginRequiredMixin tem como objetivo garantir que apenas usuários autenticados possam acessar essa view."""

class MesaListView(LoginRequiredMixin, ListView):
    model = Mesa
    template_name = 'mesa/list_mesa.html'
    context_object_name = 'mesas'
    paginate_by = 10

    def get_queryset(self):
        # Ordena o queryset antes da paginação
        return Mesa.objects.all().order_by('nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Verifique se o usuário logado tem um perfil de Usuario
        try:
            context['usuario_logado'] = self.request.user.usuario
        except Usuario.DoesNotExist:
            # Se não houver perfil, você pode definir um comportamento padrão
            context['usuario_logado'] = None  # Ou qualquer tratamento desejado

        context['mesas_abertas'] = Mesa.objects.filter(status='Aberta').order_by('nome')
        context['mesas_fechadas'] = Mesa.objects.filter(status='Fechada').order_by('nome')
        
        # Obtém as mesas já existentes no banco de dados
        mesas_existentes = set(Mesa.objects.values_list('nome', flat=True))

        # Gera uma lista de mesas entre 1 e 30 que não estão no banco de dados
        context['mesas_disponiveis'] = [f'{str(i).zfill(2)}' for i in range(1, 31) if f'{str(i).zfill(2)}' not in mesas_existentes]

        # Adiciona o usuário logado ao contexto
        context['usuario_logado'] = self.request.user.usuario  # Acessa o modelo Usuario relacionado ao User

        return context

class AbrirMesaView(View):
    def get(self, request, id_mesa):
        print("Abrir mesa em Get")
        mesa = get_object_or_404(Mesa, id=id_mesa)
        usuarios = Usuario.objects.all()
        print(f"Todos Usuarios: {usuarios}")
        produtos = Produto.objects.all()

        # Cálculo do total de cada item e o total geral no backend
        itens_calculados = []
        total_geral = 0
        
        for item in mesa.itens:
            total_item = item['quantidade'] * item['preco_unitario']
            itens_calculados.append({
                'nome_produto': item['nome_produto'],
                'quantidade': item['quantidade'],
                'preco_unitario': item['preco_unitario'],
                'total_item': total_item,
            })
            total_geral += total_item

        # Obter a data e hora atual
        now = timezone.now()

        # Inclua o `usuario` atualmente associado à mesa no contexto
        usuario_atual = self.request.user.usuario  # Acessa o modelo Usuario relacionado ao User
        print(f"Usuario Atual: {usuario_atual}")
        return render(request, 'mesa/abrir_mesa.html', {
            'mesa': mesa, 
            'usuarios': usuarios, 
            'usuario_atual_nome': usuario_atual,
            'produtos': produtos,            
            'itens_calculados': itens_calculados,  # Enviar os itens calculados para o template
            'total_geral': total_geral,  # Enviar o total geral para o template
            'now': now,  # Passar a data e hora atual para o template
        })

from usuario.forms import PasswordForm

class UpdateUserView(View):
    def post(self, request, pk):
        try:
            # Obtenha a mesa associada
            mesa = get_object_or_404(Mesa, pk=pk)
        except Exception as e:
            print(f"Erro ao obter a mesa: {e}")
            return render(request, 'usuario/login.html', {'error': 'Erro ao obter a mesa.'})

        try:
            # Obtenha o ID do usuário e a senha do POST
            usuario_id = request.POST.get('usuario')
            password = request.POST.get('password')
            print(f"ID do Usuário Selecionado: {usuario_id}")
        except Exception as e:
            print(f"Erro ao obter dados do formulário: {e}")
            return render(request, 'usuario/login.html', {'error': 'Erro ao obter dados do formulário.'})

        try:
            # Obtenha o objeto Usuario diretamente pelo ID
            usuario = get_object_or_404(Usuario, pk=usuario_id)
            user = usuario.user  # Agora obtemos o User relacionado a partir do Usuario
            print(f"Usuário relacionado obtido: {usuario.nome}")
        except Exception as e:
            print(f"Erro ao obter o Usuario: {e}")
            return render(request, 'usuario/login.html', {'error': 'Usuário relacionado não encontrado.'})

        try:
            # Obtenha o objeto Usuario relacionado ao User
            usuario = get_object_or_404(Usuario, user=user)
            print(f"Usuário relacionado obtido: {usuario.nome}")
        except Exception as e:
            print(f"Erro ao obter o Usuario: {e}")
            return render(request, 'usuario/login.html', {'error': 'Usuário relacionado não encontrado.'})

        try:
            # Tente autenticar o usuário com a senha fornecida
            user_authenticated = authenticate(request, username=user.username, password=password)
            print(f"Nome do usuário para atualização: {user.username}")
        except Exception as e:
            print(f"Erro ao autenticar o usuário: {e}")
            return render(request, 'usuario/login.html', {'error': 'Erro ao autenticar o usuário.'})

        if user_authenticated is not None:
            try:
                # Atualize o nome do objeto Usuario conforme o usuário selecionado
                usuario.nome = user.username  # Atribui o nome de usuário correto
                usuario.save()
                print(f"Usuário atualizado: {usuario.nome}")
            except Exception as e:
                print(f"Erro ao salvar o Usuario: {e}")
                return render(request, 'usuario/login.html', {'error': 'Erro ao salvar o usuário.'})

            try:
                # Realize o login do usuário autenticado
                login(request, user_authenticated)
                print(f"Usuário logado: {user.username}")
            except Exception as e:
                print(f"Erro ao realizar login: {e}")
                return render(request, 'usuario/login.html', {'error': 'Erro ao realizar login.'})

            # Redireciona para a página com a mesa atualizada
            return redirect('mesa:abrir_mesa', id_mesa=pk)
        else:
            # Se a autenticação falhar, mostre uma mensagem de erro
            print("Falha na autenticação. Senha incorreta.")
            return render(request, 'usuario/login.html', {'error': 'Senha incorreta. Tente novamente.'})


"""
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Modelo usado para uma visão do usuário, não indicado para impressão térmica
class GerarComandaPDFView(LoginRequiredMixin, View):
    def get(self, request, mesa_id):
        mesa = get_object_or_404(Mesa, pk=mesa_id)

        # Configura o response para PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="comanda_{mesa_id}.pdf"'

        # Define o tamanho do papel: 80mm de largura, altura ajustável
        largura = 80 * mm
        altura = 200 * mm  # Ajuste a altura conforme necessário
        p = canvas.Canvas(response, pagesize=(largura, altura))

        # Define a posição inicial para o texto
        y = altura - 10 * mm  # Margem superior

        # Cabeçalho da comanda
        p.setFont("Helvetica-Bold", 12)
        p.drawCentredString(largura / 2.0, y, "[Nome da Loja]")
        y -= 5 * mm
        p.setFont("Helvetica", 8)
        p.drawCentredString(largura / 2.0, y, "[Endereço]")
        y -= 4 * mm
        p.drawCentredString(largura / 2.0, y, "[Telefone]")
        y -= 4 * mm
        p.drawCentredString(largura / 2.0, y, "[CNPJ]")
        y -= 6 * mm
        p.drawString(5 * mm, y, f"Data: {timezone.now().strftime('%d/%m/%Y')}    Hora: {timezone.now().strftime('%H:%M')}")
        y -= 6 * mm

        p.drawString(5 * mm, y, "-" * 32)
        y -= 6 * mm

        # Tabela de itens
        p.setFont("Helvetica-Bold", 8)
        p.drawString(5 * mm, y, "Item")
        p.drawString(40 * mm, y, "Qtde")
        p.drawString(50 * mm, y, "Valor Unit.")
        p.drawString(65 * mm, y, "Total")
        y -= 5 * mm
        p.setFont("Helvetica", 8)
        p.drawString(5 * mm, y, "-" * 32)
        y -= 5 * mm

        # Listar os itens da mesa
        for item in mesa.itens:
            nome_produto = item['nome_produto']
            quantidade = item['quantidade']
            preco_unitario = item['preco_unitario']
            valor_total = quantidade * preco_unitario

            preco_unitario_str = f"R$ {preco_unitario:,.2f}".replace('.', ',')
            valor_total_str = f"R$ {valor_total:,.2f}".replace('.', ',')

            p.drawString(5 * mm, y, nome_produto[:12]) # Limite o nome do produto a 12 caracteres
            p.drawString(43 * mm, y, f"{quantidade}")
            p.drawString(50 * mm, y, f"{preco_unitario_str}")
            p.drawString(65 * mm, y, f"{valor_total_str}")
            y -= 5 * mm

            if y < 10 * mm:  # Evita ultrapassar o final da página
                p.showPage()
                y = altura - 10 * mm

        # Subtotal, Desconto e Total
        subtotal = sum(item['quantidade'] * item['preco_unitario'] for item in mesa.itens)
        desconto = 0  # Ajuste conforme necessário
        total = subtotal - desconto

        p.drawString(5 * mm, y, "-" * 32)
        y -= 6 * mm
        p.drawString(5 * mm, y, f"Subtotal: R$ {subtotal:.2f}")
        y -= 5 * mm
        p.drawString(5 * mm, y, f"Desconto: R$ {desconto:.2f}")
        y -= 5 * mm
        p.drawString(5 * mm, y, f"Total:    R$ {total:.2f}")
        y -= 6 * mm
        p.drawString(5 * mm, y, "-" * 32)
        y -= 6 * mm
        p.drawString(5 * mm, y, "Forma de Pagamento: Dinheiro")
        y -= 6 * mm
        p.drawString(5 * mm, y, "-" * 32)
        y -= 6 * mm

        # Mensagem de agradecimento
        p.setFont("Helvetica-Bold", 10)
        p.drawCentredString(largura / 2.0, y, "Obrigado pela preferência!")

        # Finaliza o PDF
        p.showPage()
        p.save()

        return response

"""
from reportlab.lib.pagesizes import A4
from datetime import datetime  # Adicione esta linha
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

# Modelo adequado para enviar para uma impreeora térmica
# Fonte Monoespaçada: É necessário garantir que o texto enviado para 
# a impressora esteja formatado para uma fonte monoespaçada (como Courier). 
# Isso alinha corretamente os dados.

# Método que gera a comanda do caixa em PDF
class GerarComandaPDFView(LoginRequiredMixin, View):
    def get(self, request, mesa_id):
       # Obtenha o usuário autenticado
        user = request.user
        
        # Encontre o correspondente no modelo Usuario (se for necessário)
        usuario_logado = get_object_or_404(Usuario, user=user)

        mesa = get_object_or_404(Mesa, pk=mesa_id)
        empresa = get_empresa_padrao() 

        usuarios = Usuario.objects.all()
        print(f"Funcionario: {usuario_logado.nome}")              

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="comanda_{mesa_id}.pdf"'

        p = canvas.Canvas(response)

        largura = 80 * mm
        altura = 297 * mm  # Tamanho A4 para o exemplo, ajustar conforme a necessidade

        # Fonte monoespaçada
        p.setFont("Courier", 10)

        # Cabeçalho
        p.drawString(5, altura - 20, "------------------------------")
        p.drawString(5, altura - 30, empresa.nome)
        p.drawString(5, altura - 40, empresa.endereco)
        p.drawString(5, altura - 50, f"CNPJ: {empresa.cnpj}")
        p.drawString(5, altura - 60, f"Telefone: {empresa.telefone}")
        p.drawString(5, altura - 70, "------------------------------")

        # Exibindo a Mesa e Funcionário
        p.drawString(5, altura - 80, f"Mesa: {mesa.nome}")
        p.drawString(5, altura - 90, f"Funcionário: {usuario_logado.nome}")
        p.drawString(5, altura - 100, "------------------------------")
        
        # Data e Hora
        p.drawString(5, altura - 120, f"Data: {datetime.now().strftime('%d/%m/%Y')}")
        p.drawString(5, altura - 130, f"Hora: {datetime.now().strftime('%H:%M:%S')}")
        p.drawString(5, altura - 140, "------------------------------")

        # Cabeçalho da Tabela
        p.drawString(5, altura - 150, "Item        Qtde  Unit   Total")
        p.drawString(5, altura - 160, "------------------------------")

        y = altura - 170
        total = 0

        # Itens
        for item in mesa.itens:
            nome = item['nome_produto']
            quantidade = str(item['quantidade']).rjust(4)
            preco_unitario = item['preco_unitario']
            preco_total = item['quantidade'] * item['preco_unitario']
            total += preco_total
            preco_unitario_str = f"{preco_unitario:,.2f}".replace('.', ',').rjust(6)
            preco_total_str = f"{preco_total:,.2f}".replace('.', ',').rjust(7)

            # Quebra o nome em múltiplas linhas se necessário
            linhas_nome = [nome[i:i+10] for i in range(0, len(nome), 10)]

            for linha in linhas_nome:
                p.drawString(5, y, f"{linha.ljust(10)} {quantidade} {preco_unitario_str} {preco_total_str}")
                y -= 10
                # Só mostra a quantidade, valor unitário e total na primeira linha
                quantidade = ""
                preco_unitario_str = ""
                preco_total_str = ""

        p.drawString(5, y, "------------------------------")
        y -= 10

        # Subtotal e Total
        p.drawString(5, y, f"Subtotal:           R$ {total:.2f}".replace('.', ','))
        y -= 10

        desconto = 5.00  # Exemplo
        p.drawString(5, y, f"Desconto:           R$ {desconto:.2f}".replace('.', ','))
        y -= 10

        total_final = total - desconto
        p.drawString(5, y, f"Total:              R$ {total_final:.2f}".replace('.', ','))
        y -= 10

        p.drawString(5, y, "------------------------------")
        y -= 10

        # Forma de Pagamento
        p.drawString(5, y, "Forma de Pagamento: Dinheiro")
        y -= 20

        # Agradecimento
        p.drawCentredString(largura / 2, y, "Obrigado pela preferência!")
        p.showPage()
        p.save()

        # Gera a comanda PDF e envia para a impressora da cozinha
        self.enviar_para_cozinha(request, mesa.id)  # Aqui usa 'mesa.id' ao invés de 'mesa'

        return response

    def enviar_para_cozinha(self, request, mesa_id):
        response = EnviarParaCozinhaView().post(request, mesa_id)
        return response

    
    
from escpos.printer import Network
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Mesa
from datetime import datetime

"""class EnviarParaCozinhaView(View): # Envia via ip
    def post(self, request, mesa_id):
        mesa = get_object_or_404(Mesa, pk=mesa_id)
        
        try:
            # Conecte-se à impressora via IP
            impressora = Network("192.168.0.100")  # IP da impressora de cozinha
            
            # Cabeçalho do Pedido
            impressora.set(align='center', bold=True)
            impressora.text("Pedido de Cozinha\n")
            impressora.text(f"Mesa: {mesa.nome}\n")
            impressora.text(f"Data: {datetime.now().strftime('%d/%m/%Y')}\n")
            impressora.text(f"Hora: {datetime.now().strftime('%H:%M:%S')}\n")
            impressora.text("-----------------------------\n")
            
            # Itens do Pedido
            impressora.set(align='left', bold=False)
            for item in mesa.itens:
                impressora.text(f"{item['nome_produto']}\n")
                impressora.text(f"Quantidade: {item['quantidade']}\n")
                if 'descricao' in item:
                    impressora.text(f"Descrição: {item['descricao']}\n")
                impressora.text("-----------------------------\n")

            # Finalizar o Pedido
            impressora.set(align='center', bold=True)
            impressora.text("----- FIM DO PEDIDO -----\n")
            impressora.cut()  # Comando para cortar o papel
            
            impressora.close()
            return HttpResponse("Pedido enviado para a cozinha com sucesso!")
        
        except Exception as e:
            return HttpResponse(f"Erro ao enviar para a cozinha: {str(e)}", status=500)"""

class EnviarParaCozinhaView(View): # Envia via arquivo txt
    def post(self, request, mesa_id):
        mesa = get_object_or_404(Mesa, pk=mesa_id)
        itens_calculados = [
            {
                'nome_produto': item['nome_produto'],
                'quantidade': item['quantidade'],
                'descricao': item.get('descricao', 'N/A')
            }
            for item in mesa.itens
        ]

        # Simulação de impressão em arquivo
        try:
            caminho_arquivo = os.path.join(os.path.dirname(__file__), "saida_cozinha.txt")
            with open(caminho_arquivo, "w") as file:
                file.write("---- COMANDA DE COZINHA ----\n")
                file.write(f"Mesa: {mesa.nome}  Pedido: {mesa.pedido}\n")
                file.write(f"Data: {datetime.now().strftime('%d/%m/%Y')}\n")
                file.write(f"Hora: {datetime.now().strftime('%H:%M:%S')}\n")
                file.write("-----------------------------\n")
                for item in itens_calculados:
                    file.write(f"{item['nome_produto']} - {item['quantidade']}\n")
                    file.write(f"Descrição: {item['descricao']}\n")
                file.write("-----------------------------\n")
                file.write("Preparar com atenção!\n")

        except Exception as e:
            return HttpResponse(f"Erro ao enviar para a cozinha: {str(e)}", status=500)

        return HttpResponse("Comanda enviada para a cozinha (simulada).")


class ExcluirItemView(LoginRequiredMixin, View):
    def post(self, request, pk):
        mesa = get_object_or_404(Mesa, pk=pk)
        item_codigo = request.POST.get('item_codigo')
        quantidade = int(request.POST.get('quantidade', 1))

        item_removido = False
        for item in mesa.itens:
            if item['codigo'] == item_codigo:
                if item['quantidade'] > quantidade:
                    item['quantidade'] -= quantidade
                else:
                    mesa.itens.remove(item)
                item_removido = True
                break

        if item_removido:
            try:
                produto = Produto.objects.get(codigo=item_codigo)
                produto.estoque += quantidade
                produto.save()
            except Produto.DoesNotExist:
                pass

            total_itens = sum(item['quantidade'] for item in mesa.itens)

            if total_itens <= 0:
                mesa.itens = []
                mesa.status = 'Fechada'
                mesa.pedido = 0

            mesa.save()

        return redirect('mesa:abrir_mesa', pk=pk)




