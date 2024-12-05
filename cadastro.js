function validarFormulario() {
    // Recuperar os valores dos campos
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    const nome = document.getElementById("nome").value;

    // Variáveis para controle de erro
    let valido = true;

    // Mensagens de erro
    const emailError = document.getElementById("emailError");
    const senhaError = document.getElementById("senhaError");
    const nomeError = document.getElementById("nomeError");

    // Validação do e-mail
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!email || !emailRegex.test(email)) {
        emailError.textContent = "Por favor, insira um e-mail válido!";
        emailError.style.display = "block";
        valido = false;
    } else {
        emailError.style.display = "none";
    }

    // Validação da senha (pelo menos 8 caracteres)
    if (!senha || senha.length < 8) {
        senhaError.textContent = "A senha deve ter pelo menos 8 caracteres!";
        senhaError.style.display = "block";
        valido = false;
    } else {
        senhaError.style.display = "none";
    }

    // Validação do nome de usuário
    if (!nome) {
        nomeError.textContent = "Por favor, insira um nome de usuário!";
        nomeError.style.display = "block";
        valido = false;
    } else {
        nomeError.style.display = "none";
    }

    // Se algum campo for inválido, não envia o formulário
    return valido;
}
