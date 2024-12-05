from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
# from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'seu_segredo_aqui'  # Defina uma chave secreta para sessões

# Função de conexão ao banco de dados
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ifprquedas",
        database="banco"
    )

# Rota principal - página inicial
@app.route("/")
def index():
    return render_template("telaCadastro.html") # mudar dps

# Rota para cadastro
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        nome = request.form.get("nome")
        
        # Verifica se já existe um usuário com o mesmo email
        try:
            with conectar() as conexao:
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM docente WHERE email = %s", (email,))
                if cursor.fetchone():
                    flash("Este email já está cadastrado.", "error")
                    return redirect(url_for("cadastro"))

                # Criptografa a senha antes de salvar
                # senha_hash = generate_password_hash(senha)

                cursor.execute("""
                    INSERT INTO docente(nome, email, senha)
                    VALUES (%s, %s, %s)
                """, (nome, email, senha))
                conexao.commit()

                session["user_email"] = email

                flash("Cadastro realizado com sucesso!", "success")

                return redirect(url_for("perfil"))
            
        except Exception as e:
            print(f"Erro ao inserir no banco de dados: {e}")
            flash("Erro ao cadastrar. Tente novamente!", "error")
    
    return render_template("telaCadastro.html")

# Rota para login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        # Validação do login
        try:
            with conectar() as conexao:
                cursor = conexao.cursor()
                cursor.execute("SELECT * FROM docente WHERE email = %s", (email,))
                user = cursor.fetchone()

                if user[3]==senha:  # user[3] é a senha
                    session["user_id"] = user[0]  # Armazena o ID do usuário na sessão
                    session["user_nome"] = user[1]  # Armazena o nome do usuário na sessão
                    session["user_email"] = user[2]
                    print("o login foi feito com sucesso!")
                    return redirect(url_for("perfil"))
                else:
                    flash("Email ou senha incorretos.", "error")
                    return render_template("telaLogin.html")

        except Exception as e:
            print(f"Erro ao consultar banco de dados: {e}")
            flash("Erro ao tentar fazer login. Tente novamente!", "error")
            return render_template("login.html")

    return render_template("telaLogin.html")

# Rota para exibir o perfil do usuário
@app.route("/perfil")
def perfil():
    # Verifica se o usuário está logado
    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]
    user_nome = session["user_nome"]

    return render_template("perfil.html", nome=user_nome, email=session.get("user_email"))

# Rota para logout
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("user_nome", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)