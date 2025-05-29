import tkinter as tk
from tkinter import messagebox, ttk
import random

class ProjetoAVA:
    def _init_(self, root):
        self.root = root
        self.root.title("Projeto AVA - Digital Education")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f8ff")
        
        # Dados simulados de usuários
        self.usuarios = {
            "aluno": {"senha": "1234", "cursos": {
                "Python": {"progresso": 0, "aulas_completas": [], "nota": 0},
                "Cyber Segurança": {"progresso": 0, "aulas_completas": [], "nota": 0},
                "Privacidade": {"progresso": 0, "aulas_completas": [], "nota": 0}
            }},
            "admin": {"senha": "admin", "cursos": {
                "Python": {"progresso": 100, "aulas_completas": [1,2,3], "nota": 9.5},
                "Cyber Segurança": {"progresso": 100, "aulas_completas": [1,2,3], "nota": 8.7},
                "Privacidade": {"progresso": 100, "aulas_completas": [1,2,3], "nota": 9.0}
            }}
        }
        
        self.usuario_atual = None
        self.curso_atual = None
        
        # Cores e estilos
        self.cor_principal = "#4682b4"
        self.cor_secundaria = "#5f9ea0"
        self.cor_destaque = "#ff7f50"
        
        # Fontes
        self.fonte_titulo = ("Arial", 24, "bold")
        self.fonte_subtitulo = ("Arial", 16)
        self.fonte_normal = ("Arial", 12)
        
        self.criar_tela_login()
    
    def criar_tela_login(self):
        self.limpar_tela()
        
        # Frame principal
        frame = tk.Frame(self.root, bg=self.cor_principal, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Título
        titulo = tk.Label(frame, text="Projeto AVA", font=self.fonte_titulo, 
                         bg=self.cor_principal, fg="white")
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Subtítulo
        subtitulo = tk.Label(frame, text="Digital Education", font=self.fonte_subtitulo, 
                            bg=self.cor_principal, fg="white")
        subtitulo.grid(row=1, column=0, columnspan=2, pady=(0, 30))
        
        # Campo usuário
        lbl_usuario = tk.Label(frame, text="Usuário:", font=self.fonte_normal, 
                              bg=self.cor_principal, fg="white")
        lbl_usuario.grid(row=2, column=0, sticky="e", padx=(0, 10))
        
        self.entry_usuario = tk.Entry(frame, font=self.fonte_normal)
        self.entry_usuario.grid(row=2, column=1, pady=5)
        
        # Campo senha
        lbl_senha = tk.Label(frame, text="Senha:", font=self.fonte_normal, 
                            bg=self.cor_principal, fg="white")
        lbl_senha.grid(row=3, column=0, sticky="e", padx=(0, 10))
        
        self.entry_senha = tk.Entry(frame, show="*", font=self.fonte_normal)
        self.entry_senha.grid(row=3, column=1, pady=5)
        
        # Botão login
        btn_login = tk.Button(frame, text="Login", font=self.fonte_normal, 
                             bg=self.cor_destaque, fg="white", 
                             command=self.fazer_login)
        btn_login.grid(row=4, column=0, columnspan=2, pady=(20, 10), sticky="we")
        
        # Botão cadastro
        btn_cadastro = tk.Button(frame, text="Cadastrar", font=self.fonte_normal, 
                                bg=self.cor_secundaria, fg="white", 
                                command=self.criar_tela_cadastro)
        btn_cadastro.grid(row=5, column=0, columnspan=2, pady=(0, 10), sticky="we")
        
        # Dica animada
        self.dica_label = tk.Label(frame, text="Dica: Use 'aluno' e '1234' para testar", 
                                  font=("Arial", 10), bg=self.cor_principal, fg="white")
        self.dica_label.grid(row=6, column=0, columnspan=2, pady=(20, 0))
        
        # Animação simples
        self.animar_dica()
    
    def animar_dica(self):
        cores = ["#ff7f50", "#ffa07a", "#ffb6c1", "#98fb98", "#afeeee"]
        cor_atual = self.dica_label.cget("fg")
        nova_cor = random.choice([c for c in cores if c != cor_atual])
        self.dica_label.config(fg=nova_cor)
        self.root.after(1000, self.animar_dica)
    
    def criar_tela_cadastro(self):
        self.limpar_tela()
        
        # Frame principal
        frame = tk.Frame(self.root, bg=self.cor_principal, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Título
        titulo = tk.Label(frame, text="Cadastro", font=self.fonte_titulo, 
                         bg=self.cor_principal, fg="white")
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Campos de cadastro
        campos = [
            ("Usuário:", "entry_usuario"),
            ("Senha:", "entry_senha"),
            ("Confirmar Senha:", "entry_confirmar_senha"),
            ("Email:", "entry_email")
        ]
        
        for i, (texto, nome_var) in enumerate(campos, start=1):
            lbl = tk.Label(frame, text=texto, font=self.fonte_normal, 
                          bg=self.cor_principal, fg="white")
            lbl.grid(row=i, column=0, sticky="e", padx=(0, 10))
            
            entry = tk.Entry(frame, font=self.fonte_normal)
            if "senha" in nome_var:
                entry.config(show="*")
            entry.grid(row=i, column=1, pady=5)
            setattr(self, nome_var, entry)
        
        # Botão cadastrar
        btn_cadastrar = tk.Button(frame, text="Cadastrar", font=self.fonte_normal, 
                                  bg=self.cor_destaque, fg="white", 
                                  command=self.cadastrar_usuario)
        btn_cadastrar.grid(row=len(campos)+1, column=0, columnspan=2, pady=(20, 10), sticky="we")
        
        # Botão voltar
        btn_voltar = tk.Button(frame, text="Voltar", font=self.fonte_normal, 
                              bg=self.cor_secundaria, fg="white", 
                              command=self.criar_tela_login)
        btn_voltar.grid(row=len(campos)+2, column=0, columnspan=2, pady=(0, 10), sticky="we")
    
    def cadastrar_usuario(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()
        email = self.entry_email.get()
        
        if not usuario or not senha or not confirmar_senha:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")
            return
            
        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return
            
        if usuario in self.usuarios:
            messagebox.showerror("Erro", "Usuário já existe!")
            return
            
        # Adiciona novo usuário
        self.usuarios[usuario] = {
            "senha": senha,
            "email": email,
            "cursos": {
                "Python": {"progresso": 0, "aulas_completas": [], "nota": 0},
                "Cyber Segurança": {"progresso": 0, "aulas_completas": [], "nota": 0},
                "Privacidade": {"progresso": 0, "aulas_completas": [], "nota": 0}
            }
        }
        
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        self.criar_tela_login()
    
    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        if usuario in self.usuarios and self.usuarios[usuario]["senha"] == senha:
            self.usuario_atual = usuario
            self.criar_tela_inicial()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
    
    def criar_tela_inicial(self):
        self.limpar_tela()
        
        # Frame principal
        frame = tk.Frame(self.root, bg="#f0f8ff")
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Cabeçalho
        cabecalho = tk.Frame(frame, bg=self.cor_principal)
        cabecalho.pack(fill="x", pady=(0, 20))
        
        # Título
        titulo = tk.Label(cabecalho, text="Digital Education", font=self.fonte_titulo, 
                         bg=self.cor_principal, fg="white")
        titulo.pack(pady=10)
        
        # Mensagem de boas-vindas
        mensagem = tk.Label(frame, text=f"Bem-vindo, {self.usuario_atual}!", 
                           font=self.fonte_subtitulo, bg="#f0f8ff")
        mensagem.pack(pady=(0, 30))
        
        # Frame dos cursos
        frame_cursos = tk.Frame(frame, bg="#f0f8ff")
        frame_cursos.pack()
        
        # Botões dos cursos
        cursos = [
            ("Python", "Aprenda os fundamentos da programação com Python", self.criar_tela_python),
            ("Cyber Segurança", "Introdução à segurança digital", self.criar_tela_cyber),
            ("Privacidade", "Proteção de dados pessoais", self.criar_tela_privacidade),
            ("Estatísticas", "Veja seu progresso", self.criar_tela_estatisticas)
        ]
        
        for i, (nome, descricao, comando) in enumerate(cursos):
            btn_frame = tk.Frame(frame_cursos, bg="#e6f2ff", bd=1, relief="solid")
            btn_frame.grid(row=i, column=0, pady=5, sticky="we")
            
            btn = tk.Button(btn_frame, text=nome, font=self.fonte_normal, 
                           bg=self.cor_secundaria, fg="white", 
                           command=comando)
            btn.pack(side="left", padx=5, pady=5)
            
            lbl_desc = tk.Label(btn_frame, text=descricao, font=("Arial", 10), 
                               bg="#e6f2ff", wraplength=400, justify="left")
            lbl_desc.pack(side="left", fill="x", expand=True, padx=5)
        
        # Botão sair
        btn_sair = tk.Button(frame, text="Sair", font=self.fonte_normal, 
                             bg=self.cor_destaque, fg="white", 
                             command=self.criar_tela_login)
        btn_sair.pack(pady=(20, 0))
    
    def criar_tela_curso(self, nome_curso, aulas):
        self.limpar_tela()
        self.curso_atual = nome_curso
        
        # Frame principal
        frame = tk.Frame(self.root, bg="#f0f8ff")
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Cabeçalho
        cabecalho = tk.Frame(frame, bg=self.cor_principal)
        cabecalho.pack(fill="x", pady=(0, 20))
        
        # Título
        titulo = tk.Label(cabecalho, text=nome_curso, font=self.fonte_titulo, 
                         bg=self.cor_principal, fg="white")
        titulo.pack(pady=10)
        
        # Barra de progresso
        progresso = self.usuarios[self.usuario_atual]["cursos"][nome_curso]["progresso"]
        lbl_progresso = tk.Label(frame, text=f"Progresso: {progresso}%", 
                                font=self.fonte_normal, bg="#f0f8ff")
        lbl_progresso.pack(pady=(0, 5))
        
        progress_bar = ttk.Progressbar(frame, orient="horizontal", 
                                      length=400, mode="determinate", 
                                      value=progresso)
        progress_bar.pack(pady=(0, 20))
        
        # Frame das aulas
        frame_aulas = tk.Frame(frame, bg="#f0f8ff")
        frame_aulas.pack()
        
        # Aulas
        aulas_completas = self.usuarios[self.usuario_atual]["cursos"][nome_curso]["aulas_completas"]
        
        for i, aula in enumerate(aulas, start=1):
            aula_frame = tk.Frame(frame_aulas, bg="#e6f2ff", bd=1, relief="solid")
            aula_frame.pack(fill="x", pady=5)
            
            status = "✓" if i in aulas_completas else "▶"
            cor_status = "green" if i in aulas_completas else "orange"
            
            lbl_status = tk.Label(aula_frame, text=status, font=("Arial", 12), 
                                 fg=cor_status, bg="#e6f2ff")
            lbl_status.pack(side="left", padx=5)
            
            lbl_aula = tk.Label(aula_frame, text=f"Aula {i}: {aula}", 
                               font=self.fonte_normal, bg="#e6f2ff")
            lbl_aula.pack(side="left", padx=5)
            
            if i not in aulas_completas:
                btn_assistir = tk.Button(aula_frame, text="Assistir", 
                                        font=("Arial", 10), bg=self.cor_secundaria, 
                                        fg="white", command=lambda i=i: self.completar_aula(nome_curso, i))
                btn_assistir.pack(side="right", padx=5)
        
        # Botão voltar
        btn_voltar = tk.Button(frame, text="Voltar", font=self.fonte_normal, 
                              bg=self.cor_destaque, fg="white", 
                              command=self.criar_tela_inicial)
        btn_voltar.pack(side="left", pady=(20, 0))
        
        # Botão estatísticas (só aparece se todas as aulas estiverem completas)
        if len(aulas_completas) == len(aulas):
            btn_estatisticas = tk.Button(frame, text="Ver Estatísticas", 
                                         font=self.fonte_normal, 
                                         bg=self.cor_secundaria, fg="white", 
                                         command=self.criar_tela_estatisticas)
            btn_estatisticas.pack(side="right", pady=(20, 0))
            
            btn_prova = tk.Button(frame, text="Fazer Prova", 
                                 font=self.fonte_normal, 
                                 bg="#8a2be2", fg="white", 
                                 command=lambda: self.criar_tela_prova(nome_curso))
            btn_prova.pack(side="right", padx=10, pady=(20, 0))
    
    def completar_aula(self, curso, aula_num):
        if aula_num not in self.usuarios[self.usuario_atual]["cursos"][curso]["aulas_completas"]:
            self.usuarios[self.usuario_atual]["cursos"][curso]["aulas_completas"].append(aula_num)
            
            # Atualiza progresso
            total_aulas = 3 
            progresso = (len(self.usuarios[self.usuario_atual]["cursos"][curso]["aulas_completas"]) / total_aulas) * 100
            self.usuarios[self.usuario_atual]["cursos"][curso]["progresso"] = progresso
            
            messagebox.showinfo("Sucesso", f"Aula {aula_num} marcada como completa!")
            self.criar_tela_curso(curso, self.obter_aulas_curso(curso))
    
    def obter_aulas_curso(self, curso):
        # Simulando aulas para cada curso
        aulas = {
            "Python": [
                "Introdução ao Python",
                "Variáveis e Tipos de Dados",
                "Estruturas de Controle"
            ],
            "Cyber Segurança": [
                "Conceitos Básicos",
                "Ameaças Digitais",
                "Proteção Pessoal"
            ],
            "Privacidade": [
                "O que são Dados Pessoais?",
                "Leis de Proteção",
                "Boas Práticas"
            ]
        }
        return aulas.get(curso, [])
    
    def criar_tela_python(self):
        aulas = self.obter_aulas_curso("Python")
        self.criar_tela_curso("Python", aulas)
    
    def criar_tela_cyber(self):
        aulas = self.obter_aulas_curso("Cyber Segurança")
        self.criar_tela_curso("Cyber Segurança", aulas)
    
    def criar_tela_privacidade(self):
        aulas = self.obter_aulas_curso("Privacidade")
        self.criar_tela_curso("Privacidade", aulas)
    
    def criar_tela_estatisticas(self):
        self.limpar_tela()
        
        # Frame principal
        frame = tk.Frame(self.root, bg="#f0f8ff")
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Cabeçalho
        cabecalho = tk.Frame(frame, bg=self.cor_principal)
        cabecalho.pack(fill="x", pady=(0, 20))
        
        # Título
        titulo = tk.Label(cabecalho, text="Estatísticas", font=self.fonte_titulo, 
                         bg=self.cor_principal, fg="white")
        titulo.pack(pady=10)
        
        # Frame das estatísticas
        frame_stats = tk.Frame(frame, bg="#f0f8ff")
        frame_stats.pack()
        
        # Estatísticas por curso
        cursos = ["Python", "Cyber Segurança", "Privacidade"]
        
        for i, curso in enumerate(cursos):
            stats_frame = tk.Frame(frame_stats, bg="#e6f2ff", bd=1, relief="solid")
            stats_frame.grid(row=i, column=0, pady=5, sticky="we")
            
            lbl_curso = tk.Label(stats_frame, text=curso, font=self.fonte_normal, 
                                bg="#e6f2ff")
            lbl_curso.pack(side="left", padx=5, pady=5)
            
            dados = self.usuarios[self.usuario_atual]["cursos"][curso]
            
            lbl_progresso = tk.Label(stats_frame, 
                                    text=f"Progresso: {dados['progresso']}%", 
                                    font=("Arial", 10), bg="#e6f2ff")
            lbl_progresso.pack(side="left", padx=10)
            
            lbl_nota = tk.Label(stats_frame, 
                               text=f"Nota: {dados['nota'] if dados['nota'] else 'N/A'}", 
                               font=("Arial", 10), bg="#e6f2ff")
            lbl_nota.pack(side="left", padx=10)
        
        # Botão voltar
        btn_voltar = tk.Button(frame, text="Voltar", font=self.fonte_normal, 
                              bg=self.cor_destaque, fg="white", 
                              command=self.criar_tela_inicial)
        btn_voltar.pack(pady=(20, 0))
    
    def criar_tela_prova(self, curso):
        self.limpar_tela()
        
        # Frame principal
        frame = tk.Frame(self.root, bg="#f0f8ff")
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Cabeçalho
        cabecalho = tk.Frame(frame, bg=self.cor_principal)
        cabecalho.pack(fill="x", pady=(0, 20))
        
        # Título
        titulo = tk.Label(cabecalho, text=f"Prova: {curso}", font=self.fonte_titulo, 
                         bg=self.cor_principal, fg="white")
        titulo.pack(pady=10)
        
        # Perguntas (simuladas)
        perguntas = {
            "Python": [
                {"pergunta": "O que é uma variável em Python?", 
                 "opcoes": ["Um valor fixo", "Um nome que referencia um valor", "Um tipo de dado", "Um comando"], 
                 "resposta": 1},
                {"pergunta": "Qual comando imprime algo na tela?", 
                 "opcoes": ["input()", "print()", "write()", "show()"], 
                 "resposta": 1},
                {"pergunta": "Como se inicia um loop for em Python?", 
                 "opcoes": ["for i in range", "for (i=0; i<10; i++)", "loop i from 1 to 10", "for each i in list"], 
                 "resposta": 0}
            ],
            "Cyber Segurança": [
                {"pergunta": "O que é phishing?", 
                 "opcoes": ["Um tipo de vírus", "Pescar dados pessoais enganando usuários", "Um ataque de negação de serviço", "Um método de criptografia"], 
                 "resposta": 1},
                {"pergunta": "Qual destes é um exemplo de senha forte?", 
                 "opcoes": ["123456", "password", "Senha@2023!", "nome123"], 
                 "resposta": 2},
                {"pergunta": "O que é autenticação de dois fatores?", 
                 "opcoes": ["Usar duas senhas", "Confirmar identidade por dois métodos diferentes", "Ter duas contas de usuário", "Usar dois dispositivos"], 
                 "resposta": 1}
            ],
            "Privacidade": [
                {"pergunta": "O que são dados pessoais?", 
                 "opcoes": ["Informações sobre dispositivos", "Qualquer informação relacionada a uma pessoa", "Apenas documentos oficiais", "Dados financeiros"], 
                 "resposta": 1},
                {"pergunta": "Qual lei brasileira protege dados pessoais?", 
                 "opcoes": ["Lei do Direito Autoral", "LGPD", "Lei do Software", "Marco Civil da Internet"], 
                 "resposta": 1},
                {"pergunta": "Quando podemos compartilhar dados pessoais?", 
                 "opcoes": ["Sempre que necessário", "Apenas com autorização", "Quando não forem importantes", "Quando recebermos algo em troca"], 
                 "resposta": 1}
            ]
        }
        
        self.respostas_usuario = [None] * len(perguntas[curso])
        
        # Frame das perguntas
        frame_perguntas = tk.Frame(frame, bg="#f0f8ff")
        frame_perguntas.pack()
        
        for i, pergunta in enumerate(perguntas[curso]):
            pergunta_frame = tk.Frame(frame_perguntas, bg="#e6f2ff", bd=1, relief="solid")
            pergunta_frame.pack(fill="x", pady=5)
            
            lbl_pergunta = tk.Label(pergunta_frame, 
                                   text=f"{i+1}. {pergunta['pergunta']}", 
                                   font=self.fonte_normal, bg="#e6f2ff", 
                                   wraplength=600, justify="left")
            lbl_pergunta.pack(anchor="w", padx=5, pady=5)
            
            for j, opcao in enumerate(pergunta['opcoes']):
                rb = tk.Radiobutton(pergunta_frame, text=opcao, 
                                    font=("Arial", 10), bg="#e6f2ff", 
                                    variable=tk.IntVar(value=self.respostas_usuario[i] if self.respostas_usuario[i] is not None else -1), 
                                    value=j, 
                                    command=lambda i=i, j=j: self.marcar_resposta(i, j))
                rb.pack(anchor="w", padx=20)
        
        # Botões
        frame_botoes = tk.Frame(frame, bg="#f0f8ff")
        frame_botoes.pack(pady=(20, 0))
        
        btn_concluir = tk.Button(frame_botoes, text="Concluir Prova", 
                                font=self.fonte_normal, 
                                bg="#8a2be2", fg="white", 
                                command=lambda: self.corrigir_prova(curso, perguntas[curso]))
        btn_concluir.pack(side="left", padx=5)
        
        btn_voltar = tk.Button(frame_botoes, text="Voltar", 
                              font=self.fonte_normal, 
                              bg=self.cor_destaque, fg="white", 
                              command=lambda: self.criar_tela_curso(curso, self.obter_aulas_curso(curso)))
        btn_voltar.pack(side="left", padx=5)
        
        btn_estatisticas = tk.Button(frame_botoes, text="Estatísticas", 
                                     font=self.fonte_normal, 
                                     bg=self.cor_secundaria, fg="white", 
                                     command=self.criar_tela_estatisticas)
        btn_estatisticas.pack(side="left", padx=5)
    
    def marcar_resposta(self, pergunta_idx, resposta_idx):
        self.respostas_usuario[pergunta_idx] = resposta_idx
    
    def corrigir_prova(self, curso, perguntas):
        if None in self.respostas_usuario:
            messagebox.showwarning("Atenção", "Responda todas as perguntas antes de concluir!")
            return
        
        acertos = 0
        for i, pergunta in enumerate(perguntas):
            if self.respostas_usuario[i] == pergunta['resposta']:
                acertos += 1
        
        nota = (acertos / len(perguntas)) * 10
        self.usuarios[self.usuario_atual]["cursos"][curso]["nota"] = nota
        
        messagebox.showinfo("Resultado", f"Você acertou {acertos} de {len(perguntas)} questões!\nNota: {nota:.1f}")
        self.criar_tela_estatisticas()
    
    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Iniciar aplicação
if _name_ == "_main_":
    root = tk.Tk()
    app = ProjetoAVA(root)
    root.mainloop()