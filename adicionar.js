// Espera o carregamento da página para adicionar o evento
document.addEventListener('DOMContentLoaded', function () {
    // Obtém o botão "Adicionar" e os inputs
    const btnAdicionar = document.getElementById('adicionar');
    const inputAvaliacao = document.getElementById('avaliacao');
    const inputData = document.getElementById('data');

    // Define o que acontece quando o botão é clicado
    btnAdicionar.addEventListener('click', function() {
        // Captura os valores dos inputs
        const avaliacao = inputAvaliacao.value;
        const data = inputData.value;

        // Verifica se ambos os campos foram preenchidos
        if (avaliacao && data) {
            // Aqui você pode fazer o que quiser com os dados (por exemplo, exibir no console)
            console.log('Avaliação:', avaliacao);
            console.log('Data:', data);

            // Opcional: Limpa os campos após o envio
            inputAvaliacao.value = '';
            inputData.value = '';
        } else {
            // Exibe uma mensagem de erro se algum campo estiver vazio
            alert('Por favor, preencha todos os campos.');
        }
    });
});
